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
from utils.helpers import limpiar_para_whatsapp, ocultar_email

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
    actualizar_datos_mascota(
        1,
        "🐶 Tina 🐶",
        "Castrada. Mansa pero asustadiza. Toma Levotiroxina 0.4 mg al día.",
        "123456789",
        "tina@pawtag.demo"
    )

    actualizar_datos_mascota(
        2,
        "🐱 Batito 🐱",
        "Castrado. Hace pis en las piedritas pero hace 💩 fuera de la bandeja sanitaria. Es manso, cariñoso y sociable.",
        "987654321",
        "batito@pawtag.demo"
    )   

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
# AVISO DE EDICIÓN
# =============================================================================
@app.route("/aviso_edicion/<int:id_mascota>")
def aviso_edicion(id_mascota):

    mascota = buscar_mascota(id_mascota)

    if mascota is None:
        return "Mascota no encontrada"

    email_oculto = ocultar_email(
        mascota["email_contacto"]
    )

    return render_template(
        "aviso_edicion.html",
        mascota=mascota,
        email_oculto=email_oculto
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

    try:

        registrar_mascota(
            id_tag,
            nombre_mascota,
            observaciones,
            telefono_contacto,
            email_contacto
        )

    except ValueError as e:

        errores = {}

        if str(e) == "Teléfono inválido":
            errores["telefono_contacto"] = str(e)

        elif str(e) == "Email inválido":
            errores["email_contacto"] = str(e)

        return render_template(
            "alta.html",
            id_tag=id_tag,
            errores=errores,
            datos=request.form
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

    try:

        actualizar_datos_mascota(
            id_tag,
            nombre_mascota,
            observaciones,
            telefono_contacto,
            email_contacto
        )

    except ValueError as e:

        errores = {}

        if str(e) == "Teléfono inválido":
            errores["telefono_contacto"] = str(e)

        elif str(e) == "Email inválido":
            errores["email_contacto"] = str(e)

        mascota = {
            "id": id_tag,
            "nombre_mascota": nombre_mascota,
            "observaciones": observaciones,
            "telefono_contacto": telefono_contacto,
            "email_contacto": email_contacto
        }

        return render_template(
            "editar.html",
            mascota=mascota,
            errores=errores
        )

    return redirect(f"/tag/{id_tag}")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



