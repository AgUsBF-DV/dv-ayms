#!/bin/bash

# Project Status Checker
echo "=== DVAYMS Project Status Check ==="
echo ""

# Check Python
echo "🐍 Python Status:"
if command -v python3 &> /dev/null; then
    echo "✓ Python3 is installed: $(python3 --version)"
else
    echo "✗ Python3 is not installed"
fi

# Check virtual environment
echo ""
echo "📦 Virtual Environment:"
if [ -d "venv" ]; then
    echo "✓ Virtual environment exists"
    if [ -f "venv/bin/activate" ]; then
        echo "✓ Virtual environment is properly configured"
    else
        echo "✗ Virtual environment seems corrupted"
    fi
else
    echo "✗ Virtual environment not found"
fi

# Check Python dependencies
echo ""
echo "📚 Python Dependencies:"
if [ -f "requirements.txt" ]; then
    echo "✓ requirements.txt exists"
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
        if pip list | grep -q "Django"; then
            echo "✓ Django is installed: $(python -c "import django; print(django.VERSION)")"
        else
            echo "✗ Django is not installed"
        fi
        if pip list | grep -q "psycopg2"; then
            echo "✓ PostgreSQL adapter is installed"
        else
            echo "✗ PostgreSQL adapter is not installed"
        fi
        deactivate
    else
        echo "⚠ Cannot check - virtual environment not activated"
    fi
else
    echo "✗ requirements.txt not found"
fi

# Check Node.js
echo ""
echo "🟢 Node.js Status:"
if command -v node &> /dev/null; then
    echo "✓ Node.js is installed: $(node --version)"
else
    echo "✗ Node.js is not installed"
fi

if command -v npm &> /dev/null; then
    echo "✓ npm is installed: $(npm --version)"
else
    echo "✗ npm is not installed"
fi

# Check Node dependencies
echo ""
echo "🎨 Frontend Dependencies:"
if [ -d "yenny/node_modules" ]; then
    echo "✓ Node modules are installed"
    if [ -f "yenny/package.json" ]; then
        cd yenny
        if npm list tailwindcss &> /dev/null; then
            echo "✓ Tailwind CSS is installed"
        else
            echo "✗ Tailwind CSS is not installed"
        fi
        if npm list flowbite &> /dev/null; then
            echo "✓ Flowbite is installed"
        else
            echo "✗ Flowbite is not installed"
        fi
        cd ..
    fi
else
    echo "✗ Node modules not found"
fi

# Check Tailwind config
echo ""
echo "⚙️ Configuration Files:"
if [ -f "yenny/tailwind.config.js" ]; then
    echo "✓ Tailwind configuration exists"
else
    echo "✗ Tailwind configuration missing"
fi

if [ -f "yenny/static/src/input.css" ]; then
    echo "✓ Tailwind input CSS exists"
else
    echo "✗ Tailwind input CSS missing"
fi

# Check PostgreSQL
echo ""
echo "🐘 PostgreSQL Status:"
if command -v psql &> /dev/null; then
    echo "✓ PostgreSQL client is installed"
    # Try to connect to the database
    if psql -h localhost -U postgres -d yenny_db -c "SELECT 1;" &> /dev/null; then
        echo "✓ Can connect to yenny_db database"
    else
        echo "⚠ Cannot connect to yenny_db database (may need setup)"
    fi
else
    echo "✗ PostgreSQL client is not installed"
fi

# Check Django project
echo ""
echo "🌐 Django Project:"
if [ -f "yenny/manage.py" ]; then
    echo "✓ Django project exists"
    cd yenny
    source ../venv/bin/activate 2>/dev/null

    # Check if migrations are needed
    if python manage.py showmigrations 2>/dev/null | grep -q '\[ \]'; then
        echo "⚠ Pending migrations found - run 'python manage.py migrate'"
    else
        echo "✓ All migrations are up to date"
    fi

    deactivate 2>/dev/null
    cd ..
else
    echo "✗ Django project not found"
fi

echo ""
echo "=== Setup Recommendations ==="
echo ""

# Provide setup recommendations
if [ ! -d "venv" ]; then
    echo "1. Create virtual environment: python3 -m venv venv"
fi

if [ ! -f "venv/bin/activate" ] || ! pip list 2>/dev/null | grep -q "Django"; then
    echo "2. Install Python dependencies: source venv/bin/activate && pip install -r requirements.txt"
fi

if [ ! -d "yenny/node_modules" ]; then
    echo "3. Install Node dependencies: cd yenny && npm install"
fi

if [ ! -f "yenny/static/src/output.css" ]; then
    echo "4. Build Tailwind CSS: cd yenny && npm run build-prod"
fi

if ! psql -h localhost -U postgres -d yenny_db -c "SELECT 1;" &> /dev/null; then
    echo "5. Setup PostgreSQL database using docs/db/install.sql"
fi

if python manage.py showmigrations 2>/dev/null | grep -q '\[ \]'; then
    echo "6. Run Django migrations: cd yenny && python manage.py migrate"
fi

echo ""
echo "To run the complete setup, execute: bash setup.sh"
echo "To start development server, execute: bash dev.sh"
