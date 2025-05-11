# Proyecto P05.2: Defacement Attack - Anexo

## Índice

1. [Declaración de abstención y tacha](#1-declaración-de-abstención-y-tacha)
2. [Juramento de promesa](#2-juramento-de-promesa)
3. [Figuras](#3-figuras)
4. [Hallazgos](#4-hallazgos)

## 1. Declaración de abstención y tacha

Nosotros, Grupo 3, con identificación _011002-A_, en calidad de Equipo Pericial Informático, declaramos formalmente lo siguiente:

1. Abstención

   No tenemos interés directo ni indirecto en los hechos objeto del presente informe pericial, ni relación alguna con las partes involucradas que pueda comprometer nuestra imparcialidad, conforme a lo establecido en la normativa _ISO-27000_.

2. Tacha

   Declaramos que no existen motivos de tacha que afecten nuestra idoneidad, independencia o credibilidad como peritos en este caso. No poseemos vínculos familiares, laborales ni de cualquier otra índole con las partes intervinientes.

3. Confirmación de Imparcialidad

   Nuestros análisis, conclusiones y opiniones periciales se fundamentan exclusivamente en las evidencias digitales recibidas y en las metodologías técnicas reconocidas por la disciplina de informática forense, sin influencia externa de ningún tipo.

En virtud de lo anterior, asumimos la responsabilidad de actuar con total objetividad y profesionalismo en la elaboración y presentación del presente informe.

## 2. Juramento de promesa

Nosotros, Grupo 3, identificados con _011002-A_, en calidad de Equipo de Peritaje Forense Informático, bajo juramento, prometemos solemnemente lo siguiente:

1. Realizar el análisis técnico del presente caso conforme a los principios de objetividad, veracidad y rigurosidad científica propios de la disciplina de informática forense.

2. Garantizar que todas las conclusiones presentadas en el informe pericial se sustenten exclusivamente en las evidencias digitales analizadas y las metodologías técnicamente válidas, sin alteraciones ni omisiones deliberadas.

3. Actuar de manera independiente e imparcial, sin recibir presiones, influencias externas o intereses personales que puedan comprometer la integridad de mi labor.

4. Cumplir con las disposiciones legales y éticas vigentes aplicables al ejercicio de la pericia forense en el marco del acuerdo, la confidencialidad de los datos y cumplimiento de los requisitos del proceso.

Declaro bajo juramento que honraré este compromiso en la ejecución de mis funciones como perito en este caso.

En Cádiz a 28 de Enero de 2025

Fdo:

<img src="img/victorSignWhite.png" alt="firma Victor" width="150"/>
<img src="img/israelSignWhite.png" alt="firma Israel" width="200"/>

## 3. Figuras

**Hashes de la adquisición.**

- Figura 1: Smartphone de la víctima.

- Figura 2: Smartphone del marido de la víctima

- Figura 3: Raspberry Pi (TV Inteligente).

- Figura 4: Informe de diagnóstico de Google OnHub.

- Figura 5: Datos de Amazon Echo Alexa.

- Figura 6: Tráfico de red del SmartHome.

- Figura 7: Hashes de la adquisición.

Figura 8 : Archivo encargado de resgistros sesiones de inicio (`/var/log/wtmp`) 

![](./Write-Ups/TV/img/img4.png)

Figura 9 : Dispositivo Google On Hub

![](./Write-Ups/GoogleOnHub/image.png)

## 4. Hallazgos

### 4.1 Raspberry Pi (TV Inteligente).

- Hallazgo 1: Ejecución Película

| Campo                         | Valor                                                                                                                       |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Ruta de localización completa | `/home/osmc/.kodi/temp/kodi.log`                                                                                               |
| Contenido del fichero         | ![](./Write-Ups/TV/img/img5.png) ![](./Write-Ups/TV/img/img6.png)|
| MAC time                      | 	17/Jul/2017:06:19:37 +0000                                                                                                  |

- Hallazgo 2: Dispositivos bluetooth

| Campo                         | Valor                                                                                                                       |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Ruta de localización completa | `/var/lib/bluetooth/B8:27:EB:E6:8D:79/cache`                                                                                               |
| Contenido del fichero         | ![](./Write-Ups/TV/img/img1.png) ![](./Write-Ups/TV/img/img2.png) ![](./Write-Ups/TV/img/img3.png)|
| MAC time                      | 	15/Jul/2017 23:52:00 +0000    15/Jul/2017 23:41:00 +0000                                                                                               |

