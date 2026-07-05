# 🐾 PawTag

PawTag es un experimento educativo que explora el uso de tecnología NFC para identificación de mascotas.

El proyecto permite asociar una mascota a un tag NFC físico. Al escanear la chapita con un teléfono móvil:

- Si el tag no está registrado, se muestra un formulario para cargar los datos de la mascota.
- Si el tag ya está registrado, se muestra la información de contacto y observaciones relevantes.

## Tecnologías utilizadas

- Python
- Flask
- MySQL
- HTML
- CSS
- NFC (Near Field Communication)

## Flujo de funcionamiento

1. Escanear una chapita NFC.
2. Abrir la URL asociada al tag.
3. Registrar la mascota (si corresponde).
4. Consultar la información almacenada.
5. Contactar al propietario mediante WhatsApp.

## Video demostración


https://github.com/user-attachments/assets/84ec4441-870d-4377-ab7c-1b8f0da32232


## Arquitectura

PawTag es una aplicación web desarrollada con Python, Flask y MySQL.

```text
NFC Tag
    ↓
Flask
    ↓
Lógica de negocio
    ↓
MySQL
```

La aplicación asocia cada tag NFC con un registro único de la base de datos y permite consultar o registrar información de una mascota mediante un teléfono móvil.



## Base de datos

El proyecto incluye un script de inicialización:

```text
database/paw_tag.sql
```

Este archivo crea automáticamente la base de datos, la tabla principal y los datos necesarios para ejecutar la demostración.



## Datos de prueba

El script SQL incluye dos mascotas de ejemplo:

| Tag NFC | Mascota |
|----------|----------|
| 1 | Tina |
| 2 | Batito |

Además, la demostración utiliza el tag:

| Tag NFC | Estado |
|----------|----------|
| 999 | Sin registrar |

El tag `999` permite probar el flujo completo de alta de una nueva mascota.



## Objetivo del proyecto

PawTag es un proyecto educativo y de experimentación tecnológica.

Fue desarrollado para explorar la integración entre tags NFC, aplicaciones web y bases de datos utilizando Python, Flask y MySQL. No fue concebido como un producto comercial ni se encuentra orientado a su comercialización.

## Autor

**Regina Molares**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/regina-molares/)
