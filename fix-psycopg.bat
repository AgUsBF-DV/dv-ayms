@echo off
REM DVAYMS - Fix psycopg para Python 3.14 en Windows
REM Soluciona problemas de compatibilidad con psycopg2-binary en Python 3.14

echo.
echo 🔧 DVAYMS - Fix psycopg para Python 3.14 (Windows)
echo ==================================================

REM Check if virtual environment exists
if not exist venv (
    echo ❌ Error: No se encontró el entorno virtual
    echo 💡 Ejecuta primero: setup.bat
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo 📍 Python version: %PYTHON_VERSION%

echo %PYTHON_VERSION% | findstr "3.14" >nul
if %errorlevel% neq 0 (
    echo ⚠️  Este fix es específico para Python 3.14
    echo    Tu versión: %PYTHON_VERSION%
    echo    ¿Continuar de todos modos? (s/N)
    set /p CONTINUE=
    if /i not "%CONTINUE%"=="s" (
        echo Cancelado
        pause
        exit /b 0
    )
)

echo.
echo 🔄 Aplicando fix para psycopg...

REM Remove problematic psycopg2-binary
echo    📦 Desinstalando psycopg2-binary...
python -m pip uninstall -y psycopg2-binary 2>nul

REM Install compatible psycopg3
echo    📦 Instalando psycopg3 compatible...
python -m pip install "psycopg[binary]==3.2.12" --quiet

if %errorlevel% equ 0 (
    echo.
    echo ✅ ¡Fix aplicado exitosamente!
    echo 📋 Cambios realizados:
    echo    • psycopg2-binary → psycopg[binary]==3.2.12
    echo.
    echo 🧪 Verificando instalación...
    python -c "import psycopg; print('✅ psycopg importado correctamente')" 2>nul
    if %errorlevel% equ 0 (
        echo    ✅ Verificación exitosa
        echo.
        echo 🚀 Ahora puedes ejecutar:
        echo    dev.bat
    ) else (
        echo    ❌ Error en la verificación
        echo    💡 Puede que necesites reinstalar las dependencias
    )
) else (
    echo.
    echo ❌ Error al aplicar el fix
    echo 💡 Intenta ejecutar: setup.bat
)

echo.
pause
