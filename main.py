from triggers import *
from stored_functions import * 
from stored_procedures import *
from connection import *


try:
    while True:
        print("0. Salir del sistema")
        print("----------------------------------------------------------------------")
        print("                      Obtener información general")
        print("----------------------------------------------------------------------")
        print("1. Obtener la ciudad origen, del último viaje de un camión por placa.")
        print("2. Conocer la diferencia de tiempo del último viaje realizado por un camión.")
        print("3. Conocer detalle sobre la carga del último viaje realizado por un camión.")
        print("4. Obtener detalles de conductor dada su cédula")
        print("5. Conocer la cantidad de turnos de descarga en las últimas 8 horas.")
        print("6. Conocer la ciudad de donde vienen la mayor cantidad de viajes.")
        print("7. Conocer la ciudad hacia donde se envían la mayoría de cargas.")
        print("8. Conocer la carga más transportada en la empresa.")
        print("9. Ver el camión con más viajes realizados.")
        print("10. Ver los conductores asignados a un camión.")
        print("\n")
        print("----------------------------------------------------------------------")
        print("                          Modificar información")
        print("----------------------------------------------------------------------")
        print("\n")
        print("Ingrese una opción > ", end=" ")

        opt = input()

        match opt:
            case '0':
                quit()
            case '1':
                pass
            case '2':
                ObtenerTiemposUltimoViaje()
            case '3':
                pass
            case '4':
                pass
            case '5':
                SF_CONTAR_TURNOS_JORNADA()
            case '6':
                SF_CIUDAD_MAYOR_CARGA()
            case '7':
                pass
            case '8':
                pass
            case '9':
                SF_CAMION_CON_MAS_VIAJES
            case '10':
                pass
        


except Exception as e:
    print(e)
finally:
    cursor.close()
    connection.close()
