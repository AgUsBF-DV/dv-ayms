# Guía para Ejecutar Tests en Django

Esta guía explica cómo ejecutar tests unitarios en un proyecto Django tanto en Windows como en macOS/Linux.

## 📋 Requisitos Previos

- Python 3.8+ instalado
- Django instalado en el entorno virtual
- Proyecto Django configurado correctamente

## 🔧 Configuración Inicial

### Windows (PowerShell/CMD)

```powershell
# Navegar al directorio del proyecto
cd C:\Users\tu_usuario\Downloads\dv-ayms

# Activar el entorno virtual
.\venv\Scripts\activate

# Verificar que Django está instalado
python -c "import django; print(django.get_version())"

# Navegar al directorio con manage.py
cd yenny
```

### macOS/Linux (Terminal/Bash)

```bash
# Navegar al directorio del proyecto
cd ~/Downloads/dv-ayms

# Activar el entorno virtual
source venv/bin/activate

# Verificar que Django está instalado
python -c "import django; print(django.get_version())"

# Navegar al directorio con manage.py
cd yenny
```

## 🧪 Comandos para Ejecutar Tests

### 1. Ejecutar Todos los Tests

#### Windows
```powershell
# PowerShell
python manage.py test

# CMD
python manage.py test
```

#### macOS/Linux
```bash
python manage.py test
```

### 2. Ejecutar Tests de una App Específica

#### Windows
```powershell
# Ejecutar todos los tests de la app ventas
python manage.py test ventas

# Ejecutar tests de otras apps
python manage.py test autores
python manage.py test libros
python manage.py test clientes
```

#### macOS/Linux
```bash
# Ejecutar todos los tests de la app ventas
python manage.py test ventas

# Ejecutar tests de otras apps
python manage.py test autores
python manage.py test libros
python manage.py test clientes
```

### 3. Ejecutar Tests de un Módulo Específico

#### Windows
```powershell
# Ejecutar solo los tests de modelos de ventas
python manage.py test ventas.tests.test_models

# Con verbose level 2 (más detalle)
python manage.py test ventas.tests.test_models -v 2

# Con verbose level 0 (silencioso)
python manage.py test ventas.tests.test_models -v 0
```

#### macOS/Linux
```bash
# Ejecutar solo los tests de modelos de ventas
python manage.py test ventas.tests.test_models

# Con verbose level 2 (más detalle)
python manage.py test ventas.tests.test_models -v 2

# Con verbose level 0 (silencioso)
python manage.py test ventas.tests.test_models -v 0
```

### 4. Ejecutar una Clase de Tests Específica

#### Windows
```powershell
# Ejecutar solo la clase VentaModelTest
python manage.py test ventas.tests.test_models.VentaModelTest

# Ejecutar solo la clase VentaLibroModelTest
python manage.py test ventas.tests.test_models.VentaLibroModelTest -v 2
```

#### macOS/Linux
```bash
# Ejecutar solo la clase VentaModelTest
python manage.py test ventas.tests.test_models.VentaModelTest

# Ejecutar solo la clase VentaLibroModelTest
python manage.py test ventas.tests.test_models.VentaLibroModelTest -v 2
```

### 5. Ejecutar un Test Específico

#### Windows
```powershell
# Ejecutar un test específico
python manage.py test ventas.tests.test_models.VentaLibroModelTest.test_subtotal_equals_cantidad_times_precio

# Con verbose
python manage.py test ventas.tests.test_models.VentaLibroModelTest.test_subtotal_equals_cantidad_times_precio -v 2
```

#### macOS/Linux
```bash
# Ejecutar un test específico
python manage.py test ventas.tests.test_models.VentaLibroModelTest.test_subtotal_equals_cantidad_times_precio

# Con verbose
python manage.py test ventas.tests.test_models.VentaLibroModelTest.test_subtotal_equals_cantidad_times_precio -v 2
```

## 🔍 Opciones Avanzadas

### Mantener Base de Datos de Test

#### Windows & macOS/Linux
```bash
# No borrar la base de datos de tests después de ejecutar
python manage.py test --keepdb

# Usar base de datos en memoria para tests más rápidos
python manage.py test --parallel

# Ejecutar tests en paralelo (requiere más memoria)
python manage.py test --parallel 4
```

### Debug y Desarrollo

#### Windows
```powershell
# Ejecutar con debug activado
python manage.py test --debug-mode

# Fallar rápido en el primer error
python manage.py test --failfast

# Ejecutar solo tests que fallaron la última vez
python manage.py test --liveserver
```

#### macOS/Linux
```bash
# Ejecutar con debug activado
python manage.py test --debug-mode

# Fallar rápido en el primer error
python manage.py test --failfast

# Ejecutar solo tests que fallaron la última vez
python manage.py test --liveserver
```

## 📊 Interpretando la Salida

### Salida Exitosa
```
Found 16 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
................
----------------------------------------------------------------------
Ran 16 tests in 6.671s

OK
Destroying test database for alias 'default'...
```

### Salida con Errores
```
FAIL: test_calcular_subtotal_method (ventas.tests.test_models.VentaLibroModelTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "...", line 164, in test_calcular_subtotal_method
    self.assertEqual(venta_libro.subtotal, 0)
AssertionError: None != 0

----------------------------------------------------------------------
Ran 16 tests in 6.671s

FAILED (failures=1)
```

## 🐍 Usando pytest (Alternativa)

Si prefieres usar pytest en lugar del test runner de Django:

### Instalación

#### Windows & macOS/Linux
```bash
pip install pytest-django
```

### Configuración (pytest.ini)
```ini
[tool:pytest]
DJANGO_SETTINGS_MODULE = yenny.settings
python_files = tests.py test_*.py *_tests.py
```

### Comandos pytest

#### Windows
```powershell
# Ejecutar todos los tests
pytest

# Ejecutar tests específicos
pytest yenny/ventas/tests/test_models.py

# Con verbose
pytest -v yenny/ventas/tests/test_models.py

# Ejecutar un test específico
pytest yenny/ventas/tests/test_models.py::VentaLibroModelTest::test_subtotal_equals_cantidad_times_precio
```

#### macOS/Linux
```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests específicos
pytest yenny/ventas/tests/test_models.py

# Con verbose
pytest -v yenny/ventas/tests/test_models.py

# Ejecutar un test específico
pytest yenny/ventas/tests/test_models.py::VentaLibroModelTest::test_subtotal_equals_cantidad_times_precio
```

## 🚨 Solución de Problemas Comunes

### Error: "ModuleNotFoundError: No module named 'django'"

#### Windows
```powershell
# Verificar que el entorno virtual está activado
echo $env:VIRTUAL_ENV

# Si no está activado
.\venv\Scripts\activate

# Reinstalar Django si es necesario
pip install django
```

#### macOS/Linux
```bash
# Verificar que el entorno virtual está activado
echo $VIRTUAL_ENV

# Si no está activado
source venv/bin/activate

# Reinstalar Django si es necesario
pip install django
```

### Error: "ImportError: 'tests' module incorrectly imported"

```bash
# Eliminar archivos tests.py conflictivos
rm app/tests.py  # Si tienes un directorio app/tests/

# O renombrar
mv app/tests.py app/tests_old.py
```

### Error de Base de Datos

```bash
# Recrear las migraciones
python manage.py makemigrations
python manage.py migrate

# Ejecutar tests sin base de datos persistente
python manage.py test --keepdb
```

## 📝 Ejemplos Específicos del Proyecto

### Tests de Ventas

#### Windows
```powershell
# Ejecutar todos los tests de ventas con detalle máximo
python manage.py test ventas.tests.test_models -v 2

# Solo tests de VentaLibro
python manage.py test ventas.tests.test_models.VentaLibroModelTest -v 2

# Test específico de subtotal
python manage.py test ventas.tests.test_models.VentaLibroModelTest.test_subtotal_equals_cantidad_times_precio -v 2
```

#### macOS/Linux
```bash
# Ejecutar todos los tests de ventas con detalle máximo
python manage.py test ventas.tests.test_models -v 2

# Solo tests de VentaLibro  
python manage.py test ventas.tests.test_models.VentaLibroModelTest -v 2

# Test específico de subtotal
python manage.py test ventas.tests.test_models.VentaLibroModelTest.test_subtotal_equals_cantidad_times_precio -v 2
```

### Tests de Otros Modelos

```bash
# Tests de libros
python manage.py test libros

# Tests de autores
python manage.py test autores

# Tests de clientes
python manage.py test clientes

# Ejecutar todos los tests del proyecto
python manage.py test
```

## 🏃‍♂️ Script de Automatización

### Windows (run_tests.bat)
```batch
@echo off
echo Activando entorno virtual...
call .\venv\Scripts\activate

echo Navegando al directorio del proyecto...
cd yenny

echo Ejecutando tests...
python manage.py test ventas.tests.test_models -v 2

echo Tests completados.
pause
```

### macOS/Linux (run_tests.sh)
```bash
#!/bin/bash
echo "Activando entorno virtual..."
source venv/bin/activate

echo "Navegando al directorio del proyecto..."
cd yenny

echo "Ejecutando tests..."
python manage.py test ventas.tests.test_models -v 2

echo "Tests completados."
```

```bash
# Hacer ejecutable (solo macOS/Linux)
chmod +x run_tests.sh
./run_tests.sh
```

---

## 📖 Referencias

- [Documentación oficial de Django Testing](https://docs.djangoproject.com/en/stable/topics/testing/)
- [pytest-django documentation](https://pytest-django.readthedocs.io/)
- [Django Test Case API](https://docs.djangoproject.com/en/stable/topics/testing/tools/)
