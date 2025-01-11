# Introducción

Este documento recoge las principales vulnerabilidades, tipos de ataque y sus respectivas estrategias de mitigación de los tipos de credenciales mas utilidados.

## Digitales

### Certificados digitales

### Perfiles de redes sociales

### Blockchain

### Microcredenciales

## Fisicas

### Targeta de identificación

### Diplomas y Certificados físicos

### Targetas inteligentes

### Targetas de acceso NFC

---

## Autenticación

### Códigos QR

- **Vulnerabilidades**: Los códigos QR son susceptibles a manipulación, como la creación de códigos QR maliciosos que redirigen a sitios web fraudulentos o descargan malware. También carecen de mecanismos de verificación visual, lo que dificulta distinguir entre un código QR legítimo y uno falso.

- **Tipos de ataque**: Los atacantes pueden emplear ataques de phishing mediante QR, conocidos como quishing, o superponer códigos QR maliciosos sobre los legítimos. En algunos casos, también pueden interceptar y modificar datos en tránsito si el QR es utilizado para transmitir información.

- **Mitigación**: Verificar los enlaces a los que apunta el código QR antes de interactuar con ellos, implementar firmas digitales en los códigos QR para autenticar su origen, y educar a los usuarios para que sean cautelosos con códigos QR en ubicaciones públicas no confiables.

### Autenticación de dos factores (2FA)

- **Vulnerabilidades**: El 2FA puede ser comprometido si uno de los factores es débil, como contraseñas fácilmente adivinables, o si el canal de comunicación es inseguro, como mensajes SMS que pueden ser interceptados.

- **Tipos de ataque**: Los ataques comunes incluyen intercepción de SMS mediante técnicas como SIM swapping o malware en dispositivos móviles. Además, el phishing puede engañar a los usuarios para proporcionar tanto su contraseña como el código 2FA.

- **Mitigación**: Utilizar aplicaciones de autenticación como Google Authenticator en lugar de SMS, emplear métodos de 2FA más robustos como claves físicas, y combinar el 2FA con monitoreo de acceso sospechoso para detectar anomalías.

### Biometría

- **Vulnerabilidades**: Los sistemas biométricos son vulnerables a la falsificación de datos biométricos, como huellas dactilares falsas o patrones faciales replicados. Además, si los datos biométricos son robados, no pueden ser reemplazados como una contraseña.

- **Tipos de ataque**: Ataques de falsificación biométrica (como huellas impresas en silicona) y ataques de replay donde un atacante reutiliza datos biométricos capturados anteriormente. También puede haber abuso interno si el sistema no está correctamente segmentado.

- **Mitigación**: Usar hardware seguro para almacenar datos biométricos (por ejemplo, módulos TPM), implementar detección de vida (liveness detection) en los sistemas biométricos, y asegurarse de que los datos biométricos sean cifrados en tránsito y en reposo.

### One Time Password (OTP) SMS

- **Vulnerabilidades**: Los OTP basados en SMS son vulnerables a intercepción debido a debilidades en las redes de telecomunicaciones (como SS7). También pueden ser expuestos si el dispositivo móvil está comprometido.

- **Tipos de ataque**: Técnicas como el SIM swapping, malware móvil o phishing pueden ser empleadas para obtener los códigos OTP enviados por SMS.

- **Mitigación**: Cambiar SMS por aplicaciones de autenticación, implementar límites en los intentos de ingreso, y monitorear patrones anómalos en los accesos para detectar posibles compromisos.

## Dominio y Genéricas

### Credenciales de dominio

- **Vulnerabilidades**: Las credenciales de dominio suelen tener acceso a múltiples recursos críticos en un entorno empresarial. Si no se gestionan adecuadamente, como mediante contraseñas débiles o políticas laxas, pueden ser un objetivo prioritario para los atacantes.

- **Tipos de ataque**: Ataques de fuerza bruta para adivinar credenciales, técnicas como Pass-the-Hash para reutilizar hashes de contraseñas robadas, y el uso de herramientas como Mimikatz para extraer credenciales directamente de la memoria.

- **Mitigación**: Implementar contraseñas robustas, políticas de cambio periódico de contraseñas, y activar autenticación multifactor (MFA) para credenciales de dominio. Además, segmentar privilegios y usar detección de amenazas para identificar intentos no autorizados.

### Credenciales genéricas

- **Vulnerabilidades**: Las credenciales genéricas suelen ser compartidas entre múltiples usuarios, lo que dificulta el rastreo de responsabilidades y aumenta el riesgo de que sean reutilizadas o filtradas.

- **Tipos de ataque**: Ataques de fuerza bruta o técnicas de credential stuffing donde atacantes prueban combinaciones comunes de credenciales. Además, si las credenciales se filtran, pueden ser reutilizadas en otros sistemas.

- **Mitigación**: Prohibir el uso de credenciales genéricas, asignar credenciales únicas a cada usuario y emplear herramientas de gestión de accesos para monitorizar su uso.

## Aplicaciones

### Tokens de acceso

- **Vulnerabilidades**: Los tokens de acceso, si no están configurados correctamente, pueden ser capturados y reutilizados por atacantes. También pueden no tener expiración o permisos excesivos, aumentando el riesgo de abuso.

- **Tipos de ataque**: Robo de tokens mediante la intercepción de tráfico no cifrado, almacenamiento inseguro en dispositivos cliente, o ataques de Cross-Site Scripting (XSS) para extraerlos del navegador.

- **Mitigación**: Configurar expiración y alcance limitados para los tokens, asegurar la comunicación con HTTPS, y almacenar tokens de manera segura utilizando mecanismos como almacenamiento cifrado en dispositivos.

### API keys

- **Vulnerabilidades**: Las API keys suelen ser expuestas en repositorios públicos (por ejemplo, en GitHub) o en aplicaciones cliente, lo que facilita su uso no autorizado.

- **Tipos de ataque**: Los atacantes pueden emplear ataques de abuso de API, explotando las API keys para realizar solicitudes masivas o acceder a datos sensibles. También pueden aprovechar permisos mal configurados para escalar privilegios.

- **Mitigación**: Rotar las API keys regularmente, usar restricciones de origen para limitar el uso de las claves a dominios específicos, y habilitar monitoreo para detectar actividades sospechosas.

### Certificados digitales

- **Vulnerabilidades**: Si los certificados digitales no son gestionados correctamente, como no renovarlos a tiempo o permitir el uso de algoritmos débiles, pueden ser comprometidos.

- **Tipos de ataque**: Los atacantes pueden emplear ataques de intermediario (MITM) al aprovechar certificados vencidos o robados, o incluso intentar falsificar certificados si los controles no son adecuados.

- **Mitigación**: Usar autoridades certificadoras confiables, implementar monitoreo automatizado para la expiración de certificados, y emplear estándares modernos de cifrado (como TLS 1.3) para garantizar la seguridad.
