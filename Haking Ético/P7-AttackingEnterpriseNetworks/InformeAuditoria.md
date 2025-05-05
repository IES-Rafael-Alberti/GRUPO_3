# Proyecto 7: Attacking Enterprise Networks - Informe de Auditoría

**Código**: P7

**Nombre**: Attacking Enterprise Networks

**Equipo de pentesting**: Grupo 3

**Fecha**: 24/04/2025

## Índice

1. [Resumen de la evaluación](#1-resumen-de-la-evaluación)
2. [Glosario de términos](#2-glosario-de-términos)
3. [Introducción](#3-introducción)  
   3.1. [Máquinas a auditar](#31-máquinas-a-auditar)  
   3.2. [Alcance](#32-alcance)
4. [Análisis](#4-análisis)  
   4.1. [Herramientas](#41-herramientas)
5. [Procesos](#5-procesos)  
   5.1. [PC1](#51-pc1)  
   5.2. [PC2 - symfonos1](#52-pc2---symfonos1)  
   5.3. [PC3 - Durian](#53-pc3---durian)  
   5.4. [PC4 - solstice](#54-pc4---solstice)  
   5.5. [PC5 - Corrosion](#55-pc5---corrosion)
6. [Trayectoria del ataque](#6-trayectoria-del-ataque)
7. [Índices de gravedad de los hallazgos](#7-índices-de-gravedad-de-los-hallazgos)
8. [Recomendaciones generales](#8-recomendaciones-generales)
9. [Resultados técnicos del informe](#9-resultados-técnicos-del-informe)
10. [Anexos](#10-anexos)

## 1. Resumen de la evaluación

{RESUMEN EJECUTIVO}

## 2. Glosario de términos

{GLOSARIO DE TÉRMINOS}

## 3. Introducción

### 3.1. Máquinas a auditar

El esquema y los datos de las maquinas a auditar son los siguientes:

| Nombre          | Sistema operativo      | Auditor           |
| --------------- | ---------------------- | ----------------- |
| PC1             | Windows Vista (64-bit) | Alejandro Seoane  |
| PC2 - symfonos1 | Debian (64-bit)        | Nicolas Ruiz      |
| PC3 - Durian    | Debian (64-bit)        | Alejandro Díaz    |
| PC4 - solstice  | Debian (64-bit)        | Israel Valderrama |
| PC5 - Corrosion | Ubuntu (64-bit)        | Víctor Jiménez    |

![EnvironmentDiagram.png](img/EnvironmentDiagram.png)

### 3.2. Alcance

Las pruebas se han realizado en los siguientes dominios y rangos de red:

- "External" facing target host: 192.168.68.166
- Rango de red interno: 10.10.10.0/24
- Rango de red interno: 10.10.20.0/24
- Rango de red interno: 10.10.30.0/24

Se han utilizado técnicas como la enumeración y el escaneo de vulnerabilidades evitando provocar interrupciones del servicio.

## 4. Análisis

### 4.1. Herramientas

Las herramientas utilizadas han sido las siguientes:

- Nmap 7.95
- Metasploit 6.4.45-dev
- Proxychain 4.17
- msfvenom 1.4.4
- Chisel 1.10.1

## 5. Procesos

### 5.1. PC1

{PROCESOS DE LA MAQUINA 1}

### 5.2. PC2 - symfonos1

{PROCESOS DE LA MAQUINA 2}

### 5.3. PC3 - Durian

{PROCESOS DE LA MAQUINA 3}

### 5.4. PC4 - solstice

Una vez visto que tenemos una subred en el sistema que hemos vulnerado (PC1) lo que hacemos es escanear la nueva red para ver que puertos tiene abierto, y para ello usamos el siguiente modulo de metasploit `auxiliary/scanner/portscan/tcp` y configuramos los parámetros, como se puede ver en la _Figura X_ del Anexo.

Hemos visto que tiene varias ip asociadas a esa red:

- 10.10.10.4 -> 22, 21, 25, 80, 139, 445, 2121, 3128, 8593.
- 10.10.10.5 -> 135, 139, 445, 3389, (Esta es la ip del windows).  
- 10.10.10.2 -> 135, 445, 2179, 3306, 5040, 7070, 8733,9102, 9180.
- 10.10.10.1 -> 53

Una vez que sabemos que la ip correcta es la 10.10.10.4 lo que hacemos es crear un proxy con el siguiente modulo de metasploit `server/socks_proxy` lo configuramos como se ve en la _Figura X_ del Anexo y lo ejecutamos. 

Después lo que deberemos hacer es un nmap con proxychains para ver cuales son los servicios que están ejecutándose en cada puerto como se puede ver en la _Figura X_ del Anexo.

Como hay un servicio que no sabemos cual es, entonces para saber que servicio es hemos probado hacer curl por si tiene una página y es un servicio http. Una vez realizado el curl al puerto `8593` nos ha devuelto una página y vemos que tiene dos enlaces uno que sería a `/index.php` y otro que tiene `/index.php?book=list` como se puede ver en la _Figura X_ del Anexo.

Una vez visto esto podemos probar si tiene una vulnerabilidad de LFI para ver si nos muestra algo del sistema y hemos probado para ver si nos muestra el contenido del `/etc/passwd`y para ello lo hemos probado como se puede ver desde la _Figura X_ hasta la _Figura X_ del Anexo

Otra de las vulnerabilidades que hemos encontrado es que el servicio del Samba es vulnerable y hemos probado el módulo de `scanner/smb/smb_login` y hemos puesto en la configuración los parámetros de USER_FILE y PASs_FILE le hemos pasados dos diccionarios y lo hemos ejecutado y nos ha creado varias sesiones como se puede ver en la _Figura X_ del Anexo.

### 5.5. PC5 - Corrosion

{PROCESOS DE LA MAQUINA 5}

## 6. Trayectoria del ataque

Durante la auditoría se llevó a cabo un reconocimiento inicial de la red local 192.168.68.0/24, identificando un servidor (PC1) vulnerable. Tras comprometer esta máquina, se detectó su pertenencia a una red adicional (10.10.10.0/24), lo que permitió expandir el alcance del análisis. A través de técnicas de pivoting desde PC1, se logró acceder a las máquinas PC2 y PC4, las cuales también presentaban vulnerabilidades explotables. Desde estas, se identificaron nuevas redes internas (10.10.20.0/24 y 10.10.30.0/24), que fueron igualmente mapeadas y analizadas. Finalmente, mediante técnicas de _pivoting_ desde PC2 y PC4, se comprometieron las máquinas PC3 y PC5. Este proceso evidenció una segmentación deficiente de la red interna y una falta de controles adecuados para aislar los distintos segmentos, facilitando el movimiento lateral entre máquinas comprometidas.

## 7. Índices de gravedad de los hallazgos

| ID  | Vulnerabilidad   | Riesgo | Impacto | Probabilidad | Severidad Final |
| --- | ---------------- | ------ | ------- | ------------ | --------------- |
| 1   | Vulnerabilidad 1 | Alto   | Alto    | Alta         | Crítica         |
| 2   | Vulnerabilidad 2 | Medio  | Medio   | Media        | Media           |
| ..  | ...              | ...    | ...     | ...          | ...             |

## 8. Recomendaciones generales

Para mitigar los riesgos lo que deberíamos hacer es actualizar las versiones que contengan vulnerabilidades.

## 9. Resultados técnicos del informe

{CONCLUSIÓN DE LOS RESULTADOS DEL INFORME}

## 10. Anexos

Las figuras y hallazgos relacionados con el análisis, se encuentran recogidos en el siguiente anexo:

[Anexo auditoría](./AnexoAuditoria.md)

---

Documento redactado por **_Grupo 3_**.

Fdo:

<img src="./img/victorSignWhite.png" width="200">
<img src="./img/israelSignWhite.png" width="200">
