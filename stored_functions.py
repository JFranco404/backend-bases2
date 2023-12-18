from connection import *

def SF_CIUDAD_MAYOR_CARGA():
    return cursor.callfunc("SF_CIUDAD_MAYOR_CARGA", cx_Oracle.STRING)


def ObtenerTiemposUltimoViaje():
    print("Ingrese la placa del camión el cual quiere consultar su tiempo del último viaje realizado")
    placa = input()
    return cursor.callfunc("ObtenerTiemposUltimoViaje", cx_Oracle.STRING, [placa])