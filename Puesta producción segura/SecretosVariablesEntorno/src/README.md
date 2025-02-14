# Guía Completa: Gestión de Secretos y Despliegue con Ansible Vault y Docker Compose


## Setup

```bash
docker compose up --build
```

```
http://0.0.0.0:8000
```
---


## 1. Introducción

Esta guía explica cómo:

- Proteger variables sensibles usando Ansible Vault.
- Generar un archivo Docker Compose a partir de una plantilla Jinja2.
- Desplegar el archivo generado para levantar contenedores Docker (FastAPI y MongoDB).

## 2. Estructura del Proyecto

Organiza tu proyecto de la siguiente manera:

```
SecretosVariablesEntorno/
└── src/
    ├── deploy_docker_compose.yml   # Playbook de despliegue
    ├── secrets.yml                 # Archivo de variables sensibles (cifrado con Vault)
    ├── docker-compose.yml.j2       # Plantilla Jinja2 para Docker Compose
    └── (otros archivos de tu proyecto)
```

## 3. Creación y Cifrado del Archivo de Secretos

### 3.1 Archivo de Secretos (secrets.yml)

Define tus variables sensibles:

```yaml
# secrets.yml
SECRET_KEY: "contraseña"
MONGO_USER: "root"
MONGO_PASSWORD: "mi_contraseña_segura"
MONGO_DB: "userdb"
MONGO_AUTH_SOURCE: "admin"
```

### 3.2 Cifrado con Ansible Vault

Ejecuta en la terminal:

```bash
ansible-vault encrypt secrets.yml
```

- Ingresa la contraseña que se usará para descifrar el archivo.
- Ahora, `secrets.yml` estará protegido y solo se podrá leer con la contraseña correcta.

## 4. Creación de la Plantilla Jinja2 para Docker Compose

Crea un archivo llamado `docker-compose.yml.j2` con el siguiente contenido:

```yaml
version: "3.8"

services:
  fastapi:
    build: .
    container_name: fastapi_app
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - mongo
    environment:
      SECRET_KEY: "{{ SECRET_KEY }}"
      ALGORITHM: "HS256"
      MONGO_USER: "{{ MONGO_USER }}"
      MONGO_PASSWORD: "{{ MONGO_PASSWORD }}"
      MONGO_DB: "{{ MONGO_DB }}"
      MONGO_AUTH_SOURCE: "{{ MONGO_AUTH_SOURCE }}"
      MONGO_CONN_STR: "mongodb://{{ MONGO_USER }}:{{ MONGO_PASSWORD }}@mongo:27017/{{ MONGO_DB }}?authSource={{ MONGO_AUTH_SOURCE }}"
    networks:
      - screct_api

  mongo:
    image: mongo:latest
    container_name: mongo_db
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db
    environment:
      MONGO_INITDB_ROOT_USERNAME: "{{ MONGO_USER }}"
      MONGO_INITDB_ROOT_PASSWORD: "{{ MONGO_PASSWORD }}"
      MONGO_INITDB_DATABASE: "{{ MONGO_DB }}"
    networks:
      - screct_api

volumes:
  mongo_data:

networks:
  screct_api:
    driver: bridge
```

## 5. Playbook de Ansible para Generar el Docker Compose

Crea el archivo `deploy_docker_compose.yml` con el siguiente contenido:

```yaml
---
- hosts: localhost
  gather_facts: false
  vars_files:
    - secrets.yml
  tasks:
    - name: Generar docker-compose con variables
      template:
        src: docker-compose.yml.j2
        dest: ./docker-compose.generated.yml
```

**Puntos clave:**
- `vars_files` carga las variables del archivo cifrado.
- La tarea `template` renderiza la plantilla y genera el archivo `docker-compose.generated.yml`.

## 6. Despliegue del Archivo Generado

### 6.1 Ejecución del Playbook

Desde el directorio donde se encuentran tus archivos, ejecuta:

```bash
ansible-playbook deploy_docker_compose.yml --ask-vault-pass
```

- Ingresa la contraseña de Vault cuando se te solicite.
- Se generará el archivo `docker-compose.generated.yml` con las variables sustituidas en texto claro.

### 6.2 Levantamiento de Contenedores con Docker Compose

Usa el archivo generado para levantar tus contenedores:

```bash
docker-compose -f docker-compose.generated.yml up --build
```

- El contenedor `fastapi_app` se levantará en el puerto `8000`.
- El contenedor `mongo_db` se levantará en el puerto `27017`.
- Ambos contenedores compartirán la red `screct_api` para comunicarse internamente.

## 7. Consideraciones de Seguridad

- **Protección en el repositorio:** El archivo `secrets.yml` permanece cifrado en el repositorio.
- **Archivo generado:** `docker-compose.generated.yml` contiene datos en texto claro; añádelo a `.gitignore` para evitar subirlo a repositorios públicos.
- **Entorno seguro:** Usa este método en entornos controlados y considera herramientas de gestión de secretos para producción.

## 8. Resumen del Flujo

1. **Definir variables sensibles:** Crear y cifrar `secrets.yml`.
2. **Plantilla Jinja2:** Crear `docker-compose.yml.j2` con placeholders.
3. **Playbook de despliegue:** Usar `deploy_docker_compose.yml` para renderizar la plantilla.
4. **Generar archivo final:** Ejecutar el playbook con `--ask-vault-pass`.
5. **Desplegar contenedores:** Levantar contenedores con el archivo generado.

---

Hecho por:

- Víctor Jiménez
- Alejandro Seoane
- Israel Valderrama
- Nicolas Ruiz
- Alejandro Díaz 
