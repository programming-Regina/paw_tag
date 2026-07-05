# 🐾 PawTag

PawTag es un proyecto educativo que explora el uso de tecnología NFC para la identificación de mascotas.

El proyecto permite asociar una mascota a un tag NFC físico. Al escanear la chapita con un teléfono móvil:

- Si el tag no está registrado, se muestra un formulario para cargar los datos de la mascota.
- Si el tag ya está registrado, se muestra la información de contacto y observaciones relevantes.

## Captura de la ficha de mascota
<img width="746" height="1600" alt="screenshot" src="https://github.com/user-attachments/assets/e129bf2c-1475-4a87-b2ab-64f50ad9858b" />


## Demostración en línea

🔗 https://pawtag-production-8fca.up.railway.app

#### Abrir la demostración desde el celular
Escaneá el código QR para acceder directamente a la aplicación:

<img width="400" height="400" alt="QR_PawTag" src="https://github.com/user-attachments/assets/7014d8f1-95cf-4f43-8922-6e5deec4bf88" />


> Esta es una demostración pública. No utilice información personal real al realizar pruebas.


## Video demostración



https://github.com/user-attachments/assets/74479165-9449-4152-9fbf-4d354c4d9324


## Tecnologías utilizadas

- Python
- Flask
- MySQL
- HTML5
- CSS3
- NFC (Near Field Communication)
- Railway (deploy)



## Flujo de funcionamiento

1. Escanear una chapita NFC.
2. Abrir la URL asociada al tag.
3. Registrar la mascota (si corresponde).
4. Consultar la información almacenada.
5. Contactar al propietario utilizando la información registrada.

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

| Tag NFC | Descripción |
|----------|----------|
| 1 | Tina |
| 2 | Batito |
| 999 | Tag sin registrar |

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
