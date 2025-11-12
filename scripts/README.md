# Scripts de Configuración DVAYMS

Este directorio contiene scripts de configuración y utilidades para el proyecto DVAYMS, organizados por sistema operativo.

## 📁 Estructura

```
scripts/
├── requirements.txt      # Dependencias Python del proyecto
├── mac/                  # Scripts para macOS
├── linux/                # Scripts para Linux
└── windows/              # Scripts para Windows
```

## 🚀 Uso

**IMPORTANTE**: Todos los scripts deben ejecutarse desde la **RAÍZ** del proyecto, no desde el directorio `scripts/`.

### Para macOS

```bash
# Desde la raíz del proyecto
bash scripts/mac/[nombre-del-script].sh
```

### Para Linux

```bash
# Desde la raíz del proyecto
bash scripts/linux/[nombre-del-script].sh
```

### Para Windows

```cmd
# Desde la raíz del proyecto
scripts\windows\[nombre-del-script].bat
```

## 📜 Scripts Disponibles

### macOS (`scripts/mac/`)

| Script | Descripción | Uso |
|--------|-------------|-----|
| `setup.sh` | Configuración inicial completa del proyecto | `bash scripts/mac/setup.sh` |
| `setup-python314.sh` | Configuración para Python 3.14 específicamente | `bash scripts/mac/setup-python314.sh` |
| `run.sh` | Configuración automática y ejecución one-click | `bash scripts/mac/run.sh` |
| `dev.sh` | Inicio rápido del servidor de desarrollo | `bash scripts/mac/dev.sh` |
| `status.sh` | Verifica el estado del proyecto y dependencias | `bash scripts/mac/status.sh` |
| `fix-psycopg.sh` | Repara problemas con psycopg en Python 3.14 | `bash scripts/mac/fix-psycopg.sh` |
| `quick-fix.sh` | Reparación rápida de problemas comunes | `bash scripts/mac/quick-fix.sh` |

### Linux (`scripts/linux/`)

| Script | Descripción | Uso |
|--------|-------------|-----|
| `setup.sh` | Configuración inicial completa del proyecto | `bash scripts/linux/setup.sh` |
| `setup-python314.sh` | Configuración para Python 3.14 específicamente | `bash scripts/linux/setup-python314.sh` |
| `run.sh` | Configuración automática y ejecución one-click | `bash scripts/linux/run.sh` |
| `dev.sh` | Inicio rápido del servidor de desarrollo | `bash scripts/linux/dev.sh` |
| `status.sh` | Verifica el estado del proyecto y dependencias | `bash scripts/linux/status.sh` |
| `fix-psycopg.sh` | Repara problemas con psycopg en Python 3.14 | `bash scripts/linux/fix-psycopg.sh` |
| `quick-fix.sh` | Reparación rápida de problemas comunes | `bash scripts/linux/quick-fix.sh` |

### Windows (`scripts/windows/`)

| Script | Descripción | Uso |
|--------|-------------|-----|
| `setup.bat` | Configuración inicial completa del proyecto | `scripts\windows\setup.bat` |
| `run.bat` | Configuración automática y ejecución one-click | `scripts\windows\run.bat` |
| `dev.bat` | Inicio rápido del servidor de desarrollo | `scripts\windows\dev.bat` |
| `status.bat` | Verifica el estado del proyecto y dependencias | `scripts\windows\status.bat` |
| `fix-psycopg.bat` | Repara problemas con psycopg en Python 3.14 | `scripts\windows\fix-psycopg.bat` |
| `quick-fix.bat` | Reparación rápida de problemas comunes | `scripts\windows\quick-fix.bat` |

## 🔄 Flujo de Trabajo Recomendado

### Primera Instalación

#### macOS
```bash
# 1. Configuración completa automática (recomendado)
bash scripts/mac/run.sh

# O configuración paso a paso
bash scripts/mac/setup.sh
```

#### Linux
```bash
# 1. Configuración completa automática (recomendado)
bash scripts/linux/run.sh

# O configuración paso a paso
bash scripts/linux/setup.sh
```

#### Windows
```cmd
# 1. Configuración completa automática (recomendado)
scripts\windows\run.bat

# O configuración paso a paso
scripts\windows\setup.bat
```

### Desarrollo Diario

#### macOS
```bash
# Iniciar servidor de desarrollo
bash scripts/mac/dev.sh
```

#### Linux
```bash
# Iniciar servidor de desarrollo
bash scripts/linux/dev.sh
```

#### Windows
```cmd
# Iniciar servidor de desarrollo
scripts\windows\dev.bat
```

### Solución de Problemas

#### macOS
```bash
# Verificar estado del proyecto
bash scripts/mac/status.sh

# Reparación rápida de problemas comunes
bash scripts/mac/quick-fix.sh

# Fix específico para Python 3.14
bash scripts/mac/fix-psycopg.sh
```

#### Linux
```bash
# Verificar estado del proyecto
bash scripts/linux/status.sh

# Reparación rápida de problemas comunes
bash scripts/linux/quick-fix.sh

# Fix específico para Python 3.14
bash scripts/linux/fix-psycopg.sh
```

#### Windows
```cmd
# Verificar estado del proyecto
scripts\windows\status.bat

# Reparación rápida de problemas comunes
scripts\windows\quick-fix.bat

# Fix específico para Python 3.14
scripts\windows\fix-psycopg.bat
```

## ⚙️ Compatibilidad

### Python
- ✅ Python 3.8+
- ✅ Python 3.14 (con manejo automático de psycopg3)

### Sistemas Operativos
- ✅ macOS (scripts/mac/)
- ✅ Linux (scripts/linux/)
- ✅ Windows 10/11 (scripts/windows/)

## 📋 Requisitos Previos

Antes de ejecutar los scripts, asegúrate de tener instalado:

1. **Python 3.8 o superior**
   - macOS/Linux: `python3 --version`
   - Windows: `python --version`

2. **Node.js y npm** (para Tailwind CSS)
   - `node --version`
   - `npm --version`

3. **PostgreSQL** (para la base de datos)
   - Servidor PostgreSQL ejecutándose
   - Cliente psql (opcional pero recomendado)

## 🐛 Solución de Problemas Comunes

### Error: "Este script debe ejecutarse desde la raíz del proyecto"
**Solución**: Navega a la raíz del proyecto antes de ejecutar el script:
```bash
# macOS
cd /ruta/al/proyecto/dv-ayms
bash scripts/mac/[script].sh

# Linux
cd /ruta/al/proyecto/dv-ayms
bash scripts/linux/[script].sh

# Windows
cd C:\ruta\al\proyecto\dv-ayms
scripts\windows\[script].bat
```

### Error: "No se encontró el entorno virtual"
**Solución**: Ejecuta primero el script de configuración:
```bash
# macOS
bash scripts/mac/setup.sh

# Linux
bash scripts/linux/setup.sh

# Windows
scripts\windows\setup.bat
```

### Problemas con psycopg en Python 3.14
**Solución**: Usa el script de reparación específico:
```bash
# macOS
bash scripts/mac/fix-psycopg.sh

# Linux
bash scripts/linux/fix-psycopg.sh

# Windows
scripts\windows\fix-psycopg.bat
```

## 📝 Notas

- Todos los scripts están en **español** para facilitar su uso
- Los scripts de Windows usan separadores de ruta `\` (backslash)
- Los scripts de macOS/Linux usan separadores de ruta `/` (forward slash)
- La ruta a `requirements.txt` es relativa: `scripts/requirements.txt` o `scripts\requirements.txt`
- macOS y Linux comparten la misma sintaxis bash, pero están separados para mejor organización

## 🆘 Soporte

Si encuentras problemas:

1. Ejecuta el script de status para diagnosticar:
   - macOS: `bash scripts/mac/status.sh`
   - Linux: `bash scripts/linux/status.sh`
   - Windows: `scripts\windows\status.bat`

2. Intenta el quick-fix:
   - macOS: `bash scripts/mac/quick-fix.sh`
   - Linux: `bash scripts/linux/quick-fix.sh`
   - Windows: `scripts\windows\quick-fix.bat`

3. Consulta la documentación en la raíz del proyecto:
   - `SETUP.md` - Guía de configuración
   - `TROUBLESHOOTING.md` - Solución de problemas
   - `README.md` - Información general del proyecto
