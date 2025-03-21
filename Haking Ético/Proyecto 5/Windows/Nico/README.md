# Toma de datos Windows (Nico)

> [!IMPORTANT]
> Vale a ver, este documento no es para entregar, es para recoger información acerca de las vulnerabilidades que vamos encontrando y viendo si son reales o no. Lo voy a hacer rollo *Write Up* de máquinas, un poco explicando que voy haciendo, como, si fallo y si lo consigo.

# Reparto de trabajo

Alenadro Seoane y yo, nos hemos dividido las vulnerabilidades encontradas de la siguiente manera:

- Vulnerabilidades críticas

![alt text](image.png)

# Análisis

- Vulnerabilidades críticas

 - Apache Tomcat AJP Connector Request Injection (Ghostcat)

![alt text](image-9.png)
![alt text](image-10.png)
![alt text](image-11.png)
![alt text](image-12.png)
![alt text](image-13.png)

Esta vulnerabilidad permite subir archivos JavaServer Pages al servidor y poder así ejecutar código de manera remota. Busco la vulneravilidad en metasploitable:

![alt text](image-14.png)

Esta es la única que aparece, miramos y cambiamos sus ajustes:

![alt text](image-15.png)

E iniciamos el exploit:

![alt text](image-16.png)
> Este contenido ya nos lo da el Nessus.

Voy a intentar subir un archivo, para ello voy a utilizar [ajpShooter.py](https://github.com/00theway/Ghostcat-CNVD-2020-10487.git)

![alt text](image-17.png)

Primero que nada, voy a crear un shell.jsp con la que voy a intentar ejecutar código en el sistema, y ahora la subo con el siguiente comando:

![alt text](image-18.png)

Parece que dan algunos errores, no consigo sacar nada de aquí.

 - Elasticsearch ESA-2015-06

![alt text](image-19.png)
![alt text](image-20.png)
![alt text](image-21.png)

Esta vulnerabilidad nos permite ejecutar código de forma remota en el sistema a traves del protocolo Elasticsearch, lo primero que haré, es probar si el servicio está activo:

![alt text](image-4.png)

La petición nos devuelve un resultado, por lo que está funcionando. Uso mfsconsole para buscar algún módulo de expotación:

![alt text](image-5.png)
> Este es el único exploit que trata de ejecutar código de manera remota.

Ajustamos las opciones necesarias y arrancamos el exploit:

![alt text](image-6.png)
![alt text](image-7.png)

De esta forma, dmuestro que la vulnerabilidad es verídica y puede comprometer el sistema.

![alt text](image-8.png)


 - Elasticsearch Transport Protocol Unspecified Remote Code Execution

![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)

Esta vulnerabilidad se explota de la misma forma que la anterior vulnerabilidad, mismos exploits y resultados. 

 - ManageEngine Desktop Central < 10 Build 10.0.533 Integer Overflow

![alt text](image-22.png)
![alt text](image-23.png)
![alt text](image-24.png)
![alt text](image-25.png)
![alt text](image-26.png)

Esta vulnerabilidad permite, a traves del envío de peticiones HTTP, a los atacantes hacer una denegación de servicio o la ejecución de código arbitrário.