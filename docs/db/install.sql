-- Script de creación de la base de datos
-- Run as a superuser

-- Create role if it doesn't exist
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'dvayms_user') THEN
    CREATE ROLE dvayms_user LOGIN PASSWORD 'dvayms_pass';
  END IF;
END$$;

-- Create database (must be outside DO block)
SELECT 'CREATE DATABASE dvayms_db OWNER dvayms_user ENCODING ''UTF8'''
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'dvayms_db')\gexec

-- Connect to the database
\connect dvayms_db

-- Grant permissions
GRANT ALL ON SCHEMA public TO dvayms_user;
ALTER ROLE dvayms_user SET search_path TO public;

-- Show results
\du
\l+ dvayms_db
