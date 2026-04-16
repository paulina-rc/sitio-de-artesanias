"""
main.py — Punto de entrada de la aplicación Flask "Artesanías del Campo".

Define la aplicación, la clave secreta para sesiones y mensajes flash,
y registra las tres rutas principales:
  - /            → página de inicio
  - /productos   → catálogo de artesanías
  - /contactenos → formulario de contacto (GET y POST)
"""

from flask import Flask, render_template, request, flash
from controllers.productos_controller import *

# Instancia principal de la aplicación Flask.
# Flask usa __name__ para localizar plantillas y archivos estáticos.
app = Flask(__name__)

# Clave secreta requerida por Flask para firmar las cookies de sesión
# y habilitar el sistema de mensajes flash.

# Firmar cookies de sesión:
# Flask utiliza cookies para almacenar información de la sesión de los usuarios (por ejemplo, datos temporales mientras navegan en el sitio).
# La clave secreta se usa para "firmar" estas cookies, lo que significa que Flask genera un hash seguro que verifica que las cookies no han sido manipuladas por terceros.
# Sin una clave secreta, cualquier persona podría modificar las cookies y potencialmente comprometer la seguridad de tu aplicación.

# Mensajes flash:
# Los mensajes flash son una forma de mostrar notificaciones temporales al usuario, como "¡Formulario enviado con éxito!" o "Error: Por favor, complete todos los campos".
# Flask almacena estos mensajes en la sesión del usuario, y la clave secreta asegura que los mensajes sean confiables y no puedan ser alterados.


app.secret_key = "artesanias_secreto_2024"


# ---------------------------------------------------------------------------
# Rutas / Vistas
# ---------------------------------------------------------------------------

@app.route("/")
def inicio():
    """
    Vista de la página principal (home).

    Renderiza la plantilla 'inicio.html', que muestra la sección hero,
    los valores diferenciadores de la tienda y un llamado a la acción.

    Returns:
        Response: HTML de la página de inicio.
    """
    return render_template("inicio.html")


@app.route("/productos")
def productos():
    """
    Vista del catálogo de productos.

    Obtiene la lista completa de artículos desde el controlador y la
    pasa a la plantilla 'productos.html' para su renderizado en tarjetas.

    Returns:
        Response: HTML con la cuadrícula de artesanías disponibles.
    """
    articulos = get_todos_los_articulos()
    return render_template("productos.html", articulos=articulos)


@app.route("/contactenos", methods=["GET", "POST"])
def contactenos():
    """
    Vista del formulario de contacto.

    GET:  Muestra el formulario vacío.
    POST: Valida que los campos 'nombre', 'email' y 'mensaje' estén
          presentes. Si la validación pasa, muestra un mensaje flash de
          éxito; de lo contrario, muestra un mensaje de error.

    Returns:
        Response: HTML de la página de contacto con el formulario
                  y, en caso de POST, un mensaje flash con el resultado.
    """
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        mensaje = request.form.get("mensaje")

        if nombre and email and mensaje:
            # Todos los campos presentes → confirmación al usuario
            flash(f"Gracias {nombre}, tu mensaje fue enviado correctamente.", "success") #success es la categoría del mensaje flash, que se puede usar en la plantilla para estilos específicos.

            flash(f"Gracias otra vez {nombre}, tu mensaje fue enviado correctamente.", "success")
        else:
            # Algún campo faltante → aviso de error
            flash("Por favor completa todos los campos.", "danger") #danger es otra categoría de mensaje flash, comúnmente usada para errores.

    return render_template("contactenos.html")


# ---------------------------------------------------------------------------
# Arranque del servidor de desarrollo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # debug=True activa el recargador automático y el depurador interactivo.
    # No usar debug=True en producción.
    app.run(debug=True)
