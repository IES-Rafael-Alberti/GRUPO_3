# Hardening a un router

## Introducción

En esta parte del proyecto se nos pide usar un emulador de routers reales y hacer una guía de bastionado.
He elegido el emulador online de [ASUS](https://demoui.asus.com/ES/) porque es accesible, completo y muy intuitivo.

![alt text](img/image.png)

## Antes de Empezar

Antes de entrar al lío, hay que tener claras unas medidas básicas de seguridad que deberíamos aplicar sí o sí en cualquier router:

**1. Actualizar el Firmware**

![alt text](img/image-1.png)

Tener el firmware al día es clave para corregir fallos de seguridad que ya se conocen. Nada nuevo, pero mucha gente lo pasa por alto.

**2. Cambiar las Credenciales por Defecto**

![alt text](img/image-2.png)

La mayoría de routers vienen con usuario y contraseña por defecto, y son tan conocidas que cualquiera podría entrar si no se cambian.

![alt text](img/image-3.png)

Aprovechamos y cambiamos también la contraseña del WiFi, que muchas veces arrastra el mismo problema.

**3. Desactivar Servicios Innecesarios**

Esto depende mucho del entorno, pero por lo general, hay cosas que sobran.
Por ejemplo, **AiCloud**, que sirve para compartir archivos desde un USB conectado al router. Si ya hay un NAS o carpetas compartidas, sobra completamente.

![alt text](img/image-4.png)

## Bastionado

Ahora sí, vamos con el recorrido completo por las secciones del router, viendo qué se puede reforzar y qué es mejor desactivar.

### Sección General

**1. Mapa de la red**

![alt text](img/image-5.png)

EAquí se ve lo típico: dispositivos conectados, estado general del WiFi, etc.

![alt text](img/image-6.png)

![alt text](img/image-7.png)

También nos deja tocar cosas importantes como el SSID, tipo de cifrado y contraseña.

![alt text](img/image-8.png)

**2. AiMesh**

Sirve para montar una red en malla usando varios routers ASUS.
No se puede desactivar, pero tampoco molesta. Si se quiere usar, basta con conectar otro router y asignarle IP.

![alt text](img/image-9.png)

**3. Red para invitados**

Crea una red separada, así que no representa mucho riesgo, pero puede afectar al rendimiento.
Viene desactivada por defecto, y así se puede quedar salvo que sea estrictamente necesario.

![alt text](img/image-10.png)
> Por defecto viene desactivado.

**4. AiProtection**

Funciona como IDS/IPS, detecta amenazas antes de que lleguen a los dispositivos. Tiene dos partes:

![alt text](img/image-13.png)

**4.1. Protección de red**

![alt text](img/image-14.png)

Dejar activado. Aporta bastante a nivel de seguridad.

**4.2. Control paterno**

![alt text](img/image-15.png)

Esto lo quitaría. No bloquea contenido realmente peligroso, solo páginas *adultas*, y encima consume recursos.

**5. Adaptive QoS**

Solo muestra estadísticas de ancho de banda. No afecta a la seguridad.

**6. Traffic Analyzer**

Permite ver qué dispositivos consumen más red y qué aplicaciones están usando.

![alt text](img/image-16.png)

**7. USB applications**

Si se puede, mejor desactivarlas. Son un punto de entrada físico que no siempre se controla bien.

**8. AiCloed 2.0**

![alt text](img/image-17.png)

Desactivamos todo: Cloud Disk y Smart Access. Si la empresa usa NAS, ya se accede por red, no por aquí.

### Configuración avanzada

**1. Wireless**

![alt text](img/image-18.png)

Si hay que dejar el WiFi activado, que sea con autenticación WPA2 Enterprise.
Y si hay un servidor RADIUS, se configura así:

![alt text](img/image-19.png)

**2. LAN**

Aquí se configura la IP del router, la máscara de red...

![alt text](img/image-20.png)

![alt text](img/image-21.png)

...y el DHCP. Si se desactiva, habría que asignar IPs a mano por MAC.

**3. WAN**

Permite que los dispositivos tengan internet. No hay mucho que pensar: activado.

![alt text](img/image-22.png)

**4. Alexa & IFTTT**

**Ni tocarlo.**
Abre la puerta a servicios externos que no pintan nada en una red segura.

**5. IPv6**

Aunque está en auge, todavía no está 100% implantado en todos lados. Mejor desactivado salvo que sea necesario.

![alt text](img/image-23.png)

**6. VPN**

Si hay teletrabajo, se puede activar para que se conecten desde fuera de forma segura.

![alt text](img/image-24.png)

**7. Firewall**

![alt text](img/image-25.png)

Sirve para bloquear tráfico entrante/saliente por IP o puerto.
El sistema de este router no permite filtrar todo lo que quisiéramos, pero sí podemos hacer redirecciones (port forwarding), útil por ejemplo si tenemos una VPN local.

![alt text](img/image-27.png)
> Ejemplo de redireccionamiento

También se pueden bloquear URLs concretas.

![alt text](img/image-28.png)

**8. Administration**

Aquí se gestiona el acceso al router, las actualizaciones y las copias de seguridad:



![alt text](img/image-29.png)

![alt text](img/image-30.png)

![alt text](img/image-31.png)
> Para las copias, se necesita activar temporalmente el USB.

**9. System Log**

![alt text](img/image-32.png)

Registro de eventos del router. Útil para revisar fallos, accesos y demás.

![alt text](img/image-33.png)

![alt text](img/image-34.png)

**10. Network Tools**

No se va a usar en esta práctica.

## Conclusión

Y con esto tendríamos el bastionado del router ASUS.
Obviamente, he configurado el router como yo lo veo más seguro, pero cada empresa tiene sus necesidades. Lo que para unos sobra, para otros puede ser imprescindible.
Esta guía sirve como punto de partida. A partir de aquí, lo suyo es adaptarlo según el entorno y lo que se quiera proteger.