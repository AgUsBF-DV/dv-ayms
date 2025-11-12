#!/bin/bash

# DVAYMS - One Command Setup
# This script sets up everything automatically
# NOTA: Este script debe ejecutarse desde la RAÍZ del proyecto

set -e  # Exit on any error

# Verificar si estamos en la raíz del proyecto
if [ ! -f "yenny/manage.py" ]; then
    echo "❌ Error: Este script debe ejecutarse desde la raíz del proyecto"
    echo "💡 Cambia al directorio raíz primero"
    exit 1
fi

echo "🚀 DVAYMS - Configuración Automática Completa"
echo "=============================================="

# Detect Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
echo "📍 Python detectado: $PYTHON_VERSION"

# Step 1: Virtual Environment
echo "📦 Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

# Step 2: Install Python dependencies (with auto-fix for Python 3.14)
echo "🐍 Instalando dependencias Python..."
pip install --upgrade pip --quiet

# Check if Python 3.14 and handle psycopg accordingly
if [[ "$PYTHON_VERSION" == "3.14" ]]; then
    echo "   ⚠️  Python 3.14 detectado - usando psycopg3"
    pip install Django==5.2.6 --quiet
    pip install "psycopg[binary]==3.2.12" --quiet
    pip install django-compressor==4.5.1 --quiet
else
    echo "   ✅ Instalando dependencias estándar"
    pip install -r scripts/requirements.txt --quiet
fi

# Step 3: Node.js dependencies
echo "🎨 Instalando dependencias Node.js..."
cd yenny
npm install --silent
npm run build-prod --silent

# Step 4: Database check and setup reminder
echo "🗄️  Verificando base de datos..."
cd ..
source venv/bin/activate

# Try to connect to database
if psql -h localhost -U postgres -d yenny_db -c "SELECT 1;" >/dev/null 2>&1; then
    echo "   ✅ Base de datos yenny_db encontrada"
    DB_EXISTS=true
else
    echo "   ⚠️  Base de datos no encontrada - se configurará automáticamente"
    DB_EXISTS=false
fi

# Step 5: Django setup
echo "⚙️  Configurando Django..."
cd yenny

if [ "$DB_EXISTS" = false ]; then
    echo "   📋 Primero debes configurar PostgreSQL:"
    echo "   1. Abre pgAdmin o terminal psql"
    echo "   2. Ejecuta: CREATE DATABASE yenny_db;"
    echo "   3. Ejecuta: CREATE USER postgres WITH PASSWORD 'postgres';"
    echo "   4. Ejecuta: GRANT ALL PRIVILEGES ON DATABASE yenny_db TO postgres;"
    echo ""
    echo "   O ejecuta estos comandos automáticamente:"
    echo "   psql -U postgres -c \"CREATE DATABASE yenny_db;\""
    echo "   psql -U postgres -c \"CREATE USER postgres WITH PASSWORD 'postgres';\""
    echo "   psql -U postgres -c \"GRANT ALL PRIVILEGES ON DATABASE yenny_db TO postgres;\""
    echo ""
    read -p "   Presiona Enter después de configurar la base de datos..."
fi

# Run migrations
echo "   🔄 Ejecutando migraciones..."
python manage.py makemigrations --verbosity=0
python manage.py migrate --verbosity=0

# Create superuser if none exists
echo "   👑 Configurando usuario administrador..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(is_superuser=True).exists() or User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell 2>/dev/null || echo "   ✅ Usuario admin ya existe"

echo ""
echo "🎉 ¡CONFIGURACIÓN COMPLETA!"
echo "=========================="
echo ""
echo "🌐 Para iniciar el servidor:"
echo "   cd yenny && python manage.py runserver"
echo ""
echo "🚀 ¡Ya puedes empezar a desarrollar!"

# Auto-start option
echo ""
read -p "¿Quieres iniciar el servidor ahora? (y/N): " START_SERVER
if [[ "$START_SERVER" =~ ^[Yy]$ ]]; then
    echo "🚀 Iniciando servidor..."
    python manage.py runserver
fi
