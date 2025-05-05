# Writeup PC4 - Israel Valderrama

## Pivoting

Una vez visto que tenemos una subred en el sistema que hemos vulnerado (PC1) lo que hacemos es escanear la nueva red para ver que puertos tiene abierto, y para ello usamos el siguiente modulo de metasploit `auxiliary/scanner/portscan/tcp` y configuramos los parametros.

![alt text](img/image-123.png)
![alt text](img/image.png)

Hemos visto que tiene varias ip asociadas a esa red:

- 10.10.10.4 -> 22, 21, 25, 80, 139, 445, 2121, 3128, 8593.
- 10.10.10.5 -> 135, 139, 445, 3389, (Esta es la ip del windows).  
- 10.10.10.2 -> 135, 445, 2179, 3306, 5040, 7070, 8733,9102, 9180.
- 10.10.10.1 -> 53

## Explotacion de PC4

![alt text](img/image-2.png)

![alt text](img/image-3.png)

Ahora hemos intentado saber que servicio hay en el puerto 8593 y lo que hemos probado es si hay un http y para ello le hemos hecho curl a esa dirección y hemos encontrado que hay una página detrás.

![alt text](img/image-5.png)

En el curl vemos que hay dos enlaces y vemos que hay una pagina que se llama `index.php` que contiene un parámetro book que lista los libros que hay. Entonces podemos probar ahora con esa url pero cambiando el parámetro de list por algún directorio de linux ya que sabemos que está alojado en un linux y por si podemos sacar algo de información.

![alt text](img/image-6.png)

![alt text](img/image-7.png)



## SAMBA

Hemos utilizado el samba para ver si podriamos conseguir acceos y para ello hemos utilizado el modulo  `scanner/smb/smb_login` de metasploit y hemos ajustados las opciones y hemos conseguido acceso a 17 sesiones de samba

![alt text](img/image-9.png)

![alt text](img/image-10.png)

![alt text](img/image-11.png)
