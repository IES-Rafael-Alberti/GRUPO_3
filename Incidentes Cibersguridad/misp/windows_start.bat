@echo off
set SCRIPT_DIR=C:\Users\aleca\Desktop\GRUPO_3\Incidentes Cibersguridad\misp
set APP_SCRIPT=%SCRIPT_DIR%\main.py
set REQUIREMENTS_FILE=%SCRIPT_DIR%\requirements.txt

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
