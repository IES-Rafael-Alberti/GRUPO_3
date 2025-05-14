# Proyecto 9: Murder investigation

**Código**: P09

**Nombre**: Murder investigation

**Equipo forense**: Grupo 3

**Fecha**: 11/05/2025

## Índice

1. [Resumen Ejecutivo](#1-resumen-ejecutivo)
2. [Glosario de términos](#2-glosario-de-términos)
3. [Introducción](#3-introducción)  
   3.1. [Datos del equipo](#31-datos-del-equipo)  
   3.2. [Antecedentes](#32-antecedentes)  
   3.3. [Objetivos](#33-objetivos)  
   3.4. [Verificación](#34-verificación)
4. [Fuente de información](#4-fuente-de-información)  
   4.1. [Cadena de custodia](#41-cadena-de-custodia)
5. [Análisis](#5-análisis)  
   5.1. [Herramientas](#51-herramientas)  
   5.2. [Metodología](#52-metodología)
6. [Procesos](#6-procesos)  
7. [Línea de tiempo](#7-línea-de-tiempo)
8. [Limitaciones](#8-limitaciones)
9. [Conclusión](#9-conclusión)
10. [Anexo](#10-anexos)

## 1. Resumen Ejecutivo

## 2. Glosario de términos

## 3. Introducción

### 3.1 Datos del equipo

El equipo pericial responsable de la redacción de este informe es el Grupo 3. Los peritos especializados en ciberseguridad en entornos de las tecnologías de la información que conforman dicho equipo son los siguientes:

- Víctor Jiménez Corada, <vjimcor955@g.educaand.es>
- Nicolás Ruiz Ruiz, <nruirui@g.educaand.es>
- Israel Valderrama García, <ivalgar260@g.educaand.es>
- Alejandro Seoane Martínez, <aseomar110@g.educaand.es>
- Alejandro Díaz Barea, <adiabar0510@g.educaand.es>

### 3.2. Antecedentes

El 17 de julio de 2017, a las 15:31, un conserje del edificio alertó a la policía tras recibir el aviso de un vecino, quien informó que había encontrado a su esposa fallecida en su domicilio, presentando signos de múltiples puñaladas. La policía llegó al lugar a las 15:40, hallando el cuerpo sin vida de la víctima en el salón de la vivienda. Posteriormente, los agentes procedieron a interrogar tanto al conserje como al marido de la víctima.

El esposo declaró que él se había mudado recientemente al piso. Según su testimonio, antes de encontrar el cuerpo, estaba viendo una película en el dormitorio con auriculares puestos, ya que su mujer había puesto música y no podía oír nada del exterior. Una vez finalizada la película, se dirigió al salón, donde encontró a su esposa sin vida y avisó al conserje para que llamara a la policía.

### 3.3. Objetivos

El objetivo de este informe forense es realizar una investigación de las evidencias aportadas que expliquen los hechos ocurridos para informar adecuadamente sobre los mismos.

### 3.4. Verificación

## 4. Fuente de información

### 4.1 Cadena de custodia

#### 1. Información del caso

| **Sección**           | **Campo**                            |
| --------------------- | ------------------------------------ |
| Número de Caso        | P09                                |
| Tipo de Investigación | Análisis Forense                     |
| Fecha de Adquisición  | xx de x de 2025, xx:00           |
| Lugar de Adquisición  | C/ Amiel, s/n – 11012, Cádiz (Cádiz) |
| Recibido por          | Manuel Jesús Rivas Sández            |

#### 2. Descripción de las evidencias

| **Sección**         | **Campo**                                           |
| ------------------- | --------------------------------------------------- |
| Tipo de Dispositivo | Smartphone  |
| Nombre del archivo  | smartphone_victima.zip |
| Hash MD5            | 8daf9d23e39675452f99c5099a72b317 |
| Hash SHA256         | c3e334c996b811c51067e9e0657cb621523576f15eb2c19ec52c32bf36e3e5ff |
| ------------------- | --------------------------------------------------- |
| Tipo de Dispositivo | Smartphone |
| Nombre del archivo  | smartphone_marido_victima.zip |
| Hash MD5            | 1472be511173e7e0f4919958b1c96ffe |
| Hash SHA256         | 5a46acdf7fb5a70734a2e0e39a8c9b5cc9b7ee799fe800a0a7512af08e15c025 |
| ------------------- | --------------------------------------------------- |
| Tipo de Dispositivo | Televisión |
| Nombre del archivo  | TV_Inteligente.zip |
| Hash MD5            | d9d2b3b3048a836289cec02c6353b6e9 |
| Hash SHA256         | 5423ea3f60d4ad0874346d3ba31c8783e5f2ce4b15b261ba0085e07f11e650e6 |
| ------------------- | --------------------------------------------------- |
| Tipo de Dispositivo | Router de Google |
| Nombre del archivo  | InformeDiagnosticoOnHub |
| Hash MD5            |  |
| Hash SHA256         |  |
| ------------------- | ------------------------------------------------------- |
| Tipo de Dispositivo | Altavoz inteligente con asistente virtual (Amazon Echo) |
| Nombre del archivo  | Alexa.zip |
| Hash MD5            | 4a07bd78d8f4ba227841c971eeb7d1b3 |
| Hash SHA256         | 4767513d714698afcd7506dd2304528a8db8243e2dff1be6e1ede591d0d19f83 |
| ------------------- | ------------------------------------------------------- |
| Tipo de Dispositivo | Medio de almacenamiento |
| Nombre del archivo  | Tráfico_SmartHome_PorCOAP.pcap |
| Hash MD5            | 67ab09760148a66402aa7d9b0abaa322 |
| Hash SHA256         | f5ad42a50ca0d16261c1ca4742d78fd99c9e7fc6ab67fdb3a53909ff7f786ce0 |
| ------------------- | ------------------------------------------------------- |
| Tipo de Dispositivo | Medio de almacenamiento |
| Nombre del archivo  | Tráfico_SmartHome_PorIP.pcap |
| Hash MD5            | 8fb0edb521c9ad191adf55054203a6f4 |
| Hash SHA256         | a4664f1719d26382edd6d352cc8715fea3ee73bbb00245d71943fbacbbeeca3e |
| ------------------- | ------------------------------------------------------- |
| Tipo de Dispositivo |  |
| Nombre del archivo  | Hashes.zip |
| Hash MD5            |  |
| Hash SHA256         |  |

## 5. Análisis

### 5.1. Herramientas

Las herramientas utilizadas durante la investigación han sido las siguientes:

- Autopsy 4.21.0
- FTK imager 7.5
- VLC 3.0.16
- Wireshark 4.4.6

### 5.2. Metodología

En primer lugar se ha verificado la integridad de las evidencias obtenidas en vista de mantener la integridad de los datos que estas contienen.
Tras ello se ha procedido al análisis de las dos adquisiciones móviles que se nos da con Autopsy, se ha analizado los archivos de la SmartTV con FTK Imager, se han analizado los audios de Alexa con VLC y por último hemos utilizado Wireshark para analizar el tráfico de red del SmartHome.

## 6. Procesos

### 6.1 Análisis móvil victima

En el aná

### 6.2 Análisis móvil marido de la victima

### 6.3 Análisis SmartTV

### 6.4 Análisis Alexa

### 6.5 Análisis tráfico de red SmartHome

### 6.6 Análisis informe diagnóstico Google OnHub

## 7. Línea de tiempo

Tras el análisis hemos creado la siguiente linea del tiempo con los hechos acontecidos:

## 8. Limitaciones

## 9. Conclusión

## 10. Anexos

La Declaración de abstención y tacha, el Juramento de promesa, así como las figuras y hallazgos relacionados con el caso, se encuentran recogidos en el siguiente anexo:

---

Documento redactado por el equipo de peritos forenses informático _Grupo 3_.

Fdo:

<img src="img/victorSignWhite.png" alt="firma Victor" width="150"/>
<img src="img/israelSignWhite.png" alt="firma Israel" width="200"/>