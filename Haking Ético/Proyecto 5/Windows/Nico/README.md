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

Esta vulnerabilidad permite subir archivos JavaServer Pages al servidor y poder así ejecutar código de manera remota.

 - Elasticsearch ESA-2015-06
 - Elasticsearch Transport Protocol Unspecified Remote Code Execution

![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)

Esta vulnerabilidad nos permite ejecutar código de forma remota en el sistema a traves del protocolo Elasticsearch, lo primero que haré, es probar si el servicio está activo:

![alt text](image-4.png)

La petición nos devuelve un resultado, por lo que está funcionando. Voy a usar mfscosole para buscar alguna vulnerabilidad relevante:

![alt text](image-5.png)
> Este es el único exploit que trata de ejecutar código de manera remota.

Ajustamos las opciones necesarias y arrancamos el exploit:

![alt text](image-6.png)
![alt text](image-7.png)

De esta forma, dmuestro que la vulnerabilidad es verídica y puede comprometer el sistema.

![alt text](image-8.png)

 - ManageEngine Desktop Central < 10 Build 10.0.533 Integer Overflow