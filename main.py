from triggers import *
from stored_functions import * 
from stored_procedures import *






try:
    results = ObtenerTiemposUltimoViaje()
    print(results)
except Exception as e:
    print(e)
finally:
    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()






# while True:    

#     print("1. Ver el historial de viajes de un camión")
#     print("2. Procedimiento 2")
#     print("3. Procedimiento 3")
#     print("4. Función 1")
#     print("5. Función 2")
#     print("0. Salir")


#     opt = input()

#     match opt:
#         case str(1): 
#             SP_HISTORIAL_VIAJES_CAMION(cursor)






    # # Ejecutar una función
    # function_result = cursor.callfunc('nombre_funcion', cx_Oracle.NUMBER, ['parametro1', 'parametro2'])
    # print(f'Resultado de la función: {function_result}')

    # # Ejecutar un procedimiento almacenado
    # procedure_params = {'parametro1': 'valor1', 'parametro2': 'valor2'}
    # cursor.callproc('nombre_procedimiento', keywordParameters=procedure_params)

    # # Confirmar los cambios en la base de datos
    # connection.commit()



    # Resto de tu código aquí...
    