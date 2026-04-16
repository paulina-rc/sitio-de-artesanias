"""
controllers/productos_controller.py — Controlador de productos.

Este módulo actúa como la capa de datos (modelo) y lógica de negocio
para las artesanías. Almacena el catálogo en memoria mediante una lista
de diccionarios y expone funciones para consultarlo.

Estructura de cada artículo:
    {
        "id"         (int):  Identificador único del artículo.
        "nombre"     (str):  Nombre descriptivo de la pieza.
        "descripcion"(str):  Texto corto que explica el artículo.
        "precio"     (int):  Precio en pesos colombianos (COP).
        "categoria"  (str):  Categoría artesanal (p. ej. "Cerámica").
        "imagen"     (str):  Nombre del archivo de imagen en /static/img/.
    }
"""

# ---------------------------------------------------------------------------
# Fuente de datos en memoria
# ---------------------------------------------------------------------------

from controllers.db import conectar

# ---------------------------------------------------------------------------
# Funciones de consulta (API del controlador)
# ---------------------------------------------------------------------------

def get_todos_los_articulos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos")
    datos = cursor.fetchall()

    articulos = []
    for fila in datos:
        articulos.append({
            "id": fila[0],
            "nombre": fila[1],
            "descripcion": fila[2],
            "precio": fila[3],
            "categoria": fila[4],
            "imagen": fila[5]
        })

    conn.close()
    return articulos


def get_articulo_por_id(articulo_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos WHERE id = %s", (articulo_id,))
    fila = cursor.fetchone()

    conn.close()

    if fila:
        return {
            "id": fila[0],
            "nombre": fila[1],
            "descripcion": fila[2],
            "precio": fila[3],
            "categoria": fila[4],
            "imagen": fila[5]
        }
    return None


def get_articulos_por_categoria(categoria):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos WHERE categoria = %s", (categoria,))
    datos = cursor.fetchall()

    conn.close()

    articulos = []
    for fila in datos:
        articulos.append({
            "id": fila[0],
            "nombre": fila[1],
            "descripcion": fila[2],
            "precio": fila[3],
            "categoria": fila[4],
            "imagen": fila[5]
        })

    return articulos