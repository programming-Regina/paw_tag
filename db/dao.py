from mysql.connector import Error
from db.connection import conectar_bd, cerrar_bd


# =============================================================================
# OBTENER MASCOTA POR ID
# =============================================================================
def obtener_mascota_por_id(id_mascota):
    """
    PROPÓSITO: Recupera los datos de una mascota a partir de su identificador.
    CODER: Regina

    PARÁMETROS:
        :param id_mascota: Identificador único de la mascota.

    RETORNO:
        :return: Diccionario con los datos de la mascota si existe.
                 None si no se encuentra el registro.

    ERRORES:
        Captura excepciones de tipo mysql.connector.Error.
    """

    conexion = conectar_bd()

    if conexion is None:
        return None

    cursor = None

    try:
        cursor = conexion.cursor(dictionary=True)

        consulta = """
            SELECT
                id,
                nombre_mascota,
                observaciones,
                telefono_contacto,
                email_contacto
            FROM mascotas
            WHERE id = %s
        """

        cursor.execute(consulta, (id_mascota,))
        mascota = cursor.fetchone()

        return mascota

    except Error as e:
        print(f"Error al obtener mascota: {e}")
        return None

    finally:
        if cursor:
            cursor.close()

        cerrar_bd(conexion)



# =============================================================================
# INSERTAR MASCOTA
# =============================================================================
def insertar_mascota(id_tag, nombre_mascota, observaciones, telefono_contacto, email_contacto):
    """
    PROPÓSITO: Inserta una nueva mascota en la base de datos.
    CODER: Regina

    PARÁMETROS:
        :param nombre_mascota: Nombre de la mascota.
        :param observaciones: Rasgos de carácter, medicación u observaciones generales.
        :param telefono_contacto: Número de contacto.
        :param email_contacto: Correo electrónico de contacto.

    RETORNO:
        :return: ID generado para la mascota.
                 None si ocurre un error.

    ERRORES:
        Captura excepciones de tipo mysql.connector.Error.
    """

    conexion = conectar_bd()

    if conexion is None:
        return None

    cursor = None

    try:

        cursor = conexion.cursor()

        consulta = """
            INSERT INTO mascotas
            (
                id,
                nombre_mascota,
                observaciones,
                telefono_contacto,
                email_contacto
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s
            )
        """

        cursor.execute(
            consulta,
            (
                id_tag,
                nombre_mascota,
                observaciones,
                telefono_contacto,
                email_contacto
            )
        )

        conexion.commit()

        return cursor.lastrowid

    except Error as e:
        print(f"Error al insertar mascota: {e}")
        return None

    finally:

        if cursor:
            cursor.close()

        cerrar_bd(conexion)


# =============================================================================
# ACTUALIZAR MASCOTA
# =============================================================================
def actualizar_mascota(
    id_mascota,
    nombre_mascota,
    observaciones,
    telefono_contacto,
    email_contacto
):
    """
    PROPÓSITO: Actualiza los datos de una mascota existente.
    CODER: Regina

    PARÁMETROS:
        :param id_mascota: ID de la mascota.
        :param nombre_mascota: Nombre de la mascota.
        :param observaciones: Observaciones generales.
        :param telefono_contacto: Número de contacto.
        :param email_contacto: Correo electrónico.

    RETORNO:
        :return: True si la actualización fue exitosa.
                 False si ocurrió un error.
    """

    conexion = conectar_bd()

    if conexion is None:
        return False

    cursor = None

    try:

        cursor = conexion.cursor()

        consulta = """
            UPDATE mascotas
            SET
                nombre_mascota = %s,
                observaciones = %s,
                telefono_contacto = %s,
                email_contacto = %s
            WHERE id = %s
        """

        cursor.execute(
            consulta,
            (
                nombre_mascota,
                observaciones,
                telefono_contacto,
                email_contacto,
                id_mascota
            )
        )

        conexion.commit()

        return True

    except Error as e:
        print(f"Error al actualizar mascota: {e}")
        return False

    finally:

        if cursor:
            cursor.close()

        cerrar_bd(conexion)


# =============================================================================
# ELIMINAR MASCOTA
# =============================================================================
def eliminar_mascota_por_id(id_mascota):
    """
    PROPÓSITO: Elimina una mascota de la base de datos.
    CODER: Regina

    PARÁMETROS:
        :param id_mascota: Identificador único de la mascota.

    RETORNO:
        :return: True si la eliminación fue exitosa.
                 False si ocurrió un error.

    ERRORES:
        Captura excepciones de tipo mysql.connector.Error.
    """

    conexion = conectar_bd()

    if conexion is None:
        return False

    cursor = None

    try:

        cursor = conexion.cursor()

        consulta = """
            DELETE FROM mascotas
            WHERE id = %s
        """

        cursor.execute(consulta, (id_mascota,))

        conexion.commit()

        return True

    except Error as e:
        print(f"Error al eliminar mascota: {e}")
        return False

    finally:

        if cursor:
            cursor.close()

        cerrar_bd(conexion)        