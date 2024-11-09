# Despliegue de una Aplicación Web con Spring-Boot y Docker

Este documento recoge el proceso para desplegar una aplicación web desarrollada en **Spring-Boot** en **Docker**.

## Requisitos

1. Tener instalados **docker**.
2. Tener instalados **docker-compose**.
3. Tener instalado java 17. 
4. Tener instalado maven. 

## 1. Creación de directorio para el contenedor de spring boot

```bash
mkdir springboot-docker
cd springboot-docker
```
## 2. Creación de un proyecto spring boot

Nos dirigiremos a la siguiente [página](https://start.spring.io/) y crearemos un proyecto inicial.   
Nosotros hemos escogido las siguientes características:
- Project: Maven
- Language: Java
- Spring Boot (version): 3.3.5
- Java (version): 17

También hay una opción donde nos deja añadir dependencias. Nosotros hemos agregado las siguientes:
- Spring Web
- Dcoker Compose Support

Una vez hemos acabado le daremos a descargar y nos dará un `archivo.jar` el cuál lo descomprimiremos dentro del directorio que hemos creado en el paso anterior. 

## 3. Configuración de DockerFile

Dentro de la carpeta springboot-docker crearemos el archivo `Dockerfile`. Dentro añadiremos el siguiente contenido: 
```bash
FROM openjdk:17-jdk-slim
WORKDIR /app
COPY target/*.jar app.jar
EXPOSE 8081 # Puerto al que nos conectaremos
ENTRYPOINT ["java","-jar","/app/app.jar"]
```

## 4. Ajustar la configuración de Spring Boot

Modificaremos el archivo `application.properties` el cuál se encuentra dentro de src/main/resources dentro de la carpeta principal.   
Le añadiremos el siguiente contenido: 
```bash
spring.application.name=springboot-docker
server.address=0.0.0.0
server.port=8081
```

Nosotros como vamos a utilizar maven tendremso que editar el archivo pom.xml y añadirle la dependencia de Thymeleaf. 
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

Por último crearemos un controlador para que al conectarnos nos salga algo en la página. Crearemos el archivo `HelloController.java` en *src/main/java/com/grupo3/springboot_docker*. 

```bash
package com.example.springbootapp.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/")
    public String hello() {
        return "Hola mundo";
    }
}
```

## 5. Creación de contenedor en docker

Crearemos en la raiz de la carpeta el archivo `docker-compose.yml`. Tendrá el siguiente contenido:
```yml
version: '3'
services:
  springboot:
    build: .
    ports:
      - "8081:8081"
```

## 6. Construcción y ejecución de los contenedores

Nos pondremos en la carpeta de spring boot y ejecutaremos el siguiente comando para contruir el contenedor y levantarlo:
```bash
docker-compose up -d
```
Por último verificaremos que los contenedores estén activos.
```bash
docker ps
```

## 7. Conexión al contenedor

Una vez levantado el contenedor, abriremos el navegador y nos pondremos la siguiente URL: `http://localhost:8081`. Nos deberá conectar a nuestra página y nos saldrá el mensaje que configuramos anteriormente "*Hola mundo*"