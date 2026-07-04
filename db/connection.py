# correr en consola "python -m pip install mysql-connector-python"
import os
import mysql.connector
from mysql.connector import Error 
from config import (
    DB_HOST,
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
    DB_PORT
)

# =============================================================================
# CONEXION CON LA BD
# =============================================================================
def conectar_bd():
    """
    PROPÓSITO: Establece y gestiona la conexión inicial con el motor de base de datos local.
    CODER: Regina
    PARÁMETROS: 
        Ninguno. Usa constantes locales para los parámetros de XAMPP (Puerto 3306).
    RETORNO:     
        :return: Objeto mysql.connector.connection si el enlace es exitoso, o None si falla.
    ERRORES: Captura excepciones de tipo mysql.connector.Error para evitar caídas del sistema.
    """
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT,
            charset="utf8mb4"
        )
        
        if conexion.is_connected():
            return conexion

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    


def cerrar_bd(conexion):
    if conexion and conexion.is_connected():
        conexion.close()

    
# Cómo usar en las funciones:
# conn = conectar_bd()
# if conn:
#     print("Conexión establecida con éxito.")
#     conn.close()