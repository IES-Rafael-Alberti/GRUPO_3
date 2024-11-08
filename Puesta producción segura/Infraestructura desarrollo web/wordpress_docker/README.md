# Despliegue de una Aplicación Web con Wordpress y Docker

Este documento recoge el proceso para desplegar una aplicación web desarrollada en **Wordpress** en **Docker**.

## Requisitos

1. Tener instalado **docker**.
2. Tener instalado **docker-compose**. 
3. Crear un directorio para instalar el cotenedor de wordpress. 

## 1. Crear archivo docker-compose.yml para WordPress

1. Creación de directorio para el proyecto:

```bash
mkdir wordpress-docker
cd wordpress-docker
```

2. Crearemos el archivo `docker-compose.yml` dentro del directorio creado. El archivo tendrá el siguiente contenido:

```yaml
version: '3.7'

services:
  wordpress:
    image: wordpress:latest
    container_name: wordpress
    ports:
      - "8080:80" #Puerto por el que nos conectaremos a Wordpress 8080
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_NAME: wordpress
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
    volumes:
      - wordpress_data:/var/www/html
    depends_on:
      - db
    restart: always

  db:
    image: mysql:5.7
    container_name: wordpress-db
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    volumes:
      - db_data:/var/lib/mysql
    restart: always

volumes:
  wordpress_data:
  db_data:

```

Las contraseñas que vienen dentro del archivo .yml tendremos que cambiarlas debido a que son contraseñas genéricas que vienen en la imagen por defecto de Wordpress. 

## 3. Levantar el contenedor

Una vez hemos configurado el archivo docker-compose.yml, ejecutaremos el siguiente comando para iniciar los contenedores: 

```bash
docker-compose up -d
```

Esto nos descargará las imágenes de WordPress y de MySQL (si aún no las tenías) y ejecutará los contenedores en segundo plano. 

## 4. Comprobar y verificar que todo funciona

Para verificar que los contenedores están activos y funcionando usaremos: 

```bash
docker ps
```

Donde nos tendrá que salir una salida en la consola parecida a esta: 
```bash
CONTAINER ID    IMAGE               COMMAND                  CREATED         STATUS         PORTS                  NAMES
id_contenedor   wordpress:latest    "docker-entrypoint.s…"   x minutes ago   Up x minutes   0.0.0.0:8080->80/tcp   wordpress
id_contenedor   mysql:5.7           "docker-entrypoint.s…"   x minutes ago   Up x minutes   3306/tcp               wordpress-db

```

## 5. Conectarnos a WordPress

Abriremos el navegador y nos conectaremos a `http://localhost:8080`. En pantalla nos saldrá el instalador de WordPress la cuál nos preguntará datos sobre la instalación como nombre de la página, usuario, contraseña, etc.  
Una vez acabada la instalación ya tendremos WordPress instalado en nuestro contenedor y podremos conectarnos. 