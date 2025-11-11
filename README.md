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

- ☕ **Lenguaje:** Python 3.8+
- 💻 **Framework Backend:** Django 5.2.6
- 🗃️ **Base de Datos:** PostgreSQL
- 🎨 **Framework Frontend:** Tailwind CSS + Flowbite
- 📦 **Gestor de Paquetes:** pip (Python), npm (Node.js)

## 🚀 Configuración Rápida

### ⚡ Un Solo Comando (Recomendado)

#### **🐧 Linux / 🍎 macOS:**
```bash
# 1. Clonar y navegar al proyecto
git clone <repository-url>
cd dvayms

# 2. Ejecutar configuración automática completa
chmod +x run.sh && ./run.sh
```

#### **🪟 Windows:**
```bash
# 1. Clonar y navegar al proyecto
git clone <repository-url>
cd dvayms

# 2. Ejecutar configuración automática completa
run.bat
```

**¡Eso es todo!** Los scripts detectan tu versión de Python automáticamente y configuran todo.

### 📋 Prerrequisitos
- **Python 3.8+** (⚠️ Si usas Python 3.14, ver nota de compatibilidad abajo)
- **Node.js 16+** (para compilar Tailwind CSS)
- **PostgreSQL** (para base de datos)

### 🗒️ Documentación Específica
- **🪟 Windows:** Ver [WINDOWS-SETUP.md](WINDOWS-SETUP.md) para guía detallada
- **🐧 Linux/macOS:** Ver [SETUP.md](SETUP.md) para guía detallada
- **⚡ Referencia Rápida:** Ver [QUICK-REFERENCE.md](QUICK-REFERENCE.md) para comandos comunes

## 📋 Scripts Disponibles

### **🐧 Linux/macOS:**
| Script | Descripción |
|--------|-------------|
| `run.sh` | Configuración inicial completa con servidor |
| `dev.sh` | Iniciar servidor de desarrollo |
| `setup.sh` | Configuración inicial sin servidor |
| `status.sh` | Verificar estado del proyecto |
| `fix-psycopg.sh` | Fix para Python 3.14 |
| `quick-fix.sh` | Solución rápida de problemas |

### **🪟 Windows:**
| Script | Descripción |
|--------|-------------|
| `run.bat` | Configuración inicial completa con servidor |
| `dev.bat` | Iniciar servidor de desarrollo |
| `setup.bat` | Configuración inicial sin servidor |
| `status.bat` | Verificar estado del proyecto |
| `fix-psycopg.bat` | Fix para Python 3.14 |
| `quick-fix.bat` | Solución rápida de problemas |

## 🏗️ Estructura del Proyecto

```
dvayms/
├── docs/              # Documentación y scripts de base de datos
│   ├── db/           # Scripts SQL para PostgreSQL
│   └── img/          # Diagramas y documentación visual
├── yenny/            # Aplicación Django principal
│   ├── autores/      # Gestión de autores
│   ├── categorias/   # Gestión de categorías
│   ├── clientes/     # Gestión de clientes
│   ├── editoriales/  # Gestión de editoriales
│   ├── empleados/    # Gestión de empleados (modelo de usuario)
│   ├── libros/       # Gestión de libros
│   ├── ventas/       # Gestión de ventas
│   ├── static/       # Archivos estáticos (CSS, JS, imágenes)
│   ├── templates/    # Plantillas HTML
│   └── yenny/        # Configuración del proyecto Django
├── requirements.txt  # Dependencias de Python
├── setup.sh         # Script de configuración
├── dev.sh           # Script de desarrollo
├── status.sh        # Script de verificación
└── SETUP.md         # Guía detallada de instalación
```

## 🌐 Módulos de la Aplicación

- **Autores** - Gestión de información de autores
- **Categorías** - Clasificación de libros por categorías
- **Clientes** - Registro y gestión de clientes
- **Editoriales** - Información de casas editoriales
- **Empleados** - Sistema de usuarios y autenticación
- **Libros** - Inventario y gestión de libros
- **Ventas** - Procesamiento y registro de ventas

## 🔧 Desarrollo

### Comandos Útiles
```bash
# Verificar estado del proyecto
./status.sh    # Linux/macOS
status.bat     # Windows

# Crear y aplicar migraciones
cd yenny
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Recompilar CSS
npm run build        # Desarrollo
npm run build-prod   # Producción
```

### URLs Principales
- **🏠 Aplicación:** http://127.0.0.1:8000/
- **⚙️ Admin:** http://127.0.0.1:8000/admin/
- **📚 Autores:** http://127.0.0.1:8000/autores/
- **📖 Libros:** http://127.0.0.1:8000/libros/
- **👥 Clientes:** http://127.0.0.1:8000/clientes/
- **💰 Ventas:** http://127.0.0.1:8000/ventas/

## 💼 Documentación

- **[SETUP.md](SETUP.md)** - Guía completa para Linux/macOS
- **[WINDOWS-SETUP.md](WINDOWS-SETUP.md)** - Guía completa para Windows
- **[QUICK-REFERENCE.md](QUICK-REFERENCE.md)** - Comandos de referencia rápida
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Solución de problemas comunes
- **[docs/](docs/)** - Documentación técnica y diagramas

## 🔍 Solución de Problemas

### Script de Diagnóstico
```bash
# Linux/macOS
./status.sh

# Windows
status.bat
```

### Scripts de Solución Rápida
```bash
# Linux/macOS
./quick-fix.sh        # Solución automática de problemas
./fix-psycopg.sh      # Fix específico para Python 3.14

# Windows
quick-fix.bat         # Solución automática de problemas
fix-psycopg.bat       # Fix específico para Python 3.14
```

### Para Más Ayuda
- **Problemas Generales:** Ver [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Instalación Windows:** Ver [WINDOWS-SETUP.md](WINDOWS-SETUP.md)
- **Instalación Linux/macOS:** Ver [SETUP.md](SETUP.md)

## 📄 Licencia

Este proyecto es parte del trabajo académico de la Escuela Da Vinci y se comparte bajo **GNU-GPL V3**.

## 👥 Contribución

Este es un proyecto académico. Para consultas o sugerencias, contactar a los integrantes del equipo.

