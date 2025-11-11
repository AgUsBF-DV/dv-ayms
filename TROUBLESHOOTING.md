# DVAYMS - Solución de Problemas de Instalación

## Problema: Error al instalar psycopg2-binary en Python 3.14

### Error típico:
```
Building wheel for psycopg2-binary (pyproject.toml) ... error
error: subprocess-exited-with-error
× Building wheel for psycopg2-binary (pyproject.toml) did not run successfully.
```

### Causa:
psycopg2-binary no tiene soporte nativo para Python 3.14. Se requiere una versión más nueva del adaptador PostgreSQL.

### Solución 1 (Recomendada): Usar psycopg3
```bash
# Desinstalar psycopg2 si está instalado
pip uninstall psycopg2 psycopg2-binary

# Instalar psycopg3 (compatible con Python 3.14)
pip install "psycopg[binary]==3.2.12"
```

### Solución 2: Usar script de setup específico para Python 3.14
```bash
# En lugar de setup.sh, usar:
bash setup-python314.sh
```

### Solución 3: Downgrade a Python 3.13 (alternativa)
Si prefieres mantener psycopg2:
1. Instalar Python 3.13 desde [python.org](https://python.org)
2. Crear entorno virtual con Python 3.13:
```bash
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Verificación de la instalación

Después de aplicar la solución, verifica que funcione:

```bash
# Activar entorno virtual
source venv/bin/activate

# Probar la conexión PostgreSQL
cd yenny
python manage.py check --database default
```

## Problemas adicionales con Python 3.14

### Problema: Warnings sobre funciones deprecadas
**Síntomas:** Warnings sobre `PyWeakref_GetObject` u otras funciones deprecadas.
**Solución:** Estos son warnings, no errores. El código funciona normalmente.

### Problema: Compilación de otros paquetes
Si otros paquetes fallan al compilar en Python 3.14:
1. Verifica si hay versiones más nuevas disponibles
2. Considera usar Python 3.13 para mayor compatibilidad
3. Instala dependencias de compilación: `brew install postgresql`

## Estado del proyecto con Python 3.14

✅ **Funcional:**
- Django 5.2.6
- psycopg[binary] 3.2.12
- django-compressor 4.5.1
- Tailwind CSS + Flowbite
- Todas las apps de Django

⚠️ **Warnings esperados:**
- Deprecation warnings de psycopg (no afectan funcionalidad)
- Warnings de compilación (normales en versiones beta de Python)

## Contacto

Si el problema persiste:
1. Ejecuta `bash status.sh` para diagnóstico completo
2. Revisa los logs completos de error
3. Considera usar Python 3.13 para máxima compatibilidad
