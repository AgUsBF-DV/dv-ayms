#!/bin/bash

# Quick fix for psycopg version issue
# NOTA: Este script debe ejecutarse desde la RAÍZ del proyecto

# Verificar si estamos en la raíz del proyecto
if [ ! -f "yenny/manage.py" ]; then
    echo "❌ Error: Este script debe ejecutarse desde la raíz del proyecto"
    echo "💡 Cambia al directorio raíz primero"
    exit 1
fi

echo "🔧 Reparación rápida para psycopg con Python 3.14..."

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✅ Entorno virtual activado"
else
    echo "⚠️  No se encontró entorno virtual, usando Python global"
fi

# Remove any existing psycopg installations
echo "🧹 Limpiando instalaciones antiguas de psycopg..."
pip uninstall -y psycopg2 psycopg2-binary psycopg psycopg-binary 2>/dev/null || true

# Install the correct version
echo "📦 Instalando la versión correcta de psycopg..."
pip install "psycopg[binary]==3.2.12"
pip install Django==5.2.6
pip install django-compressor==4.5.1

# Test installation
echo "🧪 Probando instalación..."
python -c "
try:
    import psycopg
    print('✅ psycopg importado exitosamente')
    import django
    print('✅ Django importado exitosamente')
    print('✅ ¡Todas las dependencias funcionando!')
    print('🎉 ¡Listo para continuar con la configuración!')
except ImportError as e:
    print(f'❌ Error de importación: {e}')
    exit(1)
"

echo ""
echo "✅ ¡Reparación aplicada! Ahora puedes ejecutar:"
echo "   bash scripts/mac/run.sh"
echo "o continuar con la configuración manual."
