#!/bin/bash

# DVAYMS Project Setup Script (Python 3.14 Compatible)
# NOTA: Este script debe ejecutarse desde la RAÍZ del proyecto

# Verificar si estamos en la raíz del proyecto
if [ ! -f "yenny/manage.py" ]; then
    echo "❌ Error: Este script debe ejecutarse desde la raíz del proyecto"
    echo "💡 Cambia al directorio raíz primero"
    exit 1
fi

echo "=== Configuración del Proyecto DVAYMS (Compatible con Python 3.14) ==="

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Versión de Python detectada: $PYTHON_VERSION"

# Step 1: Create virtual environment
echo "Paso 1: Creando entorno virtual de Python..."
python3 -m venv venv
echo "✓ Entorno virtual creado"

# Step 2: Activate virtual environment and install dependencies
echo "Paso 2: Instalando dependencias de Python (con compatibilidad Python 3.14)..."
source venv/bin/activate

# Upgrade pip first
pip install --upgrade pip

# Install dependencies one by one to handle any issues
echo "Instalando Django..."
pip install Django==5.2.6

echo "Instalando adaptador de PostgreSQL (psycopg3 para compatibilidad con Python 3.14)..."
pip install "psycopg[binary]==3.2.12"

echo "Instalando django-compressor..."
pip install django-compressor==4.5.1

echo "✓ Dependencias de Python instaladas exitosamente"

# Step 3: Install Node.js dependencies for Tailwind CSS
echo "Paso 3: Instalando dependencias de Node.js..."
cd yenny
npm install
echo "✓ Dependencias de Node.js instaladas"

# Step 4: Build Tailwind CSS
echo "Paso 4: Compilando Tailwind CSS..."
npm run build-prod
echo "✓ Recursos frontend compilados"

# Step 5: Database setup instructions
echo ""
echo "Paso 5: Configuración de Base de Datos"
echo "================================================"
echo "Antes de continuar, por favor configura PostgreSQL:"
echo "1. Asegúrate de que PostgreSQL esté instalado y ejecutándose"
echo "2. Abre pgAdmin o usa la línea de comandos psql"
echo "3. Ejecuta estos comandos:"
echo ""
echo "   CREATE DATABASE yenny_db;"
echo "   CREATE USER postgres WITH PASSWORD 'postgres';"
echo "   ALTER ROLE postgres SET client_encoding TO 'utf8';"
echo "   ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';"
echo "   ALTER ROLE postgres SET timezone TO 'UTC';"
echo "   GRANT ALL PRIVILEGES ON DATABASE yenny_db TO postgres;"
echo ""
echo "O ejecuta el archivo SQL: docs/db/install.sql"
echo "================================================"
echo ""

read -p "Presiona Enter después de configurar la base de datos para continuar..."

# Step 6: Django setup
echo "Paso 6: Configuración de Django..."
cd ..
source venv/bin/activate
cd yenny

echo "Ejecutando migraciones de Django..."
python manage.py makemigrations autores
python manage.py makemigrations categorias
python manage.py makemigrations clientes
python manage.py makemigrations editoriales
python manage.py makemigrations empleados
python manage.py makemigrations libros
python manage.py makemigrations ventas
python manage.py migrate

echo ""
echo "Creando superusuario de Django..."
echo "Por favor crea un usuario administrador para el sistema:"
python manage.py createsuperuser

echo ""
echo "=== ¡Configuración Completa! ==="
echo ""
echo "🎉 ¡Tu proyecto DVAYMS está listo!"
echo ""
echo "Para iniciar el desarrollo:"
echo "1. Activa el entorno virtual: source venv/bin/activate"
echo "2. Navega al directorio yenny: cd yenny"
echo "3. Ejecuta el servidor: python manage.py runserver"
echo ""
echo "Para desarrollo con auto-reconstrucción de CSS:"
echo "1. Terminal 1: cd yenny && npm run build (modo watch)"
echo "2. Terminal 2: cd yenny && python manage.py runserver"
echo ""
echo "🌐 Aplicación: http://127.0.0.1:8000/"
echo ""
echo "📖 ¿Necesitas ayuda? Consulta la documentacion en la Wiki del repositorio"