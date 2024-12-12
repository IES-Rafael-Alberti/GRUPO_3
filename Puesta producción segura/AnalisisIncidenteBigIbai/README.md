# Análisis de incidente desde la perspectiva de puesta en producción

Hecho por:

- Víctor Jiménez
- Israel Valderrama
- Alejandro Seoane

## Indice

1. [Introducción](#1-introducción)
2. [Análisis previo a la puesta en producción del proyecto](#2-análisis-previo-a-la-puesta-en-producción-del-proyecto)
3. [Análisis del incidente](#3-análisis-del-incidente)
4. [Puesta en marcha del sistema tras el incidente](#4-puesta-en-marcha-del-sistema-tras-el-incidente)

## 1. Introducción

## 2. Análisis previo a la puesta en producción del proyecto

La puesta en producción de un sitio web basado en WordPress debe considerar estrategias específicas para mitigar riesgos asociados a ataques de denegación de servicio (DoS) y denegación de servicio distribuido (DDoS). Tras analizar el caso, estos son los pasos a seguir para una puesta en producción segura del proyecto:

### 1. Evaluación inicial del entorno

- **Revisión de infraestructura**: Identificar el entorno donde será desplegado (hosting compartido, VPS, servidores dedicados o cloud). Los entornos en la nube como AWS, Azure o Google Cloud ofrecen herramientas específicas para mitigar ataques DDoS.
- **Evaluación de amenazas**: Identificar posibles vectores de ataque (bots, tráfico malicioso, abuso de recursos) y calcular el impacto de un ataque en términos de disponibilidad, reputación y costos.
- **Análisis de dependencia**: Evaluar plugins, temas y configuraciones de WordPress que puedan convertirse en puntos débiles si reciben demasiado tráfico.

### 2. Implementación de medidas de mitigación

#### a) Red e infraestructura

- **Uso de un WAF (Web Application Firewall)**: Configurar un WAF como Cloudflare, Sucuri o el propio AWS Shield para filtrar tráfico malicioso antes de que llegue al servidor.
- **Capas de protección DDoS**: Utilizar servicios anti-DDoS proporcionados por proveedores (p. ej., Cloudflare Advanced DDoS Protection o Akamai).
- **Rate limiting y throttling**: Implementar límites en el número de peticiones permitidas por IP en un periodo de tiempo.
- **Balanceo de carga y redundancia**: Si el tráfico esperado es elevado, emplear un balanceador de carga para distribuir el tráfico entre múltiples servidores

#### b) Servidor

- **Seguridad en el servidor web**:
  - Asegurarse de que el servidor esté configurado para resistir grandes volúmenes de tráfico (ajuste de parámetros como _max_connections_, _timeout_, etc.).
  - Activar módulos como `mod_evasive` en Apache o configuraciones similares en Nginx para bloquear ataques de fuerza bruta HTTP.
- **Monitorización en tiempo real**:
  - Implementar sistemas de monitoreo de tráfico (Zabbix, Nagios o herramientas específicas del proveedor cloud) para detectar picos anormales en tiempo real.
- **Aislamiento de recursos**:
  - Si el WordPress comparte servidor con otras aplicaciones, aislar los recursos para evitar que un ataque afecte todo el entorno.

#### c) Aplicación

- **Endurecimiento de WordPress**:
  - Desactivar XML-RPC si no es absolutamente necesario (ataques vía `xmlrpc.php` son comunes en WordPress).
  - Limitar las solicitudes REST API a direcciones IP confiables.
  - Proteger archivos críticos como `wp-config.php` y deshabilitar el acceso al listado de directorios.
- **Plugins de seguridad**: Instalar y configurar plugins como Wordfence o iThemes Security, que permiten bloquear tráfico sospechoso automáticamente.

## 3. Análisis del incidente

## 4. Puesta en marcha del sistema tras el incidente
