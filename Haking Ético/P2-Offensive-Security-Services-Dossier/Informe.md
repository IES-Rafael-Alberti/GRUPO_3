# Informe sobre tipos de ataque, metodologías de pentesting y herramientas
![Portada](portada.png)

**Participantes:** *Grupo 3*
- Jesús Cordero
- Álvaro González
- Alejandro Seoane
- Israel Valderrama

## Índice
- [Introducción](#introducción)
- [Clasificación de tipos de ataque](#clasificación-de-tipos-de-ataque)
    - [Ataques de ingeniería social](#ataques-de-ingeniería-social)
    - [Ataques de malware](#ataques-de-malware)
    - [Ataques a redes y sistemas](#ataques-a-redes-y-sistemas)
- [Metodologías de pentesting](#metodologías-de-pentesting)
    - [Selección de Metodologías](#selección-de-metodologías)
    - [Fases Clave de un Ataque y Relación con Tipos de Auditorías](#fases-clave-de-un-ataque-y-relación-con-tipos-de-auditorías)
    - [Auditoría de Ingeniería Social](#auditoría-de-ingeniería-social)
    - [Auditoría de Malware](#auditoría-de-malware)
    - [Auditoría de Redes y Sistemas](#auditoría-de-redes-y-sistemas)
- [Evaluación de herramientas de monitorización](#evaluación-de-herramientas-de-monitorización)
    - [Herramientas ataques de ingeniería social](#herramientas-ataques-de-ingeniería-social)
    - [Herramientas ataques de malware](#herramientas-ataques-de-malware)
    - [Herramientas ataques a sistemas y redes](#ataques-a-redes-y-sistemas)
- [Conclusiones](#conclusiones)
- [Fuentes](#fuentes)


## Introducción
El trabajo se centra en la investigación y clasificación de ciberataques, teniendo en cuenta métodos, características y objetivos de los ataques mas comunes. Lo hemos clasificado en tres categorías principales:
1. **Ataque de Ingeniería Social:** Estos ataques manipulan a las persoan para obtener información sensible. Incluyen técnicas como phising, speat phising, donde los ciberdelincuentes se hacen pasar por entidades confiables para engañar a las personas.
2. **Ataques de Malware:** Estos ataques utilizan software malicioso para infiltrarse y dañar sistemas. Hay varios tipos como pueden ser gusanos, ransomware y spyware y cada uno actua de forma distinta.
3. **Ataque de Redes y Sistemas:** Estos ataques aprovechan vulnerabilidades en la infraestructura tecnológica. Hay varios tipos como pueden ser DDoS, inyección SQL y ataques Man-in-the-Middle.

Además también examinanos metodologías de pentesting y herramientas específicas para auditar la seguridad de los sistemas, con el objetivo de mejorar la defensa contra estas amenazas.
Entender estos aspectos son fundamental para el desarrollo de estrategias efectivas de prevención y mitigación en el ámbito de la ciberseguridad.

## Clasificación de tipos de ataque
Esta parte del informe se centrará en la investigación y clasificación de los ataques cibernéticos más comunes teniendo en cuenta los métodos, características y objetivos de cada uno.

### Ataques de ingeniería social
Este tipo de ataques consiste en manipular psicológicamente a las víctimas para obtener información del usuario o acceso a sus dispositivos. Existen tres tipos:

+ **Phishing:** Se usa principalmente para robar datos del usuario como números de tarjetas de crédito o contraseñas. Los ciberdelincuentes se suelen hacer pasar por personas o entidades de confianza (servicio de correos, bancos...) y engañan a la víctima con un mensaje normalmente alarmante para que pinchen en el enlace malicioso proporcionado. 

    Se le llama smishing en caso de realizarse por SMS o vishing si se realiza a través de una llamada.

+ **Spear Phishing:** Son ataques de phishing dirigidos a una persona o empleado concreto de una compañía específica con el fin de obtener información o acceso a dicha compañía. Para ganarse su confianza los ciberdelincuentes investigan meticulosamente a la víctima recopilando toda la información posible antes de comenzar.
+ **Whaling:** Estos ataques, también conocidos como "cazas de ballenas", son similares a los ataques de spear phishing. La principal diferencia es que van dirigidos a altos cargos de las empresas, como CEOs y CFOs ya que estos suelen tener acceso completo a la empresa y a su información confidencial.

### Ataques de malware
Estos ataques utilizan software malicioso para infiltrarse, dañar o deshabilitar los sistemas de una red. Veremos seis tipos:

+ **Virus:** Es un código malicioso que infecta los archivos del sistema y que debe de ser ejecutado por un usuario. Una vez dentro se propaga a todo lo que tenga acceso.
+ **Gusanos:** Es un programa que, al igual que los virus, una vez infectado el dispositivo empieza a propagarse, en este caso a otros dispositivos a través de la red. Las principales diferencias con los virus son que en el caso de los gusanos no necesita que un usuario lo ejecute y que como su principal objetivos es la propagación a otros equipos no afecta al funcionamiento normal del sistema. 

    Principalmente se usan para crear botnets para luego realizar acciones de forma remota.
+ **Troyanos:** Suelen estar integrados en archivos ejecutables aparentemente inofensivos. Una vez ejecutado este archivo ejecutable, el troyano crea una puerta trasera para facilitar la entrada del ciberdelincuente u otros malwares al dispositivo.
+ **Ransomware:** Se suele propagar como los troyanos, integrado en un archivo ejecutable pero, a diferencia de los troyanos, los ransomware secuestran a los datos encriptándolos y pidiendo un rescate (normalmente en criptomonedas) a cambio de la clave para desencriptar los datos. Pagar el rescate no asegura que los ciberdelincuentes nos vayan a suministrar la clave.

    Este tipo de ataque puede provocar el paro total de las actividades de una empresa hasta que se solucione.
+ **Spyware:** Son programas espía cuyo principal objetivo es la obtención de información intentando dejar el menor rastro posible para no ser detectado.
+ **Adware:** Su principal función es mostrar publicidad de forma invasiva y, aunque su objetivo no es dañar a los sistemas, puede ser considerado un spyware ya que es posible que recopile y transmita información del usuario para mostrar publicidad más personalizada al usuario.

### Ataques a redes y sistemas
Son ataques que aprovechan vulnerabilidades en la infraestructura de redes y sistemas informáticos con el objetivo de comprometer la seguridad, interrumpir operaciones u obtener acceso a datos e información sensible. Hablaremos de cuatro tipos

+ **Denegación de servicio distribuido (DDoS):** Consiste en realizar peticiones constantes a un servidor hasta lograr que colapse y deje de funcionar provocando así la parada del servicio suministrado por el servidor. Para estos ataques se suelen usar botnets formadas por equipos infectados por gusanos.

+ **Man-in-the-Middle (MitM):** Es un tipo de ataque en el que el ciberdelincuente intercepta la comunicación de dos dispositivos pudiendo leerla o modificarla. Tienen como fin el robo de datos o la manipulación de los mismos.
+ **Inyección SQL:** Consiste en infiltrar código en un campo de entrada de una aplicación web aprovechándose de vulnerabilidades en ella. De esta manera los ciberdelincuentes pueden obtener acceso a la base de datos de la aplicación web y obtener información sensible, modificarla u obtener control de la aplicación web.
+ **Cross-Site Scripting (XSS):** Es un tipo de inyección en la que el atacante envía secuencias de comandos maliciosos al contenido de páginas web para desacreditarla. Cuando una víctima accede a la aplicación web, el navegador de la víctima ve el código malicioso del ciberdelincuente como parte del sitio web y lo ejecuta.
+ **Ataques de fuerza bruta:** Consiste en intentar obtener acceso a un dispositivo de una red o a información protegida por una contraseña a base de intentar descifrar dichas contraseñas probando múltiples combinaciones hasta encontrar una. Se puede realizar probando todas las combinaciones posibles, con el uso de un diccionario de contraseñas o con una combinación de ambas.

## Metodologías de pentesting
| Metodología                               | Enfoque Principal                             | Aplicable a Ingeniería Social | Aplicable a Malware | Aplicable a Redes y Sistemas |
|-------------------------------------------|-----------------------------------------------|-------------------------------|---------------------|-------------------------------|
| OWASP Testing Guide                       | Aplicaciones web                              | Parcialmente                  | Sí                  | Sí                            |
| OSSTMM                                    | Sistemas y redes                             | Sí                            | Sí                  | Sí                            |
| ISSAF                                     | Riesgos en sistemas y redes                  | Sí                            | Sí                  | Sí                            |
| NIST Cybersecurity Framework              | Identificación y mitigación de riesgos       | Sí                            | Sí                  | Sí                            |
| OSINT                                     | Información pública                           | Sí                            | Parcialmente        | Parcialmente                  |
| Ethical Hacking                           | Simulación de ataques                         | Sí                            | Sí                  | Sí                            |
| VAPT                                      | Evaluación de vulnerabilidades y pruebas de penetración | Parcialmente          | Sí                  | Sí                            |
| PTES                                      | Planificación y ejecución de pruebas         | Sí                            | Sí                  | Sí                            |
| STIG                                      | Mejora de la seguridad en sistemas           | No                            | Sí                  | Sí                            |
| TIC                                       | Recopilación de información técnica          | Parcialmente                  | Sí                  | Sí                            |

### Selección de Metodologías

Considerando los servicios específicos mencionados (ingeniería social, malware, y ataques a redes y sistemas), las metodologías más adecuadas son:

- #### OSSTMM (Open Source Security Testing Methodology Manual):
    El OSSTMM es una metodología integral que abarca todos los aspectos de la seguridad de sistemas y redes. Su enfoque holístico permite evaluar tanto la seguridad técnica como la humana, lo que la hace ideal para abordar ataques de ingeniería social, malware y vulnerabilidades en redes y sistemas.

- #### ISSAF (Information Systems Security Assessment Framework):
    El ISSAF proporciona un marco detallado para la evaluación de riesgos en sistemas de información. Su estructura en fases (planificación, evaluación, tratamiento, acreditación y mantenimiento) permite una evaluación completa de la seguridad, cubriendo desde la ingeniería social hasta las vulnerabilidades técnicas.

- #### Ethical Hacking:
    Esta metodología se centra en simular ataques reales, lo que la hace particularmente efectiva para identificar vulnerabilidades en todos los niveles. Su enfoque práctico permite descubrir fallos de seguridad que podrían pasar desapercibidos con métodos más teóricos, siendo especialmente útil para evaluar la resistencia a ataques de ingeniería social y malware.

- #### PTES (Penetration Testing Execution Standard):
    El PTES ofrece un enfoque estandarizado para las pruebas de penetración, cubriendo todas las fases desde la recopilación de información hasta la post-explotación. Su estructura detallada permite una evaluación exhaustiva de la seguridad, siendo particularmente útil para auditar redes y sistemas, así como para evaluar la efectividad de las defensas contra malware.

### Fases Clave de un Ataque y Relación con Tipos de Auditorías

Las fases clave de un ciberataque típico son:

- #### Reconocimiento

    - **Descripción**: En esta fase, el atacante recopila información sobre el objetivo. Esto puede incluir búsquedas en internet, ingeniería social, y escaneo de redes.

    - **Relación con auditorías**: Crucial para la auditoría de ingeniería social y la evaluación de la exposición de información pública.

- #### Weaponización y entrega

    - **Descripción**: El atacante prepara las herramientas para el ataque (como malware) y las entrega al objetivo, a menudo a través de phishing o explotando vulnerabilidades conocidas.

    - **Relación con auditorías**: Fundamental para las auditorías de malware y la evaluación de la resistencia a ataques de ingeniería social.

- #### Explotación

    - **Descripción**: En esta fase, el atacante aprovecha las vulnerabilidades identificadas para ganar acceso inicial al sistema objetivo.

    - **Relación con auditorías**: Crítica para las auditorías de redes y sistemas, especialmente en la evaluación de vulnerabilidades y pruebas de penetración.

- #### Instalación

    - **Descripción**: El atacante instala herramientas adicionales o malware para mantener el acceso y facilitar futuras actividades maliciosas.

    - **Relación con auditorías**: Esencial para las auditorías de malware y la evaluación de la seguridad de los sistemas.

- #### Comando y control

    - **Descripción**: Se establece una comunicación bidireccional entre el sistema comprometido y la infraestructura del atacante.

    - **Relación con auditorías**: Importante para las auditorías de redes, especialmente en la detección de tráfico anómalo y conexiones no autorizadas.

- #### Acciones sobre los objetivos

    - **Descripción**: El atacante realiza las acciones finales para lograr sus objetivos, como exfiltración de datos, destrucción de sistemas, o extorsión.

    - **Relación con auditorías**: Relevante para todas las auditorías, ya que representa el impacto final de un ataque exitoso.

### Auditoría de Ingeniería Social

- **Fases relacionadas**: Reconocimiento, Weaponización y entrega
- **Servicios**: Evaluación de vulnerabilidades a phishing, spear phishing y whaling
- **Metodologías aplicables**: OSSTMM, ISSAF, Ethical Hacking

### Auditoría de Malware

- **Fases relacionadas**: Weaponización y entrega, Explotación, Instalación
- **Servicios**: Análisis de virus, gusanos, troyanos, ransomware, spyware y adware
- **Metodologías aplicables**: OSSTMM, ISSAF, Ethical Hacking, PTES

### Auditoría de Redes y Sistemas

- **Fases relacionadas**: Reconocimiento, Explotación, Instalación, Comando y control, Acciones sobre los objetivos
- **Servicios**:
  - Evaluación de vulnerabilidades a ataques DDoS
  - Pruebas de penetración para detectar vulnerabilidades a ataques Man-in-the-Middle
  - Auditoría de seguridad en aplicaciones web para prevenir inyecciones SQL y Cross-Site Scripting
  - Evaluación de la robustez de contraseñas y políticas de acceso para prevenir ataques de fuerza bruta
- **Metodologías aplicables**: OSSTMM, ISSAF, Ethical Hacking, PTES

## Evaluación de herramientas de monitorización
Bueno una vez analizada las metodologías que podemos encontrar en el campo del pentesting y haber elegido la nuestra propia basandonos en ellas continuaremos con las herramientas que utilizaremos. 

En este apartado, evaluaremos y seleccionaremos herramientas de auditoría, las cuales nos ayudarán a ejecutar nuestras pruebas de pentesting en los sistemas, bases de datos, aplicaciones webs..., de las empresas que contacten con nosotros.

Dentro de las diferentes herramientas que nos brinda el mercado podemos ver herramientas más enfocadas al ataque (las cuales simulan ataques cibernéticos para identificar vulnerabilidades en un sistemas) y de monitoreo (las cuales supervisan el comportamiento de la red o el sistema en busca de actividad sospechosa durante o ya después de un ataque). 

Ahora pasamos a definir las herramientas más adecuadas para los tipos de ataques de los que se encarga nuestra empresa. 

### Herramientas ataques de ingeniería social

#### Gophish
Esta aplicación es de código abierto y esta enfocada para ayudar a los profesionales de ciberseguridad y a las organizaciones a ejecutar campañas de pruebas de *pishing*.   
Esto nos permite evaluar la concienzación que tienen los empleados de una empresa sobre este tipo de ataques.   
Como punto a favor podemos ver que es multi-plataforma (Windows, Linux, macOS), gratuita, panel de control y métricas.

#### Cofense PhishMe
Es una plataforma comercial que está enfocada en la prevención y detección de atauqes de pishing mediante la capacitación de los empleados.
Lo bueno que tiene esta herramienta es que puedes efectuar simulaciones de pishing a la empresa, estos ataques podrán ser monitoreados en tiempo real con métricas.   
Si uno de los empleados cae en uno de los ataques se ofrecen módulos de capacitación para enseñar a estos a reconocer futuros ataques. Como único inconveniente es que la licencia es de pago. 

#### SET (Social-Engineer Toolkit)
Es una herramienta de código abierto muy utilizada en el ámbito de la ciberseguridad para las simulaciones de ingeniería social y evaluaciones de seguridad.   
Lo que diferencia esta aplicación son las herramientas que nos proponen. A parte de las simulaciones de pishing por correos electrónicos, también nos da la opción de crear sitios webs falsos donde con los que se podría probar a los empleados con el robo de sus credenciales.   
Como único inconveniente es que requiere de conocimientos previos debido a que su configuración es por consola de comandos. 
<br>
<br>
<br>
Una vez recabado información sobre estas aplicaciones vamos a compararlas siguiendo los siguientes parámetros. 

| Nombre         | Gophish    | Cofense | SET     |
|------------|------------------|-----------|--------|
| Precio | Gratuito (código abierto) | Pago (subscripción anual) | Gratuito (código abierto) |
| Plataforma | Windows, Linux, macOS | Basado en nube o local (Windows y Linux) | Linux (preferiblemente en Kali Linux) |
| Funcionalidad | Simulación phishing (email) | Simulación pishing (email) + concienciación | Simulación de pishing (email) + webs falsas (robo de credenciales) |
| Complejidad | Media (requiere un poco de conocimiento). Interfaz gráfica | Baja (intuitiva). Interfaz gráfica | Alta (requiere de bastantes conocimientos previos). Consola de comandos |
| Escalabilidad | Alta. Ideal para empresas de cualquier tamaño. | Muy alta, ideal para grandes organizaciones | Alta.  Adaptable pero enfocada en pruebas de penetración específicas |


### Herramientas ataques de malware

#### ClamAV
Esta es un antivirus de código abierto diseñado para detectar malware y otras amenazas. Se suele utilizar principalmente en servidores o sistemas Linux (aunque es multiplataforma) para analizar archivos en busca de gusanos, troyanos, virus y otros tipos de malware.   
Esta desarollado por Cisco y se ejecuta a través de la terminal. 

#### Cuckoo Sandbox
Es una herramienta de código abierto para el análisis dinámico de malware en entornos controlados. Su objetivo es ejecutar archivos en entornos seguros (una máquina virtual), para poder observar el comportamiento en tiempo real y generando un detallado análisis de cualquier posible actividad maliciosa.
Muy utilizado en ciberseguirdad para identificar y estudiar amenazas como pueden ser ransomware, troyanos y exploits. 
Para su instalación hay que tener cocnocimientos previos debido a que es un poco compleja. 

#### Volatility 
Es una herrmaienta avanzada de análisis de memoria forense de código abierto que se utiliza en ciberseguirdad para la investigación de incidentes y amenazas. 
Esta herramienta permite examinar el contenido de la RAM (la memoria volátil de un sistema), lo cuál es muy importante para el análisis forense y la detección de actividades maliciosas como podrían ser rootkits, spyware u otros malware residentes en memoria. 
También hace falta conocimentos previos para sacarle todo su potencial y es debido a que si ejecución es a través de terminal. 

#### Sysmon
Es una herramienta de monitoreo de eventos del sistemas desarrollada por Microsoft. Está ayuda a los equipos de seguridad a monitorear y registrar la actividad detallada de procesos, redes, archivos y cambios en el sistema a tiempo real.  
Se utiliza principalemtne para la detección y análisis de amenazas, proporcionando información valiosa sobre actividades de malware y comportamientos sospechosos. 

| Nombre     | ClamAV    | Cuckoo Sandbox | Volatility | Sysmon |
|------------|-----------|----------------|------------|--------|
| Precio     | Gratuito  | Gratuito       | Gratuito   |Gratuito|
| Plataforma | Multiplataforma (Windows, Linux, macOS)| Multiplataforma (principalmente Linux) | Multiplataforma (Windows, Linux, macOS) | Windows |
| Funcionalidad | Escaneo antivirus y antimalware | Análisis dinámico de malware en máquina virtual | Análisis de memoria forense | Monitoreo y resgitro de eventos |
| Complejidad | Media (Interfaz de consola, requiere configuración para entornos empresariales) | Alta (Requiere configuración técnica)| Alta (Requiere algo de experiencia en forense digital) | Media (necesita algunos conociemintos de logs)
| Escalabilidad | Escalable, pero depende del rendimiento del sistema y la red | Escalables dependiendo de los recursos del hardware y vistualización | Muy escalable, adecuado para incidencias de cualquier escala | Muy escalable, ideal para entornos empresariales |

Como podemos observar destaca que todas son gratuitas, algunas requieren de conocimientes para su instalación o uso (debido a que son en consola algunas). También su escalabilidad dependen algunas de la potencia de los medios tanto hardware como de red. 

### Herramientas ataques a sistemas y redes

#### Wireshark
Es una herramienta de análisis de protocolos de red de código abierto. Está se utiliza frecuentemente en redes y ciberseguridad para capturar y analizar el tráfico en una red en tiempo real.  
Wireshark nos permite analizar todos los paquetes que circulan en una red para identificar vulnerabilidades, problemas de rendimiento y actividades sospechosas.  
Para utilizarla hay que tener conocimientos de redes para poder interpretar la información. 

#### Nmap
Es una herramienta de código abierto para el escaneo y mapeo de redes, ampliamente utilizada enm ciberseguridad para identificar servicios, puertos abiertos y dispositivos de una red.   
Es de las herramientas para auditoría más utilizadas debiod a su flexibilidad, potencia y eficiencia. También hay que tener algun que otro tipo de conocimiento.

#### Wanguard
Es una solución avanzada de mitigación y monitoreo de ataques DDoS y tráfico no deseado. Esta aplicación está diseñada para proteger las redes empresariales y las infraestructuras de centros de datos contra amenazas basadas en el tráfico y ataques de denegación de servicio. 
Wanguard destaca por su capacidad para identificar y detener el tráfico malicioso, preservando así la seguridad y estabilidad de la red.   
Es una herramienta de pago y que requiere de conocimentos previos sobre redes. 

#### Metasploit
Es una plataforma de código abierto la cual se diseño para facilitar pruebas de penetración y explotación de vulnerabilidades en las redes, servicios y aplicaciones de un sistema.     
Esta permite simular ataques reales para poder indentificar y solucionar debilidades en la seguridad de un sistema antes de que puedan ser explotados por los atacantes.  
Esta aplciación es altamente utilizada en cibersguirdad debido a su ambplia biblioteca de exploits, su personalización y que es multiplataforma. Pero como inconveniente es que se utiliza a través de la línea de comandos y la personalización de los atauqes se crean en scripts. 

#### SQLMap
Es una herramienta de código abierto que permite detectar y explotar vuknerabilidades de inyección SQL en aplicaciones web. Podremos automatizar procesos de prueba para identificar si una base de datos de datos puede tener vulnerabilidades contra este tipo de ataques de inyección SQL.   
Es muy utilizada para realizar pruebas de pentración en bases de datos y detectar posibles vulnerabilidades contra estos ataques que son de los más comunes y dañinos. 

#### BruteX
Es una herramienta automatizada de fuerza bruta. Esta diseñada para relaizar múltiples ataques a servicios comunmente usados como pueden ser SSH, servicios web, FTP... Automatiza procesos de búsqueda y prueba de credenciales en redes.   
Es utilizada en el ámbito de la ciberseguridad para realizar ataques de prueba de manera efiiente y rápida. 

****

Esta tabla resume los conocimientos técnicos y la interfaz de cada herramienta para su uso en pruebas de seguridad en diferentes niveles de complejidad.

| Herramienta  | Costo | Plataforma  | Funcionalidad | Complejidad | Escalabilidad|
|----------|-------|---------|--------|-------|---|
| Wireshark | Gratuita | Windows, Linux, macOS | Análisis de tráfico de red en tiempo real, captura y filtrado de paquetes | Media (Interfaz gráfica inuitiva). Requiere conocimeintos en redes para un buen análisis | Alta. Permite analizar grandes redes, aunque depende de los recursos locales|
|Nmap| Gratuita | Windows, Linux, macOS | Escaneo y mapeo de redes, y detección de puertos o servicios abiertos | Media (Interfaz de consola). Neceita el uso de scripts para configuración y personalización | Alta. Adaptable para pequeñas o grandes redes|
| Wanguard | Pago | Linux | Detección y mitigación de ataques DDoS | Alta (Interfaz de consola). Configuraciones avanzadas | Muy alta. Ideal para grandes centros de datos con gran volumen de tráfico|
| Metasploit | Gratuita y versión de pago | Windows, Linux, macOS| Pruebas de penetración y explotación de vulnerabilidades| Alta (Interfaz gráfica en version de pago). Requiere conocimientos en ciberseguridad| Alta. Ampliamente escalable en grandes redes | 
| SQLMap | Gratuita | Windows, Linux, macOS | Escaneo y explotación de inyecciones SQL| Media (Interfaz de consola). Conocimientos básicos en base de datos | Media. Excelente para sitios individuales, y posibilidad de escalabilidad reducida para sistemas con mas de una base de datos| 
|BruteX| Gratuita| Linux | Ataques de fuerza bruta a servicios de red | Media (Interfaz de consola). Fácil de usar pero con previos conociemientos en redes| Media. Adecuada para redes pequeñas, con limitaciones para redes muy grandes|

## Conclusiones

## Fuentes
[Ciberseguridad: Tipos de ataque y en qué consisten](https://www.iebschool.com/blog/ciberseguridad-ataques-tecnologia/)

[Ataques informáticos: Causas y 15 Tipos de Ciberataques](https://winempresas.pe/blog/ataques-informaticos-causas-y-12-tipos-de-ciberataques)

[Top mejores aplicaciones para pruebas de pishing](https://geekflare.com/es/phishing-simulation-software/)

[10 herramientas de hacking ético](https://www.tokioschool.com/noticias/herramientas-hacking-etico/)
