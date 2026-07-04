from flask import Flask
from flask import render_template
from logic.mascota_logic import (
    buscar_mascota,
    registrar_mascota,
    actualizar_datos_mascota,
    eliminar_mascota
)
from urllib.parse import quote
from flask import request, redirect
from utils.helpers import limpiar_para_whatsapp

app = Flask(__name__, template_folder="views")


# =============================================================================
# HOME
# =============================================================================
@app.route("/")
def home():
    return render_template("home.html")


# =============================================================================
# REINICIAR DEMOSTRACIÓN
# =============================================================================
@app.route("/reiniciar_demo")
def reiniciar_demo():

    eliminar_mascota(999)

    return redirect("/demo")



# =============================================================================
# DEMOSTRACIÓN
# =============================================================================
@app.route("/demo")
def demo():

    mascota_demo = buscar_mascota(999)

    return render_template(
        "demo.html",
        tag_demo_registrado=(mascota_demo is not None)
    )


# =============================================================================
# VISUALIZAR MASCOTA
# =============================================================================
@app.route("/tag/<int:id_tag>")
def ver_mascota(id_tag):

    mascota = buscar_mascota(id_tag)

    if mascota is None:
        return render_template("alta.html",
        id_tag=id_tag)

    nombre_whatsapp = limpiar_para_whatsapp(
    mascota["nombre_mascota"]
)
    mensaje = quote(f"Hola, encontré a {nombre_whatsapp}. Escaneé la chapita PawTag y me gustaría coordinar la devolución.")

    return render_template(
    "ficha.html",
    mascota=mascota,
    mensaje_whatsapp=mensaje
    )


# =============================================================================
# REGISTRAR MASCOTA
# =============================================================================
@app.route("/alta/<int:id_tag>", methods=["POST"])
def alta_mascota(id_tag):

    nombre_mascota = request.form["nombre_mascota"]
    observaciones = request.form["observaciones"]
    telefono_contacto = request.form["telefono_contacto"]
    email_contacto = request.form["email_contacto"]

    id_generado = registrar_mascota(
        id_tag,
        nombre_mascota,
        observaciones,
        telefono_contacto,
        email_contacto
    )

    if id_tag == 999:
        return redirect("/demo")

    return redirect(f"/tag/{id_tag}")


# =============================================================================
# EDITAR MASCOTA
# =============================================================================
@app.route("/editar/<int:id_mascota>")
def editar_mascota(id_mascota):

    mascota = buscar_mascota(id_mascota)

    if mascota is None:
        return "Mascota no encontrada"

    return render_template(
        "editar.html",
        mascota=mascota
    )


# =============================================================================
# GUARDAR EDICIÓN
# =============================================================================
@app.route("/guardar_edicion/<int:id_tag>", methods=["POST"])
def guardar_edicion(id_tag):

    nombre_mascota = request.form["nombre_mascota"]
    observaciones = request.form["observaciones"]
    telefono_contacto = request.form["telefono_contacto"]
    email_contacto = request.form["email_contacto"]

    actualizar_datos_mascota(
        id_tag,
        nombre_mascota,
        observaciones,
        telefono_contacto,
        email_contacto
    )

    return redirect(f"/tag/{id_tag}")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



