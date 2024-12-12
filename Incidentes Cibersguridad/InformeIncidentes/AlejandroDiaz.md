# Informe Técnico de Incidente de Seguridad

---

## **1. Introducción**

Este informe técnico esta dedicado a un incidente de ciberseguridad que hemos detectado en el departamento de IT, donde una máquina fue comprometida por la instalación de un sistema operativo Windows "pirata". El objetivo principal es evaluar el impacto en la empresa y definir medidas  que permitan mitigar esta vulnerabilidad para futuros incidentes y mejorar la seguridad la organización.&#x20;

---

## **2. Aspectos clave para notificar**

| **Título**                     | **Descripción**                                                                                                                                                                                 |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Asunto**                     | Compromiso de ordenador de la empresa debido a malware  de una instalación de Windows pirata.                                                                                             |
| **OSE/PSD**                    | Departamento de IT de la empresa.                                                                                                                                                               |
| **Sector estratégico**         | Servicios de TI y soporte técnico.                                                                                                                                                              |
| **Fecha y hora del incidente** | [Fecha y hora específica a definir]                                                                                                                                                             |
| **Fecha y hora de detección**  | [Fecha y hora específica a definir]                                                                                                                                                             |
| **Descripción**                | Se detectó actividad sospechosa en una de los ordenadores de la empresa. La investigación nos dió que se había instalado un sistema operativo Windows pirata, dando la infección de un malware. |

---

## **3. Información técnica**

| **Título**                          | **Descripción**                                                                                                                  |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Recursos tecnológicos afectados** | Estación de trabajo del departamento de IT, con servicios críticos para la gestión interna.                                      |
| **Origen del incidente**            | Instalación de un sistema operativo Windows pirata sin actualizaciones de seguridad, que ha ocasionado la entrada de un malware. |
| **Taxonomía**                       | **Vulnerabilidades / Sistema vulnerable / Malware**                                                                              |
| **Nivel de peligrosidad**           | **Crítico**, por la posible filtración de datos, acceso no autorizado y riesgo de expansión dentro de la red.                    |

---

## **4. Evaluación del impacto**

| **Título**                  | **Descripción**                                                                        |
| --------------------------- | -------------------------------------------------------------------------------------- |
| **Nivel de impacto**        | **Alto**, por el acceso potencial a datos internos y posibles errores en los servicios |
| **Impacto transfronterizo** | No identificado                                                                        |
| **Afectación**              | La máquina comprometida y cualquier sistema conectado dentro de la red interna de IT.  |
| **Factores clave**          |                                                                                        |

- **Tipo de amenaza:** Malware / Instalación de software no autorizado.
- **Origen del ataque:** Vulnerabilidad interna por mala gestión de licencias.
- **Categoría afectada:** Integridad y confidencialidad de los datos.
- **Perfil de usuarios afectados:** Personal de IT con acceso a sistemas internos.
- **Número y tipo de sistemas comprometidos:** 1 estación de trabajo confirmada, con potencial de expansión a otros sistemas. |

---

## **5. Acciones y contramedidas**

| **Título**                  | **Descripción**                                                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Plan de acción**          | Aislar la máquina comprometida, analizar el malware, reinstalar sistema operativo legítimo, aplicar políticas de seguridad actualizadas. |
| **Contramedidas**           | Implementar políticas estrictas de gestión de licencias, auditorías periódicas y formación en seguridad del personal.                    |
| **Proceso de recuperación** | Reinstalación completa del sistema operativo, restauración de copias de seguridad y análisis continuo de actividad en la red.            |

---

## **6. Aspectos adicionales**

| **Título**                               | **Descripción**                                                                                                                   |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Medios necesarios para la resolución** | Equipos de análisis forense, herramientas de monitoreo y software antivirus corporativo.                                          |
| **Impacto económico estimado**           | Costos asociados a la reinstalación, licencias de software, horas de trabajo y posibles sanciones por incumplimientos normativos. |
| **Extensión geográfica del incidente**   | Local, limitado a las instalaciones internas de IT.                                                                               |
| **Daños reputacionales**                 | Potencial impacto reputacional moderado si se divulga información del incidente.                                                  |
| **Normativa afectada**                   | RGPD, NIS, ENS.                                                                                                                   |
| **Requiere actuación de FFCCSE**         | No se requiere en esta fase, a menos que se detecte actividad maliciosa externa.                                                  |

---

## **7. Anexos**

| **Título**                | **Descripción**                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Documentos adjuntos**   | Capturas de pantalla, registros de eventos, análisis de malware, informes de auditoría interna.    |
| **Referencias a la guía** | Se citarán secciones específicas de la Guía Nacional de Notificación y Gestión de Ciberincidentes. |

---

## **Implementación de Consejos**

| **Consejo**                                 | **Aplicación en el Informe**                                                                                                                                                         |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Definir una estructura base                 | El informe está organizado en secciones claras como "Introducción", "Evaluación del impacto" y "Acciones y contramedidas".                                                           |
| Distinguir hechos de hipótesis              | Los hechos comprobados se presentan en "Aspectos clave para notificar" y "Evaluación del impacto", mientras que las hipótesis y recomendaciones están en "Acciones y contramedidas". |
| Documentar todas las actividades realizadas | Se detalla cada acción, desde la identificación hasta la recuperación, en "Acciones y contramedidas" y "Anexos".                                                                     |

