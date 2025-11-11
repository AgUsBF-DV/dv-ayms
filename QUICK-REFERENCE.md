# DVAYMS - Comandos de Referencia Rápida

## 🚀 Configuración Inicial (Solo una vez)

### ⚡ Un Solo Comando (Más Fácil)

#### 🐧 Linux / 🍎 macOS:
```bash
chmod +x run.sh && ./run.sh
```

#### 🪟 Windows:
```cmd
run.bat
```

### Manual (Si prefieres control total)

#### 🐧 Linux / 🍎 macOS:
```bash
# Configuración automática completa
bash setup.sh

# O manual paso a paso:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd yenny && npm install
npm run build-prod
```

#### 🪟 Windows:
```cmd
# Configuración automática completa
setup.bat

# O manual paso a paso:
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
cd yenny && npm install
npm run build-prod
```

## 💻 Desarrollo Diario

### Iniciar Servidor de Desarrollo

#### 🐧 Linux / 🍎 macOS:
```bash
# Opción 1: Script automático (recomendado)
bash dev.sh

# Opción 2: Manual
source venv/bin/activate
cd yenny
python manage.py runserver
```

#### 🪟 Windows:
```cmd
# Opción 1: Script automático (recomendado)
dev.bat

# Opción 2: Manual
venv\Scripts\activate.bat
cd yenny
python manage.py runserver
```

### Recompilar CSS (en terminal separada)

#### 🌍 Todos los Sistemas:
```bash
cd yenny
npm run build  # Modo watch (auto-recarga)
# o
npm run build-prod  # Una sola vez, minificado
```

## 🛠️ Comandos Django Frecuentes

### Base de Datos

#### 🐧 Linux / 🍎 macOS:
```bash
cd yenny
source ../venv/bin/activate

# Crear migraciones
python manage.py makemigrations
python manage.py makemigrations [app_name]

# Aplicar migraciones
python manage.py migrate

# Ver estado de migraciones
python manage.py showmigrations

# Crear superusuario
python manage.py createsuperuser
```

#### 🪟 Windows:
```cmd
cd yenny
..\venv\Scripts\activate.bat

# Crear migraciones
python manage.py makemigrations
python manage.py makemigrations [app_name]

# Aplicar migraciones
python manage.py migrate

# Ver estado de migraciones
python manage.py showmigrations

# Crear superusuario
python manage.py createsuperuser
```

### Gestión del Proyecto

#### 🌍 Todos los Sistemas:
```bash
# Recolectar archivos estáticos
python manage.py collectstatic

# Shell de Django
python manage.py shell

# Verificar configuración
python manage.py check
```

## 🔍 Verificación y Diagnóstico

#### 🐧 Linux / 🍎 macOS:
```bash
# Verificar estado completo del proyecto
bash status.sh

# Verificar instalación de Python
python3 --version
pip list

# Verificar Node.js
node --version
npm --version
cd yenny && npm list
```

#### 🪟 Windows:
```cmd
# Verificar estado completo del proyecto
status.bat

# Verificar instalación de Python
python --version
pip list

# Verificar Node.js
node --version
npm --version
cd yenny && npm list
```

## 📁 Estructura de URLs

- **Aplicación Principal:** http://127.0.0.1:8000/
- **Admin Django:** http://127.0.0.1:8000/admin/
- **Autores:** http://127.0.0.1:8000/autores/
- **Categorías:** http://127.0.0.1:8000/categorias/
- **Clientes:** http://127.0.0.1:8000/clientes/
- **Editoriales:** http://127.0.0.1:8000/editoriales/
- **Empleados:** http://127.0.0.1:8000/empleados/
- **Libros:** http://127.0.0.1:8000/libros/
- **Ventas:** http://127.0.0.1:8000/ventas/

## 🗄️ Base de Datos PostgreSQL

### Configuración Inicial
```sql
-- Ejecutar en pgAdmin o psql:
CREATE DATABASE yenny_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE yenny_db TO postgres;
```

### Conexión de Prueba
```bash
# Verificar conexión
psql -h localhost -U postgres -d yenny_db -c "SELECT 1;"
```

## 🔧 Solución de Problemas

### Python 3.14 - Error psycopg2-binary

#### 🐧 Linux / 🍎 macOS:
```bash
# Fix rápido para Python 3.14
bash fix-psycopg.sh

# O manualmente:
source venv/bin/activate
pip uninstall -y psycopg2-binary
pip install "psycopg[binary]==3.2.12"
```

#### 🪟 Windows:
```cmd
# Fix rápido para Python 3.14
fix-psycopg.bat

# O manualmente:
venv\Scripts\activate.bat
pip uninstall -y psycopg2-binary
pip install "psycopg[binary]==3.2.12"
```

### Entorno Virtual

#### 🐧 Linux / 🍎 macOS:
```bash
# Si hay problemas con el entorno virtual:
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 🪟 Windows:
```cmd
# Si hay problemas con el entorno virtual:
rmdir /s /q venv
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Migraciones

#### 🌍 Todos los Sistemas:
```bash
# Si hay conflictos en migraciones:
python manage.py migrate --fake-initial
python manage.py makemigrations
python manage.py migrate
```

### Node.js

#### 🐧 Linux / 🍎 macOS:
```bash
# Si hay problemas con node_modules:
cd yenny
rm -rf node_modules package-lock.json
npm install
npm run build-prod
```

#### 🪟 Windows:
```cmd
# Si hay problemas con node_modules:
cd yenny
rmdir /s /q node_modules
del package-lock.json
npm install
npm run build-prod
```

## 📦 Archivos Importantes

| Archivo | Descripción | Sistema |
|---------|-------------|---------|
| `requirements.txt` | Dependencias Python | Todos |
| `yenny/package.json` | Dependencias Node.js | Todos |
| `yenny/tailwind.config.js` | Configuración Tailwind | Todos |
| `yenny/yenny/settings.py` | Configuración Django | Todos |
| `docs/db/install.sql` | Setup base de datos | Todos |
| **Scripts Unix/Linux/macOS:** |
| `run.sh` | Configuración inicial completa | Unix/Mac |
| `dev.sh` | Script desarrollo | Unix/Mac |
| `setup.sh` | Script configuración inicial | Unix/Mac |
| `status.sh` | Script verificación | Unix/Mac |
| `fix-psycopg.sh` | Fix para Python 3.14 | Unix/Mac |
| **Scripts Windows:** |
| `run.bat` | Configuración inicial completa | Windows |
| `dev.bat` | Script desarrollo | Windows |
| `setup.bat` | Script configuración inicial | Windows |
| `status.bat` | Script verificación | Windows |
| `fix-psycopg.bat` | Fix para Python 3.14 | Windows |

## 🚨 Notas Importantes

1. **Siempre activar el entorno virtual** antes de ejecutar comandos Python
   - Linux/macOS: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate.bat`

2. **Ejecutar migraciones** después de cambios en modelos
   - `python manage.py makemigrations && python manage.py migrate`

3. **Recompilar CSS** después de cambios en estilos
   - `cd yenny && npm run build-prod`

4. **PostgreSQL debe estar ejecutándose** para que la aplicación funcione
   - Verificar conexión: `psql -h localhost -U postgres -d yenny_db -c "SELECT 1;"`

5. **Scripts de diagnóstico** para resolución rápida de problemas:
   - Linux/macOS: `bash status.sh`
   - Windows: `status.bat`

6. **Python 3.14**: Usar los scripts `fix-psycopg` si hay errores de base de datos

7. **Rutas de archivos**: Windows usa `\` en lugar de `/` para separadores de directorio
