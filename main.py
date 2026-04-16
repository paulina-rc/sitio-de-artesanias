from flask import Flask, render_template, request, flash, redirect
from controllers.productos_controller import *
from controllers.db import conectar

app = Flask(__name__)

app.secret_key = "artesanias_secreto_2024"



# Rutas / Vistas

@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/productos")
def productos():
    articulos = get_todos_los_articulos()
    return render_template("productos.html", articulos=articulos)


@app.route("/contactenos", methods=["GET", "POST"])
def contactenos():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        mensaje = request.form.get("mensaje")

        if nombre and email and mensaje:
            flash(f"Gracias {nombre}, tu mensaje fue enviado correctamente.", "success")
            flash(f"Gracias otra vez {nombre}, tu mensaje fue enviado correctamente.", "success")
        else:
            flash("Por favor completa todos los campos.", "danger")

    return render_template("contactenos.html")


#VISTA CRUD
@app.route("/crud")
def crud():
    articulos = get_todos_los_articulos()
    return render_template("crud.html", articulos=articulos)


#INSERTAR PRODUCTO
@app.route("/agregar", methods=["POST"])
def agregar():
    conn = conectar()
    cursor = conn.cursor()

    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    categoria = request.form["categoria"]

    cursor.execute("""
        INSERT INTO productos (nombre, descripcion, precio, categoria, imagen)
        VALUES (%s, %s, %s, %s, %s)
    """, (nombre, descripcion, precio, categoria, "default.jpg"))

    conn.commit()
    conn.close()

    return redirect("/crud")

#ELIMINAR PRODUCTO 
@app.route("/eliminar/<int:id>")
def eliminar(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM productos WHERE id = %s", (id,))

    conn.commit()
    conn.close()

    return redirect("/crud")


# ---------------------------------------------------------------------------
# Arranque del servidor
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)