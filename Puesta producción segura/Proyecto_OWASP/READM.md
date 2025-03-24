# Informe sobre la Vulnerabilidad: Insecure API

## 1. Controles proactivos (buenas prácticas durante el desarrollo)
Una API segura comienza desde su diseño. Durante el desarrollo, es esencial aplicar principios como el de mínimo privilegio, exponiendo únicamente la información necesaria y evitando que los endpoints revelen datos sensibles de forma innecesaria. Las entradas del usuario deben ser cuidadosamente validadas y saneadas, ya que confiar ciegamente en lo que recibe el servidor es abrirle la puerta a los atacantes.

En lo que respecta a la autenticación y autorización, es imprescindible utilizar mecanismos robustos como OAuth2 o JWT, aplicándolos no solo en el login, sino también para verificar que cada petición tenga los permisos adecuados. Además, toda la comunicación debe estar cifrada usando HTTPS; exponer una API por HTTP es prácticamente regalar los datos.

También conviene limitar la frecuencia con la que los clientes pueden hacer peticiones. Implementar técnicas como el rate limiting o throttling ayuda a proteger el sistema frente a abusos, como ataques de fuerza bruta o intentos masivos de denegación de servicio. Por último, los mensajes de error que devuelve la API no deberían ser demasiado detallados. Cuanta menos información se le dé a un posible atacante, mejor.

## 2. ASVS (Application Security Verification Standard)
El estándar ASVS de OWASP ofrece un marco para verificar el nivel de seguridad en aplicaciones, y muchas de sus secciones aplican directamente al diseño de APIs. Por ejemplo, se requiere una autenticación sólida en todos los endpoints sensibles, junto con una verificación estricta de los roles y permisos de los usuarios que hacen peticiones.

Otro de los pilares del ASVS es la validación de entradas. Cada parámetro recibido por la API debe analizarse tanto en el cliente como en el servidor para evitar manipulaciones. También se exige que las comunicaciones estén cifradas correctamente y que se protejan contra ataques como el replay. Finalmente, el manejo de errores debe ser cuidadoso: nada de exponer trazas internas ni detalles técnicos en las respuestas, pero sí mantener registros auditables que permitan rastrear cualquier actividad sospechosa.

Estos controles permiten que las APIs no solo sean funcionales, sino también resilientes ante ataques, incluso en entornos complejos como arquitecturas basadas en microservicios o aplicaciones móviles.

## 3. Perspectivas de futuro
Las APIs no solo seguirán existiendo, sino que serán cada vez más protagonistas en el desarrollo de software. Con la explosión de servicios web, aplicaciones móviles, IoT, y arquitecturas de microservicios, el número de interfaces expuestas al exterior no deja de crecer. Cada una de ellas representa un posible punto de entrada para un atacante.

Además, la integración de la inteligencia artificial en el desarrollo está llevando a la creación automática de código, incluyendo APIs. Esto puede derivar en errores de seguridad si no se revisa manualmente lo generado. Por otro lado, el crecimiento del internet de las cosas implica que millones de dispositivos –muchos de ellos con recursos limitados y escasas medidas de protección– se conectarán constantemente a través de APIs.

En resumen, el futuro apunta a un ecosistema digital cada vez más interconectado, donde la seguridad de las APIs no será una opción, sino un requisito fundamental.

## 4. Posible gravedad de las amenazas
Una API mal diseñada o mal protegida puede convertirse en un auténtico desastre. Las consecuencias pueden ir desde la exposición de información sensible de los usuarios hasta el compromiso total del sistema. Si falla la autenticación o la autorización, un atacante puede asumir identidades ajenas o acceder a recursos restringidos. En otros casos, una API vulnerable puede ser utilizada como puerta de entrada para realizar movimientos laterales dentro de una red interna.

Más allá del daño técnico, está el impacto legal y reputacional. En tiempos de normativas como el GDPR, una brecha de datos ocasionada por una API insegura puede suponer multas millonarias y la pérdida de la confianza por parte de los usuarios. Casos como el de Facebook en 2018, donde se accedió a millones de tokens de usuario debido a una API vulnerable, demuestran hasta qué punto este tipo de errores puede afectar incluso a gigantes tecnológicos.