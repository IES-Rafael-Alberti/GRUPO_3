# Clasificación, valoración y documentación de un incidente

Hecho por:

- Víctor Jiménez
- Israel Valderrama
- Alejandro Seoane
- Nicolas Ruiz
- Alejandro Díaz

## Indice

1. [Introducción](#1-introducción)
2. [Estado inicial](#2-estado-inicial)
3. [Información técnica](#3-información-técnica)
4. [Evaluación del impacto](#4-evaluación-del-impacto)
5. [Acciones y contramedidas](#5-acciones-y-contramedidas)
6. [Aspectos adicionales](#6-aspectos-adicionales)
7. [Anexos](#7-anexos)

# Informe Técnico de Incidente de Seguridad

---

## **1. Introducción**  

Este documento recoge la imformación obtenida de los informes realizados por el grupo 3. Está basado en un incidente de ciberseguridad que hemos detectado en el departamento de IT, donde una máquina fue afectada por la instalación de un sistema operativo Windows "pirata" y por la instalación de un script malicioso y la explotación de una vulnerabilidad de un servicio Web para crear usuarios administradores. El objetivo es ver el impacto en la empresa y definir unas medidas que permitan mitigar esta vulnerabilidad para futuros incidentes y mejorar la seguridad la organización.

---

## **2. Estado inicial**  

Somos citados por la empresa el día 13 de diciembre de 2024 a las 09:00 de la mañana, nos informan que, un equipo del departamento de informática ha sido comprometido. Tras hablar con John Doe, el dueño del equipo, no hemos sacado nada de información de lo ocurrido en el dispositivo.

Al llegar al ordenador, nos lo encontramos de la siguiente manera:

![](image/cap1.png)
 
Podemos apreciar como se han hecho unos cambios den la máquina y que es necesario reiniciar para aplicar, un error ocasionado por un script y dos archivos extraños en el escritorio.  

---

## **3. Información técnica**

- Información técnica**  

Estos son los incidentes que hemos encontrado y su información correspondiente

| Aspecto | Descripción |
|-|-|
| *Categoría* | Contenido malicioso - Configuración de malware |
| *Impacto* | Bajo |
| *Peligrosidad* | Muy alta |
| *Prioridad* | Media |
| *Detalles* | Configuración no autorizada que permitió la introducción de código malicioso. |


- Categoría y etapas del ataque

| Aspecto | Descripción |
|-|-|
| *Categoría* | Ejecución remota de código (RCE). |
| *Impacto* | Crítico. |
| *Peligrosidad* | Crítica |
| *Prioridad* | Emergencia |
| *Etapas del ataque* | *1. Conexión inicial:* El atacante utiliza el script para establecer una conexión mediante el protocolo TCP en el puerto 8089 del servidor vulnerable.<br><br>*2. Explotación del desbordamiento de búfer:* Se envía un payload malicioso a través de una solicitud HTTP POST, generando el desbordamiento en la biblioteca vulnerable ImageLoad.dll.<br><br>*3. Ejecución del payload:* Se emplea una cadena de gadgets ROP para evadir las protecciones DEP, permitiendo la ejecució...

- Impacto, causa y riesgos

| Aspecto | Descripción |
|-|-|
| *Categoría* | Malware introducido por software no autorizado |
| *Impacto* | Crítico |
| *Peligrosidad* | Crítica |
| *Prioridad* | Emergencia |
| *Causa principal* | Instalación de un sistema operativo no autorizado sin las actualizaciones de seguridad necesarias. |
| *Consecuencia* | Introducción de malware que explotó vulnerabilidades conocidas. |
| *Riesgos* | *1. Alto riesgo de acceso no autorizado.<br>2. Posibilidad de propagación del ataque a otros sistemas dentro de la red.* |

---

## **4. Evaluación del impacto**  

| **Título** | **Descripción** |
|-|-|
| **Nivel de impacto** | Repercusión del incidente para la organización |
| **Impacto transfronterizo** | Afectación en otros estados miembros de la UE (si aplica) |
| **Afectación** | Alcance del incidente (empresas, particulares, instituciones) |
| **Factores clave** | Tipo de amenaza, origen del ataque, categoría afectada, perfil de usuarios afectados, número y tipo de sistemas comprometidos |

---

## **5. Acciones y contramedidas**  

| **Título** | **Descripción** |
|-|-|
| **Plan de acción** | Respuesta inmediata y medidas implementadas |
| **Contramedidas** | Medidas preventivas para evitar futuros incidentes |
| **Proceso de recuperación** | Pasos realizados para restablecer servicios |

---

## **6. Aspectos adicionales**  

| **Título** | **Descripción** |
|-|-|
| **Medios necesarios para la resolución** | Equipos o recursos adicionales requeridos |
| **Impacto económico estimado** | Costo potencial asociado al incidente (si aplica) |
| **Extensión geográfica del incidente** | Local, nacional o internacional |
| **Daños reputacionales** | Efectos en la imagen pública de la organización (si aplica) |
| **Normativa afectada** | ENS, RGPD, NIS, PIC, u otras regulaciones aplicables |
| **Requiere actuación de FFCCSE** | Indicación de si se requiere intervención de fuerzas de seguridad |

---

## **7. Anexos**  

| **Título** | **Descripción** |
|-------------------------------|----------------------------------------|
| **Documentos adjuntos** | Capturas de pantalla, logs, correos, configuraciones afectadas |
| **Referencias a la guía** | Citas de la documentación oficial utilizada para la elaboración del informe técnico |
