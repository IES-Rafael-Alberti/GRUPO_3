# Informe Técnico
  * **Realizado por Israel Valderrama**
## Introducción.

Este informe técnico está basado en un incidente de ciberseguridad detectado en el departamento de IT, donde se identificó una máquina comprometida por la instalación de un sistema operativo Windows no autorizado y un script malicioso. El análisis se centra en un archivo Python diseñado para explotar una vulnerabilidad una aplicación, permitiendo la ejecución de código remoto.

El objetivo de este informe es evaluar el impacto en la empresa, definir medidas de mitigación para futuras vulnerabilidades y mejorar la seguridad general de la organización. Además, revisaremos cómo el exploit identificado podría permitir comprometer el sistema y crear un usuario con privilegios administrativos.

## Aspectos claves para notificar

El incidente involucra el compromiso de un ordenador de la empresa debido a la instalación de un sistema operativo Windows pirata. Esta situación se detectó el 1 de noviembre de 2024, aunque el incidente en sí ocurrió unos días antes, el 28 de octubre. Durante la investigación, el equipo de IT descubrió que el sistema operativo pirata había permitido la ejecución de un script malicioso, lo que comprometió la seguridad del entorno interno. Este incidente afectó al usuario Jhon Doe, quien trabaja en el área de servicios de TI y soporte técnico. Este caso pone en evidencia la importancia de mantener un control estricto sobre las licencias de software utilizadas dentro de la organización.



## Información técnica

El incidente tuvo un impacto directo en servicios críticos internos, poniendo en riesgo la estabilidad de sistemas  para las operaciones de la empresa. La causa principal fue la instalación de un sistema operativo no autorizado, que no contaba con las actualizaciones de seguridad necesarias. Esto dejó la puerta abierta a la introducción de malware, que explotó vulnerabilidades conocidas. La peligrosidad del incidente se clasifica como crítica debido al alto riesgo de acceso no autorizado y a la posibilidad de que el ataque se propague a otros sistemas dentro de la red.



## Evaluación del impacto

El impacto del incidente fue significativo, afectando tanto la integridad como la confidencialidad de los datos corporativos. El atacante logró acceder a sistemas de la empresa, comprometiendo información sensible. Este ataque también representó un riesgo considerable para otros dispositivos conectados a la misma red interna, ya que podrían ser utilizados para infectar el malware a los otros equipos. El personal de IT, que tiene acceso a sistemas críticos, fue especialmente vulnerable durante el incidente. Este ataque destaca la necesidad de mejorar los controles internos y las prácticas de gestión de licencias para prevenir vulnerabilidades similares en el futuro.



## Acciones y contramedidas

En respuesta al incidente, se adoptaron varias medidas inmediatas para reducir el impacto y restaurar la seguridad del entorno. En primer lugar, se separó la máquina infectada para evitar una posible propagación del malware. Posteriormente, se llevó a cabo un análisis del script malicioso y de las vulnerabilidades explotadas. El sistema operativo fue reinstalado utilizando una versión con licencia y actualizada, asegurándose de incluir todas las medidas de seguridad necesarias. Adicionalmente, se implementaron políticas de gestión de licencias, acompañadas de sesiones de formación para el personal. Finalmente, se restauraron copias de seguridad de los sistemas afectados y se realizó una inspección profunda de la red para descartar cualquier amenaza.



## Aspectos adicionales

La resolución del incidente requirió el uso de herramientas de análisis forense, como LastActivityView, que permitieron examinar los registros del sistema comprometido. Esto facilitó la identificación de las acciones llevadas a cabo por el atacante y el alcance del ataque. Afortunadamente, el impacto geográfico del incidente estuvo limitado a las instalaciones internas del departamento de IT, aunque existía el riesgo de que la situación pudiera escalar si no se tomaban medidas oportunas. En cuanto al impacto reputacional, aunque fue moderado, la divulgación del incidente podría haber tenido consecuencias negativas para la percepción de la empresa.



## Anexos

### Log del sistema

```bash

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


### Fragmento del script malicioso

```python
payload = "A"*2278 + rop_chain + "\x90"*4 + Shellcode4 + "B"*(1790-len(Shellcode4)-len(rop_chain)) + ret
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 8089))
s.send("POST /sendemail.ghp HTTP/1.1\r\n\r\nEmail=" + payload + "&getPassword=Get+Password")
print "[+] Creado usuario ihacklabs con password Thack12/"
s.close()
```

Este fragmento de código muestra cómo el atacante aprovechó un desbordamiento de búfer para insertar un payload malicioso. Este código permitió la creación de un usuario no autorizado con privilegios administrativos, otorgando al atacante control total sobre el sistema.

### Detalles técnicos del ataque

El ataque se desarrolló en tres etapas principales. En primer lugar, el atacante estableció una conexión al puerto 8089 del sistema vulnerable mediante el protocolo TCP. A continuación, se explotó un desbordamiento de búfer utilizando un payload malicioso enviado a través de una solicitud HTTP POST. Finalmente, el atacante ejecutó el código malicioso, que evitó las protecciones y permitió la creación de un usuario con privilegios elevados. Este incidente recalca la importancia de mantener las actualizaciones de seguridad al día y de realizar auditorías frecuentes en los sistemas para identificar posibles vulnerabilidades.

