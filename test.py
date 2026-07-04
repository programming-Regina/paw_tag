from db.dao import obtener_mascota_por_id

from logic.mascota_logic import registrar_mascota

id_generado = registrar_mascota(
    "Doña Muricy",
    "No acercarse con comida.",
    "5491122222222",
    "batito@test.com"
)

print(id_generado)