import re


# =============================================================================
# LIMPIAR TEXTO PARA WHATSAPP
# =============================================================================
def limpiar_para_whatsapp(texto):
    """
    Elimina emojis para mensajes precargados de WhatsApp.
    """

    return re.sub(
        r'[\U00010000-\U0010FFFF]',
        '',
        texto
    ).strip()


# =============================================================================
# NORMALIZAR NOMBRE DE MASCOTA
# =============================================================================
def limpiar_nombre_mascota(nombre):
    """
    Elimina espacios sobrantes.
    """

    return " ".join(nombre.strip().split())


# =============================================================================
# NORMALIZAR OBSERVACIONES
# =============================================================================
def limpiar_observaciones(observaciones):
    """
    Elimina espacios sobrantes.
    """

    return " ".join(observaciones.strip().split())


# =============================================================================
# NORMALIZAR TELÉFONO
# =============================================================================
def limpiar_telefono(telefono):
    """
    Conserva únicamente números.
    """

    return re.sub(r"\D", "", telefono)


# =============================================================================
# NORMALIZAR EMAIL
# =============================================================================
def limpiar_email(email):
    """
    Elimina espacios y pasa a minúsculas.
    """

    return email.strip().lower()


# =============================================================================
# VALIDAR EMAIL
# =============================================================================
def email_valido(email):
    """
    Validación básica de email.
    """

    patron = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return bool(re.match(patron, email))


# =============================================================================
# VALIDAR TELÉFONO
# =============================================================================
def telefono_valido(telefono):
    """
    Verifica que tenga una cantidad razonable de dígitos.
    """

    return len(telefono) >= 8



# =============================================================================
# OCULTAR EMAIL
# =============================================================================
def ocultar_email(email):
    """
    Convierte:
    carlos@gmail.com

    en:

    ca*****@gmail.com
    """

    usuario, dominio = email.split("@")

    visibles = min(2, len(usuario))

    return (
        usuario[:visibles]
        + "*****@"
        + dominio
    )