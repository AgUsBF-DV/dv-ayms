@echo off
REM DVAYMS - One Command Setup para Windows
REM Este script configura todo automáticamente en Windows
REM NOTA: Este script debe ejecutarse desde la RAÍZ del proyecto

REM Verificar si estamos en la raíz del proyecto
if not exist "yenny\manage.py" (
    echo ❌ Error: Este script debe ejecutarse desde la raíz del proyecto
    echo 💡 Cambia al directorio raíz primero: cd /d "%~dp0..\.."
    pause
    exit /b 1
)

echo.
echo 🚀 DVAYMS - Configuración Automática Completa (Windows)
echo ==================================================

REM Detectar versión de Python
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo 📍 Python detectado: %PYTHON_VERSION%

REM Step 1: Virtual Environment
echo 📦 Creando entorno virtual...
python -m venv venv
call venv\Scripts\activate.bat

REM Step 2: Install Python dependencies (with auto-fix for Python 3.14)
echo 🐍 Instalando dependencias Python...
python -m pip install --upgrade pip --quiet

REM Check if Python 3.14 and handle psycopg accordingly
echo %PYTHON_VERSION% | findstr "3.14" >nul
if %errorlevel% equ 0 (
    echo    ⚠️  Python 3.14 detectado - usando psycopg3
    python -m pip install Django==5.2.6 --quiet
    python -m pip install "psycopg[binary]==3.2.12" --quiet
    python -m pip install django-compressor==4.5.1 --quiet
) else (
    echo    ✅ Instalando dependencias estándar
    python -m pip install -r scripts\requirements.txt --quiet
)

REM Step 3: Node.js dependencies
echo 🎨 Instalando dependencias Node.js...
cd yenny
call npm install --silent
call npm run build-prod --silent

REM Step 4: Database check and setup reminder
echo 🗄️  Verificando base de datos...
cd ..
call venv\Scripts\activate.bat

REM Try to connect to database (Windows psql check)
psql -h localhost -U postgres -d yenny_db -c "SELECT 1;" >nul 2>&1
if %errorlevel% neq 0 (
    echo    ⚠️  Base de datos no encontrada - se configurará automáticamente
    set DB_EXISTS=false
) else (
    echo    ✅ Base de datos yenny_db encontrada
    set DB_EXISTS=true
)

REM Step 5: Django setup
echo ⚙️  Configurando Django...
cd yenny

if "%DB_EXISTS%"=="false" (
    echo    📋 Primero debes configurar PostgreSQL:
    echo    1. Abre pgAdmin o terminal psql
    echo    2. Ejecuta: CREATE DATABASE yenny_db;
    echo    3. Ejecuta: CREATE USER postgres WITH PASSWORD 'postgres';
    echo    4. Ejecuta: GRANT ALL PRIVILEGES ON DATABASE yenny_db TO postgres;
    echo.
    echo    O ejecuta estos comandos automáticamente:
    echo    psql -U postgres -c "CREATE DATABASE yenny_db;"
    echo    psql -U postgres -c "CREATE USER postgres WITH PASSWORD 'postgres';"
    echo    psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE yenny_db TO postgres;"
    echo.
    pause
)

REM Run migrations
echo    🔄 Ejecutando migraciones...
python manage.py makemigrations >nul 2>&1
python manage.py migrate >nul 2>&1

REM Create superuser if none exists
echo    👑 Configurando usuario administrador...
echo from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(is_superuser=True).exists() or User.objects.create_superuser('admin', 'admin@admin.com', 'admin') | python manage.py shell >nul 2>&1

echo.
echo 🎉 ¡CONFIGURACIÓN COMPLETA!
echo ==========================
echo.
echo 🌐 Para iniciar el servidor:
echo    cd yenny ^&^& python manage.py runserver
echo.
echo 📱 URLs importantes:
echo    • Aplicación: http://127.0.0.1:8000/
echo.
echo 🚀 ¡Ya puedes empezar a desarrollar!

REM Auto-start option
echo.
set /p START_SERVER="¿Quieres iniciar el servidor ahora? (y/N): "
if /i "%START_SERVER%"=="y" (
    echo 🚀 Iniciando servidor...
    python manage.py runserver
)

pause
