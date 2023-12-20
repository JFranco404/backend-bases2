from connection import *

def SP_HISTORIAL_VIAJES_CAMION():
    print("Ingrese la placa del camión al que quiere verle su historial")
    placa = input()
    procedure_params = {'V_PLACA': placa}
    cursor.callproc('SP_HISTORIAL_VIAJES_CAMION', keywordParameters=procedure_params)


def SP_ELIMINAR_CONDUCTOR():
    print("Ingrese la placa del camión")
    placa = input()
    print("Ingrese la cedula del conductor a eliminar")
    cedula = input()
    
    procedure_params = {'p_placa': placa,
                        'p_id_conductor': cedula}
    cursor.callproc('SP_ELIMINAR_CONDUCTOR', keywordParameters=procedure_params)
    connection.commit()

def SP_ACTUALIZAR_COLOR():
    print("Ingrese la placa del camión al que se le cambió el color : ")
    placa = input()
    print("Ingrese el nuevo color del camión : ")
    color = input()
    procedure_params = {'p_placa': placa,
                        'p_color': color}
    cursor.callproc('SP_ACTUALIZAR_COLOR', keywordParameters=procedure_params)
    connection.commit()


def SP_ACTUALIZAR_COLOR():
    print("Ingrese la placa del camión al que quiere verle su historial")
    placa = input()
    print("Ingrese el nuevo color del camión")
    color = input()
    procedure_params = {'p_placa': placa,
                        'p_color': color}
    cursor.callproc('SP_ACTUALIZAR_COLOR', keywordParameters=procedure_params)
    connection.commit()
    
    
def actualizar_conductor():
    print("Ingrese la placa del camión")
    placa = input()
    print("Ingrese la cedula del nuevo conductor")
    cedula = input()
    procedure_params = {'p_placa': placa,
                        'p_nuevo_conductor': cedula}
    cursor.callproc('actualizar_conductor', keywordParameters=procedure_params)
    connection.commit()


def SP_DESPEDIR_CONDUCTOR():
    print("Ingrese la cedula del conductor a eliminar")
    cedula = input()
    procedure_params = {'p_nuevo_conductor': cedula}
    cursor.callproc('SP_DESPEDIR_CONDUCTOR', keywordParameters=procedure_params)
    connection.commit()
   
    
def SP_CAMBIAR_FECHA_ENTREGA():
    print("Ingrese la neuva fecha de entrega")
    fecha = input()
    procedure_params = {'V_NFECHA': fecha}
    cursor.callproc('SP_CAMBIAR_FECHA_ENTREGA', keywordParameters=procedure_params)
    connection.commit()


def ActualizarInfoConductor():
    print("Ingrese la cedula")
    cedula = input()
    print("Ingrese la foto")
    foto = input()
    print("Ingrese la licencia")
    licencia = input()
    print("Ingrese el teléfono")
    telefono = input()
    print("Ingrese el email")
    email = input()
    procedure_params = {'p_cedula': cedula,
	                    'p_foto': foto,
	                    'p_licencia' : licencia,
	                    'p_telefono' : telefono,
	                    'p_email' :email}
    cursor.callproc('ActualizarInfoConductor', keywordParameters=procedure_params)
    connection.commit() 