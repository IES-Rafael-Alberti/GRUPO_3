# Desafios CTF - Grupo 3
## VICTOR
### CRIPTOGRAFÍA

- Dificil: Se da n, e, y un mensaje cifrado con un módulo pequeño, El objetivo es factorizar n y calcular d para descifrar la flag. (Víctor)

### FORENSE

- Facil: Se proporciona una imagen con metadatos EXIF, el objetivo es usar herramientas buscar la flag entre sus metadatos. (Víctor)

### OSINT

- Facil: Se proporciona un nombre de usuario y se debe encontrar una publicación con la flag haciendo uso de Google Dorks. (Víctor)

- Intermedio: Un dominio sospechoso tiene información oculta en su historial de registros WHOIS entre los que se encuentra la flag. (Víctor)

## ALEJANDRO SEOANE

### OSINT
- Fácil: Un estudiante del centro ha dejado alguna pista en un perfil de Twitter. Le daremos el usuario. Tendrán que investigar cuál es la ciudad donde vive y usar está como flag.
Formato flag: flag{ciudad}
- Difícil: Se trata de una especie de ginkana. En un video de YT que no tiene nada de relación con la tarea habrá escondido en los subtitulos una URL durante todo el video, por lo que daremos algún tipo de pista para que sepanq ue tienen que encender los subtítulos en el vídeo (por ejemplo, no importa solo lo que oye si no lo que puedes ver o algo parecido). Esta URL te llevará a una página. En esta página a través de fuzzeo tendrán que sacar los directorios que tiene el sitio web.
En uno de los directoriso habrá una flag dentro de un zip cifrado. Para encontrar la contraseña del zip deberán buscar por alguno de los otros directorios con las pistas que encuentren en el robot.txt, donde les llevara a una página donde este la contraseña cifrada de alguna forma.

 ### METADATOS 
 - Fácil: en una página web se ha dejado una foto. Al descargar la imagen y ver los metadatos se podrá encontrar la flag.

### XSS 
- Medio: en una web hay un apartado de comentarios. De alguna forma tendrán que buscar la manera de hacer un XSS para poder ejecutarlo en la página y que está le devuelva la flag, por ejemplo a traves de un script que contenga un alert. 
