# Análisis y Metodologías de Sistemas

## 💡 Motivación

Este desarrollo es un proyecto académico dentro de la materia **Análisis y Metodologías de Sistemas** de la carrera **Analista de Sistemas** de la **Escuela Da Vinci**.

## 🧑‍🤝‍🧑 Integrantes

- [Beceyro Ferrán Agustín](https://github.com/AgUsBF)
- [Bielaszczuk Cristhian Emmanuel](https://github.com/1337B)

## 🎯 Objetivo

Desarrollar una aplicación web para gestionar las operaciones de una librería.

## 🔍 Contexto

### Descripción

Desarrollar un sistema completo para gestionar las existencias y ventas en la librería YENNY. Este sistema permitirá registrar libros con categorías y cantidades disponibles, ajustar precios, ingresar ventas y generar informes de ventas y estadísticas de popularidad.

### Enfoque

El enfoque principal estará en la creación de una interfaz que facilite a los empleados de YENNY registrar y gestionar libros, ajustar precios y procesar ventas de manera eficiente. La plataforma generará informes de ventas diarios y proporcionará estadísticas detalladas sobre la popularidad de los libros.

> [!NOTE]  
> **Alcance:** Se prevé desarrollar una primera versión (MVP) con las funcionalidades básicas y un roadmap para futuras mejoras.

## 🛠️ Tecnologías Utilizadas

- ☕ **Lenguaje:** Python
- 💻 **Framework:** TBD
- 🗃️ **Base de Datos:** TBD
<!-- - 🔗 **Conectividad:** -->

## 💼 Documentación

La documentación de la aplicación se puede encontrar en el [GitHub Wiki](https://github.com/AgUsBF-DV/dv-ayms/wiki) del repositorio.

<!-- ## 📸 Vistas -->

## 📄 Licencia

## 🚀 Guía de Instalación Completa

Esta guía te ayudará a configurar todo el proyecto desde cero en cualquier sistema operativo.

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:
- **Git** instalado 
  - macOS: `brew install git` o [Descargar](https://git-scm.com/download/mac)
  - Windows: [Descargar Git para Windows](https://git-scm.com/download/win)
  - Linux: `sudo apt install git` o `sudo yum install git`
- **Python 3.12+** instalado
  - macOS: `brew install python` o [Descargar Python](https://www.python.org/downloads/)
  - Windows: [Descargar Python](https://www.python.org/downloads/)
  - Linux: `sudo apt install python3 python3-pip` o `sudo yum install python3 python3-pip`
- **PostgreSQL 14+** instalado
  - macOS: `brew install postgresql` o [Descargar](https://www.postgresql.org/download/macos/)
  - Windows: [Descargar PostgreSQL](https://www.postgresql.org/download/windows/)
  - Linux: `sudo apt install postgresql postgresql-contrib` o `sudo yum install postgresql postgresql-server`

### Instalación Paso a Paso

#### 1. Clonar el Repositorio

```bash
# Clonar el repositorio (todos los SO)
git clone https://github.com/AgUsBF-DV/dv-ayms.git

# Navegar al directorio del proyecto
cd dv-ayms
```

#### 2. Configurar Entorno Virtual de Python

**macOS/Linux:**
```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate
```

**Windows:**
```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
.venv\Scripts\activate
```

*Nota: Deberías ver (.venv) en tu prompt de terminal después de activar*

#### 3. Instalar Dependencias de Python

```bash
# Actualizar pip (todos los SO)
python -m pip install --upgrade pip

# Instalar paquetes requeridos (todos los SO)
pip install django>=5.0
pip install django-environ
pip install psycopg2-binary
pip install pytest
pip install pytest-django
```

#### 4. Configurar Base de Datos PostgreSQL

**Opción A: Usando PostgreSQL directamente**

1. Asegúrate de que PostgreSQL esté ejecutándose:
   - **macOS:** `brew services start postgresql`
   - **Windows:** Revisar Servicios de Windows o `pg_ctl start`
   - **Linux:** `sudo systemctl start postgresql`

2. Ejecutar el script de configuración de base de datos:

**macOS/Linux:**
```bash
# Desde la raíz del proyecto
psql -h 127.0.0.1 -U postgres -f docs/db/install.sql
```

**Windows (PowerShell):**
```powershell
# Desde la raíz del proyecto
psql -h 127.0.0.1 -U postgres -f docs\db\install.sql
```

**Opción B: Usando Docker (Alternativa para todos los SO)**

Si prefieres usar Docker:

```bash
# Asegúrate de que Docker Desktop esté ejecutándose (todos los SO)
docker-compose up -d postgres

# Espera a que el contenedor esté listo, luego ejecuta la configuración
# macOS/Linux:
psql -h 127.0.0.1 -U postgres -f docs/db/install.sql

# Windows:
psql -h 127.0.0.1 -U postgres -f docs\db\install.sql
```

#### 5. Configurar Variables de Entorno

El archivo `.env` ya debería existir en la raíz del proyecto con valores por defecto:

```env
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=django-insecure-change-me-in-production
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=dvayms_db
DB_USER=dvayms_user
DB_PASSWORD=dvayms_pass
DB_HOST=127.0.0.1
DB_PORT=5432
```

*Nota: Estas son configuraciones de desarrollo.*

#### 6. Configurar Aplicación Django

```bash
# Navegar al directorio backend (todos los SO)
cd backend

# Crear migraciones de base de datos (todos los SO)
python manage.py makemigrations common core

# Aplicar migraciones a la base de datos (todos los SO)
python manage.py migrate

# Crear datos de desarrollo (roles y usuarios de prueba) (todos los SO)
python manage.py seed_dev
```

#### 7. Iniciar el Servidor de Desarrollo

```bash
# Iniciar servidor de desarrollo Django (todos los SO)
python manage.py runserver

# El servidor estará disponible en: http://127.0.0.1:8000/
```

### 🎉 ¡Listo para Usar!

Tu aplicación debería estar ejecutándose en `http://127.0.0.1:8000/`

#### Cuentas de Usuario por Defecto

Después de ejecutar `seed_dev`, tienes estas cuentas de prueba:

- **Administrador**: 
  - Usuario: `admin`
  - Contraseña: `Admin123!`
  - Acceso: Acceso completo al sistema

- **Empleado de Tienda**: 
  - Usuario: `clerk` 
  - Contraseña: `Clerk123!`
  - Acceso: Limitado a catálogo, ventas y clientes

### 🧪 Ejecutar Pruebas

```bash
# Ejecutar todas las pruebas (todos los SO)
python manage.py test

# Ejecutar archivo de prueba específico (todos los SO)
python manage.py test core.tests.test_auth

# Ejecutar con salida detallada (todos los SO)
python manage.py test --verbosity=2
```

### 🛠️ Comandos de Desarrollo

```bash
# Crear nueva app Django (todos los SO)
python manage.py startapp <nombre_app>

# Crear nuevas migraciones después de cambios en modelos (todos los SO)
python manage.py makemigrations

# Aplicar migraciones (todos los SO)
python manage.py migrate

# Acceder al admin de Django (todos los SO)
python manage.py createsuperuser

# Recopilar archivos estáticos para producción (todos los SO)
python manage.py collectstatic
```

### 🚨 Solución de Problemas

**Problemas de Conexión a Base de Datos:**

- **Verificar que PostgreSQL esté ejecutándose:**
  - **macOS:** `brew services list | grep postgresql`
  - **Windows:** `pg_ctl status` o revisar Servicios de Windows
  - **Linux:** `sudo systemctl status postgresql`

- **Verificar que el puerto 5432 esté disponible:**
  - **macOS/Linux:** `netstat -an | grep 5432`
  - **Windows:** `netstat -an | findstr 5432`

- Asegurar que `dvayms_user` y `dvayms_db` fueron creados exitosamente

**Errores de Migración:**

**macOS/Linux:**
```bash
# Eliminar archivos de migración y recrear
rm backend/*/migrations/0001_initial.py
python manage.py makemigrations common core
python manage.py migrate
```

**Windows:**
```bash
# Eliminar archivos de migración y recrear
del backend\*\migrations\0001_initial.py
python manage.py makemigrations common core
python manage.py migrate
```

**Errores de Módulo No Encontrado:**
- Asegúrate de que el entorno virtual esté activado (ver `.venv` en el prompt)
- Reinstalar dependencias: `pip install -r requirements.txt` (si existe)

**Errores de Template:**
- Asegúrate de estar en el directorio `backend` al ejecutar comandos `manage.py`
- Verificar que `frontend/templates/base.html` tenga `{% load static %}` al inicio

**Puerto Ya en Uso:**

- **Matar el proceso:**
  - **macOS/Linux:** `lsof -ti:8000 | xargs kill -9`
  - **Windows:** `netstat -ano | findstr :8000` luego `taskkill /PID <PID> /F`
- **O usar puerto diferente (todos los SO):** `python manage.py runserver 8001`

**Problemas de Permisos (macOS/Linux):**
```bash
# Si tienes problemas de permisos con PostgreSQL
sudo -u postgres psql -f docs/db/install.sql
```

**Problemas con Python en macOS:**
```bash
# Si python3 no está disponible, usar python
python --version  # Verificar versión
# O instalar con Homebrew
brew install python@3.12
```
