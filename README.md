# Análisis y Metodologías de Sistemas

## Motivación

Este desarrollo es un proyecto académico dentro de la materia **Análisis y Metodologías de Sistemas** de la carrera **Analista de Sistemas** de la **Escuela Da Vinci**.

## Integrantes

- [Beceyro Ferrán Agustín](https://github.com/AgUsBF)
- [Bielaszczuk Cristhian Emmanuel](https://github.com/1337B)

## Objetivo

Desarrollar una aplicación web para gestionar las operaciones de una librería.

## Contexto

### Descripción

Desarrollar un sistema completo para gestionar las existencias y ventas en la librería YENNY. Este sistema permitirá registrar libros con categorías y cantidades disponibles, ajustar precios, ingresar ventas y generar informes de ventas y estadísticas de popularidad.

### Enfoque

El enfoque principal estará en la creación de una interfaz que facilite a los empleados de YENNY registrar y gestionar libros, ajustar precios y procesar ventas de manera eficiente. La plataforma generará informes de ventas diarios y proporcionará estadísticas detalladas sobre la popularidad de los libros.

> [!NOTE]  
> **Alcance:** Se prevé desarrollar una primera versión (MVP) con las funcionalidades básicas y un roadmap para futuras mejoras.

## Tecnologías Utilizadas

- **Lenguaje:** Python 3.8+
- **Framework Backend:** Django 5.2.6
- **Base de Datos:** PostgreSQL
- **Framework Frontend:** Tailwind CSS + Flowbite
- **Gestor de Paquetes:** pip (Python), npm (Node.js)

## Configuración Rápida

### Opción Recomendada - Un Solo Comando

**Linux / macOS:**

```bash
# 1. Clonar y navegar al proyecto
git clone <repository-url>
cd dv-ayms

# 2. Ejecutar configuración automática completa
chmod +x scripts/linux/run.sh   # o scripts/mac/run.sh
bash scripts/linux/run.sh       # o scripts/mac/run.sh
```

**Windows:**

```cmd
# 1. Clonar y navegar al proyecto
git clone <repository-url>
cd dv-ayms

# 2. Ejecutar configuración automática completa
scripts\windows\run.bat
```

Los scripts detectan automáticamente tu versión de Python y configuran todo el entorno.

### Prerrequisitos

- **Python 3.8+** (si usa Python 3.14, consulte la nota de compatibilidad)
- **Node.js 16+** (para compilar Tailwind CSS)
- **PostgreSQL** (para base de datos)

### Documentación Específica

- **Windows:** Consulte [WINDOWS-SETUP.md](WINDOWS-SETUP.md) para guía detallada
- **Linux/macOS:** Consulte [SETUP.md](SETUP.md) para guía detallada
- **Referencia Rápida:** Consulte [QUICK-REFERENCE.md](QUICK-REFERENCE.md) para comandos comunes

## Scripts Disponibles

### Linux/macOS

| Script | Descripción |
|--------|-------------|
| `scripts/linux/run.sh` o `scripts/mac/run.sh` | Configuración inicial completa con servidor |
| `scripts/linux/dev.sh` o `scripts/mac/dev.sh` | Iniciar servidor de desarrollo |
| `scripts/linux/setup.sh` o `scripts/mac/setup.sh` | Configuración inicial sin servidor |
| `scripts/linux/status.sh` o `scripts/mac/status.sh` | Verificar estado del proyecto |
| `scripts/linux/fix-psycopg.sh` o `scripts/mac/fix-psycopg.sh` | Solución para Python 3.14 |
| `scripts/linux/quick-fix.sh` o `scripts/mac/quick-fix.sh` | Solución rápida de problemas |

### Windows

| Script | Descripción |
|--------|-------------|
| `scripts\windows\run.bat` | Configuración inicial completa con servidor |
| `scripts\windows\dev.bat` | Iniciar servidor de desarrollo |
| `scripts\windows\setup.bat` | Configuración inicial sin servidor |
| `scripts\windows\status.bat` | Verificar estado del proyecto |
| `scripts\windows\fix-psycopg.bat` | Solución para Python 3.14 |
| `scripts\windows\quick-fix.bat` | Solución rápida de problemas |

## Estructura del Proyecto

```
dv-ayms/
├── docs/                   # Documentación y scripts de base de datos
│   ├── db/                 # Scripts SQL para PostgreSQL
│   └── img/                # Diagramas y documentación visual
├── scripts/                # Scripts de automatización por plataforma
│   ├── mac/                # Scripts para macOS
│   ├── linux/              # Scripts para Linux
│   ├── windows/            # Scripts para Windows
│   └── requirements.txt    # Dependencias de Python
├── yenny/                  # Aplicación Django principal
│   ├── autores/            # Gestión de autores
│   ├── categorias/         # Gestión de categorías
│   ├── clientes/           # Gestión de clientes
│   ├── editoriales/        # Gestión de editoriales
│   ├── empleados/          # Gestión de empleados (modelo de usuario)
│   ├── libros/             # Gestión de libros
│   ├── reportes/           # Sistema de reportes
│   ├── ventas/             # Gestión de ventas
│   ├── static/             # Archivos estáticos (CSS, JS, imágenes)
│   ├── templates/          # Plantillas HTML
│   └── yenny/              # Configuración del proyecto Django
└── README.md               # Documentación del proyecto
```

## Módulos de la Aplicación

- **Autores:** Gestión de información de autores
- **Categorías:** Clasificación de libros por categorías
- **Clientes:** Registro y gestión de clientes
- **Editoriales:** Información de casas editoriales
- **Empleados:** Sistema de usuarios y autenticación
- **Libros:** Inventario y gestión de libros
- **Reportes:** Sistema de reportes y estadísticas
- **Ventas:** Procesamiento y registro de ventas

## Desarrollo

### Comandos Útiles

```bash
# Verificar estado del proyecto
bash scripts/linux/status.sh    # Linux
bash scripts/mac/status.sh      # macOS
scripts\windows\status.bat      # Windows

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

- **Aplicación:** <http://127.0.0.1:8000/>
- **Admin:** <http://127.0.0.1:8000/admin/>
- **Autores:** <http://127.0.0.1:8000/autores/>
- **Libros:** <http://127.0.0.1:8000/libros/>
- **Clientes:** <http://127.0.0.1:8000/clientes/>
- **Ventas:** <http://127.0.0.1:8000/ventas/>
- **Reportes:** <http://127.0.0.1:8000/reportes/>

## Documentación

- **[SETUP.md](SETUP.md):** Guía completa para Linux/macOS
- **[WINDOWS-SETUP.md](WINDOWS-SETUP.md):** Guía completa para Windows
- **[QUICK-REFERENCE.md](QUICK-REFERENCE.md):** Comandos de referencia rápida
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md):** Solución de problemas comunes
- **[RUNNING_TESTS.md](RUNNING_TESTS.md):** Guía para ejecutar tests
- **[docs/](docs/):** Documentación técnica y diagramas

## Solución de Problemas

### Script de Diagnóstico

```bash
# Linux
bash scripts/linux/status.sh

# macOS
bash scripts/mac/status.sh

# Windows
scripts\windows\status.bat
```

### Scripts de Solución Rápida

```bash
# Linux
bash scripts/linux/quick-fix.sh        # Solución automática de problemas
bash scripts/linux/fix-psycopg.sh      # Solución específica para Python 3.14

# macOS
bash scripts/mac/quick-fix.sh          # Solución automática de problemas
bash scripts/mac/fix-psycopg.sh        # Solución específica para Python 3.14

# Windows
scripts\windows\quick-fix.bat          # Solución automática de problemas
scripts\windows\fix-psycopg.bat        # Solución específica para Python 3.14
```

### Recursos Adicionales

- **Problemas Generales:** Consulte [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Instalación Windows:** Consulte [WINDOWS-SETUP.md](WINDOWS-SETUP.md)
- **Instalación Linux/macOS:** Consulte [SETUP.md](SETUP.md)

## 📄 Licencia

Este proyecto es parte del trabajo académico de la Escuela Da Vinci y se comparte bajo **GNU-GPL V3**.

## 👥 Contribución

Este es un proyecto académico. Para consultas o sugerencias, contactar a los integrantes del equipo.
