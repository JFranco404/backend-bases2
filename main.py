import cx_Oracle
from triggers import *
from stored_functions import * 
from stored_procedures import *
from views import *
from connection import *
from views import *


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
        print("                    Obtener reportes de información")
        print("----------------------------------------------------------------------")
        print("11. Vehículos en curso")
        print("12. Ver los camiones y conductores que se encuentran en viaje")
        print("13. Ver los camiones que han hecho viajes de más de 8 horas en la última semana")
        print("14. Ver los viajes entregados en las últimas 24 Horas")
        print("15. Ver los viajes realizados con su estado")
        print("16. Ver el tipo de carga de todos los viajes")
        print("17. Ver los camiones que más viajes han realizado en el último mes")
        print("18. Ver los camiones que menos viajes han realizado en el último mes")
        print("19. Ver los conductores con más camiones asignados")
        print("20. Ver los conductrores con menos camiones asignados")
        print("21. Ver los viajes que finalizaron fuera del timepo estimado")
        print("22. Ver los viajes que finalizaron antes del tiempo estimado")
        print("\n")
        print("----------------------------------------------------------------------")
        print("                         Modificar información")
        print("----------------------------------------------------------------------")
        print("23. eliminar la asignacion de un conductor a un camión")
        print("24. actualizar el color de un camión que se pintó")
        print("25. actualizar_conductor")
        print("26. SP_HISTORIAL_VIAJES_CAMION")
        print("27. ")
        print("28. ")
        print("29. ")
        print("30. ")
        print("31. ")
        print("32. ")

        print("Ingrese una opción > ", end=" ")

        opt = input()

        match opt:
            case '0':
                print("Gracias por usar EffiCargo Technologies")
                quit()
            case '1':
                print(origenViaje())
            case '2':
                print(ObtenerTiemposUltimoViaje())
            case '3':
                print(FnDetalleCarga())
            case '4':
                print(DetallesConductor())
            case '5':
                print('La cantidad de turnos de la última jornada ha sido de: ' + str(SF_CONTAR_TURNOS_JORNADA())+ '\n')
            case '6':
                print('La ciudad con mayor carga ha sido ' + SF_CIUDAD_MAYOR_CARGA()+ '\n')
            case '7':
                print(FnCiudadMasViajes())
            case '8':
                print(FnCargaMasTransportada())
            case '9':
                print(SF_CAMION_CON_MAS_VIAJES())
            case '10':
                print(ConductoresAsignadosACamion())
            case '11':
                print(Vehiculos_en_curso())
            case '12':
                print(CamionesConductoresEnViaje())
            case '13':
                Camiones_viajes_8h7d()
            case '14':
                ViajesEntregadosEnUltimas24Horas()
            case '15':
                ViajesRealizados()
            case '16':
                tipocarga_viajes()
            case '17':
                CamionesMasViajesUltimoMes()
            case '18':
                CamionesMenosViajesUltimoMes()
            case  '19':
                CondMasCamionesAsig()
            case  '20':
                conductorMenosAsignaciones()
            case  '21':
                ViajesEntregadosFueraDeTiempoTeorico()
            case  '22':
                ViajesEntregadosAntesDelTiempo()
            case  '23':
                SP_ELIMINAR_CONDUCTOR()
            case  '24':
                SP_ACTUALIZAR_COLOR()
            case  '25':
                actualizar_conductor()
            case  '26':
                SP_DESPEDIR_CONDUCTOR()
            case  '27':
                SP_CAMBIAR_FECHA_ENTREGA()
            case  '28':   
                SP_HISTORIAL_VIAJES_CAMION()
            case '29':
                ActualizarInfoConductor()

except Exception as e:
    print(e)
finally:
    cursor.close()
    connection.close()
