# Políticas de Autenticación

## Basada en contraseñas y frases de paso

1. Las contraseñas deben ser lo suficientemente largas y seguras, con un mínimo de 12 caracteres que incluyan una mezcla de letras mayúsculas, minúsculas, números y caracteres especiales. Esto ayuda a evitar que sean fácilmente adivinadas.
2. Se establecerá un sistema que facilite a los usuarios la creación y almacenamiento de contraseñas complejas, como un gestor de contraseñas accesible para todos los empleados.
3. Cada 90 días será necesario cambiar la contraseña, pero también se avisará a los usuarios con antelación para evitar inconvenientes.
4. Para accesos más importantes, como servidores o sistemas confidenciales, será obligatorio usar frases de paso. Estas frases deberán tener al menos 16 caracteres y estar formadas por palabras que no estén relacionadas, por ejemplo: "ElefantePianoAzul2023".
5. Las contraseñas antiguas no podrán ser reutilizadas y se verificará que ninguna de las nuevas haya sido filtrada previamente en ataques a otras plataformas.
6. Todos los empleados recibirán capacitaciones regulares para aprender cómo crear contraseñas fuertes y cómo mantenerlas seguras, evitando compartirlas.
7. Se harán auditorías cada año para asegurarse de que estas políticas están funcionando y detectar si hay puntos débiles que mejorar.
8. Las cuentas que detecten múltiples intentos fallidos de inicio de sesión serán bloqueadas temporalmente para evitar ataques de fuerza bruta.
9. En el caso de olvidar la contraseña, se implementará un proceso de recuperación que sea sencillo pero que también garantice la identidad del usuario antes de restablecer el acceso.
10. Se fomentará el uso de autenticación multifactor (MFA) en combinación con contraseñas, para proporcionar una capa adicional de seguridad.

## Basada en certificados digitales y tarjetas inteligentes

1. Se emplearán certificados digitales que cumplan con estándares actuales como RSA de 2048 bits o equivalentes más seguros. Esto asegura que los datos estén protegidos de manera adecuada.
2. Las tarjetas inteligentes serán obligatorias para cualquier persona que acceda a sistemas sensibles o información clasificada dentro de la organización.
3. Un sistema de gestión de certificados (PKI) se encargará de administrar de forma segura la emisión, renovación y revocación de certificados digitales.
4. En los procesos más críticos se requerirá una autenticación de doble factor, combinando el certificado digital con algo adicional, como un PIN único.
5. Los certificados se revisarán anualmente para confirmar que siguen siendo seguros y para aplicar actualizaciones cuando sea necesario.
6. Si una tarjeta inteligente se pierde o se ve comprometida, se deberá reportar de inmediato y el certificado asociado será revocado para prevenir accesos no autorizados.
7. Se simularán ataques para evaluar cómo responde el sistema y detectar posibles fallos en la seguridad de los certificados.
8. Los empleados recibirán formación sobre cómo proteger sus tarjetas inteligentes y evitar el uso indebido.
9. Habrá un sistema de respaldo que permita la autenticación en caso de que las tarjetas inteligentes no estén disponibles temporalmente.
10. Se implementarán medidas para garantizar que las claves privadas asociadas a los certificados nunca salgan del hardware seguro donde se generan.

## Basada en tokens y OTPs

1. Los tokens, tanto físicos como digitales, deberán generar contraseñas de un solo uso (OTP) que caduquen rápidamente, preferiblemente en 30 o 60 segundos.
2. Este tipo de autenticación será obligatorio para accesos remotos, como conexiones VPN o sistemas de pago, donde los riesgos son mayores.
3. Los dispositivos o aplicaciones que generan los tokens serán revisados regularmente para asegurarse de que no tienen vulnerabilidades.
4. Si un token es perdido, el usuario deberá reportarlo inmediatamente, y se desactivará para evitar que sea utilizado por personas no autorizadas.
5. Un sistema de supervisión verificará en tiempo real el uso de los OTP, detectando intentos de reutilización o interceptación.
6. Los empleados serán capacitados para usar sus tokens de forma segura y entender cómo reportar problemas relacionados con ellos.
7. Se implementará un sistema de respaldo que permita el acceso temporal en caso de que el token no esté disponible, sin comprometer la seguridad.
8. Todos los registros de uso de tokens serán revisados periódicamente para identificar actividades sospechosas o fuera de lo común.
9. Las soluciones basadas en tokens deberán cumplir con estándares abiertos como TOTP (Time-based One-Time Password) para garantizar su interoperabilidad.
10. En accesos críticos, los tokens serán utilizados junto a otros métodos de autenticación, como biometría o contraseñas seguras.

## Basada en características biométricas

1. Se preferirán tecnologías biométricas confiables como huellas dactilares, reconocimiento facial o escaneo de iris para áreas donde se necesita máxima seguridad.
2. Los dispositivos biométricos tendrán que cumplir con estándares altos de precisión y evitar falsos positivos, como que alguien no autorizado pueda acceder.
3. Los datos biométricos se tratarán como información extremadamente confidencial y serán almacenados solo en sistemas cifrados.
4. Nunca se almacenarán datos biométricos en su forma original; siempre estarán protegidos por algoritmos avanzados de cifrado.
5. Si un sistema biométrico detecta una anomalía, como intentos repetidos de acceso, se activarán alertas automáticas y se investigará el incidente.
6. En caso de fallos o problemas técnicos con la autenticación biométrica, se dispondrá de métodos alternativos que garanticen la continuidad del acceso.
7. Los usuarios serán informados sobre cómo se manejarán sus datos biométricos y tendrán derechos sobre estos, como la posibilidad de eliminarlos si ya no trabajan en la organización.
8. Se harán pruebas regulares para comprobar que los sistemas biométricos son resistentes a ataques de suplantación, como el uso de fotos o videos.
9. La implementación de esta tecnología respetará todas las normativas legales relacionadas con la protección de datos personales.
10. La biometría se combinará con otros métodos, como contraseñas o tokens, en situaciones donde se necesite doble verificación.

