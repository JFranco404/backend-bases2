from connection import *


def vistaprueba():
    # Consultar la vista usando SELECT
    query = f"SELECT * FROM Camiones_viajes_8h7d"
    cursor.execute(query)

    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()
    
    # Imprimir los resultados o realizar otras operaciones con ellos
    for resultado in resultados:
        print(resultado)