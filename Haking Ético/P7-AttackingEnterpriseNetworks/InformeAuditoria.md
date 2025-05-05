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

{PROCESOS DE LA MAQUINA 4}

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
