# Proyecto 8. Parte 1: Guía de Hardening

## Introducción

En esta parte del Proyecto 8 se elaborará una guía de hardening de un dispositivo de uno de los simuladores que se encuentran en [este enlace](https://routersecurity.org/resources.php). El modelo que he escogido es el extensor de red [RE190](https://emulator.tp-link.com/re190-eu-v5/index.html#firmwareCloud) del simulador de TpLink ya que es el tengo en casa.

## Procesos

### 1. Asegurar credenciales de acceso

El primer paso es cambiar la contraseña de acceso a la configuración por una que cumpla los requisitos de credenciales seguras:

- Mínimo 12 caracteres
- Incluir letras minúsculas y mayúsculas
- Incluir números
- Incluir caracteres especiales

![5bb577bd26c195a59b3137393fcbf260.png](./img/5bb577bd26c195a59b3137393fcbf260.png)

### 2. Actualizar firmware

El segundo paso será actualizar el firmware a la ultima versión disponible ya que de esta forma podremos hacer uso de las ultimas funciones en materia de seguridad.

![5e57f5a27bf0486b0177a78ef773de81.png](./img/5e57f5a27bf0486b0177a78ef773de81.png)

![e21577b2f03e2ae389480cf5a1ae74f6.png](./img/e21577b2f03e2ae389480cf5a1ae74f6.png)

### 3. Habilitar whitelist

Para evitar que se conecten dispositivos no deseados, habilitaremos una whitelist a la que añadiremos los dispositivos que queremos que puedan conectarse.

![fa9e20e319d0b9e7fc2e13fc31676eb2.png](./img/fa9e20e319d0b9e7fc2e13fc31676eb2.png)

Para ello damos un nombre al dispositivo y añadimos su dirección MAC.

![1068e3d49659397a3e3a5044347e76b5.png](./img/1068e3d49659397a3e3a5044347e76b5.png)

### 4. Alcance de la red

Para evitar que se puede acceder a la red desde fuera del área deseada, ajustaremos el rango de la red para que se mantenga dentro de la zona desde donde queremos que sea accesible.

![7ad34511d4ccc60447843888a872ef72.png](./img/7ad34511d4ccc60447843888a872ef72.png)
