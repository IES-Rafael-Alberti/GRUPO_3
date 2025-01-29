# Informe Pericial
**Código**: P03
**Nombre**: Unfaithful Employee
**Equipo pericial**: Grupo 3
**Fecha**: 28/01/2025

## 1. Resumen Ejecutivo  

El análisis forense del disco duro de Richard Warner confirma múltiples violaciones a las políticas de seguridad de InnovaTech Solutions, incluyendo el uso de dispositivos USB no autorizados, la instalación de software no permitido y la navegación en sitios ajenos a su labor durante el horario de trabajo. A través de la verificación de hashes, se detectaron inconsistencias que sugieren una posible manipulación de la imagen forense. Además, se identificaron comunicaciones con una empresa competidora en las que Warner facilitó información confidencial a cambio de beneficios económicos, empleando métodos como almacenamiento en la nube y correos electrónicos encriptados. Se realizó un análisis detallado de la línea de tiempo, el historial de navegación y las actividades del usuario en el sistema, permitiendo evidenciar la exfiltración de datos y el incumplimiento de normativas internas. Toda la evidencia ha sido documentada para respaldar posibles acciones disciplinarias o legales y garantizar la integridad del proceso investigativo.

## 2. Glosario de términos

- **Hash**: Función criptográfica que convierte datos en una cadena única de caracteres. Se usa para verificar la integridad de archivos y detectar manipulaciones.
- **Imagen** forense: Copia exacta de un dispositivo de almacenamiento, creada para análisis sin alterar el original.
- **Logon/Shutdown**: Momentos registrados por el sistema que indican cuándo un usuario inicia o cierra sesión en un dispositivo.

## 3. Introducción  

### 3.1 Datos del equipo

El equipo pericial responsable de la redacción de este informe es el Grupo 3. Los peritos especializados en ciberseguridad en entornos de las tecnologías de la información que conforman dicho equipo son los siguientes:

- Víctor Jiménez Corada, vjimcor955@g.educaand.es
- Nicolás Ruiz Ruiz, nruirui@g.educaand.es
- Israel Valderrama García, ivalgar260@g.educaand.es 
- Alejandro Seoane Martínez, aseomar110@g.educaand.es 
- Alejandro Díaz Barea, adiabar0510@g.educaand.es 

### 3.2. Antecedentes  

InnovaTech Solutions ha solicitado un análisis forense del disco duro de Richard Eduardo Warner, un ex empleado que mostró un comportamiento sospechoso antes de su salida. Se busca determinar si accedió indebidamente a información confidencial, utilizó recursos de la empresa de forma inapropiada o filtró datos.

### 3.3. Objetivos  

Los objetivos son identificar cualquier información relevante que confirme o desmienta las sospechas. Analizar la actividad del usuario en el sistema, incluyendo accesos, modificaciones de archivos y uso de dispositivos externos, además de detectar intentos de exfiltración de datos por correo, almacenamiento en la nube o USB

### 3.4. Verificación 

Tras el cálculo de los hashes de tipo MD5, SHA-1 y SHA-256, hemos llegado a la conclusión de que existen discrepancias entre los hashes resultantes de nuestros cálculos y los entregados junto a la copia de la imagen. Pueden verse en las Figuras X y X.


## 4. Fuente de información

### 4.1 Cadena de custodia

**1. INFORMACIÓN DEL CASO**

| **Sección** | **Campo** |
| ----- | ----- |
| Número de Caso | P03 |
| Tipo de Investigación | Análisis Forense |
| Fecha de Adquisición | 23 de enero de 2025 a las 08:45 |
| Lugar de Adquisición | C/ Amiel, s/n – 11012, Cádiz (Cádiz) |


**2. DESCRIPCIÓN EVIDENCIA EN ORIGINAL**

| **Sección** | **Campo** |
| ----- | ----- |
| Tipo de Dispositivo | Imagen de disco (53687091200 bytes \= 53.69 GB) |
| Hash de la Evidencia Original | MD5: dfdfba2231e3fa409676b1b737474208 SHA1: f476a81089a10f9d5393aa8c2f8bbccdb87f7d3c SHA-256: 66d6ee7a61ea7a986e8f6bb54b9986f79d95b5a0278bef86678ed42ace320d96 |

**3. PRESERVACIÓN DE LA EVIDENCIA ORIGINAL**

| **Sección** | **Campo** |
| ----- | ----- |
| Fecha de Entrega | 23 de enero de 2025 |
| Hora de Entrega | 09:00 |
| Recibido por | Manuel Jesús Rivas Sández |
| Ubicación en el Juzgado | C/ Amiel, s/n – 11012, Cádiz (Cádiz) |

**4. CREACIÓN Y VERIFICACIÓN DE COPIAS**

| **Sección** | **Campo** |
| ----- | ----- |
| Fecha y Hora de Creación  | 26 de enero de 2025 a las 09:00 A.M |
| Técnico Responsable  | Grupo3 |
| Hash de la Copia  | MD5: dfdfba2231e3fa409676b1b737474288 SHA1: f476a81089a10f9d5393aa8c2f8bbccdb87f7d3c SHA-256: 66d6ee7a61ea7a986e8f6bb54b9986f79d95b5a0278bef86678ed42ace320d9b |
| Verificación de Integridad | No, los hashes calculados no se corresponden con los que nos han sido entregados. |
| Entregado a | Manuel Jesús Rivas Sández |
| Fecha y Hora de Entrega | 29 de enero de 2025 a las 23:59 |


## 5. Análisis  

### 5.1. Metodología 

Primero se le ha calculado el hash del disco duro que se nos ha entregado, para mantener la integridad de los datos que contiene. Se ha hecho uso de la herramienta FTK imager en su versión 4.2.0.13 y MiTeC WIndows Registry Recovery con su versión 1.6.1.0 para obtener la información referente al caso y calcular los hashes de las evidencias presentadas.

## 6. Procesos

### 6.1 Línea del tiempo

En este apartado se ha creado una línea de tiempo de los pasos más importantes que se han identificado que realizó el usuario del ordenador.

## 7. Conclusión  

El análisis forense del disco duro de Richard Warner confirma múltiples violaciones a las políticas de seguridad de la empresa. Se ha verificado el uso de dispositivos USB no autorizados, la instalación de software no permitido y la navegación en sitios ajenos a su labor durante el horario de trabajo. Además, las evidencias recopiladas demuestran que mantuvo comunicación con una empresa competidora, a la cual presuntamente facilitó información confidencial a cambio de beneficios económicos.


## 8. Anexos  

La Declaración de abstención y tacha, el Juramento de promesa, así como las figuras y hallazgos relacionados con el caso, se encuentran recogidos en los anexos adjuntos.  



Firma :

![firma victor](img/Firma%20Victor.png)
![firma Isra](img/firma%20isra.png)

