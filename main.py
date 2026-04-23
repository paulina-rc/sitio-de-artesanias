from flask import Flask, render_template, request, flash, redirect, session
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
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO mensajes (nombre, email, mensaje)
                VALUES (%s, %s, %s)
            """, (nombre, email, mensaje))

            conn.commit()
            conn.close()

            flash("Mensaje enviado correctamente", "success")
        else:
            flash("Por favor completa todos los campos.", "danger")

    return render_template("contactenos.html")

#VISTA DE LOS CRUDS
@app.route("/crud")
def crud():
    articulos = get_todos_los_articulos()
    return render_template("crud.html", articulos=articulos)

@app.route("/crud_usuarios")
def crud_usuarios():
    if "tipo" not in session or session["tipo"] != 1:
        return redirect("/login")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    datos = cursor.fetchall()

    usuarios = []
    for fila in datos:
        usuarios.append({
            "id": fila[0],
            "nombre": fila[1],
            "usuario": fila[2],
            "password": fila[3],
            "tipo": fila[4],
            "estado": fila[5]
        })

    conn.close()

    return render_template("usuarios.html", usuarios=usuarios)


#INSERTAR PRODUCTO
import os

@app.route("/agregar", methods=["POST"])
def agregar():
    conn = conectar()
    cursor = conn.cursor()

    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    categoria = request.form["categoria"]

    imagen = request.files["imagen"]
    nombre_imagen = imagen.filename

    ruta = os.path.join("static/img", nombre_imagen)
    imagen.save(ruta)

    cursor.execute("""
        INSERT INTO productos (nombre, descripcion, precio, categoria, imagen)
        VALUES (%s, %s, %s, %s, %s)
    """, (nombre, descripcion, precio, categoria, nombre_imagen))

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

#EDITAR PRODUCTOS
@app.route("/editar/<int:id>")
def editar(id):
    articulo = get_articulo_por_id(id)
    return render_template("editar.html", articulo=articulo)

#ACTUALIZAR 
@app.route("/actualizar/<int:id>", methods=["POST"])
def actualizar(id):
    conn = conectar()
    cursor = conn.cursor()

    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    categoria = request.form["categoria"]

    cursor.execute("""
        UPDATE productos
        SET nombre=%s, descripcion=%s, precio=%s, categoria=%s
        WHERE id=%s
    """, (nombre, descripcion, precio, categoria, id))

    conn.commit()
    conn.close()

    return redirect("/crud")


#AGREGAR USUARIO 
@app.route("/agregar_usuario", methods=["POST"])
def agregar_usuario():
    conn = conectar()
    cursor = conn.cursor()

    nombre = request.form["nombre"]
    usuario = request.form["usuario"]
    password = request.form["password"]
    tipo = request.form["tipo"]
    estado = request.form["estado"]

    cursor.execute("""
        INSERT INTO usuarios (nombre, usuario, password, tipo, estado)
        VALUES (%s, %s, %s, %s, %s)
    """, (nombre, usuario, password, tipo, estado))

    conn.commit()
    conn.close()

    return redirect("/crud_usuarios")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM usuarios 
            WHERE usuario=%s AND password=%s AND estado=1
        """, (usuario, password))

        user = cursor.fetchone()
        conn.close()

        if user:
            session["usuario"] = user[2]
            session["tipo"] = user[4]

            return redirect("/")
        else:
            flash("Credenciales incorrectas", "danger")

    return render_template("login.html")


# ---------------------------------------------------------------------------
# Arranque del servidor
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)