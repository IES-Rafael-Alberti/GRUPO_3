# Informe de análisis de Caja Blanca

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

Este informe presenta los resultados del análisis de vulnerabilidades en modo caja blanca realizado a los servidores Windows y Linux de la empresa SecureLogistics.  
El escaneo lo ejecutamos con las credenciales (credenciales: vagrant/vagrant) mediante la aplicación de Nessus , permitiendo una evaluación extensa de las configuraciones internas y vulnerabilidades no visibles dedsde un análisis externo de caja negra.

## 2. Introducción

### 2.1 Antecedentes

La empresa de logística SecureLogistics nos ha solicitado una evaluación de vulnerabilidades de dos de sus servidores. Esta vez quieren que realicemos el analisis con los credenciales para ver si el análisis detecta más vulnerabilidades que las que se han encontrado sin las credenciales.

### 2.2 Objetivo

Para la realización de esta tarea usaremos herramientas de escaneo para evaluar el nivel de las vulnerabilidades (criticidad) y poder proponer soluciones con las que solventar dichas vulnerabilidades. Buscaremos evaluar los servicios externos e internos de los servidores debido a que tendremos acceso para escanear por dentro de los servidores.

### 2.3 Alcance

Como ya dijimos anteriormente los análisis se van a realizar a dos servidores de la empresa: un Windows Server 2008 y un Ubuntu Server 14.04.

### 2.4 Incidencias

El análisis tuvimos que plantearlo para hacerlo en un entorno local, para asegurarnos que no iba a dar ningún posible fallo de escaneo.

## 3. Metodología

Para este ejercicio hemos utilizado una herramientas basada en detección de vulnerabilidades la cuál la hemos dividido en 3 fases. Hemos querido hacer una metodología estructurada, en la que seguimos unas fases y hacemos uso de harramientas especializadas.

- Fase 1 - Recopilación de información:
   **Objetivos**: Lo primero que haremos es determinar cuales van a ser nuestros objetivos, a los que vamos a realizarles las pruebas.
   - Determinaremos si el escaner se realizara con credenciales o sin ellas (caja blaca o caja negra).
   - La dirección IP del objetivo.
   - Nos proporcionarán los credenciales de acceso de los dos servidores.

- Fase 2 - Escaneo de puertos y enumeración de servicios:
   Haremos una evaluación de los objetivos ya identificados para realizar posteriormente el escaner.
   - **Herramientas**: Usaremos la herramienta Nessus, es un programa de escaneo de vulnerabilidades en diversos sistemas operativos.
   - **Proceso**:  
      La propia herramientas de Nessus nos permite a través de la IP del objetivo realizar un escaneo de puertos para ver que servicios tiene abiertos al exterior.
      La aplicación nos permite en una pestaña seleccionar si queremos hacer el escaner con los credenciales.
      Nos aparecerán al realizar el escaner consultad "Info" las cuales nos avisan de que hay un servicio activo.

- Fase 3 - Evaluación de vulnerabilidades
   Detectaremos vulnerabilidades potenciales en los equipos analizados.
   - **Herramienta**: De nuevo utilizaremos Nessus.
   - **Proceso**: Nessus tiene la funcionalidad de escanear los servicios en busca de vulnerabilidades que contiene en su base de datos.
      Lo primero seleccionaremos el equipo objetivo para analizar
      Utilizaremos el escaner de vulnerabilidades que nos brinda Nessus.
      Automáticamente Nesssus nos clasificará las vulnerabilidades por grupos, calculando su nivel de riesgo, su CVV, etc. A parte también nos proporcionará al pinchar en la vulnerabilidad las posibles soluciones con las que solventar la vulnerabilidad.


## 4. Resultados Obtenidos

Después de realizar los análisis de los dos servidores hemos identificado las siguiente vulnerabilidades:

- ### Windows Server 2008

Como hemos realizado un análisis de caja blanca del mismo servidor las vulnerabilidades que antes ha encontrado no vamos a volver a mencionarlas. El escaneo con credenciales nos han dado numerosas detecciones por lo que pondremos una cuantas que nos parezcan interesantes y las demas las dejaremos en el [Anexo](AnexosAnálisis.md)
***

#### KB4601363: Windows 7 and Windows Server 2008 R2 February 2021 Security Update

- Explicación: Actualización de seguridad que corrige múltiples vulnerabilidades críticas, incluyendo elevación de privilegios, denegación de servicio y ejecución remota de código en Windows 7 y Windows Server 2008 R2.
- Gravedad: Crítica
- CVE: CVE-2020-1472, CVE-2021-24080, CVE-2021-24086, CVE-2021-1727, CVE-2021-24102, CVE-2021-24103, CVE-2021-25195, CVE-2021-1722, CVE-2021-24074, CVE-2021-24077, CVE-2021-24078, CVE-2021-24083, CVE-2021-24088, CVE-2021-24094, CVE-2021-1734
- CVSS: 10.0
- Sistemas afectados: Windows 7 y Windows Server 2008
- Solución: Aplicar la actualización de seguridad KB4601363 o la actualización acumulativa KB4601347.

#### Apache Log4j SEoL (<= 1.x)

- Explicación: Versiones de Apache Log4j 1.x y anteriores que ya no reciben mantenimiento ni parches de seguridad, lo que puede resultar en vulnerabilidades no corregidas.
- Gravedad: Crítica
- CVSS: 10.0
- Sistemas afectados: Apache Log4j versión 1.x y anteriores
- Solución: Actualizar a una versión de Apache Log4j que tenga soporte actualmente.

#### Apache Struts 2.5.0 < 2.5.33 / 6.0.0 < 6.3.0.2 Remote Code Execution (S2-066)

- Explicación: Vulnerabilidad que permite a un atacante manipular parámetros de carga de archivos para realizar recorrido de rutas y potencialmente ejecutar código remoto.
- Gravedad: Crítica
- CVE: CVE-2023-50164
- CVSS: 9.8
- Sistemas afectados: Apache Struts versiones anteriores a 2.5.33 o 6.3.0.2
- Solución: Actualizar a Apache Struts versión 2.5.33, 6.3.0.2 o posterior, o aplicar la solución alternativa mencionada en el boletín de seguridad del proveedor.

#### Microsoft RDP RCE (CVE-2019-0708) (BlueKeep)

- Explicación: Vulnerabilidad de ejecución remota de código en el Protocolo de Escritorio Remoto (RDP) que permite a un atacante no autenticado ejecutar código arbitrario mediante solicitudes especialmente diseñadas.
- Gravedad: Crítica
- CVE: CVE-2019-0708
- CVSS: 9.8
- Sistemas afectados: Windows XP, 2003, 2008, 7 y 2008
- Solución: Microsoft ha lanzado parches para los sistemas operativos afectados. Se recomienda aplicar estas actualizaciones de seguridad inmediatamente.

#### Elasticsearch ESA-2015-06

- Explicación: Vulnerabilidad en versiones de Elasticsearch anteriores a 1.6.1 que permite la ejecución remota de código mediante un ataque diseñado en su protocolo de transporte.
- Gravedad: Crítica
- CVE: CVE-2015-5377
- CVSS: 9.8
- Sistemas afectados: Elasticsearch versiones anteriores a 1.6.1
- Solución: Actualizar a Elasticsearch versión 1.6.1, 1.7.0 o posterior. Alternativamente, asegurar que solo aplicaciones confiables tengan acceso al puerto del protocolo de transporte.

#### MySQL 5.5.x < 5.5.62 Multiple Vulnerabilities

- Explicación: Múltiples vulnerabilidades en versiones de MySQL 5.5.x anteriores a 5.5.62, detalladas en el aviso de actualización crítica de octubre de 2018.
- Gravedad: Crítica
- CVE: Múltiples
- CVSS: 9.8
- Sistemas afectados: MySQL versiones 5.5.x anteriores a 5.5.62
- Solución: Actualizar a MySQL versión 5.5.62 o posterior.

#### Microsoft Windows SMB Server (2017-10) Multiple Vulnerabilities

- Explicación: Vulnerabilidades en el servidor SMBv1 de Windows que permiten la ejecución remota de código y denegación de servicio mediante solicitudes especialmente diseñadas.
- Gravedad: Alta
- CVE: CVE-2017-11780, CVE-2017-11781
- CVSS: 7.0 
- Sistemas afectados: Windows Server 2008, 7, 2012, 10 y 2016
- Solución: Aplicar los parches de seguridad lanzados por Microsoft para los sistemas operativos afectados.

#### 7-Zip < 23.00 Multiple Vulnerabilities

- Explicación: Vulnerabilidades de ejecución remota de código en 7-Zip debido a un desbordamiento de enteros y una escritura fuera de límites, explotables al abrir archivos maliciosos.
- Gravedad: Alta
- CVE: CVE-2023-31102, CVE-2023-40481
- CVSS: 6.9
- Sistemas afectados: Versiones de 7-Zip anteriores a 23.00
- Solución: Actualizar 7-Zip a la versión 23.00 o posterior.

#### Oracle Java SE Multiple Vulnerabilities (April 2023 CPU)

- Explicación: Múltiples vulnerabilidades en Oracle Java SE y GraalVM Enterprise Edition que afectan a componentes como JSSE, Swing y Hotspot, permitiendo acceso no autorizado a datos críticos y modificaciones no autorizadas.
- Gravedad: Alta
- CVE: CVE-2023-21930, CVE-2023-21939, CVE-2023-21954
- CVSS: 6.9
- Sistemas afectados: Varias versiones de Oracle Java SE y GraalVM Enterprise Edition
- Solución: Aplicar los parches de seguridad según el aviso de actualización crítica de Oracle de abril de 2023.

- ### Ubuntu Server 14.04

Al igual que con el escaneo de Windows al ejecutar un escaneo con credenciales en el servidor Ubuntu nos va a detectar muchas más vulnerabilidades por lo que vamos a mencionar varias de ellas pero no todas. El informe de todas la vulnerabilidades detectadas se podrá encontrar en el [Anexo](AnexosAnálisis.md)

#### Canonical Ubuntu Linux SEoL (14.04.x)

- Explicación: Según su versión, Canonical Ubuntu Linux es 14.04.x. Esta versión ya no cuenta con soporte del proveedor, lo que implica que no se lanzarán nuevos parches de seguridad. Como resultado, puede contener vulnerabilidades de seguridad que no serán corregidas.
- Gravedad: Crítica
- CVSS: 10.0
- Sistemas afectados: Canonical Ubuntu Linux 14.04.x
- Solución: Actualizar a una versión de Canonical Ubuntu Linux que esté actualmente soportada.

#### Drupal Coder Module Deserialization RCE

- Explicación: La versión de Drupal en el servidor web remoto está afectada por una vulnerabilidad de ejecución remota de código en el módulo Coder, específicamente en el archivo coder_upgrade.run.php, debido a la validación inadecuada de entradas proporcionadas por el usuario a la función unserialize(). Un atacante remoto y no autenticado puede explotar esta vulnerabilidad mediante una solicitud especialmente diseñada para ejecutar código PHP arbitrario.
- Gravedad: Crítica
- CVE: CVE-2019-6340
- CVSS: 9.8
- Sistemas afectados: Versiones del módulo Coder anteriores a 7.x-1.3 / 7.x-2.6
- Solución: Actualizar el módulo Coder a la versión 7.x-1.3 / 7.x-2.6 o posterior

#### ProFTPD mod_copy Information Disclosure

- Explicación: El host remoto ejecuta una versión de ProFTPD afectada por una vulnerabilidad de divulgación de información en el módulo mod_copy debido a los comandos SITE CPFR y SITE CPTO, que están disponibles para clientes no autenticados. Un atacante remoto y no autenticado puede explotar este fallo para leer y escribir archivos arbitrarios en cualquier ruta accesible desde la web en el host.
- Gravedad: Crítica
- CVE: CVE-2015-3306
- CVSS: 9.8
- Sistemas afectados: Versiones de ProFTPD anteriores a 1.3.5a / 1.3.6rc1
- Solución: Actualizar ProFTPD a la versión 1.3.5a / 1.3.6rc1 o posterior.

#### phpMyAdmin prior to 4.8.6 SQLi Vulnerability (PMASA-2019-3)

- Explicación: Según su número de versión autoinformado, la aplicación phpMyAdmin alojada en el servidor web remoto es anterior a la versión 4.8.6 y está afectada por una vulnerabilidad de inyección SQL (SQLi) en la función "designer". Un atacante remoto y no autenticado puede explotar esta vulnerabilidad para inyectar o manipular consultas SQL en la base de datos subyacente, lo que resulta en la divulgación o manipulación de datos arbitrarios.
- Gravedad: Crítica
- CVE: CVE-2019-11768
- CVSS: 9.8
- Sistemas afectados: Versiones de phpMyAdmin anteriores a 4.8.6
- Solución: Actualizar phpMyAdmin a la versión 4.8.6 o posterior, o aplicar los parches referenciados en los avisos del proveedor.

#### SSL Medium Strength Cipher Suites Supported (SWEET32)

- Explicación: El host remoto admite el uso de cifrados SSL que ofrecen un nivel medio de cifrado, definido como claves con longitudes entre 64 y menos de 112 bits, o el uso del cifrado 3DES. Esto facilita considerablemente eludir el cifrado si el atacante está en la misma red física.
- Gravedad: Alta
- CVE: CVE-2016-2183
- CVSS: 7.5
- Sistemas afectados: Aplicaciones configuradas para usar cifrados SSL con fuerza media.
- Solución: Reconfigurar la aplicación afectada para evitar el uso de cifrados con fuerza media siempre que sea posible.

#### Kerberos Vulnerability (USN-7257-1)

- Explicación: Las versiones de Ubuntu 14.04 LTS, 16.04 LTS, 18.04 LTS, 20.04 LTS, 22.04 LTS, 24.04 LTS y 24.10 están afectadas por una vulnerabilidad en Kerberos según el aviso de seguridad USN-7257-1. Investigadores descubrieron que Kerberos autenticaba incorrectamente ciertas respuestas, lo que permite a un atacante interceptar comunicaciones entre un cliente y servidor RADIUS para falsificar respuestas, eludir la autenticación y acceder a dispositivos y servicios de red.
- Gravedad: Crítica
- CVE: CVE-2024-3596
- CVSS: 9.2
- Sistemas afectados: Ubuntu 14.04 LTS / 16.04 LTS / 18.04 LTS / 20.04 LTS / 22.04 LTS / 24.04 LTS / 24.10
- Solución: Actualizar los paquetes afectados (libk5crypto3 y libkrad0) a las versiones corregidas disponibles en los repositorios oficiales de Ubuntu.

#### SSL Certificate with Wrong Hostname

- Explicación: El atributo commonName (CN) del certificado SSL presentado para este servicio pertenece a una máquina diferente, lo que puede causar problemas de confianza y seguridad.
- Gravedad: Media
- CVE: No aplica
- CVSS: 5.3
- Sistemas afectados: Servicios configurados con certificados SSL incorrectos.
- Solución: Comprar o generar un certificado SSL adecuado para este servicio.

#### GNU C Library Vulnerability (USN-7259-3)

- Explicación: Ubuntu 14.04 LTS tiene paquetes instalados que están afectados por una vulnerabilidad en GNU C Library según el aviso USN-7259-3. Esta actualización corrige un problema previamente identificado en USN-7259-1.
- Gravedad: Alta
- CVE: CVE-2025-0395
- CVSS: 7.5
- Sistemas afectados: Ubuntu 14.04 LTS
- Solución: Actualizar los paquetes afectados según las versiones disponibles en los repositorios oficiales.

#### PHP expose_php Information Disclosure

- Explicación: La configuración actual de PHP permite la divulgación de información sensible a través de URLs especiales que activan "Easter eggs" integrados en PHP. Esto puede ser explotado por atacantes para obtener información adicional sobre el sistema.
- Gravedad: Media
- CVSS: 5.3
- Sistemas afectados: Servidores configurados con expose_php habilitado.
- Solución: Modificar el archivo de configuración php.ini para establecer expose_php = Off y reiniciar el servidor web para aplicar los cambios.

## 5. Conclusiones y Recomendaciones

Una vez hemos realizado el análisis de vulnerabilidades de ambos servidores. Podemos recoger que se han detectado numerosas vulnerabilidades en ambos servidores, destacando que con el escaner de los servidores con sus credenciales de inicio se han podido encontrar multitud de vulnerabilidades nuevas que antes no nos aparecían.
Esto es bastante obvio debido a que con el escaner de caja negra solo teniamos acceso a la IP del servidor por lo que solo podiamos escanear los servicios que tuviese hacia el exterior, del otro modo con el análisis de caja blanca permitiendo al escaner que a parte de escanear los servicios que tenía al exterior también podía acceder con las credenciales y realizar un análisis de los servicios por dentro podía escanear y detectar muchos más servicios dandonos coo resultado muchas más vulnerabilidades.

Al final cada uno tiene sus pros y contras porque no cualquier empresq uiere brindar las credenciales de sus servidores para que le realicen análisis y se centra exclusivamente en los servicios que le conecta al exterior. Esto no esta mal pero con un escaneo completo tanto dentro como fuera del servidor se puede terminar de veríficar las vulnerabilidades que contenemos dentro del servidor y que pueden desencadenar en posibles problemas a futuro.

***

Documento redactado por el Grupo 3, compuesto por:

- Israel Valderrama
- Alejandro Seoane
- Víctor Jiménez
- Nicolas Ruiz
- Alejandro Díaz
