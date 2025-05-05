# Writeup del PC3

Partimos del [writeup anterior](../PC2/README.md)


## Pivoting

Podemos acceder por ssh a la máquina por lo que nos vamos a instalar chisel, que convierte una máquina intermedia accesible solo por SSH en una puerta de entrada a una red que no puedes ver.
```
wget https://github.com/jpillora/chisel/releases/download/v1.7.6/chisel_1.7.6_linux_amd64.gz
gunzip chisel_1.7.6_linux_amd64.gz
mv chisel_1.7.6_linux_amd64 chisel
chmod +x chisel
```

Iniciamos el servidor en modo reverse SOCKS

![alt text](img/image-4.png)

Subimos mediante meterpreter el ejecutable chisel.exe a el pc1 

Desde ahí accedemos a la maquina de esta manera 

![alt text](img/image-2.png)

Cambiamos el archivo `/etc/proxychains4.conf` y ponemos el puerto que tienes abierto para el servidor de chisel en la kali

![alt text](img/image-25.png)

Comprobamos que funciona el túnel , conectandonos por ssh a el pc2

![alt text](img/image-3.png)

>Vemos que el túnel ha funcionado correctamente

A continuación subimos el ejecutable chisel a el pc2 por scp

![alt text](img/image-1.png)

Creamos un servidor en la maquina windows (pc1)

![alt text](img/image-22.png)

y en el ssh creamos un acceso por cliente a el servidor de el pc1

![alt text](img/image-7.png)

Editamos el archivo `/etc/proxychains4.conf` y ponemos otra línea con el puerto que hemos abierto en el pc1. De forma que el archivo quede así

![alt text](img/image-26.png)

Comprobamos que el túnel ha sido exitoso, conectandonos por ssh a el pc3 y vemos que funciona perfectamente 

![alt text](img/image-23.png)

> Tenemos el pivoting hecho , ahora vamos a vulnerar la máquina

## Explotación
He empezado por un escaneo de inicio y ahora he puesto uno más profundo de los puertos que me dió

![alt text](img/image-8.png)

> Parece que tiene ssh y 4 servicios http, solo funciona ssh y el servidor http en el puerto 80 , los demas servicios te redirijen a paginas externas

He hecho un escaneo de directorios a el puerto 80

![alt text](img/image-9.png)

Se puede ver que hay dos carpetas y solo funciona una , ```cgi-data```.

Le he hecho otro fuzeo y sale un archivo que llamado  `getImage.php`, la cuál tiene un script en php que muestra archivos de el servidor.

![alt text](img/image-10.png)

Podemos ver el archivo de contraseñas

![alt text](img/image-11.png)

En estas contraseñas se puede ver dos usuarios

```
root
durian
```

Como no me funciona burpsuite he creado un pequeño script que fuzee a todos los numeros de `/proc/self/fd` y parece que el número es el 6

![alt text](img/image-50.png)

He hecho un fuzeo y el proceso es el 9 que es el que refleja los logs

![alt text](img/image-31.png)

Vamos a envenenar los logs de apache , con un user agent que sea un script de php , para poder meter comandos de terminal

![alt text](img/image-6.png)

Escribimos esto en la url en el navegador 

![alt text](img/image-37.png)

Abrimos el puerto 4445 y revisamos que se haya hecho la reverse shell

![alt text](img/image-38.png)

**Escalada de privilegios**

Tenemos las contraseñas shadow pero no se puede romper rápido con john

![alt text](img/image-40.png)

Ejecutamos este comando para escalar privilegios 

```bash
gdb -nx -ex 'python import os; os.setuid(0)' -ex '!bash' -ex quit
```
![alt text](img/image-32.png)


## Post-explotación

Vamos a hacer una backdoor que nos permita acceder a ssh mediante un certificado, creamos uno en nuestra máquina kali que se llame rsa por ejemplo.

![alt text](img/image-34.png)

Ahora probamos a conectarnos y vemos que funcioan perfectamente

![alt text](img/image-45.png)