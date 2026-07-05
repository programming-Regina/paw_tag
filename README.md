# 🐾 PawTag

PawTag es un proyecto educativo que explora el uso de tecnología NFC para la identificación de mascotas.

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



https://github.com/user-attachments/assets/bb936f62-9d6d-4cba-90c0-4b4b5e00ac3a




## Arquitectura

```text
NFC Tag
    ↓
Flask
    ↓
Lógica de negocio
    ↓
MySQL
```

Cada tag NFC se asocia a un registro único en la base de datos.



## Base de datos

El proyecto incluye un script de inicialización:

```text
database/paw_tag.sql
```

Este archivo crea automáticamente:

- La base de datos.
- La tabla principal.
- Los datos necesarios para ejecutar la demostración.



## Datos de prueba

| Tag NFC | Mascota |
|----------|----------|
| 1 | Tina |
| 2 | Batito |

La demostración también utiliza el siguiente tag:

| Tag NFC | Estado |
|----------|----------|
| 999 | Sin registrar |

El tag `999` permite probar el flujo completo de registro de una nueva mascota.



## Consideraciones sobre la demostración

Para simplificar la demostración, esta versión permite editar los datos de una mascota directamente mediante su identificador.

En una implementación productiva, la edición se realizaría mediante un enlace temporal enviado al correo electrónico registrado del propietario. El enlace contendría un token único para evitar modificaciones por parte de terceros.



## Objetivo del proyecto

Proyecto desarrollado con fines educativos para explorar la integración entre tags NFC, aplicaciones web y bases de datos utilizando Python, Flask y MySQL.

No fue concebido como un producto comercial.



## Autor

**Regina Molares**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/regina-molares/)
