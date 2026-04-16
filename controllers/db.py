import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # pon tu contraseña si tienes
        database="artesanias"
    )