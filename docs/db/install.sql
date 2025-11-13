-- Ejecutar desde pgAdmin para crear la BD y el usuario
CREATE DATABASE yenny_db;
CREATE USER postgres WITH PASSWORD 'postgres';
ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE yenny_db TO postgres;

-- Requerimiento de psycopg para conectar a PostgreSQL desde Python
-- pip install psycopg[binary]

-- Migraciones iniciales de Django (ejecutar en la terminal)
-- python manage.py makemigrations
-- python manage.py migrate

-- Carga de datos iniciales desde pgAdmin
-- Ejecutar INSERTs listados en test_data.sql
