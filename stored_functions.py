from connection import *

def SF_CIUDAD_MAYOR_CARGA():
    return cursor.callfunc("SF_CIUDAD_MAYOR_CARGA", cx_Oracle.STRING)


def ObtenerTiemposUltimoViaje():
    print("Ingrese la placa del camión el cual quiere consultar su tiempo del último viaje realizado")
    placa = input()
    return cursor.callfunc("ObtenerTiemposUltimoViaje", cx_Oracle.STRING, [placa])


def origenViaje():
    print("Ingrese la placa del camión el cual quiere consultar su origen del último viaje realizado")
    placa = input()
    return cursor.callfunc("FnOrigenViaje", cx_Oracle.STRING, [placa])

def FnDetalleCarga():
    print("Ingrese la placa del camión el cual quiere consultar el detalle de la carga")
    placa = input()
    return cursor.callfunc("FnDetalleCarga", cx_Oracle.STRING, [placa])

def FnCiudadMasViajes():
    print("se está consultando la ciudad con más viajes...")
    return cursor.callfunc("FnCiudadMasViajes", cx_Oracle.STRING, [])


def FnCargaMasTransportada():
    print("se está consultando la carga más transportada...")
    return cursor.callfunc("FnCargaMasTransportada", cx_Oracle.STRING, [])
