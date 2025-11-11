#!/bin/bash

# DVAYMS Project Setup Script
echo "=== DVAYMS Project Setup ==="

# Step 1: Create virtual environment
echo "Step 1: Creating Python virtual environment..."
python3 -m venv venv
echo "✓ Virtual environment created"

# Step 2: Activate virtual environment and install dependencies
echo "Step 2: Installing Python dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "✓ Python dependencies installed"

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
echo "Step 5: Database Setup"
echo "Please ensure PostgreSQL is installed and running, then:"
echo "1. Open pgAdmin or psql"
echo "2. Execute the SQL commands in docs/db/install.sql"
echo "   (Creates database 'yenny_db' and user 'postgres')"
echo "3. Come back and continue with Django migrations"

read -p "Press Enter after setting up the database..."

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

echo "Creating superuser..."
echo "Please create an admin user:"
python manage.py createsuperuser

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "To start the development server:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Navigate to yenny directory: cd yenny"
echo "3. Run server: python manage.py runserver"
echo ""
echo "For development with auto-rebuilding CSS:"
echo "1. In one terminal: cd yenny && npm run build"
echo "2. In another terminal: python manage.py runserver"
echo ""
echo "The application will be available at http://127.0.0.1:8000/"
echo "Admin interface available at http://127.0.0.1:8000/admin/"
