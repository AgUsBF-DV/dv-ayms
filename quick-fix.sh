#!/bin/bash

# Quick fix for psycopg version issue
echo "🔧 Fixing psycopg version for Python 3.14..."

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✅ Virtual environment activated"
else
    echo "⚠️  No virtual environment found, using global Python"
fi

# Remove any existing psycopg installations
echo "🧹 Cleaning up old psycopg installations..."
pip uninstall -y psycopg2 psycopg2-binary psycopg psycopg-binary 2>/dev/null || true

# Install the correct version
echo "📦 Installing correct psycopg version..."
pip install "psycopg[binary]==3.2.12"
pip install Django==5.2.6
pip install django-compressor==4.5.1

# Test installation
echo "🧪 Testing installation..."
python -c "
try:
    import psycopg
    print('✅ psycopg imported successfully')
    import django
    print('✅ Django imported successfully')
    print('✅ All dependencies working!')
    print('🎉 Ready to continue with setup!')
except ImportError as e:
    print(f'❌ Import error: {e}')
    exit(1)
"

echo ""
echo "✅ Fix applied! You can now run:"
echo "   ./run.sh"
echo "or continue with manual setup."
