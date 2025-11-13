@echo off
REM DVAYMS - Development Script para Windows
REM Script de desarrollo rápido para Windows
REM NOTA: Este script debe ejecutarse desde la RAÍZ del proyecto

REM Verificar si estamos en la raíz del proyecto
if not exist "yenny\manage.py" (
    echo ❌ Error: Este script debe ejecutarse desde la raíz del proyecto
    echo 💡 Ejecuta: cd /d "%~dp0..\.." ^&^& scripts\windows\dev.bat
    pause
    exit /b 1
)

REM Activar entorno virtual
if not exist "venv\Scripts\activate.bat" (
    echo ❌ Error: No se encontró el entorno virtual
    echo 💡 Ejecuta primero: scripts\windows\run.bat o scripts\windows\setup.bat
    pause
    exit /b 1
)

call venv\Scripts\activate.bat

echo.
echo 🚀 DVAYMS - Modo Desarrollo (Windows)
echo ===================================
echo 📦 Entorno virtual: ACTIVO
echo.

cd yenny

REM Quick migration check
echo 🔄 Verificando migraciones...
python manage.py makemigrations --check --dry-run >nul 2>&1
if %errorlevel% neq 0 (
    echo    ⚠️  Hay migraciones pendientes
    python manage.py makemigrations
    python manage.py migrate
) else (
    echo    ✅ Base de datos actualizada
)

REM Build frontend if needed
echo 🎨 Verificando frontend...
if not exist "static\CACHE" (
    echo    🔄 Compilando frontend...
    call npm run build-prod --silent
) else (
    echo    ✅ Frontend compilado
)

echo.
echo 🌐 Iniciando servidor de desarrollo...
echo 📱 URL: http://127.0.0.1:8000/
echo.
echo 💡 Presiona Ctrl+C para detener el servidor
echo.

python manage.py runserver
