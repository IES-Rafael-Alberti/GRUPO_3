# Proyecto 7: Attacking Enterprise Networks - Anexo

## Índice

1. [Declaración de confidencialidad](#1-declaracion-de-confidencialidad)
2. [Descargo de responsabilidad](#2-descargo-de-responsabilidad)
3. [Información de contacto](#3-informacion-de-contacto)
4. [Metodología](#4-metodologia)
  4.1. [Reconocimiento](#4.1-reconocimiento)
  4.2. [Análisis de vulnerabilidades](#4.2-analisis-de-vulnerabilidades)
  4.3. [Explotación](#4.3-explotacion)
  4.4. [Escalada de privilegio](#4.4-escalada-de-privilegios)
  4.5. [Post-explotación](#4.5-post-explotacion)
  4.6. [Documentación](#4.6-documentacion)
5. [Recopilación de información](#5recopilacion-de-informacion)
  5.1. [PC1-Sin nombre](#5.1-pc1-sin-nombre)
  5.2. [PC2-Symfonos](#5.2-pc2-symfonos)
  5.3. [PC3-Duriam](#5.3-pc3-duriam)
  5.4. [PC4-Solstice](#5.4-pc4-solstice)
  5.5. [PC5-Corrosion](#5.5-pc5-corrosion)

## Declaración de confidencialidad

El presente informe de pruebas de pentesting contiene información confidencial y sensible relacionada con la seguridad de los sistemas y la red de la empresa. La divulgación, distribución o reproducción de este documento sin la debida autorización está estrictamente prohibida.

Toda la información contenida en este informe ha sido recopilada con fines exclusivos de evaluación de seguridad y está destinada únicamente para el uso del cliente o de las partes autorizadas expresamente. Cualquier uso indebido de la información proporcionada podría comprometer la seguridad de los sistemas analizados y dar lugar a consecuencias legales.

El cliente se compromete a proteger la confidencialidad de este informe y a restringir su acceso solo a personal autorizado con el fin de mitigar riesgos de seguridad y fortalecer la protección de la información evaluada.

## Descargo de responsabilidad

El presente informe ha sido elaborado con el propósito de identificar vulnerabilidades y riesgos de seguridad en los sistemas evaluados. Las pruebas realizadas se llevaron a cabo en un entorno controlado y siguiendo buenas prácticas de seguridad informática. Sin embargo, no se garantiza la ausencia total de amenazas o vulnerabilidades no identificadas.

El equipo de pentesting y la entidad responsable de este informe no asumen responsabilidad alguna por el uso indebido de la información contenida en el mismo ni por daños derivados de la implementación o no implementación de las recomendaciones sugeridas. Es responsabilidad del cliente evaluar y aplicar las medidas de mitigación necesarias para mejorar la seguridad de su aplicación web.

Asimismo, este informe no debe considerarse una certificación de seguridad absoluta, ya que las amenazas y vulnerabilidades pueden evolucionar con el tiempo. Se recomienda realizar evaluaciones de seguridad periódicas para mantener la integridad y protección de la aplicación.

## Información de contacto

**Empresa auditada:** Pata de Palo Corp.

**Equipo auditor:** Grupo 3, IES Rafael Alberti

**Correo de contacto:** <grupo3@g.educaand.es>

**Fecha de inicio:** 22/04/2025

**Fecha de finalización:** 5/05/2025

## Metodología

Basada en estándares como OWASP, organizada en las siguientes fases:

### 1. Reconocimiento

Recopilación de información sobre los sistemas mediante escaneo de puertos, fingerprinting y servicios expuestos.

### 2. Análisis de vulnerabilidades

Identificación de vulnerabilidades conocidas utilizando herramientas automatizadas.

### 3. Explotación

Explotación de las vulnerabilidades para evaluar acceder al sistema.

### 4. Escalada de privilegios

Verificación de posibles vectores para obtener mayores privilegios.

### 5. Post-explotación

Extracción de información, persistencia y pivoting.

### 6. Documentación

Informe con todos los hallazgos, métodos utilizados y mitigación.

## Recopilación de información

En esta sección se agrupan los hallazgos y vulnerabilidades encontradas en los sistemas planteados. Además, se añade un apartado de como conseguimos persistencia en la máquina y otro de como pivotar en la red para vulnerar los siguientes sistemas.

### PC1 - Sin nombre

#### Escaneo

- Hallazgo 1: puertos abiertos de PC1

![](./Writeups/PC1/img/image2.png)

- Hallazgo 2: escaneo de vulnerabilidades

![](./Writeups/PC1/img/image4.png)

#### Vulnerabilidades

- Hallazgo 3: exploit usado

![](./Writeups/PC1/img/image4.3.png)

- Hallazgo 4: inicio en el sistema

![](./Writeups/PC1/img/image9.png)

#### Persistencia

- Hallazgo 5: creación del payload

![](./Writeups/PC1/img/image19.png)

- Hallazgo 6: exploit usado

![](./Writeups/PC1/img/image20.png)

- Hallazgo 7: Comprobación del payload

![](./Writeups/PC1/img/image26.png)

### PC2 - Symfonos

#### Pivoting

- Hallazgo 8: exploit usado para añadir las redes de PC1

![](./Writeups/PC2/img/image-2.png)

#### Escaneo

- Hallazgo 9: escaneo de puertos abiertos

![](./Writeups/PC2/img/image-4.png)

#### Vulnerabilidades

- Hallazgos 10, 11 y 12: archivos encontrados en el SMB

![](./Writeups/PC2/img/image-11.png)

![](./Writeups/PC2/img/image-12.png)

![](./Writeups/PC2/img/image-13.png)

- Hallazgo 13: wordpress instalado en la máquina

![](./Writeups/PC2/img/image-17.png)

- Hallazgo 14: plugin encontrado en carpeta _uploads_

![](./Writeups/PC2/img/image-19.png)

- Hallazgo 15: exploit que permite ver archivos del sistema

![](./Writeups/PC2/img/image-21.png)

- Hallazgo 16: correo inyectado con php

![](./Writeups/PC2/img/image-24.png)

- Hallazgos 17 y 18: inicio en el sistema

![](./Writeups/PC2/img/image-27.png)

![](./Writeups/PC2/img/image-30.png)

- Hallazgo 19, 20 y 21: escalada de privilegios

![](./Writeups/PC2/img/image-33.png)

![](./Writeups/PC2/img/image-34.png)

![](./Writeups/PC2/img/image-35.png)

#### Persistencia

- Hallazgo 22: crear persistencia copiando clave RSA de la máquina atacante

![](./Writeups/PC2/img/image-37.png)

- Hallazgo 23: comprobación

![](./Writeups/PC2/img/image-38.png)

### PC3 - Duriam

#### Pivoting

- Hallazgo 24, 25 y 26: Uso de chisel para crear un tunel desde la máquina atacante hasta Symfonos

![](./Writeups/PC3/img/image-2.png)

![](./Writeups/PC3/img/image-1.png)

![](./Writeups/PC3/img/image-23.png)

#### Escaneo

- Hallazgo 27: escaneo de puertos de PC3

![](./Writeups/PC3/img/image-8.png)

- Hallazgo 28: fuzzeo de directorios

![](./Writeups/PC3/img/image-9.png)

#### Vulnerabilidades
#### Persistencia

### PC4 - Solstice

#### Pivoting
#### Escaneo
#### Vulnerabilidades
#### Persistencia

### PC5 - Corrosion

#### Pivoting
#### Escaneo
#### Vulnerabilidades
#### Persistencia

## 1. Figuras

{FIGURAS NUMERADAS}

## 2. Hallazgos

{HALLAZGOS NUMERADOS}

| Campo                         | Valor                                   |
| ----------------------------- | --------------------------------------- |
| Ruta de localización completa | {RUTA COMPLETA DEL DISCO}               |
| Contenido del fichero         | {FOTO SI EL CONTENIDO SE PUEDE MOSTRAR} |
| MAC time                      | {MAD TIME}                              |
| Tamaño lógico del fichero     | {TAMAÑO LÓGICO DEL FICHERO}             |
| Valor hash del fichero        | {HASH DEL FICHERO}                      |
