#!/bin/bash

# Development startup script
echo "=== Starting DVAYMS Development Environment ==="

# Activate virtual environment
source venv/bin/activate

# Navigate to Django project
cd yenny

# Check if we need to run migrations
echo "Checking for pending migrations..."
python manage.py showmigrations | grep '\[ \]' > /dev/null
if [ $? -eq 0 ]; then
    echo "Found pending migrations. Running migrate..."
    python manage.py migrate
fi

# Start development server
echo "Starting Django development server..."
echo "Application will be available at: http://127.0.0.1:8000/"
echo "Admin interface at: http://127.0.0.1:8000/admin/"
echo ""
echo "To also watch and rebuild Tailwind CSS, run in another terminal:"
echo "cd yenny && npm run build"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python manage.py runserver
