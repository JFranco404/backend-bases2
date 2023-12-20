from connection import * 

def ejecutar_query(view):
    query = f"SELECT * FROM {view}"
    cursor.execute(query)


def mostrar_resultados():
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)

def Camiones_viajes_8h7d():
    ejecutar_query('Camiones_viajes_8h7d')
    mostrar_resultados()
    

def Vehiculos_en_curso():
    ejecutar_query('Vehiculos_en_curso')
    print("La cantidad de vehículos con viajes en curso es: ")
    mostrar_resultados()


def CamionesConductoresEnViaje():
    ejecutar_query('CamionesConductoresEnViaje')
    mostrar_resultados()


def ViajesEntregadosEnUltimas24Horas():
    ejecutar_query('VIAJESENULTIMAS24HORAS')
    mostrar_resultados()


def ViajesRealizados():
    ejecutar_query('ViajesRealizados')
    mostrar_resultados()


def tipocarga_viajes():
    ejecutar_query('tipocarga_viajes')
    mostrar_resultados()


def CamionesMasViajesUltimoMes():
    ejecutar_query('CamionesMasViajesUltimoMes')
    mostrar_resultados()


def CamionesMenosViajesUltimoMes():
    ejecutar_query('CamionesMenosViajesUltimoMes')
    mostrar_resultados()


def CondMasCamionesAsig():
    ejecutar_query('CondMasCamionesAsig')
    mostrar_resultados()


def conductorMenosAsignaciones():
    ejecutar_query('conductorMenosAsignaciones')
    mostrar_resultados()


def ViajesEntregadosFueraDeTiempoTeorico():
    ejecutar_query('ViajesEntregadosTarde')
    mostrar_resultados()


def ViajesEntregadosAntesDelTiempo():
    ejecutar_query('ViajesEntregadosAntesDelTiempo')
    mostrar_resultados()