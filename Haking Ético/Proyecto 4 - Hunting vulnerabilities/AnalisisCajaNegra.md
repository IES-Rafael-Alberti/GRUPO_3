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
6. [Glosario de Términos](#6-glosario-de-términos)
7. [Anexos](#7-anexos)

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

- Explicación: la versión de Apache HTTP Server 
   - Gravedad: Crítica
   - CVSS: 10.0
   - Sistemas afectados: Todas las versiones de Apache HTTP Server desde 2.1.x hasta 2.2.x
   - Solución: Actualizar a una versión de Apache HTTP Server que este soportada





## 5. Conclusiones y Recomendaciones

- Resumen de los resultados y su interpretación.
- Sugerencias de mejora o acciones correctivas, indicando el nivel de esfuerzo requerido para su implementación.

## 6. Glosario de Términos

- Listado alfabético de términos técnicos o acrónimos utilizados en el informe, junto con sus definiciones.

## 7. Anexos

- Documentación adicional que complemente el informe, como evidencias detalladas, scripts, registros de sistemas, capturas de pantalla, etc.

---

Documento redactado por el Grupo 3, compuesto por:

- Israel Valderrama
- Alejandro Seoane
- Víctor Jiménez
- Nicolas Ruiz
- Alejandro Díaz
