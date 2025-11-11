# 🪟 **DVAYMS - Guía para Windows**

## 🚀 **Instalación Rápida en Windows**

### **📋 Prerrequisitos**
- ✅ **Python 3.8+** ([Descargar](https://www.python.org/downloads/windows/))
- ✅ **Node.js 16+** ([Descargar](https://nodejs.org/en/download/))
- ✅ **PostgreSQL** ([Descargar](https://www.postgresql.org/download/windows/))
- ✅ **Git** ([Descargar](https://git-scm.com/download/win))

### **⚡ Configuración Automática**

### **⚡ Configuración Automática**

#### **Orden de Ejecución para Windows:**

##### **1. 🚀 Setup Inicial Completo**
```cmd
run.bat
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
```cmd
# Verificar estado del proyecto
status.bat

# Si hay problemas específicos de Python 3.14
fix-psycopg.bat

# Para solución rápida de problemas comunes
quick-fix.bat

# Si todo falla, configuración manual paso a paso
setup.bat
```

##### **2. 💻 Desarrollo Diario (después del setup inicial)**
```cmd
dev.bat
```
**Resultado Esperado:**
- ✅ Entorno virtual activado automáticamente
- ✅ Migraciones verificadas y aplicadas si es necesario
- ✅ Frontend compilado si hay cambios
- ✅ Servidor iniciado en modo desarrollo

**Si Falla:**
```cmd
# Diagnóstico completo
status.bat

# Fix rápido de problemas comunes
quick-fix.bat
```

#### **Scripts de Soporte (usar cuando sea necesario):**

##### **3. 🔧 Verificación de Estado**
```cmd
status.bat
```
**Cuándo Usar:** Para diagnosticar problemas o verificar configuración
**Resultado Esperado:**
- ✅ Reporte completo del estado del proyecto
- ✅ Verificación de Python, Node.js, PostgreSQL
- ✅ Estado de entorno virtual y dependencias
- ✅ Verificación de base de datos

##### **4. 🛠️ Fix para Python 3.14**
```cmd
fix-psycopg.bat
```
**Cuándo Usar:** Si usas Python 3.14 y hay errores de psycopg2
**Resultado Esperado:**
- ✅ psycopg2-binary desinstalado
- ✅ psycopg3 instalado y configurado
- ✅ Compatibilidad con Python 3.14 restaurada

##### **5. ⚡ Fix Rápido General**
```cmd
quick-fix.bat
```
**Cuándo Usar:** Para solucionar problemas comunes automáticamente
**Resultado Esperado:**
- ✅ Problemas de entorno virtual solucionados
- ✅ Dependencias faltantes instaladas
- ✅ Migraciones aplicadas
- ✅ Frontend recompilado si es necesario

##### **6. ⚙️ Setup Manual (solo si scripts automáticos fallan)**
```cmd
setup.bat
```
**Cuándo Usar:** Si `run.bat` falla o necesitas configuración sin servidor
**Resultado Esperado:**
- ✅ Mismo resultado que `run.bat` pero sin iniciar servidor automáticamente

**¡Eso es todo!** 🎉

---

## 🔧 **Archivos de Windows Incluidos**

### **📜 Scripts Principales**

#### **`run.bat` - Setup Completo**
- ✅ Crea entorno virtual
- ✅ Instala dependencias Python (con auto-detección Python 3.14)
- ✅ Instala dependencias Node.js
- ✅ Configura base de datos
- ✅ Ejecuta migraciones
- ✅ Crea usuario admin
- ✅ Inicia servidor (opcional)

#### **`dev.bat` - Desarrollo Diario**
- ✅ Activa entorno virtual
- ✅ Verifica migraciones
- ✅ Compila frontend si es necesario
- ✅ Inicia servidor de desarrollo

### **📜 Scripts de Soporte**

#### **`setup.bat` - Setup Sin Servidor**
- ✅ Configuración inicial completa
- ✅ Sin inicio automático de servidor
- ✅ Ideal para configuración en servidores

#### **`status.bat` - Diagnóstico**
- ✅ Verificación completa del proyecto
- ✅ Reporte de estado de dependencias
- ✅ Diagnóstico de problemas comunes

#### **`fix-psycopg.bat` - Fix Python 3.14**
- ✅ Soluciona problemas específicos de Python 3.14
- ✅ Reemplaza psycopg2 por psycopg3
- ✅ Verificación automática de compatibilidad

#### **`quick-fix.bat` - Solución Rápida**
- ✅ Auto-detecta y repara problemas comunes
- ✅ Reinstala dependencias si es necesario
- ✅ Aplica migraciones pendientes
- ✅ Recompila frontend

---

## 🆚 **Diferencias vs Unix/Linux**

| **Aspecto** | **Unix/Linux** | **Windows** |
|-------------|----------------|-------------|
| **Setup** | `./run.sh` | `run.bat` |
| **Desarrollo** | `./dev.sh` | `dev.bat` |
| **Entorno Virtual** | `source venv/bin/activate` | `venv\Scripts\activate.bat` |
| **Comandos** | Bash sintaxis | Batch sintaxis |

---

## 🐛 **Solución de Problemas Comunes en Windows**


### **🚨 Matriz de Problemas y Soluciones**

| **Problema** | **Síntoma** | **Solución** | **Script** |
|-------------|-------------|-------------|------------|
| **Python 3.14** | Error psycopg2-binary | Incompatibilidad conocida | `fix-psycopg.bat` |
| **Entorno Virtual** | CommandNotFound | Entorno no activado | `venv\Scripts\activate.bat` |
| **Dependencias** | ModuleNotFoundError | Dependencias no instaladas | `quick-fix.bat` |
| **Base de Datos** | Connection refused | PostgreSQL no ejecutándose | Iniciar PostgreSQL |
| **Frontend** | CSS no carga | Assets no compilados | `cd yenny && npm run build` |
| **Migraciones** | No such table | Migraciones no aplicadas | `quick-fix.bat` |
| **Node.js** | npm command not found | Node.js no instalado | Instalar Node.js |
| **Python PATH** | python no reconocido | Python no en PATH | Reinstalar Python con PATH |

### **🔍 Diagnóstico Paso a Paso**

#### **1. Verificar Estado General**
```cmd
status.bat
```
Este script te dará un reporte completo de qué está funcionando y qué no.

#### **2. Problemas de Conexión a Base de Datos**
```cmd
# Verificar si PostgreSQL está ejecutándose (Windows Services)
sc query postgresql-x64-14  # Ajustar versión según instalación

# Verificar conexión
psql -h localhost -U postgres -d yenny_db -c "SELECT 1;"
```

#### **3. Problemas de Migración**
```cmd
cd yenny
..\venv\Scripts\activate.bat

# Verificar estado de migraciones
python manage.py showmigrations

# Resetear migraciones si es necesario (¡CUIDADO! Perdirás datos)
python manage.py migrate --fake-initial

# Crear y aplicar nuevas migraciones
python manage.py makemigrations
python manage.py migrate
```

#### **4. Problemas con Archivos Estáticos/Frontend**
```cmd
cd yenny

# Verificar dependencias Node.js
npm list

# Reinstalar si es necesario
rmdir /s /q node_modules
del package-lock.json
npm install

# Recompilar CSS
npm run build-prod

# Para Django
python manage.py collectstatic
```

### **🚨 Problemas Específicos de Windows**

### **❌ "python no es reconocido como comando"**
**Solución:**
1. Reinstala Python marcando "Add Python to PATH"
2. O agrega manualmente Python al PATH del sistema
3. Reinicia Command Prompt después del cambio

### **❌ "npm no es reconocido como comando"**
**Solución:**
1. Reinstala Node.js desde [nodejs.org](https://nodejs.org)
2. Reinicia el terminal/Command Prompt
3. Verifica con: `node --version && npm --version`

### **❌ "psql no es reconocido como comando"**
**Solución:**
1. Agrega PostgreSQL bin al PATH: `C:\Program Files\PostgreSQL\[version]\bin`
2. O usa pgAdmin para crear la base de datos
3. Reinicia Command Prompt después del cambio

### **❌ Error de permisos al instalar paquetes**
**Solución:**
1. Ejecuta Command Prompt como Administrador
2. O usa: `pip install --user [package]`
3. Verifica permisos en la carpeta del proyecto

### **❌ Error con psycopg en Python 3.14**
**✅ Auto-solucionado:** 
```cmd
fix-psycopg.bat
```
Los scripts detectan Python 3.14 y usan psycopg3 automáticamente

### **❌ Entorno virtual no se activa**
**Solución:**
```cmd
# Recrear entorno virtual
rmdir /s /q venv
python -m venv venv
venv\Scripts\activate.bat
```

### **❌ Scripts .bat no se ejecutan**
**Solución:**
1. Abre Command Prompt (no PowerShell)
2. Navega al directorio del proyecto: `cd C:\path\to\dvayms`
3. Ejecuta directamente: `run.bat`

---

## 💻 **Comandos Manuales (si prefieres control total)**

### **📋 Si Fallan Todos los Scripts Automáticos:**

#### **Paso 1: Clonar Repositorio**
```cmd
git clone <repo-url>
cd dvayms
```

#### **Paso 2: Configuración Manual Completa**
```cmd
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual
venv\Scripts\activate.bat

# 3. Verificar que el entorno está activo
echo %VIRTUAL_ENV%

# 4. Actualizar pip
python -m pip install --upgrade pip

# 5. Instalar dependencias Python
# Para Python 3.14:
python -m pip install Django==5.2.6
python -m pip install "psycopg[binary]==3.2.12"
python -m pip install django-compressor==4.5.1

# Para otras versiones:
# python -m pip install -r requirements.txt

# 6. Verificar instalación Python
python -c "import django; print('Django OK')"
python -c "import psycopg; print('psycopg OK')"  # Para Python 3.14
# python -c "import psycopg2; print('psycopg2 OK')"  # Para otras versiones
```

#### **Paso 3: Configuración Frontend**
```cmd
# 7. Instalar frontend
cd yenny
npm install

# 8. Verificar instalación Node.js
npm list --depth=0

# 9. Compilar CSS
npm run build-prod

# 10. Verificar compilación
dir static\CACHE
```

#### **Paso 4: Configuración Django**
```cmd
# 11. Configurar Django (desde directorio yenny)
python manage.py check

# 12. Crear migraciones
python manage.py makemigrations

# 13. Aplicar migraciones
python manage.py migrate

# 14. Crear superusuario
python manage.py createsuperuser

# 15. Verificar configuración final
python manage.py check --deploy
```

#### **Paso 5: Iniciar Servidor**
```cmd
# 16. Iniciar servidor de desarrollo
python manage.py runserver

# El servidor estará disponible en: http://127.0.0.1:8000/
```

### **Desarrollo Diario Manual:**
```cmd
# 1. Activar entorno
venv\Scripts\activate.bat

# 2. Ir a proyecto Django
cd yenny

# 3. Verificar migraciones pendientes (opcional)
python manage.py showmigrations | findstr "[ ]"

# 4. Aplicar migraciones si hay pendientes
python manage.py migrate

# 5. Iniciar servidor
python manage.py runserver
```

---

## 🌐 **URLs Importantes**

Una vez iniciado el servidor:

- **🏠 Aplicación Principal:** http://127.0.0.1:8000/
- **⚙️ Panel de Admin:** http://127.0.0.1:8000/admin/
- **📚 Autores:** http://127.0.0.1:8000/autores/
- **📖 Libros:** http://127.0.0.1:8000/libros/
- **👥 Clientes:** http://127.0.0.1:8000/clientes/
- **💰 Ventas:** http://127.0.0.1:8000/ventas/

### **🔑 Credenciales por Defecto:**
- **Usuario:** `admin`
- **Contraseña:** `admin`

---

## 🎯 **Recomendaciones para Windows**

### **🔧 IDEs Recomendados:**
- **Visual Studio Code** + extensión Python
- **PyCharm Community Edition**
- **Sublime Text** + plugins Python

### **🐚 Terminales Recomendados:**
- **Windows Terminal** (moderno y potente)
- **PowerShell 7**
- **Git Bash** (incluido con Git)

### **🗄️ PostgreSQL en Windows:**
- **pgAdmin** para gestión visual
- **DBeaver** como alternativa universal
- **Command line:** `psql` después de agregar al PATH

---

## ✨ **Características del Sistema**

- ✅ **Gestión de Libros** con múltiples autores
- ✅ **Sistema de Ventas** completo con stock automático
- ✅ **Filtros Avanzados** en todas las secciones
- ✅ **Interfaz Responsive** con Tailwind CSS
- ✅ **Dark Mode** incluido
- ✅ **Gestión de Inventario** automática
- ✅ **Reportes de Ventas** con filtros por fecha

---

## 🚀 **¡Listo para Desarrollar!**

### **📋 Flujo de Trabajo Recomendado**

#### **🔄 Configuración Inicial (Solo Una Vez)**
```cmd
# 1. Clonar proyecto
git clone <repo-url>
cd dvayms

# 2. Setup completo automático
run.bat
```

#### **💻 Desarrollo Diario**
```cmd
# Cada día de trabajo
dev.bat
```

#### **🔧 Si Hay Problemas**
```cmd
# Diagnóstico
status.bat

# Fix automático
quick-fix.bat

# Fix específico Python 3.14
fix-psycopg.bat
```

### **📊 Verificación de Éxito**

Después de ejecutar `run.bat` o `dev.bat`, deberías ver:

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

**Para desarrollo diario, simplemente ejecuta:** `dev.bat`
