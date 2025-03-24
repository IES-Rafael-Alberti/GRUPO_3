
## Índice

1. [Cambiar contraseña por defecto](#cambiar-contraseña-por-defecto)  
2. [Revisar versión del firmware](#revisar-versión-del-firmware)  
3. [Cifrado de la red Wi-Fi](#cifrado-red-wifi)  
4. [Ajuste de potencia de transmisión](#ajuste-de-potencia-de-transmisión)  
5. [Configuración VLAN para segmentar la red](#configuracion-vlan-para-segmentar-la-red)  
6. [Habilitación de DNS sobre HTTPS](#habilitación-de-dns-sobre-https)  
7. [Control de acceso y restricciones](#control-de-acceso-y-restricciones)  
8. [Evitar el uso de ancho de banda](#evitar-el-uso-de-ancho-de-banda)  
9. [Verifica que UPNP esté desactivado](#verifica-que-upnp-este-desactivdado-en-appupnp)  
10. [Bloqueo de puertos no deseados](#bloqueo-de-puertos-no-deseados)  
11. [Bloquear para que nadie pueda hacer ping al router](#bloquear-para-que-nadie-pueda-hacer-ping-a-tu-router)  
12. [Desactivar SSH](#desactivar-ssh)  
13. [Ocultar el nombre de la red](#ocultar-el-nombre-de-la-red)  
14. [Backup de la configuración](#backup-de-la-configuración)

## Cambiar contraseña por defecto

Accedemos a `Settings > System > Change Router Password`.  
Allí reemplazamos la contraseña de administración por una contraseña segura

![alt text](<img/Pasted image 20250323204547.png>)
![alt text](<img/Pasted image 20250323204613.png>)

## Revisar versión del Firmware

En `Settings > System > Flash New Firmware`, vemos si hay una actualización disponible.  

Mantener el firmware actualizado para que se corrijan vulnerabilidades y se mejore el rendimiento.

![alt text](<img/Pasted image 20250323204931.png>)

## Cifrado red wifi

Ruta: `Settings > Wireless`

![alt text](<img/Pasted image 20250323205837.png>)

Se selecciona el cifrado **WPA-PSK** y el algoritmo **CCMP**, que es el estándar más seguro para redes domésticas. Se evita el modo "mixed" y cifrados antiguos como TKIP

![alt text](<img/Pasted image 20250323210104.png>)

## Ajuste de potencia de transmisión 

En la Wireless, ajustamos la **potencia de transmisión al 50%**, para cubrir el hogar sin necesidad de que llegue demasiado lejos de tu casa

![alt text](<img/Pasted image 20250323210713.png>)

## Configuracion VLAN para segmentar la red 

En este apartado segmentamos la red física del router creando redes virtuales independientes (VLANs), asignando cada puerto Ethernet a una red distinta: por ejemplo, el puerto 1 se asigna a la red de invitados (**Guest**), y los puertos 2 a 4 se asignan a la red interna (**LAN**).

Además, configuramos las reglas de acceso entre redes, impidiendo que los dispositivos de una VLAN accedan a otras. Por ejemplo, los dispositivos conectados a **Guest** no pueden comunicarse con **LAN** ni con las VLANs **X1, X2 o X3**, mientras que cada subred está aislada del resto.

![alt text](<img/Pasted image 20250323211052.png>)

## Habilitación de DNS sobre HTTPS

![alt text](<img/Pasted image 20250323211357.png>)

## Control de acceso y restricciones

He puesto en la lista negra a tiktok y discord, por ejemplo, para que no entren los usuario, he habitado los block ads y he puesto moderated restricted a youtube

![alt text](<img/Pasted image 20250323211704.png>)

## Evitar el uso de ancho de banda

Habilitamos el `bandwidth monitor` en apps/

![alt text](<img/Pasted image 20250323211950.png>)

## Verifica que UPNP este desactivdado en app/upnp 

![alt text](<img/Pasted image 20250323212627.png>)

## Bloqueo de puertos no deseados

En esta sección añadimos una regla específica para **evitar conexiones externas al puerto 445**, el cual es comúnmente utilizado por servicios de compartir de archivos (SMB) y es objetivo frecuente de ataques.

Se crea una entrada de _Port Forward_ apuntando al propio router con ese puerto para **bloquearlo activamente desde la interfaz WAN**. Esto impide que equipos de internet intenten conectarse a ese puerto en la red local.

![alt text](<img/Pasted image 20250323212935.png>)

## Bloquear para que nadie pueda hacer ping a tu router 

En settings>network>security

![alt text](<img/Pasted image 20250323213120.png>)

## Desactivar SSH

En un dispostivio doméstico no creo que se vaya a usar ssh por eso lo desactivo en Settings > System

![alt text](<img/Pasted image 20250323214817.png>)

## Ocultar el nombre de la red

Settings > Wireless > Disable SSID broadcast

![alt text](<img/Pasted image 20250323215035.png>)

## Backup de la configuración

Nos vamos a Settings > System > Backup

![alt text](<img/Pasted image 20250323215155.png>)

y nos guardamos en un lugar seguro el archivo comprimido con la configuración segura

