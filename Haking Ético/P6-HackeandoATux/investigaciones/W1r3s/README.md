# Write ups máquina w1r3s


Tenemos 4 servicios, un ftp , ssh, un servidor http y una base de datos mysql

![](img/3.png)

## Servidor http 

Escaneamos directorios del puerto 80 que es un servidor web

![](img/4.png)


![](img/6.png)

## `/administrator`


![](img/7.png)


![](img/5.png)


![](img/13.png)

Esta es una vulnerbailidad de acceso no autenticado a un panel de instalación

Como sale arriba en el titulo de la página (cuppa cms) he buscado un exploit para este cms

![](img/16.png)

Nos da una guía ese txt de como explotarlo , lo vamos a hacer con este comando

![](img/17.png)

Nos da esto de configuración

![](img/18.png)

y hacemos este curl y obtenemos las contraseñas del sistema, no he hecho fuerza bruta ya que tengo la contraseña desde el ssh

![](img/19.png)
## `Servidor openssh`

Vulnerabilidad de nessus

![](img/12.png)

Vulnerabilidad propia

Por fuerza bruta se ha sacado que su contraseña es `computer` bastante insegura y me conecto por ssh
![](img/8.png)

Usando el comando sudo su , me ha dado un error y se ha puesto con permisos de administrador root

Vulnerabilidad en el sistema ssh:

![](img/9.png)

![](img/10.png)


## `Servicio FTP`

Se puede acceder de forma anónima a el servidor ftp y se puede ver un listado de los trabajdores de la empresa, la vulnerabilidad es la siguiente

![](img/11.png)


Credenciales en texto plano al acceder a los paquetes del wireshark (solo funciona una vez que te has logeado en ftp)

![](img/14.png)

## Vulnerabilidades

- Acceso no autenticado a un panel de instalación
- Explotacion CMS cuppa mediante el exploit php/webapps/25971.txt
- posible ataque de man in the middle con CVE-2023-48795
- Contraseña débil de el usuario w1r3s en ssh : computer
- Comando para elevar privielgios - sudo su
- Acceder a ftp de forma anónima
- Ver credenciales de ftp en plano en wireshark
