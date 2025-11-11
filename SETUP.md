# Guía de Configuración del Proyecto DVAYMS

## Descripción General
Esta es una aplicación web Django para gestionar una librería (Librería YENNY) con las siguientes características:
- Gestión de inventario de libros
- Seguimiento de ventas
- Gestión de clientes
- Gestión de autores y editoriales
- Organización por categorías

## Tecnologías Utilizadas
- **Backend**: Django 5.2.6 con PostgreSQL
- **Frontend**: Tailwind CSS + Flowbite
- **Base de Datos**: PostgreSQL

## Prerrequisitos
Antes de configurar el proyecto, asegúrate de tener instalado:
1. **Python 3.8+** - [Descargar aquí](https://python.org)
   - ⚠️ **Nota para Python 3.14**: Si usas Python 3.14, usa `setup-python314.sh` en lugar de `setup.sh`
2. **PostgreSQL** - [Descargar aquí](https://postgresql.org)
3. **Node.js & npm** - [Descargar aquí](https://nodejs.org)

## Configuración Paso a Paso

### **⚡ Opción Rápida: Scripts Automatizados (Recomendado)**

#### **Orden de Ejecución para Linux/macOS:**

##### **1. 🚀 Setup Inicial Completo**
```bash
chmod +x run.sh && ./run.sh
```
**Resultado Esperado:**
- ✅ Entorno virtual creado y activado
- ✅ Dependencias Python instaladas (con auto-fix para Python 3.14)
- ✅ Dependencias Node.js instaladas
- ✅ Frontend compilado
- ✅ Migraciones ejecutadas
- ✅ Usuario admin creado (admin/admin)
- ✅ Servidor iniciado automáticamente

**Si Falla:**
```bash
# Verificar estado del proyecto
./status.sh

# Si hay problemas específicos de Python 3.14
./fix-psycopg.sh

# Para solución rápida de problemas comunes
./quick-fix.sh

# Si todo falla, configuración manual paso a paso
./setup.sh
```

##### **2. 💻 Desarrollo Diario (después del setup inicial)**
```bash
./dev.sh
```
**Resultado Esperado:**
- ✅ Entorno virtual activado automáticamente
- ✅ Migraciones verificadas y aplicadas si es necesario
- ✅ Frontend compilado si hay cambios
- ✅ Servidor iniciado en modo desarrollo

**Si Falla:**
```bash
# Diagnóstico completo
./status.sh

# Fix rápido de problemas comunes
./quick-fix.sh
```

#### **Scripts de Soporte (usar cuando sea necesario):**

##### **3. 🔧 Verificación de Estado**
```bash
./status.sh
```
**Cuándo Usar:** Para diagnosticar problemas o verificar configuración
**Resultado Esperado:**
- ✅ Reporte completo del estado del proyecto
- ✅ Verificación de Python, Node.js, PostgreSQL
- ✅ Estado de entorno virtual y dependencias
- ✅ Verificación de base de datos

##### **4. 🛠️ Fix para Python 3.14**
```bash
./fix-psycopg.sh
```
**Cuándo Usar:** Si usas Python 3.14 y hay errores de psycopg2
**Resultado Esperado:**
- ✅ psycopg2-binary desinstalado
- ✅ psycopg3 instalado y configurado
- ✅ Compatibilidad con Python 3.14 restaurada

##### **5. ⚡ Fix Rápido General**
```bash
./quick-fix.sh
```
**Cuándo Usar:** Para solucionar problemas comunes automáticamente
**Resultado Esperado:**
- ✅ Problemas de entorno virtual solucionados
- ✅ Dependencias faltantes instaladas
- ✅ Migraciones aplicadas
- ✅ Frontend recompilado si es necesario

##### **6. ⚙️ Setup Manual (solo si scripts automáticos fallan)**
```bash
./setup.sh
```
**Cuándo Usar:** Si `run.sh` falla o necesitas configuración sin servidor
**Resultado Esperado:**
- ✅ Mismo resultado que `run.sh` pero sin iniciar servidor automáticamente

---

### **📋 Configuración Manual (Solo si los scripts fallan)**

Si todos los scripts automáticos fallan, puedes configurar manualmente:

### 1. Clonar y Navegar al Proyecto
```bash
# Si aún no has clonado
git clone <repository-url>
cd dvayms
```

### 2. Configurar Entorno Virtual de Python
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Instalar Dependencias de Python

#### Para Python 3.8-3.13:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### Para Python 3.14 (corrección de compatibilidad):
```bash
pip install --upgrade pip
pip install Django==5.2.6
pip install "psycopg[binary]==3.2.12"
pip install django-compressor==4.5.1
```

**Nota**: Python 3.14 requiere psycopg3 en lugar de psycopg2 para la conectividad con PostgreSQL.

### 4. Instalar Dependencias de Node.js
```bash
cd yenny
npm install
cd ..
```

### 5. Configuración de Base de Datos

#### 5.1 Crear Base de Datos PostgreSQL
1. Abre pgAdmin o usa la línea de comandos psql
2. Ejecuta los comandos de `docs/db/install.sql`:
```sql
CREATE DATABASE yenny_db;
CREATE USER postgres WITH PASSWORD 'postgres';
ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE yenny_db TO postgres;
```

#### 5.2 Ejecutar Migraciones de Django
```bash
cd yenny
python manage.py makemigrations
python manage.py migrate
```

### 6. Cargar Datos de Prueba (Opcional)
```bash
# Execute the SQL commands in docs/db/test_data.sql through pgAdmin or psql
```

### 7. Crear Superusuario de Django (Opcional)
```bash
python manage.py createsuperuser
```

### 8. Compilar Assets del Frontend (Tailwind)
```bash
# If you have Tailwind configured, build the CSS
npm run build
```

## Ejecutar la Aplicación

### Servidor de Desarrollo
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Navigate to Django project
cd yenny

# Run development server
python manage.py runserver
```

La aplicación estará disponible en: **http://127.0.0.1:8000/**

### Interfaz de Administración
Accede al admin de Django en: **http://127.0.0.1:8000/admin/**
(Solo si creaste un superusuario)

## Estructura del Proyecto

```
dvayms/
├── backend/          # Alternative backend (if any)
├── docs/            # Documentation and database scripts
├── frontend/        # Static frontend assets
├── yenny/           # Main Django application
│   ├── autores/     # Authors management
│   ├── categorias/  # Categories management
│   ├── clientes/    # Customers management
│   ├── editoriales/ # Publishers management
│   ├── empleados/   # Employees management
│   ├── libros/      # Books management
│   ├── ventas/      # Sales management
│   ├── static/      # Static files (CSS, JS, images)
│   ├── templates/   # HTML templates
│   └── yenny/       # Django project settings
└── requirements.txt # Python dependencies
```

## Problemas Comunes y Solución de Problemas

### **🚨 Matriz de Problemas y Soluciones**

| **Problema** | **Síntoma** | **Solución** | **Script** |
|-------------|-------------|-------------|------------|
| **Python 3.14** | Error psycopg2-binary | Incompatibilidad conocida | `./fix-psycopg.sh` |
| **Entorno Virtual** | CommandNotFound | Entorno no activado | `source venv/bin/activate` |
| **Dependencias** | ModuleNotFoundError | Dependencias no instaladas | `./quick-fix.sh` |
| **Base de Datos** | Connection refused | PostgreSQL no ejecutándose | Iniciar PostgreSQL |
| **Frontend** | CSS no carga | Assets no compilados | `cd yenny && npm run build` |
| **Migraciones** | No such table | Migraciones no aplicadas | `./quick-fix.sh` |
| **Node.js** | npm command not found | Node.js no instalado | Instalar Node.js |
| **Permisos** | Permission denied | Scripts sin permisos | `chmod +x *.sh` |

### **🔍 Diagnóstico Paso a Paso**

#### **1. Verificar Estado General**
```bash
./status.sh
```
Este script te dará un reporte completo de qué está funcionando y qué no.

#### **2. Problemas de Conexión a Base de Datos**
```bash
# Verificar si PostgreSQL está ejecutándose
sudo systemctl status postgresql  # Linux
brew services list | grep postgresql  # macOS

# Verificar conexión
psql -h localhost -U postgres -d yenny_db -c "SELECT 1;"
```

#### **3. Problemas de Migración**
```bash
cd yenny
source ../venv/bin/activate

# Verificar estado de migraciones
python manage.py showmigrations

# Resetear migraciones si es necesario (¡CUIDADO! Perdirás datos)
python manage.py migrate --fake-initial

# Crear y aplicar nuevas migraciones
python manage.py makemigrations
python manage.py migrate
```

#### **4. Problemas con Archivos Estáticos/Frontend**
```bash
cd yenny

# Verificar dependencias Node.js
npm list

# Reinstalar si es necesario
rm -rf node_modules package-lock.json
npm install

# Recompilar CSS
npm run build-prod

# Para Django
python manage.py collectstatic
```

## Flujo de Trabajo de Desarrollo

1. **Activar entorno virtual**: `source venv/bin/activate`
2. **Navegar al proyecto**: `cd yenny`
3. **Ejecutar servidor**: `python manage.py runserver`
4. **Realizar cambios** en tu código
5. **Crear migraciones** cuando cambien los modelos: `python manage.py makemigrations`
6. **Aplicar migraciones**: `python manage.py migrate`

## Apps de Django Disponibles

- **autores**: Gestión de autores
- **categorias**: Categorías de libros
- **clientes**: Información de clientes
- **editoriales**: Detalles de editoriales
- **empleados**: Gestión de empleados (modelo de usuario personalizado)
- **libros**: Inventario de libros
- **ventas**: Transacciones de ventas

## Estructura de URLs
- `/admin/` - Interfaz de administración de Django
- `/autores/` - Sección de autores
- `/categorias/` - Sección de categorías
- `/clientes/` - Sección de clientes
- `/editoriales/` - Sección de editoriales
- `/empleados/` - Sección de empleados
- `/libros/` - Sección de libros
- `/ventas/` - Sección de ventas

## Próximos Pasos Después de la Configuración

1. **Explorar los modelos** en cada app para entender la estructura de datos
2. **Revisar la interfaz de administración** para ver los modelos registrados
3. **Probar la aplicación** creando algunos datos de ejemplo
4. **Revisar las plantillas** para entender la estructura de la interfaz
5. **Revisar los patrones de URL** en el `urls.py` de cada app

## Soporte

Este es un proyecto académico para "Análisis y Metodologías de Sistemas" en la Escuela Da Vinci.

### **📋 Flujo de Trabajo Recomendado**

#### **🔄 Configuración Inicial (Solo Una Vez)**
```bash
# 1. Clonar proyecto
git clone <repo-url>
cd dvayms

# 2. Setup completo automático
chmod +x run.sh && ./run.sh
```

#### **💻 Desarrollo Diario**
```bash
# Cada día de trabajo
./dev.sh
```

#### **🔧 Si Hay Problemas**
```bash
# Diagnóstico
./status.sh

# Fix automático
./quick-fix.sh

# Fix específico Python 3.14
./fix-psycopg.sh
```

### **📊 Verificación de Éxito**

Después de ejecutar `./run.sh` o `./dev.sh`, deberías ver:

```
✅ Entorno virtual: ACTIVO
✅ Python: [version] instalado
✅ Django: Disponible
✅ Base de datos: Conectada
✅ Frontend: Compilado
✅ Migraciones: Aplicadas
✅ Servidor: http://127.0.0.1:8000/
```

### **🎯 URLs de Verificación**

Una vez que el servidor esté ejecutándose, verifica estas URLs:

- **🏠 Home:** http://127.0.0.1:8000/ → Debe cargar sin errores
- **⚙️ Admin:** http://127.0.0.1:8000/admin/ → Login con admin/admin
- **📚 Autores:** http://127.0.0.1:8000/autores/ → Lista con filtros
- **📖 Libros:** http://127.0.0.1:8000/libros/ → Gestión de inventario
- **👥 Clientes:** http://127.0.0.1:8000/clientes/ → Base de datos de clientes
- **💰 Ventas:** http://127.0.0.1:8000/ventas/ → Sistema de ventas completo

Si todas estas URLs cargan correctamente, ¡tu instalación está perfecta!

Para problemas, consulta la documentación en la carpeta `docs/` o revisa el repositorio de GitHub.
