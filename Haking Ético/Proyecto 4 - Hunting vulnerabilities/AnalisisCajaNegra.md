# Informe de análisis de Caja Negra

![Portada](./img/portada.png)

- **Código**: Proyecto 04
- **Nombre**: Hunting vulnerabilities
- **Equipo investigador**: Grupo 3
- **Fecha**: 15/03/2025

## Índice

1. [Resumen Ejecutivo](#1-resumen-ejecutivo)
2. [Introducción](#2-introducción)  
   2.1. [Antecedentes](#21-antecedentes)  
   2.2. [Objetivo](#22-objetivo)  
   2.3. [Alcance](#23-alcance)  
   2.4. [Incidencias](#24-incidencias)
3. [Metodología](#3-metodología)
4. [Resultados Obtenidos](#4-resultados-obtenidos)
5. [Conclusiones y Recomendaciones](#5-conclusiones-y-recomendaciones)

## 1. Resumen Ejecutivo

Este resumen ejecutivo detallará los resultados obtenidos de una evaluación de vulnerabilidades en dos servidor (Windows y Linux ) de la empresa SecureLogistics. El escaneo se llevó a cabo realizando un escaneo pasivo (sin credenciales) con la aplicación Nessus. 

Se detectaron numerosas vulnerabilidades en ambos escaneos de los dos servidores. Lo más destacable es la detección de varias vulnerabilidades críticas y altas. Esto es importante debido a que muchas de ellas permiten la ejecución de código de forma remota, y la posible vulneración de la red de los servidores y los datos que pueda contener. Estas vulnerabilidades en su mayoría vemos qu estan relacionadas con Apache, SSL, PHP, RDP (el servicio de escritorio remoto de Windows) y OpenSSH. 

Se recomienda para solventar en la mayoría de casos una actualización de los servicios para utilizar los últimos parches de seguridad, aunque en otras hay que realizar una comprobación de la correcta configuración de los servicios. Estas medidas son esenciales para poder proteger la integridad de los servidores, la red y sus datos, y recomendamos que se hagan escaneos de manera rutinaria para localizar futuras vulnerabilidades. 


## 2. Introducción

### 2.1 Antecedentes

La empresa de logística SecureLogistics nos ha solicitado una evaluación de vulnerabilidades de dos de sus servidores. Tienen un presupuesto limitado para realizar las pruebas de seguridad y necesitan una evaluación rápida para identificar cualquier vulnerabilidad.

### 2.2 Objetivo

Para la realización de esta tarea usaremos herramientas de escaneo para evaluar el nivel de las vulnerabilidades (criticidad) y poder proponer soluciones con las que solventar dichas vulnerabilidades. 

### 2.3 Alcance

Como ya dijimos anteriormente los análisis se van a realizar a dos servidores de la empresa: un Windows Server 2008 y un Ubuntu Server 14.04.

### 2.4 Incidencias

El análisis tuvimos que plantearlo para hacerlo en un entorno local, para asegurarnos que no iba a dar ningún posible fallo de escaneo.

## 3. Metodología

Para este ejercicio hemos utilizado una herramientas basada en detección de vulnerabilidades la cuál la hemso dividido en 3 fases. Hemos querido hacer una metodología estructurada, en la que seguimos unas fases y hacemos uso de harramientas especializadas. 

- Fase 1 - Recopilación de información: 
   **Objetivos**: Lo primero que haremos es determinar cuales van a ser nuestros objetivos, a los que vamos a realizarles las pruebas. 
   - Determinaremos si el escaner se realizara con credenciales o sin ellas (caja blaca o caja negra).
   - La dirección IP del objetivo. 

- Fase 2 - Escaneo de puertos y enumeración de servicios:
   Haremos una evaluación de los objetivos ya identificados para realizar posteriormente el escaner. 
   - **Herramientas**: Usaremos la herramientas Nessus, es un programa de escaneo de vulnerabilidades en diversos sistemas operativos. 
   - **Proceso**:  
      La propia herramientas de Nessus nos permite a través de la IP del objetivo realizar un escaneo de puertos para ver que servicios tiene abiertos al exterior.   
      Nos aparecerán al realizar el escaner consultad "Info" las cuales nos avisan de que hay un servicio activo. 

- Fase 3 - Evaluación de vulnerabilidades
   Detectaremos vulnerabilidades potenciales en los equipos analizados. 
   - **Herramienta**: De nuevo utilizaremos Nessus. 
   - **Proceso**: Nessus tiene la funcionalidad de escanear los servicios en busca de vulnerabilidades que contiene en su base de datos. 
      Lo primero seleccionaremos el equipo objetivo para analizar.    
      Utilizaremos el escaner de vulnerabilidades que nos brinda Nessus.
      Automáticamente Nesssus nos clasificará las vulnerabilidades por grupos, calculando su nivel de riesgo, su CVV, etc. A parte también nos proporcionará al pinchar en la vulnerabilidad las posibles soluciones con las que solventar la vulnerabilidad. 


## 4. Resultados Obtenidos

Después de realizar los análisis de los dos servidores hemos identificado las siguiente vulnerabilidades: 

- ### Windows Server 2008

***

   #### Vulnerability in DNS Resolution

   - Explicación:  fallo en la resolución DNS que permitía ejecución remota de código. 
   - Gravedad: Crítica
   - CVE: CVE-2011-0657
   - CVSS: 10.0
   - Sistemas afectados:
      - Windows XP
      - Windows Server 2003 
      - Windows Vista
      - Windows Server 2008
      - Windows 7 
   - Solución: Microsoft lanzo parches de seguridad para todos los SO afectados. 

   #### PHP 5.3.x < 5.3.15 Multiple Vulnerabilities

- Explicación:  vulnerabilidad que afecta a componentes de PHP y permite la ejecución de código arbitrario y el acceso no autorizado a directorios restringidos. 
   - Gravedad: Crítica
   - CVE: CVE-2012-2688, CVE-2012-3365
   - CVSS: 10.0
   - Sistemas afectados: Todas las versiones de PHP 5.3.x anteriores a 5.3.15
   - Solución: Actualizar PHP a la versión 5.3.15 o posterior.

   #### Apache HTTP Server SEoL (2.1.x <= x <= 2.2.x)

- Explicación: la versión de Apache HTTP Server no tiene soporte para esas versión.  
   - Gravedad: Crítica
   - CVSS: 10.0
   - Sistemas afectados: Todas las versiones de Apache HTTP Server desde 2.1.x hasta 2.2.x
   - Solución: Actualizar a una versión de Apache HTTP Server que este soportada

   #### Unsupported Windows OS (remote)

- Explicación:  vulnerabilidad que afecta a componentes de PHP y permite la ejecución de código arbitrario y el acceso no autorizado a directorios restringidos. 
   - Gravedad: Crítica
   - CVSS: 10.0
   - Sistemas afectados: Versiones antiguas de Windows Server. 
   - Solución: Actualizar a versiones de Windows Server con soporte activo. 

   #### Microsoft RDP RCE (CVE-2019-0708) (BlueKeep) (uncredentialed check)

- Explicación: vulnerabilidad llamada BlueKeep permite la ejecución remota de código en el servicio de RDP de Windows.
   - Gravedad: Crítica
   - CVE: CVE-2012-2688, CVE-2012-3365
   - CVSS: 9.8
   - Sistemas afectados: Windows XP, Windows Server 2003, Windows 7, Windows Server 2008
   - Solución: Instalar las actualizaciones de seguridad proporcionadas por Microsoft para los sistemas operativos afectados

   #### Apache 2.2.x < 2.2.34 Multiple Vulnerabilities

- Explicación: vulnerabilidades que permiten a atacantes remotos no autenticados realizar diversas acciones maliciosas
   - Gravedad: Crítica
   - CVE: CVE-2017-3167, CVE-2017-3169, CVE-2017-7668, CVE-2017-7679, CVE-2017-9788
   - CVSS: 9.8
   - Sistemas afectados: Apache HTTP Server 2.2.x < 2.2.34
   - Solución: Actualizar a Apache versión 2.2.34 o posterior

   #### SSL RC4 Cipher Suites Supported (Bar Mitzvah)

 - Explicación: vulnerabilidades llamada Bar Mitzvah que permite a atacantes realizar ataques de recuperación de texto plano
   - Gravedad: Alta
   - CVE: CVE-2013-2566, CVE-2015-2808
   - CVSS: 7.5
   - Sistemas afectados: Servidores que soportan el uso de RC4 en suites de cifrado SSL/TLS
   - Solución: Reconfigurar la aplicación para evitar el uso de cifrados RC4 y considerar el uso de TLS

   ####  SNMP Agent Default Community Name (public)

 - Explicación: vulnerabilidad permite a un atacante obtener la cadena de comunidad predeterminada ("public") del servidor SNMP remoto. 
   - Gravedad: Alta
   - CVE: CVE-2013-2566, CVE-2015-2808
   - CVSS: 7.5
   - Sistemas afectados:  Dispositivos con SNMP habilitado usando la comunidad predeterminada "public"
   - Solución: Deshabilitar el servicio SNMP si no se usa, filtrar paquetes UDP entrantes al puerto SNMP, o cambiar la cadena de comunidad predeterminada

   #### Remote Desktop Protocol Server Man-in-the-Middle Weakness

 - Explicación: vulnerabilidad permite a un atacante realizar un ataque de MitM en conexiones RDP. 
   - Gravedad: Media
   - CVE: CVE-2005-1794
   - CVSS: 6.5
   - Sistemas afectados:  Servidores Windows que ejecutan RDP
   - Solución: Forzar el uso de SSL como capa de transporte y/o habilitar la autenticación de nivel de red  

   #### PHP < 7.3.28 Email Header Injection

 - Explicación: vulnerabilidad permite a un atacante remoto no autenticado inyectar encabezados de correo electrónico maliciosos
   - Gravedad: Media
   - CVE: CVE-2021-21705
   - CVSS: 5.3
   - Sistemas afectados:  Versiones de PHP anteriores a 7.3.28
   - Solución: Actualizar a PHP versión 7.3.28 o posterior

- ### Ubuntu Server 14.04

   #### Drupal Coder Module Deserialization RCE

 - Explicación: vulnerabilidad permite a un atacante remoto no autenticado ejecutar código PHP arbitrario en el servidor web que ejecuta Drupal con el módulo Coder vulnerable.
   - Gravedad: Crítica
   - CVE: CVE-2016-10045
   - CVSS: 9.8
   - Sistemas afectados: Drupal con el módulo Coder instalado, versiones anteriores a 7.x-1.3 / 7.x-2.6
   - Solución: Actualizar el módulo Coder a la versión 7.x-1.3 / 7.x-2.6 o posterior

   #### PHP Unsupported Version Detection

- Explicación: vulnerabilidad surge porque la instalación de PHP en el servidor remoto está utilizando una versión que ya no recibe soporte oficial
   - Gravedad: Crítica
   - CVSS: 10.0
   - Sistemas afectados: Instalaciones de PHP en versiones no soportadas 
   - Solución: Actualizar a una versión de PHP actualmente soportada

   #### PHP 5.4.x < 5.4.38 Multiple Vulnerabilities (GHOST)

 - Explicación: múltiples vulnerabilidades que permiten ejecutar código arbitrario, DoS y exposición de información sensible del sistema. 
   - Gravedad: Crítica
   - CVE: CVE-2014-9705, CVE-2015-0235 (GHOST), CVE-2015-0273
   - CVSS: 9.8
   - Sistemas afectados: Instalaciones de PHP 5.4.x anteriores a 5.4.38
   - Solución: Actualizar a PHP versión 5.4.38 o posterior

   #### PHP 5.4.x < 5.4.43 Multiple Vulnerabilities (BACKRONYM)

 - Explicación: estas vulnerabilidades pdrían comprometer gravemente el sistema, incluyendo la ejecución de código malicioso, denegación de servicio y divulgación de datos sensibles
   - Gravedad: Crítica
   - CVE: CVE-2014-9705, CVE-2015-0235 (GHOST), CVE-2015-0273
   - CVSS: 9.8
   - Sistemas afectados: PHP 5.4.x antes de la versión 5.4.43
   - Solución: Actualizar a PHP versión 5.4.43 o posterior

   #### Drupal Database Abstraction API SQLi

 - Explicación: vulnerabilidad afecta a la API de abstracción de base de datos en Drupal Core
   - Gravedad: Alta
   - CVE: CVE-2014-3704
   - CVSS: 7.5
   - Sistemas afectados: Drupal Core 7.x antes de la versión 7.32
   - Solución: Actualizar Drupal a la versión 7.32 o posterior

   #### SSL Medium Strength Cipher Suites Supported (SWEET32)

 - Explicación: vulnerabilidad que permite que un atacante pueda explotar esta debilidad para recuperar pequeñas porciones de texto plano cifrado
   - Gravedad: Alta
   - CVE: CVE-2016-2183
   - CVSS: 7.5
   - Sistemas afectados: Servidores que soportan cifrados SSL/TLS de fuerza media
   - Solución: Reconfigurar la aplicación afectada para evitar el uso de cifrados de fuerza media

   #### SSL Self-Signed Certificate

- Explicación: vulnerabilidad surge cuando un servidor utiliza un certificado SSL autofirmado en lugar de uno emitido por una Autoridad Certificadora (CA) reconocida. 
   - Gravedad: Media
   - CVSS: 6.5
   - Sistemas afectados: Servidores que utilizan certificados SSL autofirmados
   - Solución: Adquirir o generar un certificado SSL apropiado emitido por una Autoridad Certificadora

   #### SMB Signing not required

- Explicación: La falta de firma en los mensajes SMB permite a un atacante remoto no autenticado realizar ataques de MITM
   - Gravedad: Media
   - CVSS: 5.3
   - Sistemas afectados: Servidores SMB con la firma de mensajes deshabilitada o no requerida
   - Solución: Habilitar y requerir la firma de mensajes SMB en la configuración del servidor y cliente


## 5. Conclusiones y Recomendaciones

Una vez hemos realizado el análisis de vulnerabilidades de ambos servidores. Podemos recoger que se han detectado numerosas vulnerabilidades en ambos servidores en diferentes servicios. 
Esto desencadena en la poca confianza y fiabilidad que generan estos servidores.

Durante la explicación de las vulnerabilidades nos ido fijando en que la mayoría eran por usos de servicios desactualizados o mal configurados. Es por ellos que aconsejamos a la empresa que debido a que hay servicios que carecen de soporte y actualizaciones, por lo que la solución más óptima sería actualizar los dos servidores a versiones más actuales, el Windows Server 2008 a la versión 2019 o 2022 y el Ubuntu Server a la versión 22 o 24. 

***

Documento redactado por el Grupo 3, compuesto por:

- Israel Valderrama
- Alejandro Seoane
- Víctor Jiménez
- Nicolas Ruiz
- Alejandro Díaz
