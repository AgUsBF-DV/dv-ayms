#!/bin/bash

# Development startup script
# NOTA: Este script debe ejecutarse desde la RAÍZ del proyecto

# Verificar si estamos en la raíz del proyecto
if [ ! -f "yenny/manage.py" ]; then
    echo "❌ Error: Este script debe ejecutarse desde la raíz del proyecto"
    echo "💡 Cambia al directorio raíz primero"
    exit 1
fi

echo "=== Iniciando Entorno de Desarrollo DVAYMS ==="

# Activate virtual environment
if [ ! -f "venv/bin/activate" ]; then
    echo "❌ Error: No se encontró el entorno virtual"
    echo "💡 Ejecuta primero: bash scripts/mac/run.sh o bash scripts/mac/setup.sh"
    exit 1
fi

source venv/bin/activate

# Navigate to Django project
cd yenny

# Check if we need to run migrations
echo "Verificando migraciones pendientes..."
python manage.py showmigrations | grep '\[ \]' > /dev/null
if [ $? -eq 0 ]; then
    echo "Se encontraron migraciones pendientes. Ejecutando migrate..."
    python manage.py migrate
fi

# Start development server
echo "Iniciando servidor de desarrollo de Django..."
echo "La aplicación estará disponible en: http://127.0.0.1:8000/"
echo ""
echo "Para también observar y reconstruir Tailwind CSS, ejecuta en otra terminal:"
echo "cd yenny && npm run build"
echo ""
echo "Presiona Ctrl+C para detener el servidor"
echo ""

python manage.py runserver
