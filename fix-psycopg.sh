#!/bin/bash

# Quick fix for psycopg2-binary issue in Python 3.14
echo "🔧 Fixing psycopg2-binary issue for Python 3.14..."

# Activate virtual environment
source venv/bin/activate

# Remove problematic package
echo "Removing psycopg2-binary..."
pip uninstall -y psycopg2 psycopg2-binary 2>/dev/null || true

# Install compatible version
echo "Installing psycopg3 (Python 3.14 compatible)..."
pip install "psycopg[binary]==3.2.12"

# Install remaining dependencies
echo "Installing remaining dependencies..."
pip install Django==5.2.6
pip install django-compressor==4.5.1

# Test the installation
echo "Testing PostgreSQL connection..."
cd yenny
python -c "
try:
    import psycopg
    print('✅ psycopg imported successfully')
    import django
    print(f'✅ Django {django.VERSION} imported successfully')
    print('✅ Dependencies installed correctly!')
except ImportError as e:
    print(f'❌ Import error: {e}')
"

echo ""
echo "🎉 Fix applied successfully!"
echo ""
echo "Now you can continue with the setup:"
echo "1. Set up your PostgreSQL database (see docs/db/install.sql)"
echo "2. Run Django migrations: python manage.py migrate"
echo "3. Create superuser: python manage.py createsuperuser"
echo "4. Start server: python manage.py runserver"
