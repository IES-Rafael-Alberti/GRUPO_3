#!/bin/bash

SCRIPT_DIR="/home/alejandro/Escritorio/ia"
VENV_DIR="$SCRIPT_DIR/.venv"
APP_SCRIPT="$SCRIPT_DIR/main.py"

# Crear entorno virtual si no existe
if [ ! -d "$VENV_DIR" ]; then
    echo "Creando entorno virtual en $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "El entorno virtual ya existe en $VENV_DIR."
fi

# Activar entorno virtual
source "$VENV_DIR/bin/activate"

# Instalar requirements.txt
REQUIREMENTS_FILE="$SCRIPT_DIR/requirements.txt"
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Instalando dependencias desde $REQUIREMENTS_FILE..."
    pip install -r "$REQUIREMENTS_FILE"
else
    echo "Error: No se encontró el archivo requirements.txt en $SCRIPT_DIR."
    deactivate
    exit 1
fi

# Ejecutar script
if [ -f "$APP_SCRIPT" ]; then
    echo "Ejecutando análisis"
    python3 "$APP_SCRIPT"
else
    echo "Error: No se encontró el script Python en $APP_SCRIPT."
fi

# Desactivar env
deactivate