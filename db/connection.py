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

    print("===================================")
    print("HOST:", DB_HOST)
    print("USER:", DB_USER)
    print("DB:", DB_NAME)
    print("PORT:", DB_PORT)

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
            print("CONEXION MYSQL OK")
            return conexion

    except Error as e:
        print(f"ERROR MYSQL: {e}")
        return None
    


def cerrar_bd(conexion):
    if conexion and conexion.is_connected():
        conexion.close()

    
# Cómo usar en las funciones:
# conn = conectar_bd()
# if conn:
#     print("Conexión establecida con éxito.")
#     conn.close()