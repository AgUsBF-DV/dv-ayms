@echo off
REM DVAYMS - Status Check Script para Windows
REM Verifica el estado completo del proyecto

echo.
echo 🔍 DVAYMS - Verificación de Estado (Windows)
echo =============================================

REM Check Python
echo 📍 Verificando Python...
python --version 2>nul
if %errorlevel% neq 0 (
    echo    ❌ Python no está instalado o no está en PATH
) else (
    echo    ✅ Python instalado
)

REM Check Node.js
echo.
echo 📍 Verificando Node.js...
node --version 2>nul
if %errorlevel% neq 0 (
    echo    ❌ Node.js no está instalado o no está en PATH
) else (
    echo    ✅ Node.js instalado
    npm --version 2>nul
    if %errorlevel% equ 0 (
        echo    ✅ npm disponible
    )
)

REM Check PostgreSQL
echo.
echo 📍 Verificando PostgreSQL...
psql --version 2>nul
if %errorlevel% neq 0 (
    echo    ⚠️  psql no está en PATH (pero PostgreSQL puede estar instalado)
) else (
    echo    ✅ PostgreSQL CLI disponible
)

REM Check Virtual Environment
echo.
echo 📍 Verificando entorno virtual...
if exist venv (
    echo    ✅ Directorio venv existe
    if exist venv\Scripts\activate.bat (
        echo    ✅ Script de activación existe
    ) else (
        echo    ❌ Script de activación no encontrado
    )
) else (
    echo    ❌ Entorno virtual no encontrado
    echo    💡 Ejecuta: setup.bat
)

REM Check Django project
echo.
echo 📍 Verificando proyecto Django...
if exist yenny (
    echo    ✅ Directorio yenny existe
    if exist yenny\manage.py (
        echo    ✅ manage.py encontrado
    ) else (
        echo    ❌ manage.py no encontrado
    )

    if exist yenny\package.json (
        echo    ✅ package.json encontrado
    ) else (
        echo    ❌ package.json no encontrado
    )
) else (
    echo    ❌ Directorio del proyecto Django no encontrado
)

REM Check requirements.txt
echo.
echo 📍 Verificando archivos de configuración...
if exist requirements.txt (
    echo    ✅ requirements.txt existe
) else (
    echo    ❌ requirements.txt no encontrado
)

REM Test database connection (if venv exists)
echo.
echo 📍 Verificando conexión a base de datos...
if exist venv (
    call venv\Scripts\activate.bat
    cd yenny 2>nul
    python -c "import django; django.setup()" 2>nul
    if %errorlevel% equ 0 (
        echo    ✅ Django se puede importar
        python manage.py check --deploy 2>nul
        if %errorlevel% equ 0 (
            echo    ✅ Configuración Django válida
        ) else (
            echo    ⚠️  Hay warnings en la configuración Django
        )
    ) else (
        echo    ❌ Error al importar Django
    )
    cd ..
) else (
    echo    ⚠️  No se puede verificar sin entorno virtual
)

echo.
echo 📊 Resumen:
echo =========
if exist venv (
    if exist yenny\manage.py (
        echo ✅ Proyecto configurado correctamente
        echo 💡 Ejecuta: dev.bat
    ) else (
        echo ⚠️  Proyecto parcialmente configurado
        echo 💡 Ejecuta: run.bat
    )
) else (
    echo ❌ Proyecto no configurado
    echo 💡 Ejecuta: setup.bat o run.bat
)

echo.
pause
