import cx_Oracle
from triggers import *
from stored_functions import * 
from stored_procedures import *
from connection import *

try:

    results = FnCargaMasTransportada()
    print(results)
except Exception as e:
    print(e)
finally:
    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()
#

##
#while True:    
#    print("1. Ver el historial de viajes de un camión")
#    print("2. Procedimiento 2")
#    print("3. Procedimiento 3")
#    print("4. Función 1")
#    print("5. Función 2")
#    print("0. Salir")
#
#
#    opt = input()
#
#    match opt:
#        case '1':
#            SP_HISTORIAL_VIAJES_CAMION()
#        case '2':
#            print("Opción 2 seleccionada")
#        case '0':
#            quit()
#        case _:
#            print("Opción no válida")
#
#    try:
#
#        # # Ejecutar una función
#        # function_result = cursor.callfunc('nombre_funcion', cx_Oracle.NUMBER, ['parametro1', 'parametro2'])
#        # print(f'Resultado de la función: {function_result}')
#
#        # # Ejecutar un procedimiento almacenado
#        # procedure_params = {'parametro1': 'valor1', 'parametro2': 'valor2'}
#        # cursor.callproc('nombre_procedimiento', keywordParameters=procedure_params)
#
#        # # Confirmar los cambios en la base de datos
#        # connection.commit()
#
#
#
#        # Resto de tu código aquí...
#        
#        sql_query = "SELECT * FROM CAMIONES"
#        ola = cursor.execute(sql_query)
#        for r in ola: 
#            print(r)
#            
#    except Exception as e:
#        print(e)
#    finally:
#        # Cerrar el cursor y la conexión
#        cursor.close()
#        connection.close()
#


