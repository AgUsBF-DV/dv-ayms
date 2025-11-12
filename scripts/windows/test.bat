@echo off
REM DVAYMS - Test Runner para Windows
REM Este script ejecuta tests desde cualquier ubicación

REM Obtener el directorio del script actual y navegar a la raíz del proyecto
set SCRIPT_DIR=%~dp0
set PROJECT_ROOT=%SCRIPT_DIR%..\..

echo 📍 Navegando al directorio raíz del proyecto...
cd /d "%PROJECT_ROOT%"

REM Verificar si estamos en la raíz del proyecto
if not exist "yenny\manage.py" (
    echo ❌ Error: No se puede encontrar el directorio raíz del proyecto
    echo 💡 Verifica que la estructura del proyecto esté correcta
    echo 📂 Buscando desde: %CD%
    pause
    exit /b 1
)

echo ✅ Directorio raíz encontrado: %CD%
echo.

REM Activar entorno virtual
echo 🐍 Activando entorno virtual...
if not exist "venv\Scripts\activate.bat" (
    echo ❌ Error: Entorno virtual no encontrado
    echo 💡 Ejecuta primero: .\scripts\windows\run.bat
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
echo ✅ Entorno virtual activado
echo.

REM Navegar al directorio de Django
cd yenny

echo 🧪 Ejecutando Tests
echo ==================

REM Si se pasa un parámetro, ejecutar ese test específico
if "%1"=="" (
    echo 📋 Ejecutando todos los tests...
    python manage.py test -v 2
) else (
    echo 📋 Ejecutando: %1
    python manage.py test %1 -v 2
)

echo.
echo ✅ Tests completados
echo.

REM Volver al directorio original
cd ..

pause
