from connection import *

def SP_HISTORIAL_VIAJES_CAMION(cursor):
    print("Ingrese la placa del camión al que quiere verle su historial")
    placa = input()
    procedure_params = {'V_PLACA': placa}
    cursor.callproc('SP_HISTORIAL_VIAJES_CAMION', keywordParameters=procedure_params)
