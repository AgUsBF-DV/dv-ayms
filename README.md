# Análisis y Metodologías de Sistemas

## 💡 Motivación

Este desarrollo es un proyecto académico dentro de la materia **Análisis y Metodologías de Sistemas** de la carrera **Analista de Sistemas** de la **Escuela Da Vinci**.

## 🎯 Objetivo

Desarrollar una aplicación web para gestionar las operaciones de una librería.

## 🔍 Contexto

### Descripción

Desarrollar un sistema completo para gestionar las existencias y ventas en la librería YENNY. Este sistema permitirá registrar libros con categorías y cantidades disponibles, ajustar precios, ingresar ventas y generar informes de ventas y estadísticas de popularidad.

### Enfoque

El enfoque principal estará en la creación de una interfaz que facilite a los empleados de YENNY registrar y gestionar libros, ajustar precios y procesar ventas de manera eficiente. La plataforma generará informes de ventas diarios y proporcionará estadísticas detalladas sobre la popularidad de los libros.

## 🛠️ Tecnologías Utilizadas

- ☕ **Lenguaje:** Python
- 💻 **Framework:**
- 🔗 **Conectividad:**
- 🗃️ **Base de Datos:**

## 📱 Funcionalidades

- 📦 **ABM de libros, autores, marcas y categorias**
- 👥 **ABM de empleados**
- 🛒 **Gestión de ventas**
- 📋 **Reportes de Ventas**

## 🗂️ Estructura del Proyecto

```bash
dv-ayms
├── docs
│   ├── db
│   │   ├── install.sql
│   │   └── test_data.sql
│   └── manual.md
├── LICENSE
├── README.md
└── src
    ├── model
    │   ├── Autor.py
    │   ├── Categoria.py
    │   ├── Cliente.py
    │   ├── Editorial.py
    │   ├── Empleado.py
    │   ├── Libro.py
    │   ├── Rol.py
    │   ├── VentaLibro.py
    │   └── Venta.py
    └── test.py
```

## 💼 Documentación

La documentación de la aplicación se puede encontrar [aquí](./docs/manual.md).

## 📸 Vistas

## 📄 Licencia

Este proyecto es parte del trabajo académico de la Escuela Da Vinci y se comparte bajo **GNU-GPL V3**.
