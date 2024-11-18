# Despliegue de una Aplicación Web con FastAPI y Docker.

Este documento recoge el proceso para desplegar una aplicación web desarrollada en **Python con FastAPI** en **Docker**.

## Requisitos

1. Tener instalado **docker**. Para comprobar que lo tenemos instalado miraremos la versión con el siguiente comando.

```bash
docker --version
```

2. Tener instalado **docker-compose**. Para comprobar que lo tenemos instalado miraremos la versión con el siguiente comando.

```bash
docker-compose --version
```

3. Crear un directorio para instalar el contenedor de FastAPI.

## 1. Crear archivo docker-compose.yml para FastAPI.

1. Creación de directorio para el proyecto:

```bash
mkdir fastapi
cd fastapi
```

2. Crearemos el archivo `docker-compose-yml` dentro del directorio creado. El archivo tendrá el siguiente contenido.

```yaml
services:
  api:
    build:
      context: .
      dockerfile: DockerFile
    ports:
      - "8000:8000"
    volumes:
      - .:/code
```

## 3. Levantar el contenedor.

Una vez configurado el archivo docker-compose.yml, ejecutaremos el siguiente comando para iniciar los contenedores:

```bash
docker-compose build

docker-compose up -d
```

## 4. Comprobar y verificar que todo funciona.

Para verificar que los contenedores están activos y funcionando usaremos: 

```bash
docker ps
```

Donde nos tendrá que salir una salida en la consola parecida a esta: 

```bash
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS         PORTS                    NAMES
b3c9c8abcaea   fastapi-api   "uvicorn main:app --…"   21 minutes ago   Up 4 seconds   0.0.0.0:8000->8000/tcp   fastapi-api-1
```

## 5.Conectarnos a FastAPI.

Abrimos el navegador y nos conectamos a `http://localhost:8000`. Ahí nos aparecerá la primera parte de la api y si nos vamos a */info* nos aparecerá qué es FastAPI.
Una vez ya instalado tenemos nuestro contenedor y nos podremos conectar. 