# Clasificación, valoración y documentación de un incidente

Hecho por:

- Víctor Jiménez
- Israel Valderrama
- Alejandro Seoane
- Nicolas Ruiz
- Alejandro Díaz

## Indice

1. [Introducción](#1-introducción)
2. [Estado inicial](#2-estado-y-contexto-inicial)
3. [Información técnica](#3-información-técnica)
4. [Evaluación del impacto](#4-evaluación-del-impacto)
5. [Acciones y contramedidas](#5-acciones-y-contramedidas)
6. [Anexos](#6-anexos)

# Informe Técnico de Incidente de Seguridad

---

## **1. Introducción**  

Este documento recoge la imformación obtenida de los informes realizados por el grupo 3. Está basado en un incidente de ciberseguridad que hemos detectado en el departamento de IT, donde una máquina fue afectada por la instalación de un sistema operativo Windows "pirata" y por la instalación de un script malicioso y la explotación de una vulnerabilidad de un servicio Web para crear usuarios administradores. El objetivo es ver el impacto en la empresa y definir unas medidas que permitan mitigar esta vulnerabilidad para futuros incidentes y mejorar la seguridad la organización.

---

## **2. Estado y contexto inicial**  

Somos citados por la empresa el día *13 de diciembre de 2024* a las 09:00 de la mañana, nos informan que, un equipo del departamento de informática ha sido comprometido. Decidimos hablar con el dueño de la máquina, John Doe, el cual no nos aclara nada de lo que podría haber pasado en el equipo.

Al llegar al puesto de trabajo, nos lo encontramos el equipo de la siguiente manera:

![PlaceHolder](image/cap1.png)

Apreciamos varias cosas importantes:

- Dos archivos en el escritorio
- Una ventana que precisa reiniciar la máquina para aplicar la configuración
- Una ventana de error de un script en una carpeta temporal

---

## **3. Información técnica**

- Scripts maliciosos en carpeta temporal 

Estos son los incidentes que hemos encontrado y su información correspondiente

| Aspecto | Descripción |
|-|-|
| *Categoría* | Contenido malicioso - Configuración de malware |
| *Impacto* | Bajo |
| *Peligrosidad* | Muy alta |
| *Prioridad* | Media |
| *Detalles* | Configuración no autorizada que permitió la introducción de código malicioso. |


- Explotación de vulnerabilidad web para crear usuarios administradores

| Aspecto | Descripción |
|-|-|
| *Categoría* | Ejecución remota de código (RCE). |
| *Impacto* | Crítico. |
| *Peligrosidad* | Crítica |
| *Prioridad* | Emergencia |
| *Etapas del ataque* | *1. Conexión inicial:* El atacante utiliza el script para establecer una conexión mediante el protocolo TCP en el puerto 8089 del servidor vulnerable.<br><br>*2. Explotación del desbordamiento de búfer:* Se envía un payload malicioso a través de una solicitud HTTP POST, generando el desbordamiento en la biblioteca vulnerable ImageLoad.dll.<br><br>*3. Ejecución del payload:* Se emplea una cadena de gadgets ROP para evadir las protecciones DEP, permitiendo la ejecució...

- Activación de windows mediante KMSpico

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

El impacto del incidente fue significativo, afectando tanto la integridad como la confidencialidad de los datos corporativos. El atacante logró acceder a sistemas de la empresa, comprometiendo información sensible. Este ataque también representó un riesgo considerable para otros dispositivos conectados a la misma red interna, ya que podrían ser utilizados para infectar el malware a los otros equipos. El personal de IT, que tiene acceso a sistemas críticos, fue especialmente vulnerable durante el incidente. Este ataque destaca la necesidad de mejorar los controles internos y las prácticas de gestión de licencias para prevenir vulnerabilidades similares en el futuro.

---

## **5. Acciones y contramedidas**  

Es necesario aislar completamente el equipo hasta asegurar que esté libre de malware que puedan comprometer los servicios de la empresa, hacer una limpieza exhaustiva del equipo para eliminar los archivos descubiertos en este análisis y concienciar al empleado del uso correcto de las herramientas de trabajo.

---

## **6. Anexos**  

| **Alumno** | **Informe** |
|-|-|
| **Yo** | Capturas de pantalla, logs, correos, configuraciones afectadas |
| **resto** | Citas de la documentación oficial utilizada para la elaboración del informe técnico |

## **Implementación de Consejos**

| **Consejo** | **Aplicación en el Informe** |
| - | - |
| Definir una estructura base | El informe está organizado en secciones claras como "Introducción", "Evaluación del impacto" y "Acciones y contramedidas" |
| Distinguir hechos de hipótesis | Se incluyen los "aspectos clave para notificar" y "evaluación del impacto", las hipótesis y recomendaciones están en "Acciones y contramedidas". |
| Documentar todas las actividades realizadas | Se dice cada acción, desde la identificación hasta la recuperación, en "acciones y contramedidas" y "anexos". |
