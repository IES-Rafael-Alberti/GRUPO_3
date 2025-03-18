# IS-3.a-G3

## Índice

1. [Introducción](#1-introducción)
2. [Normas investigadas](#2-normas-investigadas)
3. [Puntos relevantes y Principios identificados durante la investigación](#3-puntos-relevantes-y-principios-identificados-durante-la-investigación)
4. [Procedimientos](#4-procedimientos)
   4.1. [Recolección](#41-recolección)
   4.2. [Almacenado](#42-almacenado)
   4.3. [Análisis](#43-análisis)
   4.4. [Presentación](#44-presentación)
5. [Herramientas](#5-herramientas)
6. [Conclusiones](#6-conclusiones)
7. [Bibliografía](#7-bibliografía)

## 1. Introducción

Para esta tarea, se nos ha pedido que desarrollemos una metodología propia para la recolección, el almacenamiento y el análisis de evidencias digitales. Para ello, debemos analizar las normativas y estandares ya creados y crear una metodología nosostros mismos.

## 2. Normas investigadas

A continueación, presentamos las normativas y estandares que hemos análiazado, dividiendolos en **Normas ISO**, **Normas UNE** y **RFC**:

- Normas ISO (International Organization for Standardization):

  1. ISO 27001
  2. ISO 27002
  3. ISO 27037-2012
  4. ISO 27042-2015

- Normas UNE (Una Norma Española):

  1. UNE 71506-2013
  2. UNE 71505-2
  3. UNE 71505-3
  4. UNE 197001-2011
  5. UNE 197010-2015

- Publicaciónes para el desarrollo de un estándar de Internet (Request for Comments):

  1. RFC 3227

## 3. Puntos relevantes y Principios identificados durante la investigación

## 4. Procedimientos

### 4.1. Recolección

Para la recolección de evidencias digitales, nos hemos basado en la ISO 27037-2012 ya que se puede aplicar a nivel internacional, pudiendo usarla tanto en España como en el extrangero.
Esta sección se centra en _identificar_ posibles dispositivos digitales y objetos relacionados, como pendrives, notas en los equipos, etc; y en la propia _adquisición_ de estos.
Cuando se identifiquen las posibles fuentes de evidencias, debemos _evidenciar_ el estado inicial de estas con una fotografía y anotando su estado inicial, si está encendido o apagado, que programas tiene abiertos, etc; y localización en la compañía, departamentos, salas, etc. Es importante que se respete el estado de dichos dispositivos y que nadie no a autorizado los manipule.
Por último, debemos diferenciar entre un equipo encendido de una apagado.

#### Recolección de evidencias en un equipo _encendido_

Lo primero que debemos hacer es la adquisición de memoria volátil(RAM), documentando todo el proceso y utilizando herramientas propias como **Dumpit**(para linux) y **RAM Capture**(para windows).
Déspues, para evitar desgacias, hacemos la adquisición de disco duro con **FTK imager** o **Autopsy**, y así evitamos el peligro de que el disco esté cifrado y al llegar al laboratorio, no podamos acceder a los datos. Para dispositivos móviles, utilizamos herramientas como **Cellebrite UFED**, **XRY** o **Oxygen Forensic Detective**, que permiten extraer información sin modificar la original Por último, podemos apagar el equipo, desenchufarlo de la corriente, etiquetarlo y almacenarlo en un recipiente adecuado, para su posterior transporte.

#### Recolección de evidencias en un equipo _apagado_

En estos casos, la memoria volátil ha quedado completamente en blanco, por lo que solo podremos hacer la adquisición del disco. Para ello, debemos extraer el disco y usar herramientas que **NO** lo modifiquen, como **FTK imager** o **Autopsy**, y esperar que los discos no esten cifrados. En caso que lo estén, solo podríamos hacer pruebas de fuerza bruta en la copia, no en original. Por último, podremos proceder con la etiquetación y el almacenaje de estos.

En dispositivos móviles apagados, no se puede adquirir memoria volátil, por lo que la recolección se va a centrar en el almacenamiento interno. Por lo que hacemos una extracción física utilizando herramientas como **Cellebrite UFED, XRY o Oxygen Forensic Detective**, las cuales no alteran la evidencia y ya la hemos mencionado anteriormente en los equipos encendidos.

Es importante recalcar que todo este procedimiento debe estar correctamente documentado, incluyendo fecha y hora, nombre o descripción de los dispositivos y evidencias, en caso de crear archivos, incluir el hash **MD5** y **sha256** y la firma del operario que lo realiza(cadena de custodia).
Toda copia de datos que se haga, se debe hacer en discos nuevos o debidamente formateados.

### 4.2. Almacenado

Para el proceso de almacenaje, nos hemos basado en el UNE 71506-2013, la cuál pensamos que es la que mejor explica el procedimiento de preservación y el almacenaje de evidencias digitales.
Una vez acabado el proceso de recolección de evidencias, debemos asegurar que los dispositivos estén correctamente protegidos y almacenados hasta la llegada al laboratorio forense. Para ello, hacemos uso del siguiente material:

- Bolsas antiestáticas y cajas de seguridad selladas, para los dispositivos de almacenamiento como discos duros, pendrives, tarjetas SD, etc
- Contenedores acolchados y sellados, para ordenadores, portátiles o móviles.
- También podemos incluir algún material que no deje pasar las altas temperaturas.
- Para los dispositivos que requiran energía, debemos conectarlos a un SAI hasta la llegada al laboratorio.

Además, debemos tener en cuenta los siguientes principios a la hora de manejar datos:

1. Documentar todo el proceso de almacenado

   La documentación en estos casos es clave, de esta forma, queda registrado todo el material adquirido, fecha y hora y _dueño_ de los datos en cada momento, lo que se conoce como **la cadena de custodia**.
   Un ejemplo de cadena de custodia es:

   - Datos del caso

   | Cadena de custodia                           | Campo |
   | -------------------------------------------- | ----- |
   | **Sección**                                  |       |
   | **1. INFORMACIÓN DEL CASO**                  |       |
   | Número de Caso                               |       |
   | Tipo de investigación                        |       |
   | Fecha de Adquisición                         |       |
   | Lugar de Adquisición                         |       |
   | **2. DESCRIPCIÓN EVIDENCIA EN ORIGINAL**     |       |
   | Tipo de Dispositivo                          |       |
   | Hash de la evidencia original                |       |
   | **3. PRESERVACIÓN DE LA EVIDENCIA ORIGINAL** |       |
   | Fecha de Entrega                             |       |
   | Hora de Entrega                              |       |
   | Recibidor por                                |       |
   | Ubicación en el Juzgado                      |       |
   | **4. CREACIÓN Y VERIFICACIÓN DE COPIAS**     |       |
   | Fecha y Hora de Creación                     |       |
   | Técnico Responsable                          |       |
   | Hash de la Copia                             |       |
   | Verificación de Integridad                   |       |

2. Securizar las evidencias en todo momento

   Ahora que tenemos todas las evidencias guardadas y registradas, debemos asegurarnos de que la copia original llegue al laboratorio en las mismas condiciones. Para ello, debemos tener en cuenta los siguientes aspectos:

   - Evitar accesos no autorizados.
     Podemos implementar pequeños controles de acceso donde solo el personal autorizado pueda acceder, o en caso del transporte que nadie pueda acceder a estos hasta llegar al laboratorio.

   - Evitar zonas de peligro.
     Zonas electromagnéticas o zonas de calor, pueden dañar significativamente los dispositivos digitales, por lo que es muy importante mantenerlos en sus recipientes sellados hasta que sea necesario.

3. Llegada al laboratorio

   Por último, y antes de empezar el análisis, debemos proceder con la verificación del estado de las evidencias. Debemos seguir el siguiente esquema:

   - Verificar el estado de los recipientes sellados y comprobar que no haya habido alguna alteración en el transporte.
   - Comprobar los hashes que hicimos en la ubicación inicial.
   - Rellenar la cadena de custodia con los nuevos datos.

### 4.3. Análisis

Para adaptar el análisis, después de valorar las diferentes opciones disponibles hemos optado por usar la normativa UNE 71506 esta normativa se centra en el análisis forense y la ISO 27042:2015 que esta dice que tenemos que justificar los métodos utilizados donde se tiene que explicar los más adecuados para el caso y tiene que ser una elección imparcial.

El análisis forense de evidencia digitales debe seguir un proceso metódico, auditable y repetible. El objetivo es responder a preguntas sobre el tiempo de intrusión, su origen, sistemas afectados ,etc. Antes de iniciar un análisis se debe cumplir los siguientes pasos:

1. **Comprobar competencias.** Esto significa que tendriamos que verificar si el análisis solicitado está dentro de la competencia de laboratorio forense.
2. **Revisión documental.** Esto sería estudiar la documentación para tener el contexto de las evidencias y relaciones etre ellas.
3. **Supervisión de la cadena de custodia.** En este paso lo que haremos es comprobar quién recogió las evidencias, cuando, dónde y cómo se almacenaron hasta llegar al laboratorio.
4. **Autorizaciones.** Esto simplemente es tener los permisos legales para realizar el análisis, según la normativa vigente.
5. **Comprobación de estado.** Verificamos que las evidencias no están dañadas y son susceptibles de análisis.
6. **Evidencias adicionales.** Si se encuentran nuevas evidencias como pueden ser discos, memorias, etc. Estas evidencias se deben registrar y se debe obtener de nuevo las autorizaciones para analizarlas.
7. **Hora de la BIOS.** Registramos la hora de la BIOS del equipo donde se alojan los discos para poder comparar la cronología.
8. **Establecer prioridades.** Definimos los criterios de prioridad en el análisis.

#### Recuperación de ficheros borrados

Este proceso busca recuperar archivos eliminados de almacenamientos. Además se recuperan archivos de áreas no asignadas del disco o ficheros 'huérfanos'. También se localizan fragmentos de archivos mediante búsqueda en las cabeceras. Toda información recuperada debe estar documentada en el informe.

#### Estudio de particiones y sistemas de archivos

Se analiza la estructura de almacenamiento como pueden ser particiones, volúmenes físicos y lógicos, etc. Este proceso incluye:

- **Enumeración de particiones.** Actuales y previas.

- **Identificación de áreas ocultas.**

- **Reconocimiento** de sistemas de archivos en contenedores y discos cifrados.

- **Análisis de archivos.** Archivos comprimidos y sus cabeceras.

- **Para móviles**, se examinan particiones del sistema, almacenamiento interno y externo, así como posibles áreas cifradas o eliminadas.

#### Estudio del sistema operativo

Se identifican los SO instalados, su fecha de instalación, actualizaciones, usuarios, privilegios y las últimas actividades registradas.También se examinan los dispositivos de hardware y software reconocido por el sistema. Para móviles, se revisan las versiones del sistema, logs del dispositivo y datos de las aplicaciones.

#### Estudio de la seguridad implementada

Evaluamos si las evidencias han sido compromentidas mediante métodos de intrusión, modificación o eliminación. Se deben identidicar malware y evaluar su impacto.

#### Análisis detallado de los datos obtenidos

Realizaremos un análisis exhaustivo de las evidencias electrónicas utilizando software especializzado. Este análisis incluye clasificación y el indexado de los datos, lo que agiliza la búsqueda de información clave. Además analizaremos los ddiversos elementos del sistema como hardware, configuración regional, última actividad y dispositivos conectados como puede ser USBs, impresoras y móviles. Tambíen deberemos analizar las conexiones de red, protocolos utilizados y las comunicaciones realizadas desde el equipo. Revisaremos los registros del sistema, los epacios no asignados del disco, cola de impresión y enlaces a archivos recientes.

El análisis tendrá las carpetas de los distintos usuarios, programas instalados, metadatos de archivos y las aplicaciones de virtualización junto con sus configuraciones. También debermos analizar las Bases de datos y gestores asociados, archivos cifrados y particiones protegidas. Relacionado con la web debermos analizar el historial de navegación, cookies, correos electrónicos y registros de chats. Con todo este analisis podemos saber todo lo que hizo y encontrar las posibles evidencias importantes.

### 4.4. Presentación

Para garantizar la integridad y fiabilidad del análisis forense, seguimos las normativas **ISO 27042:2015**, **UNE 197001-2011**, **UNE 197010-2015** y **RFC 3227**, asegurando que la presentación de resultados sea clara y verificable.

#### Estructura del informe

1. **Portada**: Datos del caso y analista.
2. **Introducción**: Contexto, objetivos y normativas aplicadas.
3. **Descripción de evidencias**: Métodos de adquisición, estado y hashes.
4. **Metodología de análisis**: Herramientas y técnicas empleadas.
5. **Resultados**: Hallazgos clave, línea de tiempo y actividad sospechosa.
6. **Conclusiones y recomendaciones**: Impacto del incidente y medidas correctivas.
7. **Anexos**: Capturas, logs y verificación de integridad.

#### Validación y entrega

El informe debe estar firmado y contener un hash de verificación. Se recomienda entregarlo en **PDF firmado digitalmente**, con cifrado y bajo cadena de custodia cuando sea necesario.

## 5. Herramientas

### Adquisición

- DumpIt (Linux): RAM
  
- RAM Capture (Windows): RAM

- FTK Imager (Windows/Linux): Disco duro

- Autopsy (Windows/Linux): Disco duro

- Cellebrite UFED (Móviles): Extracción forense de datos móviles.

- XRY (Móviles): Extracción forense de datos móviles.

- Oxygen Forensic Detective (Móviles): Extracción avanzada de datos desde dispositivos móviles y almacenamiento en la nube.

### Almacenamiento

- Bolsas antiestáticas y cajas de seguridad selladas: Para la preservación de discos duros, pendrives y tarjetas SD.

- Contenedores sellados: Protección de ordenadores y móviles.

- SAI (Sistema de Alimentación Ininterrumpida): Mantenimiento de dispositivos que requieren energía hasta su llegada al laboratorio.

### Análisis

Para el análisis usamos la ISO 27042:2015 que esta dice que tenemos que justificar las herramientas  más adecuados para el caso y tiene que ser una elección imparcial. Aún así se pueden usar estas herramientas:

- Autopsy

- Cellebrite UFED

- XRY

- Oxygen Forensic Detective
  
- FTK Imager


### Presentación

- Editor de notas markdown: Joplin, Obsidian, Visual Studio Code.
- Editor de texto: Google Docs, Microsoft Word.

## 6. Conclusiones

## 7. Bibliografía

1. [Norma Española UNE 197001, Criterios generales para la elaboración de informes y dictámenes periciales](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/pluginfile.php/700890/mod_resource/content/0/UNE_1970012011.pdf)
2. [peritoinformaticocolegiado.es, Estándares nacionales e internacionales que puede seguir un perito informático para realizar el análisis forense de una evidencia y para la elaboración de un peritaje informático](https://peritoinformaticocolegiado.es/blog/estandares-nacionales-e-internacionales-que-puede-seguir-un-perito-informatico-para-realizar-el-analisis-forense-de-una-evidencia-y-para-la-elaboracion-de-un-peritaje-informatico/)
3. [cristiancuerdaperito.es, Aplicación de la norma UNE 197010 a la elaboración de Informes Periciales Informáticos](https://cristiancuerdaperito.es/2023/02/28/aplicacion-de-la-norma-une-197010-a-la-elaboracion-de-informes-periciales-informaticos/)
4. [acta.es, Importancia del método de la prueba pericial en materias de tecnología y su impacto en la agilidad del proceso judicial](https://www.acta.es/medios/articulos/cultura_y_sociedad/059001.pdf)
5. [josedelgado.net, Qué es el Informe Pericial](https://josedelgado.net/que-es-el-informe-pericial/)
6. [peritosinformaticos.es, ISO 197010/2015. Normas Generales para la elaboración de informes y dictámenes periciales sobre TIC.](https://peritosinformaticos.es/iso-197010-perito-informatico/)
7. [indalics.com, Informe pericial informático](https://indalics.com/informe-pericial-informatico)

---

Documento redactado por el Grupo 3, compuesto por:

- Víctor Jiménez
- Israel Valderrama
- Alejandro Seoane
- Nicolas Ruiz
- Alejandro Díaz
