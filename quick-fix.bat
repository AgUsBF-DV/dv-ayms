@echo off
REM DVAYMS - Quick Fix Script para Windows
REM Fix rápido para problemas comunes del proyecto

echo.
echo ⚡ DVAYMS - Quick Fix (Windows)
echo ==============================

echo 🔍 Diagnosticando problemas comunes...
echo.

REM Check if venv exists
if not exist venv (
    echo ❌ Problema: Entorno virtual no existe
    echo 🔧 Solucionando: Creando entorno virtual...
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install --upgrade pip --quiet

    if exist requirements.txt (
        echo    📦 Instalando dependencias...
        pip install -r requirements.txt --quiet
    )
    echo    ✅ Entorno virtual creado
) else (
    echo ✅ Entorno virtual existe
    call venv\Scripts\activate.bat
)

REM Check Django
echo.
echo 🔍 Verificando Django...
python -c "import django" 2>nul
if %errorlevel% neq 0 (
    echo ❌ Problema: Django no está instalado
    echo 🔧 Solucionando: Instalando Django...
    pip install Django==5.2.6 --quiet
    echo    ✅ Django instalado
) else (
    echo ✅ Django disponible
)

REM Check psycopg issues
echo.
echo 🔍 Verificando psycopg...
python -c "import psycopg2" 2>nul
if %errorlevel% neq 0 (
    echo ❌ Problema: psycopg2 no disponible
    for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
    echo %PYTHON_VERSION% | findstr "3.14" >nul
    if %errorlevel% equ 0 (
        echo 🔧 Solucionando: Aplicando fix para Python 3.14...
        pip uninstall -y psycopg2-binary 2>nul
        pip install "psycopg[binary]==3.2.12" --quiet
        echo    ✅ Fix Python 3.14 aplicado
    ) else (
        echo 🔧 Solucionando: Instalando psycopg2...
        pip install psycopg2-binary --quiet
        echo    ✅ psycopg2 instalado
    )
) else (
    echo ✅ psycopg disponible
)

REM Check Node modules
echo.
echo 🔍 Verificando Node.js dependencies...
if exist yenny (
    cd yenny
    if not exist node_modules (
        echo ❌ Problema: node_modules no existe
        if exist package.json (
            echo 🔧 Solucionando: Instalando dependencias Node.js...
            call npm install --silent
            echo    ✅ Dependencias Node.js instaladas
        ) else (
            echo ⚠️  package.json no encontrado
        )
    ) else (
        echo ✅ node_modules existe
    )

    REM Check if CSS needs building
    if exist package.json (
        if not exist static\CACHE (
            echo 🔧 Compilando CSS...
            call npm run build-prod --silent 2>nul
            echo    ✅ CSS compilado
        )
    )
    cd ..
) else (
    echo ⚠️  Directorio yenny no encontrado
)

REM Check migrations
echo.
echo 🔍 Verificando migraciones...
if exist yenny (
    cd yenny
    python manage.py makemigrations --check --dry-run >nul 2>&1
    if %errorlevel% neq 0 (
        echo ❌ Problema: Migraciones pendientes
        echo 🔧 Solucionando: Aplicando migraciones...
        python manage.py makemigrations >nul 2>&1
        python manage.py migrate >nul 2>&1
        echo    ✅ Migraciones aplicadas
    ) else (
        echo ✅ Migraciones actualizadas
    )
    cd ..
)

echo.
echo 🎉 ¡Quick Fix completado!
echo =========================
echo.
echo 🚀 Ahora puedes ejecutar:
echo    dev.bat
echo.

pause
