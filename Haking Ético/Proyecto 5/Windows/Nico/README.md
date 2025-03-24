# Toma de datos Windows (Nico)

> [!IMPORTANT]
> Vale a ver, este documento no es para entregar, es para recoger información acerca de las vulnerabilidades que vamos encontrando y viendo si son reales o no. Lo voy a hacer rollo *Write Up* de máquinas, un poco explicando que voy haciendo, como, si fallo y si lo consigo.

# Reparto de trabajo

Alenadro Seoane y yo, nos hemos dividido las vulnerabilidades encontradas de la siguiente manera:

- Vulnerabilidades críticas

![alt text](image.png)

- Vulnerabilidades altas

![alt text](image-27.png)

- Vulnerabilidades medias

![alt text](image-50.png)

- Vulnerabilidades bajas

# Análisis

### Vulnerabilidades críticas

#### Apache Tomcat AJP Connector Request Injection (Ghostcat)

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

#### Elasticsearch ESA-2015-06

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


#### Elasticsearch Transport Protocol Unspecified Remote Code Execution

![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)

Esta vulnerabilidad se explota de la misma forma que la anterior vulnerabilidad, mismos exploits y resultados. 

#### ManageEngine Desktop Central < 10 Build 10.0.533 Integer Overflow

![alt text](image-22.png)
![alt text](image-23.png)
![alt text](image-24.png)
![alt text](image-25.png)
![alt text](image-26.png)

Esta vulnerabilidad permite, a traves del envío de peticiones HTTP, a los atacantes hacer una denegación de servicio o la ejecución de código arbitrário.

> [!WARNING]
> Tampoco consigo hacer nada

#### SSL RC4 Cipher Suites Supported (Bar Mitzvah)

![alt text](image-28.png)
![alt text](image-29.png)
![alt text](image-30.png)
![alt text](image-31.png)

Esta vulnerabilidad explica que el host utiliza RC4 para cifrar los datos. RC4 tiene un fallo a la hora de cifrar, y es que no lo hace de manera 100% aleatoria, entonces, si pudieramos obtener miles de datos cifrados(por ejemplo cookies), podríamos llegar a descifrar todos los datos del servidor.

### Vulnerabilidades altas

#### SSL Medium Strength Cipher Suites Supported (SWEET32)

![alt text](image-32.png)
![alt text](image-33.png)
![alt text](image-34.png)
![alt text](image-35.png)
![alt text](image-36.png)

Esta vulnerabilidad explica que el host utiliza cifrado SSL de fuerza media, de 64 a 112 bits, o encriptación 3DES. Ambos son cifrados obsoletos e insuficientes.

#### Oracle GlassFish Server Path Traversal

![alt text](image-37.png)
![alt text](image-38.png)
![alt text](image-39.png)
![alt text](image-40.png)

Esta vulnerabilidad permite a los atacantes acceder a archivos arbitrarios en el servidor, debido a una vulnerabilidad de cruce de rutas autenticadas y no autenticadas.

Utilizando el navegador y URLs como esta:
`https://windows:4848/theme/META-INF%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%afusers`
podremos ver el contenido de la carpeta users:

![alt text](image-41.png)

Si al final de la URL, le añadimos:
`%c0%afvagrant`
listaremos el contenido de la carpeta de `vagrant`

![alt text](image-42.png)

#### SSL Certificate Signed Using Weak Hashing Algorithm

![alt text](image-43.png)
![alt text](image-44.png)
![alt text](image-45.png)
![alt text](image-46.png)

Esta vulnerabilidad explica que el host utiliza algoritmos criptográficos débiles, permitiendo a los atacantes falsificar certificados y hacerse pasar por el verdadero host.

#### Oracle GlassFish Server URL normalization Denial of Service

![alt text](image-47.png)
![alt text](image-48.png)
![alt text](image-49.png)

Esta vulnerabilidad detecta una falla de denegación de servicio en el servidor Oracle GlassFish. La vulneravilidad es el resultado de un loop infinito en la función normalize() y se puede explotar mandando peticioenes a la consola del administrador.

### Vulnerabilidades medias

#### SSH Terrapin Prefix Truncation Weakness (CVE-2023-48795)

![alt text](image-51.png)
![alt text](image-52.png)
![alt text](image-53.png)
![alt text](image-54.png)

Esta vulnerabilidad explica que el servidor SSH es vulnerable a Terrapin, lo que permite ataques de man-in-the-middle.

#### SSL Anonymous Cipher Suites Supported

![alt text](image-55.png)
![alt text](image-56.png)
![alt text](image-57.png)
![alt text](image-58.png)

Esta vulnerabilidad expone una configuración insegura en la que el host remoto permite cifrados SSL anónimos (también llamados anonymous cipher suites), los cuales no utilizan certificados ni autenticación en el proceso de establecer una conexión segura.

#### SSL Certificate Expiry

![alt text](image-59.png)
![alt text](image-60.png)
![alt text](image-61.png)

Esta vulnerabilidad explica que el host utiliza certificados SSL que ya han expirado, lo que permite a los atacantes aprovechar la falta de validación para suplantar la identidad del servidor.

#### SSL Certificate with Wrong Hostname

![alt text](image-62.png)
![alt text](image-63.png)
![alt text](image-64.png)

Esta vulnerabilidad explica que el host presenta un certificado SSL cuyo atributo 'commonName' (CN) no coincide con el nombre del servidor al que se está conectando, lo que permite a los atacantes suplantar la identidad del servidor.

#### Elasticsearch Unrestricted Access Information Disclosure

![alt text](image-65.png)
![alt text](image-66.png)

Esta vulnerabilidad explica que la aplicación Elasticsearch en el servidor web permite el acceso a recursos sensibles sin requerir autenticación, lo que permite a un atacante remoto y no autenticado extraer información de la base de datos.

Podemos explotar esta vulnerabilidad de la siguiente forma:
Buscamos un exploit en metasploit:

![alt text](image-67.png)
> Este es el exploit que estamos buscando.

Usamos el exploit  y asignamos las opciones necesarias:

![alt text](image-68.png)

E iniciamos el exploit:
> metasploitable no soporta versiones tan antiguas de Elasticsearch, igualmente, podemos hacer peticiones con curl o el propio navegador:

![alt text](image-69.png)
![alt text](image-70.png)

#### SMB Signing not required

![alt text](image-71.png)
![alt text](image-72.png)
![alt text](image-73.png)
![alt text](image-73.png)

Esta vulnerabilidad explica que el servidor SMB remoto no requiere firma en las comunicaciones, lo que permite a un atacante sin autenticar realizar ataques de tipo Man-in-the-Middle (MitM) y manipular el tráfico SMB.

#### Terminal Services Encryption Level is Medium or Low

![alt text](image-74.png)
![alt text](image-75.png)

Esta vulnerabilidad explica que el servicio de Escritorio Remoto (RDP) del host no está configurado para usar cifrado fuerte, lo que permite a un atacante interceptar fácilmente las comunicaciones y obtener capturas de pantalla, pulsaciones de teclas u otra información sensible.

#### Terminal Services Doesn't Use Network Level Authentication (NLA) Only

![alt text](image-76.png)
![alt text](image-77.png)

Esta vulnerabilidad explica que el servicio de Escritorio Remoto (RDP) del host no está configurado para exigir Network Level Authentication (NLA), lo que permite a un atacante establecer conexiones RDP completas sin autenticación previa, facilitando ataques de fuerza bruta, exploits y man-in-the-middle.