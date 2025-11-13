#!/bin/bash

# Project Status Checker
# NOTA: Este script debe ejecutarse desde la RAÍZ del proyecto

# Verificar si estamos en la raíz del proyecto
if [ ! -f "yenny/manage.py" ]; then
    echo "❌ Error: Este script debe ejecutarse desde la raíz del proyecto"
    echo "💡 Cambia al directorio raíz primero"
    exit 1
fi

echo "=== Verificación de Estado del Proyecto DVAYMS ==="
echo ""

# Check Python
echo "🐍 Estado de Python:"
if command -v python3 &> /dev/null; then
    echo "✓ Python3 está instalado: $(python3 --version)"
else
    echo "✗ Python3 no está instalado"
fi

# Check virtual environment
echo ""
echo "📦 Entorno Virtual:"
if [ -d "venv" ]; then
    echo "✓ El entorno virtual existe"
    if [ -f "venv/bin/activate" ]; then
        echo "✓ El entorno virtual está configurado correctamente"
    else
        echo "✗ El entorno virtual parece estar corrupto"
    fi
else
    echo "✗ Entorno virtual no encontrado"
fi

# Check Python dependencies
echo ""
echo "📚 Dependencias de Python:"
if [ -f "scripts/requirements.txt" ]; then
    echo "✓ scripts/requirements.txt existe"
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
        if pip list | grep -q "Django"; then
            echo "✓ Django está instalado: $(python -c "import django; print(django.VERSION)")"
        else
            echo "✗ Django no está instalado"
        fi
        if pip list | grep -q "psycopg"; then
            echo "✓ El adaptador de PostgreSQL está instalado"
        else
            echo "✗ El adaptador de PostgreSQL no está instalado"
        fi
        deactivate
    else
        echo "⚠ No se puede verificar - entorno virtual no activado"
    fi
else
    echo "✗ scripts/requirements.txt no encontrado"
fi

# Check Node.js
echo ""
echo "🟢 Estado de Node.js:"
if command -v node &> /dev/null; then
    echo "✓ Node.js está instalado: $(node --version)"
else
    echo "✗ Node.js no está instalado"
fi

if command -v npm &> /dev/null; then
    echo "✓ npm está instalado: $(npm --version)"
else
    echo "✗ npm no está instalado"
fi

# Check Node dependencies
echo ""
echo "🎨 Dependencias de Frontend:"
if [ -d "yenny/node_modules" ]; then
    echo "✓ Los módulos de Node están instalados"
    if [ -f "yenny/package.json" ]; then
        cd yenny
        if npm list tailwindcss &> /dev/null; then
            echo "✓ Tailwind CSS está instalado"
        else
            echo "✗ Tailwind CSS no está instalado"
        fi
        if npm list flowbite &> /dev/null; then
            echo "✓ Flowbite está instalado"
        else
            echo "✗ Flowbite no está instalado"
        fi
        cd ..
    fi
else
    echo "✗ Módulos de Node no encontrados"
fi

# Check Tailwind config
echo ""
echo "⚙️ Archivos de Configuración:"
if [ -f "yenny/tailwind.config.js" ]; then
    echo "✓ Configuración de Tailwind existe"
else
    echo "✗ Configuración de Tailwind no encontrada"
fi

if [ -f "yenny/static/src/input.css" ]; then
    echo "✓ CSS de entrada de Tailwind existe"
else
    echo "✗ CSS de entrada de Tailwind no encontrado"
fi

# Check PostgreSQL
echo ""
echo "🐘 Estado de PostgreSQL:"
if command -v psql &> /dev/null; then
    echo "✓ El cliente de PostgreSQL está instalado"
    # Try to connect to the database
    if psql -h localhost -U postgres -d yenny_db -c "SELECT 1;" &> /dev/null; then
        echo "✓ Se puede conectar a la base de datos yenny_db"
    else
        echo "⚠ No se puede conectar a la base de datos yenny_db (puede necesitar configuración)"
    fi
else
    echo "✗ El cliente de PostgreSQL no está instalado"
fi

# Check Django project
echo ""
echo "🌐 Proyecto Django:"
if [ -f "yenny/manage.py" ]; then
    echo "✓ El proyecto Django existe"
    cd yenny
    source ../venv/bin/activate 2>/dev/null

    # Check if migrations are needed
    if python manage.py showmigrations 2>/dev/null | grep -q '\[ \]'; then
        echo "⚠ Se encontraron migraciones pendientes - ejecuta 'python manage.py migrate'"
    else
        echo "✓ Todas las migraciones están actualizadas"
    fi

    deactivate 2>/dev/null
    cd ..
else
    echo "✗ Proyecto Django no encontrado"
fi

echo ""
echo "=== Recomendaciones de Configuración ==="
echo ""

# Provide setup recommendations
if [ ! -d "venv" ]; then
    echo "1. Crear entorno virtual: python3 -m venv venv"
fi

if [ ! -f "venv/bin/activate" ] || ! pip list 2>/dev/null | grep -q "Django"; then
    echo "2. Instalar dependencias de Python: source venv/bin/activate && pip install -r scripts/requirements.txt"
fi

if [ ! -d "yenny/node_modules" ]; then
    echo "3. Instalar dependencias de Node: cd yenny && npm install"
fi

if [ ! -f "yenny/static/src/output.css" ]; then
    echo "4. Compilar Tailwind CSS: cd yenny && npm run build-prod"
fi

if ! psql -h localhost -U postgres -d yenny_db -c "SELECT 1;" &> /dev/null; then
    echo "5. Configurar la base de datos PostgreSQL usando docs/db/install.sql"
fi

if python manage.py showmigrations 2>/dev/null | grep -q '\[ \]'; then
    echo "6. Ejecutar migraciones de Django: cd yenny && python manage.py migrate"
fi

echo ""
echo "Para ejecutar la configuración completa, ejecuta: bash scripts/mac/setup.sh"
echo "Para iniciar el servidor de desarrollo, ejecuta: bash scripts/mac/dev.sh"
