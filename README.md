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

Los scripts detectan tu versión de Python automáticamente y configuran todo.

### 📋 Prerrequisitos
- **Python 3.8+** (⚠️ Si usas Python 3.14, ver nota de compatibilidad abajo)
- **Node.js 16+** (para compilar Tailwind CSS)
- **PostgreSQL** (para base de datos)

### 🗒️ Documentación Específica
- **🪟 Windows:** Ver `WINDOWS-SETUP.md` para guía detallada
- **🐧 Linux/macOS:** Los scripts `.sh` funcionan directamente
- PostgreSQL
- Node.js & npm

### Instalación Automática

#### Python 3.8-3.13:
```bash
# 1. Clonar el repositorio
git clone <repository-url>
cd dvayms

# 2. Ejecutar script de configuración automática
bash setup.sh

# 3. Iniciar servidor de desarrollo
bash dev.sh
```

#### Python 3.14 (Compatibilidad):
```bash
# 1. Clonar el repositorio
git clone <repository-url>
cd dvayms

# 2. Ejecutar script compatible con Python 3.14
bash setup-python314.sh

# 3. Iniciar servidor de desarrollo
bash dev.sh
```

### Instalación Manual
Ver [SETUP.md](SETUP.md) para instrucciones detalladas paso a paso.

## 📋 Scripts Disponibles

| Script | Descripción |
|--------|-------------|
| `setup.sh` | Configuración inicial completa del proyecto |
| `dev.sh` | Inicia el servidor de desarrollo |
| `status.sh` | Verifica el estado de la configuración del proyecto |

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
bash status.sh

# Crear migraciones
cd yenny && python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Recompilar CSS (modo desarrollo)
npm run build

# Recompilar CSS (modo producción)
npm run build-prod
```

### URLs Principales
- **Aplicación:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/
- **API Endpoints:** Según configuración en `urls.py` de cada módulo

## 💼 Documentación

La documentación completa de la aplicación se puede encontrar en:
- [SETUP.md](SETUP.md) - Guía de instalación detallada
- [docs/](docs/) - Documentación técnica y diagramas
- [GitHub Wiki](https://github.com/AgUsBF-DV/dv-ayms/wiki) - Wiki del repositorio

## 🔍 Solución de Problemas

### Problemas Comunes
1. **Error de conexión a base de datos**: Verificar que PostgreSQL esté ejecutándose y la base de datos `yenny_db` exista
2. **Migraciones pendientes**: Ejecutar `python manage.py migrate`
3. **CSS no se actualiza**: Ejecutar `npm run build` para recompilar Tailwind
4. **Módulos no encontrados**: Verificar que el entorno virtual esté activado

### Verificación de Estado
```bash
# Ejecutar diagnóstico completo
bash status.sh
```

## 📄 Licencia

Este proyecto es parte del trabajo académico de la Escuela Da Vinci y se comparte bajo **GNU-GPL V3**.

## 👥 Contribución

Este es un proyecto académico. Para consultas o sugerencias, contactar a los integrantes del equipo.

