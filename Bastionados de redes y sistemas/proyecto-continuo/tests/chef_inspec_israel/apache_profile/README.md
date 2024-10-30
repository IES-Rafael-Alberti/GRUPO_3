# Documentación test de MariaDB
**Objetivos**
El objetivo principal es comprobar si mariadb esta correctamente instalado y pasa los test.

1) Actualizamos los repositorios de Linux.
    ```bash
    apt update
    ```

2) Instalamos MariaDB Server.
    ```bash
    apt install mariadb-server
    ```

<<<<<<< HEAD
**2. Comprobamos si el servicio de apache está corriendo:**
+ Verifica si el servicio de Apache está habilitado y en funcionamiento ejecutando:
```bash
    systemctl status apache2
```
+ Si el servicio está en ejecución aparecerá como "activo" en los resultados. Si no está habilitado o en ejecución, puedes habilitarlo y arrancarlo de esta forma:
```bash
    sudo systemctl enable apache2
    sudo systemctl start apache2
```
**3. Verificar si Apache está escuchando en el puerto 80:**
+ Apache tiene por defecto el puerto 80 en escucha, asi que solo tendremos que crear una nueva para el puerto 81 para ello entraremos en:`/etc/apache2/ports.conf` y cambiar el puerto 80 por el 81.
=======
3) Iniciamos el servicio.
    ```bash
    systemctl start mariadb
    ```
>>>>>>> fd914919714eb103bbe0e16f14ee3294599fc563

4) Comprobamos que se ha iniciado correctamente y sale activo.
    ```bash
    systemctl status mariadb
    ```

5) El puerto 3306 se nos abre directamente al instalar y iniciar mariadb.

6) Nos pide que tenemos que tener una base de datos llamada ciberseguridad. 
    + Nos metemos en mariadb
    ```bash
    mysql
    ```
    + Creamos una base de datos con el nombre que nos piden
    ```bash
    create database ciberseguridad; 
    ```
    + Comprobamos que se nos haya creado la base de datos correctamente
    ```bash
    show databases;
    ```

7) Una vez creada la base de datos, nos pide que dentro de la misma tiene que haber una tabla que se llame redes.
    + Entramos en la base de datos.
    ```bash
    use ciberseguridad;
    ```
    + Creamos la tabla llamada redes, le pondremos un id y un nombre como campos
    ```bash
    create table redes (
        id int primary key,
        nombre varchar(100)
    );
    ```
    + Comprobamos que se nos haya creado la tabla correctamente
    ```bash
    show tables; 
    ```
8) Una vez finalizado los pasos que nos piden, ejecutaremos el comando de cinc con el profile que nos ha pasado el compañero)
    ```bash
    cinc-auditor exec mariadb-server
    ```
    No nos da ningún fallo al ejecutar dicho comando y nos dice que hemos pasado todos los test