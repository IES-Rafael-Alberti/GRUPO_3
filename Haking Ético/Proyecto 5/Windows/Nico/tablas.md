| Descripción de la vulnerabilidad | Ejecución remota de código a través del protocolo de transporte de Elasticsearch |
|---------------------------------|-----------------------------------------------------------------------------------|
| **CVE/CWE**                     | [CVE-2015-5377](https://nvd.nist.gov/vuln/detail/CVE-2015-5377) / [CWE-94](https://cwe.mitre.org/data/definitions/94.html) |
| **CVSS v3**                     | 9.8 |
| **Severidad**                   | Crítica |
| **Impacto**                     | Permite a un atacante remoto ejecutar código arbitrario en el servidor afectado mediante el protocolo de transporte de Elasticsearch sin autenticación previa. |
| **Sistemas afectados**          | Versiones de Elasticsearch anteriores a la 1.6.1. |
| **Prueba de concepto (POC)**    | ![alt text](image-5.png) ![alt text](image-8.png)
|
| **Remediación**                 | Actualizar Elasticsearch a la versión 1.6.1 o superior. Alternativamente, asegurar que solo aplicaciones de confianza tengan acceso al puerto del protocolo de transporte. |
| **Enlaces de referencia**       | [Elasticsearch ESA-2015-06 - Tenable](https://www.tenable.com/plugins/nessus/119499), [Exploit-DB: ElasticSearch - Remote Code Execution](https://www.exploit-db.com/exploits/36337) |


| Description of vulnerability | Vulnerabilidad de Path Traversal en Oracle GlassFish Server |
|------------------------------|----------------------------------------------------------------|
| **CVE/CWE**                  | [CVE-2017-1000028](https://nvd.nist.gov/vuln/detail/CVE-2017-1000028) / [CWE-22](https://cwe.mitre.org/data/definitions/22.html) |
| **CVSS v3**                  | 7.5 |
| **Severity**                 | Alta |
| **Impact**                   | Permite a un atacante remoto acceder a archivos arbitrarios en el sistema a través de una petición HTTP especialmente diseñada. No requiere autenticación. |
| **Affected systems**         | Servidor con Oracle GlassFish accesible en el puerto 4848 |
| **Proof Of Concept (POC)**   | Acceso a la ruta `https://windows:4848/theme/META-INF%c0%af.../users` permite visualizar el contenido de carpetas como `vagrant`, `Documents`, `AppData`, etc. ![alt text](image-37.png)![alt text](image-41.png)|
| **Remediation**              | Aplicar parches de seguridad proporcionados por Oracle. Restringir el acceso al puerto 4848 desde redes no autorizadas. Deshabilitar interfaces administrativas innecesarias. |
| **Reference links**          | [CVE-2017-1000028 - NVD](https://nvd.nist.gov/vuln/detail/CVE-2017-1000028), [EDB-39441 - Exploit DB](https://www.exploit-db.com/exploits/39441) |
