#!/bin/bash

# Quick fix for psycopg2-binary issue in Python 3.14
# NOTA: Este script debe ejecutarse desde la RAÍZ del proyecto

# Verificar si estamos en la raíz del proyecto
if [ ! -f "yenny/manage.py" ]; then
    echo "❌ Error: Este script debe ejecutarse desde la raíz del proyecto"
    echo "💡 Cambia al directorio raíz primero"
    exit 1
fi

# Verificar si existe el entorno virtual
if [ ! -f "venv/bin/activate" ]; then
    echo "❌ Error: No se encontró el entorno virtual"
    echo "💡 Ejecuta primero: bash scripts/linux/setup.sh"
    exit 1
fi

echo "🔧 Reparando problema de psycopg2-binary para Python 3.14..."

# Activate virtual environment
source venv/bin/activate

# Remove problematic package
echo "Eliminando paquete problemático..."
pip uninstall -y psycopg2 psycopg2-binary 2>/dev/null || true

# Install compatible version
echo "Instalando psycopg3 (compatible con Python 3.14)..."
pip install "psycopg[binary]==3.2.12"

# Install remaining dependencies
echo "Instalando dependencias restantes..."
pip install Django==5.2.6
pip install django-compressor==4.5.1

# Test the installation
echo "Probando la instalación..."
cd yenny
python -c "
try:
    import psycopg
    print('✅ psycopg importado exitosamente')
    import django
    print(f'✅ Django {django.VERSION} importado exitosamente')
    print('✅ ¡Dependencias instaladas correctamente!')
except ImportError as e:
    print(f'❌ Error de importación: {e}')
"

echo ""
echo "🎉 ¡Reparación aplicada exitosamente!"
echo ""
echo "Ahora puedes continuar con la configuración:"
echo "1. Configura tu base de datos PostgreSQL (ver docs/db/install.sql)"
echo "2. Ejecuta las migraciones de Django: python manage.py migrate"
echo "3. Crea un superusuario: python manage.py createsuperuser"
echo "4. Inicia el servidor: python manage.py runserver"
