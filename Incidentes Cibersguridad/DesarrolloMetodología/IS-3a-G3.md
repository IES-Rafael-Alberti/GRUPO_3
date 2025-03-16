# IS-3.a-G3

## Índice

1. [Introducción](#1-introducción)
2. [Normas investigadas](#2-normas-investigadas)
3. [Puntos relevantes y Principios identificados durante la investigación](#3-puntos-relevantes-y-principios-identificados-durante-la-investigación)
4. [Procedimiento de Recolección](#4-procedimiento-de-recolección)
5. [Procedimiento de Almacenado](#5-procedimiento-de-almacenado)
6. [Procedimiento de Análisis de evidencias](#6-procedimiento-de-análisis-de-evidencias)
7. [Presentación de resultados del análisis de evidencias](#7-presentación-de-resultados-del-análisis-de-evidencias)
8. [Herramientas a usar](#8-herramientas-a-usar)
9. [Conclusiones](#8-herramientas-a-usar)
10. [Bibliografía](#10-bibliografía)

## 1. Introducción

Para esta tarea, se nos ha pedido que desarrollemos una metodología propia para la recolección, el almacenamiento y el análisis de evidencias digitales. Para ello, debemos analizar las normativas y estandares ya creados y crear una metodología nosostros mismos.

## 2. Normas investigadas

A continueación, presentamos las normativas y estandares que hemos análiazado, dividiendolos en **Normas ISO**, **Normas UNE** y **RFC**:

- Normas ISO (International Organization for Standardization):

  1. ISO 27001(Sistema de Gestión de Seguridad de la Información (SGSI).)
  2. ISO 27002(Controles de seguridad de la información.)
  3. ISO 27037-2012(Directrices para la identificación, recolección y adquisición de evidencias digitales.)
  4. ISO 27042-2015(Directrices para el análisis e interpretación de evidencias digitales.)

- Normas UNE (Una Norma Española):

  1. UNE 7106-2013(Gestión de incidentes de seguridad de la información.)
  2. UNE 71505-2(Buenas prácticas en la gestión de evidencias electrónicas.)
  3. UNE 71505-3(Formatos y mecanismos técnicos para evidencias electrónicas.)
  4. UNE 197001-2011(Criterios generales para la elaboración de informes y dictámenes periciales.)
  5. UNE 197010-2015(Criterios generales para la elaboración de informes y dictámenes periciales sobre TIC.)

- Publicaciónes para el desarrollo de un estándar de Internet (Request for Comments):

  1. RFC 3227(Directrices para la recopilación y archivo de evidencias.)

## 3. Puntos relevantes y Principios identificados durante la investigación

## 4. Procedimiento de Recolección

Para la recolección de evidencias digitales, nos hemos basado en la ISO 27037-2012 ya que se puede aplicar a nivel internacional, pudiendo usarla tanto en España como en el extrangero.
Esta sección se centra en *identificar* posibles dispositivos digitales y objetos relacionados, como pendrives, notas en los equipos, etc; y en la propia *adquisición* de estos.
Cuando se identifiquen las posibles fuentes de evidencias, debemos *evidenciar* el estado inicial de estas con una fotografía y anotando su estado inicial, si está encendido o apagado, que programas tiene abiertos, etc; y localización en la compañía, departamentos, salas, etc. Es importante que se respete el estado de dichos dispositivos y que nadie no a autorizado los manipule.
Por último, debemos diferenciar entre un equipo encendido de una apagado.

### Recolección de evidencias en un equipo *encendido*

Lo primero que debemos hacer es la adquisición de memoria volátil(RAM), documentando todo el proceso y utilizando herramientas propias como **Dumpit**.
Déspues, para evitar desgacias, hacemos la adquisición de disco duro con **FTK imager** o **Autopsy**, y así evitamos el peligro de que el disco esté cifrado y al llegar al laboratorio, no podamos acceder a los datos.
Por último, podemos apagar el equipo, desenchufarlo de la corriente, etiquetarlo y almacenarlo en un recipiente adecuado, para su posterior transporte.

### Recolección de evidencias en un equipo *apagado*

En estos casos, la memoria volátil ha quedado completamente en blanco, por lo que solo podremos hacer la adquisición del disco. Para ello, debemos extraer el disco y usar herramientas que **NO** lo modifiquen, como **FTK imager** o **Autopsy**, y esperar que los discos no esten cifrados. En caso que lo estén, solo podríamos hacer pruebas de fuerza bruta en la copia, no en original. Por último, podremos proceder con la etiquetación y el almacenaje de estos.

  Es importante recalcar que todo este procedimiento debe estar correctamente documentado, incluyendo fecha y hora, nombre o descripción de los dispositivos y evidencias, en caso de crear archivos, incluir el hash **MD5** y **sha256** y la firma del operario que lo realiza.
  Toda copia de datos que se haga, se debe hacer en discos nuevos o debidamente formateados.

## 5. Procedimiento de Almacenado

Para el proceso de almacenaje, nos hemos basado en el UNE 71506-2013, la cuál pensamos que es la que mejor explica el procedimiento de preservación y el almacenaje.


## 6. Procedimiento de Análisis de evidencias

## 7. Presentación de resultados del análisis de evidencias

## 8. Herramientas a usar

## 9. Conclusiones

## 10. Bibliografía

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
