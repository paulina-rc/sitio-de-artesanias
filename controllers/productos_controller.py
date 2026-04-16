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
    """
    Retorna el catálogo completo de artículos.

    Returns:
        list[dict]: Lista con todos los artículos disponibles.
    """
    return articulos


def get_articulo_por_id(articulo_id):
    """
    Busca y retorna un artículo por su identificador único.

    Recorre la lista hasta encontrar la primera coincidencia.
    Si no existe ningún artículo con ese id, retorna None.

    Args:
        articulo_id (int): Identificador del artículo a buscar.

    Returns:
        dict | None: Diccionario con los datos del artículo,
                     o None si no se encontró.
    """
    for articulo in articulos:
        if articulo["id"] == articulo_id:
            return articulo
    return None


def get_articulos_por_categoria(categoria):
    """
    Filtra los artículos que pertenecen a una categoría dada.

    La comparación se realiza en minúsculas para que sea insensible
    a mayúsculas (p. ej. "Tejidos" == "tejidos").

    Args:
        categoria (str): Nombre de la categoría a filtrar.

    Returns:
        list[dict]: Lista de artículos que coinciden con la categoría.
                    Retorna una lista vacía si no hay coincidencias.
    """
    return [a for a in articulos if a["categoria"].lower() == categoria.lower()]
