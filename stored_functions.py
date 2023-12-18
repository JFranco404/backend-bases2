from connection import *

def SF_CIUDAD_MAYOR_CARGA():
    return cursor.callfunc("SF_CIUDAD_MAYOR_CARGA", cx_Oracle.STRING)


def ObtenerTiemposUltimoViaje():
    print("Ingrese la placa del camión el cual quiere consultar su tiempo del último viaje realizado")
    placa = input()
    return cursor.callfunc("ObtenerTiemposUltimoViaje", cx_Oracle.STRING, [placa])


def DetallesConductor():
    print("Ingrese la cedula del conductar el cual quiere consultar su información")
    cedula = input()
    return cursor.callfunc("DetallesConductor", cx_Oracle.STRING, [cedula])


def SF_CONTAR_TURNOS_JORNADA():
    return cursor.callfunc("SF_CONTAR_TURNOS_JORNADA", cx_Oracle.NUMBER)


def SF_CAMION_CON_MAS_VIAJES():
    return cursor.callfunc("SF_CAMION_CON_MAS_VIAJES", cx_Oracle.STRING)