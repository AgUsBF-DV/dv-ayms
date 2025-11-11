@echo off
REM DVAYMS - Setup Script para Windows
REM Este script configura el proyecto automáticamente

echo.
echo 🚀 DVAYMS - Configuración Inicial (Windows)
echo ==========================================

REM Detectar versión de Python
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo 📍 Python detectado: %PYTHON_VERSION%

REM Step 1: Virtual Environment
echo 📦 Creando entorno virtual...
if exist venv rmdir /s /q venv
python -m venv venv
call venv\Scripts\activate.bat

REM Step 2: Install Python dependencies
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
    python -m pip install -r requirements.txt --quiet
)

REM Step 3: Node.js dependencies
echo 🎨 Instalando dependencias Node.js...
cd yenny
call npm install --silent

echo.
echo ✅ ¡Configuración completada!
echo.
echo 🌐 Para continuar:
echo    1. Configura PostgreSQL (ver SETUP.md)
echo    2. Ejecuta: dev.bat
echo.

pause
