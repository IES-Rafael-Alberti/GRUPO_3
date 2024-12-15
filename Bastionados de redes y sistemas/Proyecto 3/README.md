# Windows 10

Para este proyecto, comenzaré con la instalación de un sistema operativo Windows en una máquina virtual. Mi objetivo será analizar el entorno inicial, identificando, listando y eliminando todos aquellos programas, servicios y protocolos que considere innecesarios. Este proceso permitirá optimizar el equipo para un uso específico: navegación web y tareas básicas de ofimática.

## Indice:

- [**Limpieza de programas**](#limpieza-de-programas)
- [**Limpieza de protocolos**](#limpieza-de-protocolos)
- [**Limpieza de servicios**](#limpieza-de-servicios)

---
## Limpieza de programas

Empecemos por quitar todos los programas inecesarios de la computadora. Para ello debemos abrir la configuración de Windows pulsando las teclas Windows+I, y pulsar en aplicaciones. Deberíamos tener algo así:

![](/images/1.png)

Debemos borrar todas las aplicaciones que sean innecesarias de la siguiente manera:

![](/images/2.png)

Tendremos que hacer esto con todos los programas que queramos eliminar, y deberimos quedarnos con algo así:

![](/images/3.png)

De esta forma ya habríamos acabado con la eliminación de programas innecesarios. Alternativamente, podríamos optar por la instalación de aplicaciones de terceros para hacer más fácil el trabajo de los empleados. Algunas de ellas podrían ser un navegador, un lector de PDFs, etc:

![](/images/4.png)

---
## Limpieza de protocolos

Pasemos ahora a la limpieza de protocolos innecesarios o que puedan vulnerar al sistema. Lo primero que quitaremos es el ipv6, el cual en un futuro proximo puede llegar a ser de utilidad, pero a día de hoy da más problemas que soluciones. Para hacerlo seguimos los siguientes pasos:

![](/images/5.png)

![](/images/6.png)

De esta forma ya quedaría deshabilitado ipv6 de nuestro sistema, quitemos ahora el protocolo NetBIOS, que al estar anticuado puede traer problemas de vulnerabilidad. Para hacerlo, entramos en la configuración anterior y hacemos lo siguiente:

![](/images/7.png)

Por último, vamos a bloquear los protocolos **ICMP** y **SNMP**. El protocolo **ICMP** lo podemos bloquear creando una regla en el firewall que rechace todo el tráfico ICMP que provenga del exterior. Para conseguir esto hacemos lo siguiente:

![](/images/8.png)

![](/images/9.png)

![](/images/10.png)

![](/images/11.png)

![](/images/12.png)

![](/images/13.png)

![](/images/14.png)

![](/images/15.png)

![](/images/16.png)

De esta forma, ya habremos bloqueado todos los accesos ICMP que provengan del exterior como los PING.

Ahora vamos a quitar el protocolo **SNMP** con el siguiente comando en la consola del adiministrador(powershell):

>Para ver si está instalado
![](/images/18.png)

>Para quitarlo en caso que esté
![](/images/19.png)

Adicionalmente, podemos desactivar **LLDP** y **QoS** de nuestro sistema ya que no los necesitamos:

![](/images/20.png)

SMBv1, que está anticuado y puede ser vulnerable:

![](/images/21.png)

Y los protocolos **TFTP** y **TELNET**

![](/images/22.png)

---
## Limpieza de servicios

Por último vamos a configurar los servicios de nuestro sistema y vamos a quitar todos los que no vayamos a utilizar. Para quitar servicios, podemos hacerlo de la siguiente manera: 

![](/images/23.png)

![](/images/24.png)

Tras un vistazo a todos los servicios en ejecución, creemos oportunos quitar los siguientes:

- Administrador de conexiones de acceso remoto
- Agente de eventos de tiempo
- Aplicación auxiliar de NetBIOS sobre TCP/IP
- Servicio de administración de radio
- Servicio de geolocalización
- Servicio de Panel de escritura a mano y teclado táctil
- Temas
