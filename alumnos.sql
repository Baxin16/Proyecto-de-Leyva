-- ==========================================
-- PROYECTO FINAL
-- Kevin Eduardo Baxin
-- Base de Datos: escuela
-- ==========================================

CREATE DATABASE IF NOT EXISTS escuela;
USE escuela;

DROP TABLE IF EXISTS alumnos;
DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios(
id INT AUTO_INCREMENT PRIMARY KEY,
usuario VARCHAR(50) UNIQUE NOT NULL,
password VARCHAR(255) NOT NULL
);

CREATE TABLE alumnos(
matricula VARCHAR(15) PRIMARY KEY,
apellido_paterno VARCHAR(50) NOT NULL,
apellido_materno VARCHAR(50) NOT NULL,
nombres VARCHAR(100) NOT NULL,
curp VARCHAR(18) NOT NULL,
especialidad VARCHAR(100) NOT NULL,
telefono VARCHAR(10) NOT NULL,
ciudad_origen VARCHAR(100) NOT NULL,
estado VARCHAR(100) NOT NULL,
disciplina VARCHAR(100) NOT NULL,
foto VARCHAR(255)
);

-- El usuario Baxin se agregará después,
-- cuando generemos el hash bcrypt.
