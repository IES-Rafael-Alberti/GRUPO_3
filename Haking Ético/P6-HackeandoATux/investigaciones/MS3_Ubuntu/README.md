# Investigación MS3_Ubuntu

**Pentesters**: Nicolás Ruiz Ruiz y Victor Jimenez Corada

## Índice

1. [Detección de vulnerabilidades](#1-detección-de-vulnerabilidades)
2. [Desarrollo de vulnerabilidades](#2-desarrollo-de-vulnerabilidades)

## 1. Detección de vulnerabilidades

Para la detección de vulnerabilidades hemos usado Nessus para escanear la maquina, realizando dos escaneos para asegurarnos de encontrar todas las vulnerabilidades posibles. Los resultados han sido los siguientes:

- Reporte 1, realizado por Nicolás Ruiz:

  - [Base de datos](./metasploit_jmvm55.nessus)
  - [Documento PDF](./metasploit_j2oghf.pdf)

- Reporte 2, realizado por Víctor Jiménez:

  - [Archivo Nessus](./ms3_ubuntu_s9n7be.nessus)
  - [Reporte PDF](./ms3_ubuntu_pg4nxa.pdf)

## 2. Desarrollo de vulnerabilidades

La investigación y comprobación de vulnerabilidades detectadas la hemos dividido de la siguiente forma:

- Grupo 1, Nicolas Ruiz

![vulnerabilidadesNicolas.png](img/vulnerabilidadesNicolas.png)

- Grupo 2, Víctor Jiménez

![vulnerabilidadesVictor.png](img/vulnerabilidadesVictor.png)

### Explotación de vulnerabilidades

#### Críticas

- Canonical Ubuntu Linux SEoL (14.04.x)
- Drupal Coder Module Deserialization RCE
- ProFTPD mod_copy Information Disclosure

| Campo      | Valor     |
|------------|-----------|
| Severity   | Critical  |
| ID         | 84215     |
| Version    | 1.11      |
| Type       | remote    |
| Family     | FTP       |
| CVSS score | 9.8       |
| CVE        | 2015-3306 |

Esta vulnerabilidad permite a los atacantes usar el módulo **mod_copy** quee permite ejecutar comandos para copiar y pegar en el servidor FTP (**SITE CPFR** y **SITE CPTO**) sin la necesidad de estar autenticados:

![alt text](./img/ProFTPD1.png)

![alt text](./img/ProFTPD2.png)

#### Altas

- Drupal Database Abstraction API SQLi
- SSL Medium Strength Cipher Suites Supported (SWEET32)

| Campo      | Valor     |
|------------|-----------|
| Severity   | High      |
| ID         | 42873     |
| Version    | 1.22      |
| Type       | remote    |
| Family     | General   |
| CVSS score | 7.5       |
| CVE        | 2016-2183 |

![alt text](./img/SSL_Strength.png)

La vulnerabilidad indica que el host usa  encriptación media (entre 64 y 112 bits o encriptación 3DES).

#### Medias

- IP Forwarding Enabled
- SSL Certificate Cannot Be Trusted
- SSL Self-Signed Certificate
- TLS Version 1.0 Protocol Detection
- TLS Version 1.1 Deprecated Protocol
- SSH Terrapin Prefix Truncation Weakness (CVE-2023-48795)

| Campo      | Valor      |
|------------|------------|
| Severity   | Medium     |
| ID         | 187315     |
| Version    | 1.4        |
| Type       | remote     |
| Family     | Misc.      |
| CVSS score | 5.9        |
| CVE        | 2023-48795 |

La entrada indica que el servidor es vulnerable a Man-in-the-Middle para manipular los paquetes iniciales de la negociación, sin que el cliente ni el servidor lo noten.

- Apache Multiviews Arbitrary Directory Listing

| Campo      | Valor      |
|------------|------------|
| Severity   | Medium     |
| ID         | 10704      |
| Version    | 1.38       |
| Type       | remote     |
| Family     | Web Server |
| CVSS score | 5.3        |
| CVE        | 2001-0731  |

**Multiviews** es un módulo de apache que intenta mostrar archivos basandose en coincidencias. Por ejemplo /index. -> /index.html

![alt text](./img/Apache_Multiviews1.png)

Esto indica que el servicio es vulnerable y podríamos hacer un dirbuster para listar todo el contenido de este:

![alt text](./img/Apache_Multiviews2
.png)

- SMB Signing not required

| Campo      | Valor      |
|------------|------------|
| Severity   | Medium     |
| ID         | 57608      |
| Version    | 1.20       |
| Type       | remote     |
| Family     | Misc.      |
| CVSS score | 5.3        |
| CVE        | N/A        |

Esta vulnerabilidad indica que el servidor SMB no exige el uso de firmas digitales en las comunicaciones. Esto permite que un atacante no autenticado intercepte y manipule el tráfico entre clientes y el servidor, facilitando ataques de tipo MitM.

- SSH Weak Algorithms Supported

| Campo      | Valor      |
|------------|------------|
| Severity   | Medium     |
| ID         | 90317      |
| Version    | Rev. 1.3   |
| Type       | remote     |
| Family     | Misc.      |
| CVSS score | 4.3        |
| CVE        | N/A        |

Indica que el servidor SSH está configurado para utilizar algoritmos de cifrado débiles, específicamente el cifrado de flujo Arcfour.

#### Bajas

- SSH Server CBC Mode Ciphers Enabled
- SSH Weak Key Exchange Algorithms Enabled
- SSH Weak MAC Algorithms Enabled

| Campo      | Valor      |
|------------|------------|
| Severity   | Low        |
| ID         | 71049      |
| Version    | Rev. 1.4   |
| Type       | remote     |
| Family     | Misc.      |
| CVSS score | 2.6        |
| CVE        | N/A        |

​La vulnerabilidad indica que el servidor SSH está configurado para permitir algoritmos débiles, específicamente MD5 y algoritmos de 96 bits.

- ICMP Timestamp Request Remote Date Disclosure

| Campo      | Valor      |
|------------|------------|
| Severity   | Low        |
| ID         | 10114      |
| Version    | 1.56       |
| Type       | remote     |
| Family     | General    |
| CVSS score | 2.9        |
| CVE        | 1999-0524  |

Esta vulnerabilidad indica que el host responde a solicitudes ICMP de marca de tiempo, permitiendo a los atacantes conocer la hora local del sistema.

![alt text](./img/ICMP_timesting.png)

---

Hecho por Nicolas Ruiz y Víctor Jiménez
