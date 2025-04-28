# Informe sobre la Vulnerabilidad: Insecure API

## 1. Controles proactivos (buenas prácticas durante el desarrollo)
Durante el desarrollo, es esencial aplicar principios como el de mínimo privilegio, exponiendo únicamente la información necesaria y evitando que los endpoints revelen datos sensibles de forma innecesaria. Las entradas del usuario deben ser validadas y saneadas, ya que confiar ciegamente en lo que recibe el servidor es abrirle la puerta a los atacantes.

En lo que respecta a la autenticación y autorización, es imprescindible utilizar mecanismos robustos como OAuth2 o JWT, aplicándolos no solo en el login, sino también para verificar que cada petición tenga los permisos adecuados. Además, toda la comunicación debe estar cifrada usando HTTPS.

También se podría implementar una limitación de peticiones por clientes. Implementar técnicas como el rate limiting o throttling ayuda a proteger el sistema frente a abusos, como ataques de fuerza bruta o intentos masivos de denegación de servicio.
Por último, los logs deberían estar implementados y detallar información relevante; como cliente, petición, URL, fecha y hora.

## 2. ASVS (Application Security Verification Standard)
El estándar ASVS de OWASP es, basicamente, un checklist para comprobar si una aplicación web es segura. Por ejemplo, se requiere una autenticación sólida en todos los endpoints sensibles, junto con una verificación estricta de los roles y permisos de los usuarios que hacen peticiones.

Otro de los pilares del ASVS es la validación de entradas. Cada parámetro recibido por la API debe analizarse tanto en el cliente como en el servidor para evitar manipulaciones.
También se exige que las comunicaciones estén cifradas correctamente y que se protejan contra ataques como el replay.
En el tema de errores, debe ser cuidadoso: nada de exponer trazas internas ni detalles técnicos en las respuestas, pero sí mantener registros auditables que permitan rastrear cualquier actividad sospechosa.

Siguiendo esta checklist, las APIs serán más resistentes a los ataques, incluso en entornos complejos como arquitecturas basadas en microservicios o aplicaciones móviles.

## 3. Perspectivas de futuro
Las APIs no se van a dejar de usar, al contrario, se van a usar más que nunca.
Con la explosión de servicios web, aplicaciones móviles, IoT, y arquitecturas de microservicios, el número de interfaces expuestas al exterior no deja de crecer.
Cada una de ellas representa un posible punto de entrada para un atacante.

La IA puede ayudar en el desarrollo, sí, pero también puede colar APIs llenas de bugs si no hay revisión humana. Y el tema IoT es otra jungla: millones de cacharros conectándose por APIs, muchos de ellos sin ni media capa de seguridad.

En resumen, el futuro apunta a un ecosistema digital cada vez más interconectado, donde la seguridad de las APIs no será una opción, sino un requisito para el correcto funcionamiento de las webs.

## 4. Posible gravedad de las amenazas
Una API insegura puede convertirse en un auténtico desastre. 
Las consecuencias pueden ir desde la exposición de información sensible de los usuarios hasta el compromiso total del sistema.
Si falla la autenticación o la autorización, un atacante puede asumir identidades ajenas o acceder a recursos no autorizados.
En otros casos, una API vulnerable puede ser utilizada como puerta de entrada para realizar movimientos laterales dentro de una red interna.

También está el impacto legal y reputacional. Existiendo leyes como el GDPR(Reglamento General de Protección de Datos), una brecha de datos ocasionada por una API insegura puede suponer multas millonarias y la pérdida de la confianza por parte de los usuarios.

Tenemos el caso de Facebook, que, en 2018, se accedió a millones de tokens de usuario debido a una API vulnerable. Esto demuestra que hasta los gigantes en la industria pueden sufrir de este tipo de vulnerabilidades y ocasionar muchisimo daño tanto a la empresa como a los usuarios.
