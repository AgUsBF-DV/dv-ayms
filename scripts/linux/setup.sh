#!/bin/bash

# DVAYMS Project Setup Script
# NOTA: Este script debe ejecutarse desde la RAÍZ del proyecto

# Verificar si estamos en la raíz del proyecto
if [ ! -f "yenny/manage.py" ]; then
    echo "❌ Error: Este script debe ejecutarse desde la raíz del proyecto"
    echo "💡 Cambia al directorio raíz primero"
    exit 1
fi

echo "=== Configuración del Proyecto DVAYMS ==="

# Step 1: Create virtual environment
echo "Paso 1: Creando entorno virtual de Python..."
python3 -m venv venv
echo "✓ Entorno virtual creado"

# Step 2: Activate virtual environment and install dependencies
echo "Paso 2: Instalando dependencias de Python..."
source venv/bin/activate
pip install --upgrade pip
pip install -r scripts/requirements.txt
echo "✓ Dependencias de Python instaladas"

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
echo "Paso 5: Configuración de Base de Datos"
echo "Por favor asegúrate de que PostgreSQL esté instalado y ejecutándose, luego:"
echo "1. Abre pgAdmin o psql"
echo "2. Ejecuta los comandos SQL en docs/db/install.sql"
echo "   (Crea la base de datos 'yenny_db' y el usuario 'postgres')"
echo "3. Regresa y continúa con las migraciones de Django"

read -p "Presiona Enter después de configurar la base de datos..."

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

echo "Creando superusuario..."
echo "Por favor crea un usuario administrador:"
python manage.py createsuperuser

echo ""
echo "=== ¡Configuración Completa! ==="
echo ""
echo "Para iniciar el servidor de desarrollo:"
echo "1. Activa el entorno virtual: source venv/bin/activate"
echo "2. Navega al directorio yenny: cd yenny"
echo "3. Ejecuta el servidor: python manage.py runserver"
echo ""
echo "Para desarrollo con auto-reconstrucción de CSS:"
echo "1. En una terminal: cd yenny && npm run build"
echo "2. En otra terminal: python manage.py runserver"
echo ""
echo "O simplemente ejecuta: bash scripts/linux/dev.sh"
echo ""
echo "La aplicación estará disponible en http://127.0.0.1:8000/"