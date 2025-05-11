# Investigación del móvil del marido de la victima

## Comprobación del Hash

![Imagen que aún no existe]

Para el análisis del dispositivo móvil del marido, voy a usar esta [seetcheat](https://pbs.twimg.com/media/FL-GAXBUUAEJRZq.jpg) de móvil. Voy a hacer una amalgama de información y al final hago un resumen de todo.

| Dato | Valor |
|-|-|
| Modelo | SHV-E250S |
| Fabricante | Samsung |
| Nombre interno | t0lteskt (Note II versión coreana) |
| Versión de Android | 4.4.2 (KitKat) |
| SDK | 19 |
| Fecha de compilación | 24 agosto 2015 - 16:21:59 KST |
| Región | Reino Unido (en-GB) |
| Idioma del sistema | Inglés (en) |
| Densidad de pantalla | 320 dpi (ro.sf.lcd_density) |
| CPU ABI | armeabi-v7a / armeabi |
| Plataforma | Exynos 4 (SMDK4X12_PRIME) |
| Knox | Activado (ro.config.knox=1) |
| Zona horaria del build | KST (Korea Standard Time) |
| Fingerprint | samsung/t0lteskt/t0lteskt:4.4.2/KOT49H/E250SKSUKOH4:user/release-keys |
| timezoneInstance | Asia/Seoul |
| localTimezone | Asia/Seoul |
| account_name | simonhallym@gmail.com |
| fifi_p2p_devide_name | Simon (SHV-E250S) |
| device_name | Simon (SHV-E250S) |
| handwriting_language_list | ko_KR;en_US; |
| Última hora de check-in | 1500103204379 15/07/2017 16:00:04 UTC |
| Hora de última tarea programada | 1500103102206 15/07/2017 15:48:22 UTC|
| auth_zen_enable | true |
| location:ulr_enable_wifi_batching | false |
| auth_credentials_api_is_enabled | true |
| pubkey_blacklist | Censurado ||abcdef1234567890|| |
| facelock_max_center_movement | 15 |
| date_format | yyyy-MM-dd |
| networks | "T wifi zone_secure", "T wifi zone", "U+zone", "IoTLab_WAN", "IoTLab", "neo_house5", "home", "setupEBC2", "HOME" |

Vale, creo que con esta información inicial del telefono será suficiente, voy a empezar a investigar los archivos en busca de información relevante para poder hacer una línea del tiempo. Lo haré por orden de encontrado y luego lo ordenaré todo.

- Notas del teléfono:

Se encuentra una nota de lo que parece ser un diario: El autor, lleva a sus hijos(Jasin y otro) a "Fantasy World" para ver "Carnival Fantasy" el día 05/09/2012

Un posible mapa:
![alt text](img/snb_thumbnailimage_001.jpg)

Se encuentra una nota con la siguiente información: Viaje a "Abbey Sacred" 05/09/2012

Se encuentra un folleto de "Fantasy Parade"
![alt text](img/snb_thumbnailimage_001-1.jpg)

Se encuentran varias entradas relacionadas con el trabajo del autor:
![alt text](img/snb_thumbnailimage_001-2.jpg)
![alt text](img/snb_thumbnailimage_001-3.jpg)
![alt text](vsnb_thumbnailimage_001-4.jpg)
![alt text](img/snb_thumbnailimage_001-5.jpg)

Se encuentra una nota del trabajo que indica una reunión el día 29 de abril de 2012 a las 4 p.m.
![alt text](img/snb_thumbnailimage_001-6.jpg)
![alt text](img/snb_thumbnailimage_002.jpg)

- Aplicaciones instaladas:

> Carácteristica de "Autopsy"

Hay un montón de aplicaciones, pero las que más pueden interesar son:

ChatOn(El WhatsApp de Samsumng)
Google Talk(Hangouts)
Gmail
Chrome
Alexacommands
Dropbox
Kodi

- Conversaciones:

> /data/data/com.sec.chaton

Parece que la aplicación "ChatOn" nunca se usó, ya que el directorio no contine los archivos necesarios.

> /data/data/com.google.anroid.gm

Tampoco se encuentra información relevante, más que muchos mensajes de spam de vuelos.

- Historial de navegación:

![alt text](img/image.png)

Lo único interesante que sacamos son las busquedas relacionadas con la programación, que junto con las notas anteriores, podemos teorizar que el usurio es programador.

En el archivo "Coockies" encontramos entradas normales, servicios de google, samsung, etc.

