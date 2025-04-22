# Script MISP

Este script analiza automáticamente una URL con la API de VirusTotal y crear un evento en MISP

## Instalación y configuración

### 1. Configura las variables de entorno

Copia y modifica el archivo template.env y dejalo con el nombre de .env

```bash
cp template.env .env
```

Edita el archivo `.env`:

```env
MISP_URL=https://localhost
MISP_KEY=tu_clave_api_de_misp
MISP_VERIFYCERT=False
VT_API_KEY=tu_clave_api_de_virustotal
```

> Si usas un certificado autofirmado, deja `MISP_VERIFYCERT=False`.

## Uso

El script `start.sh` automatiza todo el proceso:

1. Crea el entorno virtual (si no existe).
2. Instala dependencias.
3. Ejecuta el script Python con la URL indicada.

### Ejecuta así:

```bash
bash start.sh https://ejemplo.com
```

Asegúrate de que `start.sh` tenga configurada la ruta correcta del proyecto:

```bash
SCRIPT_DIR="/home/alejandro/Escritorio/misp"
```

## Ejemplo de salida

```
Ejecutando análisis para: https://ejemplo.com
🔍 Analizando la URL con VirusTotal: https://ejemplo.com
✅ Evento creado con ID: 12
⚠️ VirusTotal detecta 2 motores que marcaron esta URL como maliciosa.

📋 Lista de eventos en MISP:
🆔 ID: 12 | 📅 Fecha: 2025-04-22 | 📝 Info: URL Analysis: https://ejemplo.com | 🔢 Atributos: 1
...
```

## Requisitos

- Python3
- Cuenta en [VirusTotal](https://www.virustotal.com/) con clave API
- Instancia de [MISP](https://www.misp-project.org/) accesible