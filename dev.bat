@echo off
REM DVAYMS - Development Script para Windows
REM Script de desarrollo rápido para Windows

call venv\Scripts\activate.bat

echo.
echo 🚀 DVAYMS - Modo Desarrollo (Windows)
echo ===================================

REM Check if virtual environment is active
if "%VIRTUAL_ENV%"=="" (
    echo ❌ Error: Entorno virtual no está activo
    echo 💡 Ejecuta primero: run.bat
    pause
    exit /b 1
)

echo 📦 Entorno virtual: ACTIVO
echo 🐍 Python: %PYTHON_VERSION%

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
echo 🔑 Admin: http://127.0.0.1:8000/admin/ (admin/admin)
echo.
echo 💡 Presiona Ctrl+C para detener el servidor
echo.

python manage.py runserver
