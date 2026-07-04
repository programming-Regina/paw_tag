from db.dao import (
    obtener_mascota_por_id,
    insertar_mascota,
    actualizar_mascota,
    eliminar_mascota_por_id
)
from utils.helpers import (    
    limpiar_observaciones,
    limpiar_telefono,
    limpiar_email,
    email_valido,
    telefono_valido
)


# =============================================================================
# BUSCAR MASCOTA
# =============================================================================
def buscar_mascota(id_mascota):
    """
    PROPÓSITO: Gestiona la búsqueda de una mascota por identificador.

    PARÁMETROS:
        :param id_mascota: Identador de la mascota.

    RETORNO:
        :return: Diccionario con los datos de la mascota.
                 None si no existe.

    OBSERVACIONES:
        Esta capa permite incorporar futuras reglas de negocio sin modificar
        la capa de acceso a datos.
    """

    return obtener_mascota_por_id(id_mascota)



# =============================================================================
# REGISTRAR MASCOTA
# =============================================================================
def registrar_mascota(
    id_tag,
    nombre_mascota,
    observaciones,
    telefono_contacto,
    email_contacto
):
    """
    PROPÓSITO: Gestiona el alta de una nueva mascota.

    PARÁMETROS:
        :param id_tag: ID del tag NFC.
        :param nombre_mascota: Nombre de la mascota.
        :param observaciones: Observaciones generales.
        :param telefono_contacto: Número de contacto.
        :param email_contacto: Correo electrónico de contacto.

    RETORNO:
        :return: ID generado para la mascota.
                 None si ocurre un error.
    """

    observaciones = limpiar_observaciones(observaciones)
    telefono_contacto = limpiar_telefono(telefono_contacto)
    email_contacto = limpiar_email(email_contacto)

    if not email_valido(email_contacto):
        raise ValueError("Email inválido")

    if not telefono_valido(telefono_contacto):
        raise ValueError("Teléfono inválido")

    return insertar_mascota(
        id_tag,
        nombre_mascota,
        observaciones,
        telefono_contacto,
        email_contacto
    )


# =============================================================================
# ACTUALIZAR MASCOTA
# =============================================================================
def actualizar_datos_mascota(
    id_mascota,
    nombre_mascota,
    observaciones,
    telefono_contacto,
    email_contacto
):
    """
    PROPÓSITO: Gestiona la actualización de una mascota existente.

    PARÁMETROS:
        :param id_mascota: ID de la mascota.
        :param nombre_mascota: Nombre de la mascota.
        :param observaciones: Observaciones generales.
        :param telefono_contacto: Número de contacto.
        :param email_contacto: Correo electrónico.

    RETORNO:
        :return: True si la actualización fue exitosa.
                 False en caso contrario.
    """
  
    observaciones = limpiar_observaciones(observaciones)
    telefono_contacto = limpiar_telefono(telefono_contacto)
    email_contacto = limpiar_email(email_contacto)

    if not email_valido(email_contacto):
        raise ValueError("Email inválido")

    if not telefono_valido(telefono_contacto):
        raise ValueError("Teléfono inválido")
    

    return actualizar_mascota(
        id_mascota,
        nombre_mascota,
        observaciones,
        telefono_contacto,
        email_contacto
    )


# =============================================================================
# ELIMINAR MASCOTA
# =============================================================================
def eliminar_mascota(id_mascota):
    """
    PROPÓSITO: Gestiona la eliminación de una mascota.

    PARÁMETROS:
        :param id_mascota: ID de la mascota.

    RETORNO:
        :return: True si la eliminación fue exitosa.
                 False en caso contrario.
    """

    return eliminar_mascota_por_id(id_mascota)