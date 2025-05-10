# Justicio - Grupo 3

## Instalación y configuración

### 1. Configura las variables de entorno

Crea un archivo con el nombre de `.env`, con las siguientes variables

```.env
# HELICONE_API_KEY=tuAPIKEY
HELICONE_API_KEY=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
OPENROUTER_API_KEY=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
OPENROUTER_BASE_URL=https://openrouter.helicone.ai/api/v1
TAVILY_API_KEY=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
```

### 2. Ejecución del script

#### Para windows

El script `windows/start.bat` automatiza todo el proceso:

1. Crea el entorno virtual (si no existe).
2. Instala dependencias.
3. Ejecuta el script Python con la URL indicada.

**Ejecuta así:**

```bash
start.bat
```

Asegúrate de que `start.bat` tenga configurada la ruta correcta del proyecto:

```bash
set SCRIPT_DIR=C:\Users\juan\Desktop\ia
```

#### Para linux

El script `linux/start.sh` automatiza todo el proceso:

1. Crea el entorno virtual (si no existe).
2. Instala dependencias.
3. Ejecuta el script Python con la URL indicada.

**Ejecuta así:**

```bash
bash start.sh
```

Asegúrate de que `start.sh` tenga configurada la ruta correcta del proyecto:

```bash
SCRIPT_DIR="/home/alejandro/Escritorio/ia"
```

## Contexto normativo proporcionado a la IA

Para que nuestra ia pueda generar respuestas rápidas y concisas sobre normativas de ciberseguridad, se le ha proporcionado contexto a partir de cinco fuentes clave. Estas incluyen el **reglamento general de protección de datos (rgpd)** desde el portal oficial de eur-lex, una guía práctica sobre la aplicación de la **ley de servicios de la sociedad de la información (lssi)**, un artículo que resume las principales **normativas de ciberseguridad que deben cumplir las empresas**, un análisis sobre las **normas iso aplicables a la seguridad informática**, y finalmente el listado actualizado de los **top 10 riesgos de seguridad web según owasp**. Este contenido ha sido procesado para que la ia pueda consultarlo y extraer información precisa cuando se le hagan preguntas relacionadas.

```python
url = "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32016R0679&from=ES"       # REGLAMENTO (UE) 2016/679 DEL PARLAMENTO EUROPEO Y DEL CONSEJO
url1 = "https://lssi.digital.gob.es/la-ley/aspectos-basicos/como-se-aplica-la-lssi"             # ¿Cómo se aplica la Ley de Servicios de la Sociedad de la Información?
url2 = "https://www.esedsl.com/blog/que-normativas-de-ciberseguridad-debe-cumplir-tu-empresa"   # Qué normativas de ciberseguridad debe cumplir tu empresa
url3 = "https://www.globalsuitesolutions.com/es/normas-iso-para-mejorar-la-ciberseguridad/"     # Estándares y normas ISO para mejorar la ciberseguridad
url4 = "https://owasp.org/www-project-top-ten/"                                                 # OWASP Top 10
```