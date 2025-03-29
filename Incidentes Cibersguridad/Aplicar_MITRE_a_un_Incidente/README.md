## Descripción del incidente
En mayo de 2021, la empresa estadounidense Colonial Pipeline, sufrió una parálisis temporal debido a un ransomware, que cortó el suministro de combustible a gran parte de Estados Unidos.

El grupo de ciberdelincuentes *Darkside*, coló un ransomware en la infraestructura de la empresa debido a unas credenciales de VPN filtradas, con lo que consiguieron cifrar los sistemas internos para exigir un pago.

La empresa acabó pagando 4.4 millones de dólares en Bitocin, aunque pudieron recuperar parte de ella gracias al FBI.

## Análisis MITRE ATT&CK (Aplicación práctica)

| **Táctica**          | **Técnica usada**                                    |
| -------------------- | ---------------------------------------------------- |
| Initial Access       | T1078 – Valid Accounts (uso de credenciales robadas) |
| Execution            | T1059 – Command and Scripting Interpreter            |
| Persistence          | T1547 – Boot or Logon Autostart Execution            |
| Privilege Escalation | T1068 – Exploitation for Privilege Escalation        |
| Defense Evasion      | T1562 – Impair Defenses                              |
| Command and Control  | T1071 – Application Layer Protocol                   |
| Exfiltration         | T1041 – Exfiltration Over C2 Channel                 |
| Impact               | T1486 – Data Encrypted for Impact (ransomware)       |

### 1. Initial Access T1078 – Valid Accounts
[Entrada en el Mitre](https://attack.mitre.org/techniques/T1078/)

### 2. Execution T1059 – Command and Scripting Interpreter
[Entrada en el Mitre](https://attack.mitre.org/techniques/T1059/)

### 3. Persistence T1547 – Boot or Logon Autostart Execution
[Entrada en el Mitre](https://attack.mitre.org/techniques/T1547/)

### 4. Privilege Escalation	T1068 – Exploitation for Privilege Escalation
[Entrada en el Mitre](https://attack.mitre.org/techniques/T1068/)

### 5. Defense Evasion T1562 – Impair Defenses
[Entrada en el Mitre](https://attack.mitre.org/techniques/T1562/)

### 6. Command and Control T1071 – Application Layer Protocol
[Entrada en el Mitre](https://attack.mitre.org/techniques/T1071/)

### 7. Exfiltration	T1041 – Exfiltration Over C2 Channel
[Entrada en el Mitre](https://attack.mitre.org/techniques/T1041/)

### 8. Impact T1486 – Data Encrypted for Impact (ransomware)
[Entrada en el Mitre](https://attack.mitre.org/techniques/T1486/)

## Herramientas y vectores usados
Software/métodos empleados por los atacantes.

Cómo se relacionan con técnicas ATT&CK.

Opcional: mención del grupo APT si es conocido y su perfil en MITRE.

## Evaluación de defensa
¿Qué falló? ¿Qué podría haberlo prevenido o detectado?

Técnicas de mitigación y detección (según MITRE).

Controles que podrían haberse aplicado (EDR, segmentación, MFA, etc.).

## Lecciones aprendidas y correlación con ASVS u otros marcos (opcional)
Qué aporta MITRE a la respuesta ante incidentes.

Qué se debería implementar tras el incidente.

Breve reflexión final, con enfoque técnico.