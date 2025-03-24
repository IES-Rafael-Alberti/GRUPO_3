# Toma de datos Windows (Alejandro S.)

> [!IMPORTANT]
> Este será mi writeup, donde iré recoginedo el proceso que he seguido para explotar las vulnerabilidades escaneadas. Ire poniendo la vulnerabilidad que estamos investigando y si hemos conseguido explotarla.

# Reparto de trabajo

Nico y yo nos hemos repartido cada nivel de vulnerabilidad de manera equitativa para que los dos hagamos las mismas críticas, altas, medias...

## Vulnerabilidades críticas

![alt text](img/image.png)

### MS11-030: Vulnerability in DNS Resolution Could Allow Remote Code Execution (2509553) (remote check)

![alt text](img/image_7.png)

+ Descripción: es una falla crítica en la resolución DNS de Windows que permite la ejecución remota de código

+ CVE: CVE-2011-0657

+ CVSS: 10.0

+ Output

    ![alt text](img/image_10.png)

Hemos buscado en metaexploit por el nombre de la vulnerabilidad y solo nos sale una en común.

![alt text](img/image_8.png)

+ Options

![alt text](img/image_9.png)

Configuramos las opciones con la IP del servidor y el puerto del servicio vulnerable.
![alt text](img/image_11.png)

Y por último ejetuamos el exploit.

![alt text](img/image_12.png)

Esto puede provocar una denegación del servicio DNS del servidor. En el mensaje nos dice que el servicio se reiniciará automaticamente 2 veces y que para asegurarnos de que esta completamente muerto esperemos 5 min y lo volvamos a ejecutar.

### ManageEngine Desktop Central 8 / 9 < Build 91100 Multiple RCE

![alt text](img/image_6.png)

+ Descripción: Esta vulnerabilidad afecta a ManageEngine Desktop Central versiones 8 y 9 anteriores a la compilación 91100, permitiendo la ejecución remota de código.
Estas vulnerabilidades son críticas ya que permiten la ejecución de código remoto sin necesidad de autenticación, otorgando al atacante control total del sistema afectado.

+ Output:

![alt text](img/image_13.png)

Al conectarnos vemos como efectivamente es la página del ManageEngine Desktop Central 9

![alt text](img/image_1.png)

Sabiendo esto vamos a bucar en metaexploit ese nombre literalmente a ver si encontramos algo. Hay nos encuentra numerosos resultados pero hay uno que nos nombra la versión 9 por lo que vamos a utilizar ese.

![alt text](img/image_2.png)

+ Options

![alt text](img/image_3.png)

+ Configuramos las opciones

![alt text](img/image_4.png)

+ Ejecución exploit

![alt text](img/image_5.png)

Como podemos ver una vez ejecutado el exploit se introduce un payload con una reverse shell, lo que nos abre una consola con la que tenemos acceso al sistema. Hemos comprobado con que permisos y somos usuario autorizado del sistema por lo que tenemos permiso de administrador.

### Unsupported Windows OS (remote)

![alt text](img/image_15.png)

+ Descripción: esta vulnerabilidad indica que el sistema operativo ya no recibe actualizaciones de seguridad, lo que lo hace al servidor altamente vulnerable.

+ Output:

![alt text](img/image_14.png)

Vamos a buscar alguna vulnerabilidad que tenga relación con la version de Windows Server del servidor. En contramos un exploit de eternal blue el cuál nos permite seleccionar como target un Windows Server 2008 R2.

![alt text](img/image_16.png)

+ Options

![alt text](img/image_17.png)

+ Configuramos las opciones

![alt text](img/image_18.png)

+ Ejecución exploit

![alt text](img/image_19.png)

Con la ejecución del exploit conseguimos acceder al sistema a través de una payload con una reverse shell. Podemos ver que encima los permisos que nos otorga son los permisos de sistema.

### Microsoft RDP RCE (CVE-2019-0708) (BlueKeep) (uncredentialed check)

![alt text](img/image_20.png)

+ Descripción: esta vulnerabilidad permite ejecución remota de código (RCE) sin autenticación en versiones antiguas de Windows con RDP habilitado.

+ Output:

![alt text](img/image_21.png)

Vamos a buscar un exploit con el CVE que nos dan. Solo nos aparece una la cuál coincide ya que habla de BlueKeep. 

![alt text](img/image_22.png)

+ Options:

![alt text](img/image_23.png)

+ Configuramos las opciones:

![alt text](img/image_24.png)

+ Ejecutamos exploit:

![alt text](img/image_25.png)

Parece ser que el exploit se ejecuta pero no nos crea ninguna sesión.

## Vulnerabilidades altas

### MS12-020: Vulnerabilities in Remote Desktop Could Allow Remote Code Execution (2671387) (uncredentialed check)

![alt text](img/image_26.png)

+ Descripción: esta vulnerabilidad nos permite ejecutar codigo remoto y poder hacer un ataque de denegación al servicio.
+ CVE: CVE-2012-0152, CVE-2012-0002

+ Output:

![alt text](img/image_27.png)

A través de los dos CVEs que nos proporcionan hemos encontrado un exploit el cuál nos permite hacer un ataque de denegación de servicio al servicio RDP.

![alt text](img/image_28.png)

+ Options:

![alt text](img/image_29.png)

+ Ejecutamos exploit:

![alt text](img/image_30.png)
![alt text](img/image_31.png)

### MS14-066: Vulnerability in Schannel Could Allow Remote Code Execution (2992611) (uncredentialed check)

![alt text](img/image_32.png)

+ Descripción: esta vulnerabilidad permite la ejecución de código remoto mediante paquetes TLS.
+ CVE: CVE-2014-6321

+ Output:

![alt text](img/image_33.png)

Hemos buscando algún exploit pero no hemos podido encontrar ninguno que se pueda ejecutar.

### 



+ Descripción: 
+ CVE: 

+ Output:







+ Options:



+ Configuramos las opciones:



+ Ejecutamos exploit: