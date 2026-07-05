-- =============================================================================
-- PawTag
-- Base de datos de demostración
--
-- Este script crea la estructura necesaria para ejecutar el proyecto
-- e incluye datos de ejemplo utilizados por la demostración NFC.
-- =============================================================================

CREATE DATABASE IF NOT EXISTS paw_tag
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE paw_tag;

-- =============================================================================
-- TABLA: mascotas
--
-- El campo id corresponde al identificador utilizado por el tag NFC.
-- No es autoincremental.
-- =============================================================================

CREATE TABLE mascotas (
    id INT UNSIGNED NOT NULL,
    nombre_mascota VARCHAR(100) NOT NULL,
    observaciones TEXT NOT NULL,
    telefono_contacto VARCHAR(30) NOT NULL,
    email_contacto VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

-- =============================================================================
-- DATOS DE DEMOSTRACIÓN
--
-- Tag 1: Tina
-- Tag 2: Batito
--
-- El tag 999 se utiliza para demostrar el flujo de registro de una
-- nueva mascota y NO debe existir en la base inicialmente.
-- =============================================================================

INSERT INTO mascotas (
    id,
    nombre_mascota,
    observaciones,
    telefono_contacto,
    email_contacto
)
VALUES
(
    1,
    '🐶 Tina 🐶',
    'Castrada. Mansa pero asustadiza. Toma Levotiroxina 0.4 mg al día.',
    '12345678',
    'tina@example.com'
),
(
    2,
    'Batito',
    'Castrado. Hace pis en las piedritas pero hace 💩 fuera de la bandeja sanitaria. Es manso, cariñoso y sociable.',
    '23456789',
    'batito@example.com'
);