@echo off
set SCRIPT_DIR=C:\Users\aleca\Desktop\ia-pps
set VENV_DIR=%SCRIPT_DIR%.venv
set ACTIVATE=%VENV_DIR%\Scripts\activate.bat
set APP_SCRIPT=%SCRIPT_DIR%\main.py
set REQUIREMENTS_FILE=%SCRIPT_DIR%\requirements.txt

REM Crear entorno virtual si no existe
if not exist "%VENV_DIR%" (
    echo Creando entorno virtual en %VENV_DIR%...
    python -m venv "%VENV_DIR%"
) else (
    echo El entorno virtual ya existe en %VENV_DIR%.
)

REM Activar entorno virtual
call "%ACTIVATE%"

REM Instalar dependencias
if exist "%REQUIREMENTS_FILE%" (
    echo Instalando dependencias desde %REQUIREMENTS_FILE%...
    pip install -r "%REQUIREMENTS_FILE%"
) else (
    echo Error: No se encontró el archivo requirements.txt en %SCRIPT_DIR%.
    exit /b 1
)

REM Ejecutar script
if exist "%APP_SCRIPT%" (
    echo Ejecutando análisis...
    python "%APP_SCRIPT%"
) else (
    echo Error: No se encontró el script Python en %APP_SCRIPT%.
)
