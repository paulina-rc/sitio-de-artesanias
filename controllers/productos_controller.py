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

from controllers.db import *

articulos = [
    {
        "id": 1,
        "nombre": "Jarron de Barro Pintado",
        "descripcion": "Jarron elaborado a mano con barro negro, decorado con motivos florales tradicionales.",
        "precio": 85000,
        "categoria": "Ceramica",
        "imagen": "jarron.jpg"
    },
    {
        "id": 2,
        "nombre": "Mochila Wayuu",
        "descripcion": "Bolso tejido a mano por comunidades indigenas con hilos de colores vibrantes.",
        "precio": 120000,
        "categoria": "Tejidos",
        "imagen": "mochila.jpg"
    },
    {
        "id": 3,
        "nombre": "Mascara Tallada en Madera",
        "descripcion": "Mascara decorativa tallada en cedro, inspirada en rituales ancestrales.",
        "precio": 95000,
        "categoria": "Madera",
        "imagen": "mascara.jpg"
    },
    {
        "id": 4,
        "nombre": "Canasto de Palma",
        "descripcion": "Canasto tejido con palma de iraca, ideal para almacenamiento y decoracion.",
        "precio": 45000,
        "categoria": "Fibras Naturales",
        "imagen": "canasto.jpg"
    },
    {
        "id": 5,
        "nombre": "Collar de Chaquiras",
        "descripcion": "Collar elaborado con cuentas de vidrio multicolor siguiendo patrones tradicionales.",
        "precio": 35000,
        "categoria": "Joyeria",
        "imagen": "collar.jpg"
    },
    {
        "id": 6,
        "nombre": "Tapiz Bordado",
        "descripcion": "Tapiz de lino bordado a mano con escenas de paisajes campesinos colombianos.",
        "precio": 150000,
        "categoria": "Bordados",
        "imagen": "tapiz.jpg"
    },
    {
        "id": 7,
        "nombre": "Figura de Totumo",
        "descripcion": "Recipiente decorativo elaborado con totumo natural, tallado y pintado a mano.",
        "precio": 28000,
        "categoria": "Artesania Natural",
        "imagen": "totumo.jpg"
    },
    {
        "id": 8,
        "nombre": "Sombrero Vueltiao",
        "descripcion": "Sombrero tipico colombiano tejido con caña flecha, declarado patrimonio cultural.",
        "precio": 200000,
        "categoria": "Sombreros",
        "imagen": "sombrero.jpg"
    }
]


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