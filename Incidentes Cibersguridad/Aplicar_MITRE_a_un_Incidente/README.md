## Descripción del incidente
En mayo de 2021, la empresa estadounidense Colonial Pipeline, sufrió una parálisis temporal debido a un ransomware, que cortó el suministro de combustible a gran parte de Estados Unidos.

El grupo de ciberdelincuentes *Darkside*, coló un ransomware en la infraestructura de la empresa debido a unas credenciales de VPN filtradas, con lo que consiguieron cifrar los sistemas internos para exigir un pago.

La empresa acabó pagando 4.4 millones de dólares en Bitocin, aunque pudieron recuperar parte de ella gracias al FBI.

## Análisis MITRE ATT&CK

| **Táctica**          | **Técnica usada**                                    |
| -------------------- | ---------------------------------------------------- |
| Initial Access       | T1078 – Valid Accounts (uso de credenciales robadas) |
| Execution            | T1059 – Command and Scripting Interpreter            |
| Persistence          | T1547 – Boot or Logon Autostart Execution            |
| Privilege Escalation | T1068 – Exploitation for Privilege Escalation        |
| Defense Evasion      | T1562 – Impair Defenses                              |
| Command and Control  | T1071 – Application Layer Protocol                   |
| Exfiltration         | T1041 – Exfiltration Over C2 Channel                 |
| Impact               | T1486 – Data Encrypted for Impact (ransomware)       |

### [1. Initial Access T1078 – Valid Accounts (uso de credenciales robadas)](https://attack.mitre.org/techniques/T1078/)

El grupo *Darkside* accedió a las credenciales de la VPN en la **DarkWeb**, estás estaban ahí debido a un leakeo de contraseña de parte de uno de los trabajadores, el cual compartía la contraseña con ese servicio vulnerado y la VPN.

### [2. Execution T1059 – Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)

Una vez dentro de la red, los delincuentes estuvieron durante 5 días sin ser detectados, utilizando herramientas de **PowerShell** y **PsExec** como payloads y backdoors y robando información crítica de la empresa.

### [3. Persistence T1547 – Boot or Logon Autostart Execution](https://attack.mitre.org/techniques/T1547/)

Para mantener el acceso, crearon **scripts** y **payloads** para crear persistencia en los sistemas y poder volver a entrar en todo momento, sin importar los reinicios y cierres de sesión.

### [4. Privilege Escalation T1068 – Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/)

Utilizaron vulnerabilidades conocidas en los sistemas desactualizados para escalar privilegios, concretamente, aprovecharon las vulnerabiliades **CVE-2019-5544 y CVE-2020-3992 en VMware ESXi**, que les permitía ejecutar código remoto con privilegios de administrador.

### [5. Defense Evasion T1562 – Impair Defenses](https://attack.mitre.org/techniques/T1562/)

Como dijimos antes, *Darkside* estuvo conectado a la red de la compañía durante 5 días sin ser detectados, esquivando todos los controles de detección de intrusos, que a estas alturas, me creo que ni tuvieran alguno.

### [6. Command and Control T1071 – Application Layer Protocol](https://attack.mitre.org/techniques/T1071/)

Para mantener la comunicación con los sistemas vulnerados, los atacantes utilizaron los protocolos HTTP y HTTPS para camuflar el tráfico malicioso entre el tráfico real.

### [7. Exfiltration T1041 – Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041/)

*Darkside* filtró **100GB** de datos críticos de la empresa a través de los canales creados, de esta forma, pudieron extorsionar a la empresa con publicar la información si no hacían el pago.

### [8. Impact T1486 – Data Encrypted for Impact (ransomware)](https://attack.mitre.org/techniques/T1486/)

Finalmente, activaron el ransomware *Darkside* creados por ellos mismos, cifrando los sistemas esenciales de Colonial Pipeline, provocando la interrupción del trabajo y producción. De esta forma, la empresa se vió obligada a pagar 4.4 millones de dolares en bitcoin como rescate.

## Herramientas y vectores usados

### 1. Acceso a la infraestructura informática

- Método: se accedió a través de unas credenciales filtradas en una VPN que utilizaba la empresa para que los empleados se conectasen de forma remota sin autenticación multifactor.
- Herramientas utilizadas: para encontrar las credenciales los ciberdelincuentes utilizaron bases de datos filtradas en la Dark Web.
- Técnica MITRE: [T1078 – Valid Accounts](https://attack.mitre.org/techniques/T1078/)

### 2. Navegación por el sistema

- Una vez consiguieron acceso al sistema hiceron uso de comnados de PowerSHell y CMD para moverse por el sistema y ejecutar cargas maliciosas.
- Técnica MITRE: [T1059 - Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)

### 3. Cifrado de Archivos y Extorsión (Ransomware)

- Para atacar a los archivos de la empresa con un virus utilizaron `DarkSide Ransomware` un malware personalizado que cifraba archivos críticos y dejaba notas de rescate. 
- Técnica MITRE: [T1486 – Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486/)

## Evaluación de defensa

### ¿Qué falló?

El grupo accedió a la red de la empresa a traves de una filtración de credenciales de la VPN, igualmente, esto se podría haber evitado utilizando autenticación multifactor, lo que facilitó mucho el vector de ataque.

La empresa fue incapaz de detectar el movimiento de los atacantes en la red, y tampoco pudieron detectar la ejecución del virus a tiempo. De esta forma, el ransomware afectó a todos los sistemas de la red, lo cual indica que la red estaba mal segmentada.

Cuando la compañía se enteró del ataque, ya era demasiado tarde, y el impacto fue tan grave, que decidieron pagar el rescate.

### Técnicas MITRE de mitigación y detección

| Categoría        | Técnica MITRE ATT&CK              | Mitigación / Detección                  |
| ---------------- | --------------------------------- | --------------------------------------- |
| Initial Access   | T1078 – Valid Accounts            | M1032 – Multi-factor Authentication     |
| Execution        | T1059 – Command & Scripting       | M1040 – Behavior Monitoring             |
| Lateral Movement | T1021 – Remote Services           | M1031 – Network Segmentation            |
| Impact           | T1486 – Data Encrypted for Impact | M1053 – Data Backup + M1049 – Antivirus |
| Defense Evasion  | T1562 – Impair Defenses           | M1038 – Execution Prevention            |

#### 1. Multi-factor Authentication

Implementar MFA (Autenticación Multifactor) en todos los accesos remotos y servicios críticos de la empresa.

#### 2. Behavior Monitoring

Controlar quién entra en la red, usando ubicaciones geográficas o identificadores MAC, y bloquear todo acceso desconocido.

#### 3. Network Segmentation

Separar la red en varias VLANs, diferenciando entre zonas críticas y comunes, para que en futuros incidentes no se propaguen por toda la infraestructura.

#### 4. Data Backup + Antivirus

Realizar copias de seguridad periódicas para en caso de peridada de datos, mitigar los daños; e implementar buenos antivirus capaces de detectar y prevenir malwares.

#### 5. Execution Prevention

Bloquear la ejecución de código en un sistema a través del control de aplicaciones y/o el bloqueo de scripts.

## Lecciones aprendidas y correlación con ASVS u otros marcos (opcional)
Qué aporta MITRE a la respuesta ante incidentes.

Qué se debería implementar tras el incidente.

Breve reflexión final, con enfoque técnico.

## Fuentes

https://attack.mitre.org/

https://www.trendmicro.com/es_es/research/21/e/what-we-know-about-darkside-ransomware-and-the-us-pipeline-attac.html

https://www.securin.io/articles/darkside-the-ransomware-that-brought-a-us-pipeline-to-a-halt/

https://en.wikipedia.org/wiki/Colonial_Pipeline_ransomware_attack

https://www.metabaseq.com/threat/inside-darkside-the-ransomware-that-attacked-colonial-pipeline/
