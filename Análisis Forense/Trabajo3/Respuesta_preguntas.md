Este documento consta de la parte 1 del proyecto que consiste en la investigación de la imagen de disco y la respuesta a las preguntas planteadas.

1. Verificar la integridad de la imagen del disco a través de CMD o PowerShell, comparando los hashes proporcionados. ¿Coinciden los tres hashes?

	Para comprobar la integridad del disco, hemos hecho uso de las herramientas por consola de Windows, y hemos sacado los siguientes hashes:

- md5:

| **Hash esperado** | **Hash conseguido** |
| - | - |
| **dfdfba2231e3fa409676b1b737474208** | **dfdfba2231e3fa409676b1b737474288** |

- sha1:

| **Hash esperado** | **Hash conseguido** |
| - | - |
| **f476a81089a10f9d5393aa8c2f8bbccdb87f7d3c** | **f476a81089a10f9d5393aa8c2f8bbccdb87f7d3c** |

- sha256:

| **Hash esperado** | **Hash conseguido** |
| - | - |
| **f476a81089a10f9d5393aa8c2f8bbccdb87f7d3c** | **66d6ee7a61ea7a986e8f6bb54b9986f79d95b5a0278bef86678ed42ace320d9b** |

Comprobamos que los hashes MD5 y SHA256 no coinciden con los proporcionados en el documento.

---

2. Confirmar la existencia de un usuario correspondiente a Richard en el equipo y determinar cuándo fue su último inicio de sesión.

Para comprobar la existencia del usuario Richard, debemos extraer el archivo *SAM* del directorio *C://windows/system32/config* y importarlo a la herramienta WRR.

![[Pasted image 20250128183202.png]]

Vemos que el único usuario de la máquina es Richard, el resto son usuario que crea Windows por defecto, y también observamos que el último inicio de sesión es el día 22 de febrero de 2023 a las 13 horas, 55 minutos y 18 segundos.

---

3. Identificar el nombre del equipo y la versión del Sistema Operativo utilizado.

Para identificar el nombre y la versión del equipo, debemos extraer los archivos *software* y *system* del directorio *C://windows/system32/config*. 

![[Pasted image 20250128183555.png]]

Aquí podemos comprobar la versión de Windows 10 que tiene instalado el disco: **Pro Education N**.

![[Pasted image 20250128183808.png]]

Y aquí el nombre del equipo: **LADRONERA**.

---

4. Investigar si se introdujo algún dispositivo USB en el equipo, a pesar de las políticas de la empresa contra su uso por parte de Richard. En caso afirmativo, especificar los detalles del dispositivo USB y el momento de su conexión.

Para identificar los dispositivos USB del equipo, debemos extraer el archivo *system* del directorio *C:windows/system32/config*. 

![[Pasted image 20250128185419.png]]

![[Pasted image 20250128190514.png]]

![[Pasted image 20250128190909.png]]

En esta serie de imágenes, podemos comprobar que se introdujo un dispositivo USB con el siguiente id: **{4D36E967-E325-11CE-BFC1-08002BE10318}**, y cuya última conexión fue el 22 de febrero de 2023 a las 00 horas, 27 minutos y 42 segundos.

---

5. Dado el interés conocido de Richard por el fútbol y la música rock y heavy, investigar su actividad en línea relacionada con estos intereses. Además, verificar si ha visualizado contenido en línea que pueda justificar un despido procedente, como la visualización de una película online. Documentar cualquier hallazgo relevante.

![[Pasted image 20250128194536.png]]

Hemos encontrado esta URL en el historial de navegación que proviene del video titulado: **El truco con nata y monedas que le vuela la cabeza a Jennifer Aniston**

![[Pasted image 20250128195050.png]]

Accedió a CUEVANAHD para ver la película *Trabajo basura*.

![[Pasted image 20250128195606.png]]

Entró en Amazon y buscó dispositivos pendrive.

![[Pasted image 20250128195701.png]]

Hizo búsquedas sobre *Equipo de futbol* en internet

![[Pasted image 20250128200416.png]]

Si exportamos el archivo *places.sqlite* del directorio *C://Users/Richard/AppData/Roaming/Mozilla/Firefox/Profiles/mt13hmmn.default-release* veremos las páginas que ha visitado en firefox.

![[Pasted image 20250128201111.png]]
![[Pasted image 20250128201131.png]]
![[Pasted image 20250128201143.png]]
![[Pasted image 20250128201201.png]]
![[Pasted image 20250128201217.png]]
![[Pasted image 20250128201235.png]]

Por último, podemos ver todo el historial del navegador *Opera*, en el cual hace numerosas búsquedas relacionadas con futbol y videos de YouTube.

6. Determinar si, tras su salida de la empresa, Richard tenía planes de visitar otro lugar y, de ser así, cómo planeaba llegar allí.

Como vemos en la imagen:

![[Pasted image 20250128201201.png]]

Apreciamos que *Richard* buscó vuelos baratos a las ciudades europea y hoteles en *Las Palmas de Gran Canaria*.

7. Comprobar si existe algún navegador web, aparte de los proporcionados por Microsoft, configurado para ejecutarse al iniciar sesión Richard.

![[Pasted image 20250128203533.png]]

Si importamos el **NTUSER.DAT** en *regedit* vemos que los navegadores que se inician al arrancar son Edge y Opera.

8. Buscar evidencia de que Richard haya asistido a competidores o terceros mediante la exfiltración de datos por correo electrónico.

Tras exportar la carpeta *C://Users/Richard/AppData/Roaming/Thunderbird/Profiles/tvtlv94f.default-release/*, e importar el archivo *ImapMail/imap.gmail.com/INBOX* en el programa **Mail Viewer**, encontramos los siguientes correos relevantes.

![[Pasted image 20250128212343.png]]
![[Pasted image 20250128212501.png]]
![[Pasted image 20250128212601.png]]
![[Pasted image 20250128212632.png]]
![[Pasted image 20250128212725.png]]
![[Pasted image 20250128212738.png]]

Apreciamos que:

- 20 de febrero de 2023
	- 20:53
		- Richard mantiene una conversación con proba2.seguridade@gmail.com acerca de ser contratado por estos y enviarles un *material* a cambio de una compensación económica.
- 22 de febrero de 2023
	- 00:59
		- Richard mantiene una conversación con proba2.seguridade@gmail.com sobre cambiar su lugar de trabajo al día siguiente, de enviarle la *muestra* y de recibir un pago.
	- 01:01
		- Richard envía un mensaje a proba2.seguridade@gmail.com diciéndole que le envía la *muestra*.
	- 01:06
		- proba2.seguridade@gmail.com le dice a Richard que el pago es demasiado grande(100k) y que se tendrá que hacer por bitcoin.
	- 01:40
		- Richard habla con phy.reg@gmail.com y le dice que se ha ido de la empresa.
	- 15:06
		- Richard mantiene una conversación con proba2.seguridade@gmail.com, le envía un enlace a *Google Drive* con el *material* acordado en el primer mensaje, pero que solo revelará la contraseña al depositar el dinero.
	- 15:25
		- Richard habla por última vez con phy.reg@gmail.com para despedirse y aclara que ha dejado la empresa.