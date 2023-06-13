import re
def validacion_fecha(fecha):
    patron = re.compile(r'^(0[1-9]|[1-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])(\/|-)\d{4}$')
   
    if patron.match(fecha):
        print('La fecha ingresada es correcta')
    else:
        print('La fecha ingresada es incorrecta')

def validacion_id(id):
    patron= re.compile(r'^\d{6,7}$')
    if patron.match(id):
        print('El id ingresado es correcto')
    else:
        print('El id ingresado es incorrecto')

def validacion_id_sesion(id_sesion):
    patron= re.compile(r'^[A-F0-9]{8}-[A-F0-9]{8}$')
    if patron.match(id_sesion):
        print('El id de sesion ingresado es correcto')
    else:
        print('El id de sesion ingresado es incorrecto')

def validacion_id_conexion_unico(id_conexion_unico):
    patron= re.compile(r'^[a-f0-9]{16}$')
    if patron.match(id_conexion_unico):
        print('El id de conexion unico ingresado es correcto')
    else:
        print('El id de conexion unico ingresado es incorrecto')

def validacion_usuario(usuario):
    patron= re.compile(r'^[a-zA-Z-]{8,25}$')
    if patron.match(usuario):
        print('El usuario ingresado es correcto')
    else:
        print('El usuario ingresado es incorrecto')

def validacion_ip_nas_ap(ip_nas_ap):
    patron= re.compile(r'^192\.168\.274\.[0-9]{2}$')
    if patron.match(ip_nas_ap):
        print('La ip nas ap ingresada es correcta')
    else:
        print('La ip nas ap ingresada es incorrecta')

def validacion_inicio_de_conexion_dia(inicio_de_conexion_dia):
    patron= re.compile(r'^(?:19|20)\d\d-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$')
    if patron.match(inicio_de_conexion_dia):
        print('El inicio de conexion dia ingresado es correcto')
    else:
        print('El inicio de conexion dia ingresado es incorrecto')
    
def validacion_inicio_de_conexion_hora(inicio_de_conexion_hora):
    patron= re.compile(r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$')
    if patron.match(inicio_de_conexion_hora):
        print('El inicio de conexion hora ingresado es correcto')
    else:
        print('El inicio de conexion hora ingresado es incorrecto')

def validacion_fin_de_conexion_dia(fin_de_conexion_dia):
    patron= re.compile(r'^(?:19|20)\d\d-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$')
    if patron.match(fin_de_conexion_dia):
        print('El fin de conexion dia ingresado es correcto')
    else:
        print('El fin de conexion dia ingresado es incorrecto')

def validacion_fin_de_conexion_hora(fin_de_conexion_hora):
    patron= re.compile(r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$')
    if patron.match(fin_de_conexion_hora):
        print('El fin de conexion hora ingresado es correcto')
    else:
        print('El fin de conexion hora ingresado es incorrecto')

def validacion_session_time(session_time):
    patron= re.compile(r'^\d+(\.\d+)?$')
    if patron.match(session_time):
        print('El session time ingresado es correcto')
    else:
        print('El session time ingresado es incorrecto')

def validacion_mac_ap(mac_ap):
    patron= re.compile(r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}:HCDD$')
    if patron.match(mac_ap):
        print('La mac ap ingresada es correcta')
    else:
        print('La mac ap ingresada es incorrecta')

def validacion_mac_cliente(mac_cliente):
    patron= re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    if patron.match(mac_cliente):
        print('La mac cliente ingresada es correcta')
    else:
        print('La mac cliente ingresada es incorrecta')


# if opcion == 1:
#     # fecha = input('Ingrese una fecha (dd/mm/aaaa) o (dd-mm-aaaa): ')
#     verificacion=validacion_fecha(fecha)
# elif opcion == 2:
#     id=603877
#     # id = input('Ingrese un id (6 o 7 digitos): ')
#     verificacion=validacion_id(id)
# elif opcion == 3:
#     id_sesion='5AA0184E-000001CA'

#     # id_sesion = input('Ingrese un id de sesion (8 digitos - 8 digitos): ')
#     verificacion=validacion_id_sesion(id_sesion)
# elif opcion == 4:
#     # id_conexion_unico = input('Ingrese un id de conexion unico (16 digitos): ')
#     verificacion=validacion_id_conexion_unico(id_conexion_unico)
# elif opcion == 5:
#     # validacion_usuario= input('Ingrese un usuario (1 a 25 caracteres, letras mayusculas, minusculas y guion medio): ')
#     verificacion=validacion_usuario(usuario)
# elif opcion == 6:
#     # ip_nas_ap = input('Ingrese una ip nas ap (192.168.274.00): ')
#     verificacion=validacion_ip_nas_ap(ip_nas_ap)
# elif opcion == 7:
#     # inicio_de_conexion_dia = input('Ingrese un inicio de conexion dia (aaaa-mm-dd): ')
#     verificacion=validacion_inicio_de_conexion_dia(inicio_de_conexion_dia)
# elif opcion == 8:
#     # inicio_de_conexion_hora = input('Ingrese un inicio de conexion hora (hh:mm:ss): ')
#     verificacion=validacion_inicio_de_conexion_hora(inicio_de_conexion_hora)
# elif opcion == 9:
#     # fin_de_conexion_dia = input('Ingrese un fin de conexion dia (aaaa-mm-dd): ')
#     verificacion=validacion_fin_de_conexion_dia(fin_de_conexion_dia)
# elif opcion == 10:
#     # fin_de_conexion_hora = input('Ingrese un fin de conexion hora (hh:mm:ss): ')
#     verificacion=validacion_fin_de_conexion_hora(fin_de_conexion_hora)
# elif opcion == 11:
#     # session_time = input('Ingrese un session time (numero): ')
#     verificacion=validacion_session_time(session_time)
# elif opcion == 12:
#     # mac_ap = input('Ingrese una mac ap (00:00:00:00:00:00): ')
#     verificacion=validacion_mac_ap(mac_ap)
# elif opcion == 13:
#     # mac_cliente = input('Ingrese una mac cliente (00:00:00:00:00:00): ')
#     verificacion=validacion_mac_cliente(mac_cliente)
# else:
#     print('La opcion ingresada no es correcta')


validacion_id('603877')
validacion_id_sesion('5AA0184E-000001CA')
validacion_id_conexion_unico('d6104707df0cd315')
validacion_usuario('invitado-deca')
validacion_usuario('lalbul-crndu')
validacion_ip_nas_ap('192.168.274.11')
validacion_inicio_de_conexion_dia('2019-02-07')
validacion_inicio_de_conexion_hora('19:46:08')
validacion_fin_de_conexion_dia('2019-03-13')
validacion_fin_de_conexion_hora('11:27:57')
validacion_session_time('25')
validacion_mac_ap('DC-9F-DB-12-F3-EA:HCDD')

validacion_mac_cliente('DC-BF-E9-1A-B5-D0')



expresiones_regulares = {

    'ID': r'^\d{6,7}$',
    'ID_Sesion': r'^[A-F0-9]{8}-[A-F0-9]{8}$',
    'ID_Conexión_unico': r'^[a-f0-9]{16}$',
    'Usuario': r'^[a-zA-Z-]{3,25}$',
    'IP_NAS_AP': r'^192\.168\.274\.[0-9]{2}$',
    'Inicio_de_Conexión_Dia': r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$',
    'Inicio_de_Conexión_Hora': r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
    'FIN_de_Conexión_Dia': r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$',
    'FIN_de_Conexión_Hora': r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
    'Session_Time': r'^\d+(\.\d+)?$',
    'MAC_AP':  r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}:HCDD$',  #DC-9F-DB-12-F3-EA:HCDD
    'MAC_Cliente': r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$' #DC-BF-E9-1A-B5-D0
}