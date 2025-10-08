-- Script de creación de la base de datos
-- Run as a superuser

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'dvayms_user') THEN
CREATE ROLE dvayms_user LOGIN PASSWORD 'dvayms_pass';
END IF;
END$$;

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'dvayms_db') THEN
    CREATE DATABASE dvayms_db OWNER dvayms_user ENCODING 'UTF8';
END IF;
END$$;

\connect dvayms_db

GRANT ALL ON SCHEMA public TO dvayms_user;
ALTER ROLE dvayms_user SET search_path TO public;

\du
\l+ dvayms_db
