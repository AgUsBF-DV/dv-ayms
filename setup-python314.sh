#!/bin/bash

# DVAYMS Project Setup Script (Python 3.14 Compatible)
echo "=== DVAYMS Project Setup (Python 3.14 Compatible) ==="

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Detected Python version: $PYTHON_VERSION"

# Step 1: Create virtual environment
echo "Step 1: Creating Python virtual environment..."
python3 -m venv venv
echo "✓ Virtual environment created"

# Step 2: Activate virtual environment and install dependencies
echo "Step 2: Installing Python dependencies (with Python 3.14 compatibility)..."
source venv/bin/activate

# Upgrade pip first
pip install --upgrade pip

# Install dependencies one by one to handle any issues
echo "Installing Django..."
pip install Django==5.2.6

echo "Installing PostgreSQL adapter (psycopg3 for Python 3.14 compatibility)..."
pip install "psycopg[binary]==3.2.12"

echo "Installing django-compressor..."
pip install django-compressor==4.5.1

echo "✓ Python dependencies installed successfully"

# Step 3: Install Node.js dependencies for Tailwind CSS
echo "Step 3: Installing Node.js dependencies..."
cd yenny
npm install
echo "✓ Node.js dependencies installed"

# Step 4: Build Tailwind CSS
echo "Step 4: Building Tailwind CSS..."
npm run build-prod
echo "✓ Frontend assets compiled"

# Step 5: Database setup instructions
echo ""
echo "Step 5: Database Setup"
echo "================================================"
echo "Before continuing, please set up PostgreSQL:"
echo "1. Ensure PostgreSQL is installed and running"
echo "2. Open pgAdmin or use psql command line"
echo "3. Execute these commands:"
echo ""
echo "   CREATE DATABASE yenny_db;"
echo "   CREATE USER postgres WITH PASSWORD 'postgres';"
echo "   ALTER ROLE postgres SET client_encoding TO 'utf8';"
echo "   ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';"
echo "   ALTER ROLE postgres SET timezone TO 'UTC';"
echo "   GRANT ALL PRIVILEGES ON DATABASE yenny_db TO postgres;"
echo ""
echo "Or run the SQL file: docs/db/install.sql"
echo "================================================"
echo ""

read -p "Press Enter after setting up the database to continue..."

# Step 6: Django setup
echo "Step 6: Django setup..."
cd ..
source venv/bin/activate
cd yenny

echo "Running Django migrations..."
python manage.py makemigrations autores
python manage.py makemigrations categorias
python manage.py makemigrations clientes
python manage.py makemigrations editoriales
python manage.py makemigrations empleados
python manage.py makemigrations libros
python manage.py makemigrations ventas
python manage.py migrate

echo ""
echo "Creating Django superuser..."
echo "Please create an admin user for the system:"
python manage.py createsuperuser

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "🎉 Your DVAYMS project is now ready!"
echo ""
echo "To start development:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Navigate to yenny directory: cd yenny"
echo "3. Run server: python manage.py runserver"
echo ""
echo "For development with auto-rebuilding CSS:"
echo "1. Terminal 1: cd yenny && npm run build (watch mode)"
echo "2. Terminal 2: cd yenny && python manage.py runserver"
echo ""
echo "🌐 Application: http://127.0.0.1:8000/"
echo "👑 Admin panel: http://127.0.0.1:8000/admin/"
echo ""
echo "📖 Need help? Check SETUP.md or QUICK-REFERENCE.md"
