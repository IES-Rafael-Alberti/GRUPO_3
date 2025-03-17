# IS-3.a-G3

## Índice

- [IS-3.a-G3](#is-3a-g3)
  - [Índice](#índice)
  - [1. Introducción](#1-introducción)
  - [2. Normas investigadas](#2-normas-investigadas)
  - [3. Puntos relevantes y Principios identificados durante la investigación](#3-puntos-relevantes-y-principios-identificados-durante-la-investigación)
  - [4. Procedimiento de recolección](#4-procedimiento-de-recolección)
    - [Recolección de evidencias en un equipo _encendido_](#recolección-de-evidencias-en-un-equipo-encendido)
    - [Recolección de evidencias en un equipo _apagado_](#recolección-de-evidencias-en-un-equipo-apagado)
  - [5. Procedimiento de almacenado](#5-procedimiento-de-almacenado)
  - [6. Procedimiento de análisis de evidencias](#6-procedimiento-de-análisis-de-evidencias)
  - [7. Presentación de resultados del análisis de evidencias](#7-presentación-de-resultados-del-análisis-de-evidencias)
  - [8. Herramientas a usar](#8-herramientas-a-usar)
  - [9. Conclusiones](#9-conclusiones)
  - [10. Bibliografía](#10-bibliografía)

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

  1. UNE 7106-2013
  2. UNE 71505-2
  3. UNE 71505-3
  4. UNE 71506-2013
  5. UNE 197001-2011
  6. UNE 197010-2015

- Publicaciónes para el desarrollo de un estándar de Internet (Request for Comments):

  1. RFC 3227

## 3. Puntos relevantes y Principios identificados durante la investigación

## 4. Procedimiento de recolección

Para la recolección de evidencias digitales, nos hemos basado en la ISO 27037-2012 ya que se puede aplicar a nivel internacional, pudiendo usarla tanto en España como en el extrangero.
Esta sección se centra en _identificar_ posibles dispositivos digitales y objetos relacionados, como pendrives, notas en los equipos, etc; y en la propia _adquisición_ de estos.
Cuando se identifiquen las posibles fuentes de evidencias, debemos _evidenciar_ el estado inicial de estas con una fotografía y anotando su estado inicial, si está encendido o apagado, que programas tiene abiertos, etc; y localización en la compañía, departamentos, salas, etc. Es importante que se respete el estado de dichos dispositivos y que nadie no a autorizado los manipule.
Por último, debemos diferenciar entre un equipo encendido de una apagado.

### Recolección de evidencias en un equipo _encendido_

Lo primero que debemos hacer es la adquisición de memoria volátil(RAM), documentando todo el proceso y utilizando herramientas propias como **Dumpit**.
Déspues, para evitar desgacias, hacemos la adquisición de disco duro con **FTK imager** o **Autopsy**, y así evitamos el peligro de que el disco esté cifrado y al llegar al laboratorio, no podamos acceder a los datos.
Por último, podemos apagar el equipo, desenchufarlo de la corriente, etiquetarlo y almacenarlo en un recipiente adecuado, para su posterior transporte.

### Recolección de evidencias en un equipo _apagado_

En estos casos, la memoria volátil ha quedado completamente en blanco, por lo que solo podremos hacer la adquisición del disco. Para ello, debemos extraer el disco y usar herramientas que **NO** lo modifiquen, como **FTK imager** o **Autopsy**, y esperar que los discos no esten cifrados. En caso que lo estén, solo podríamos hacer pruebas de fuerza bruta en la copia, no en original. Por último, podremos proceder con la etiquetación y el almacenaje de estos.

Es importante recalcar que todo este procedimiento debe estar correctamente documentado, incluyendo fecha y hora, nombre o descripción de los dispositivos y evidencias, en caso de crear archivos, incluir el hash **MD5** y **sha256** y la firma del operario que lo realiza(cadena de custodia).
Toda copia de datos que se haga, se debe hacer en discos nuevos o debidamente formateados.

## 5. Procedimiento de almacenado

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

   |                    |     |
   | ------------------ | --- |
   | Número de caso:    |     |
   | Fecha de apertura: |     |
   | Hora de apertura:  |     |

   - Datos de la evidencia

   |                                     |                                              |
   | ----------------------------------- | -------------------------------------------- |
   | Tipo de evidencia                   | Disco duro, Pendrive, Ordenador, Móvil, etc. |
   | Identificador                       | Número de la etiqueta                        |
   | Descripción                         |                                              |
   | Ubicación de recolección:           |                                              |
   | Persona que recolecta la evidencia: | Nombre + Firma                               |
   | Fecha y hora de recolección:        |                                              |
   | HASH MD5                            | Si es necesario                              |
   | HASH sha256                         | Si es necesario                              |

   - Observaciones

   |                                                  |     |
   | ------------------------------------------------ | --- |
   | Nombre del responsable de la cadena de custodia: |     |
   | Firma del responsable de la cadena de custodia:  |     |
   | Fecha de cierre de la cadena de custodia:        |     |

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

## 6. Procedimiento de análisis de evidencias

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
