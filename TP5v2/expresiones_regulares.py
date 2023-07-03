import re

def validar_patron(patron, entrada):
    return re.match(patron, entrada) is not None

def validar_formato(entrada, patron):
    return validar_patron(patron, entrada)

def validacion_fecha(fecha):
    patron = r'^(0[1-9]|[1-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])(\/|-)\d{4}$'
    return validar_formato(fecha, patron)

def validacion_id(id):
    patron = r'^\d{6,7}$'
    return validar_formato(id, patron)

def validacion_id_sesion(id_sesion):
    patron = r'^[A-F0-9]{8}-[A-F0-9]{8}$'
    return validar_formato(id_sesion, patron)

def validacion_id_conexion_unico(id_conexion_unico):
    patron = r'^[a-f0-9]{16}$'
    return validar_formato(id_conexion_unico, patron)

def validacion_usuario(usuario):
    patron = r'^[a-zA-Z.-]{3,25}$'
    return validar_formato(usuario, patron)

def validacion_ip_nas_ap(ip_nas_ap):
    patron = r'^((?:192\.168\.247\.[0-9]{2})|(?:192\.168\.1\.20))$'
    return validar_formato(ip_nas_ap, patron)

def validacion_inicio_de_conexion_dia(inicio_de_conexion_dia):
    patron = r'^(?:19|20)\d\d-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])$'
    return validar_formato(inicio_de_conexion_dia, patron)

def validacion_inicio_de_conexion_hora(inicio_de_conexion_hora):
    patron = r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$'
    return validar_formato(inicio_de_conexion_hora, patron)

def validacion_fin_de_conexion_dia(fin_de_conexion_dia):
    patron = r'^(?:19|20)\d\d-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])$'
    return validar_formato(fin_de_conexion_dia, patron)

def validacion_fin_de_conexion_hora(fin_de_conexion_hora):
    patron = r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$'
    return validar_formato(fin_de_conexion_hora, patron)

def validacion_session_time(session_time):
    patron = r'^\d+(\.\d+)?$'
    return validar_formato(session_time, patron)

def validacion_mac_ap(mac_ap):
    patron = r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}:HCDD$'
    return validar_formato(mac_ap, patron)

def validacion_mac_cliente(mac_cliente):
    patron = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return validar_formato(mac_cliente, patron)

# import re

def validar_formato(entrada, patron):
    return re.match(patron, entrada) is not None

patrones = {
    'fecha': r'^(0[1-9]|[1-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])(\/|-)\d{4}$',
    'id': r'^\d{6,7}$',
    'id_sesion': r'^[A-F0-9]{8}-[A-F0-9]{8}$',
    'id_conexion_unico': r'^[a-f0-9]{16}$',
    'usuario': r'^[a-zA-Z.-]{3,25}$',
    'ip_nas_ap': r'^((?:192\.168\.247\.[0-9]{2})|(?:192\.168\.1\.20))$',
    'inicio_de_conexion_dia': r'^(?:19|20)\d\d-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])$',
    'inicio_de_conexion_hora': r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
    'fin_de_conexion_dia': r'^(?:19|20)\d\d-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])$',
    'fin_de_conexion_hora': r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
    'session_time': r'^\d+(\.\d+)?$',
    'mac_ap': r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}:HCDD$',
    'mac_cliente': r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
}

def validar(entrada, tipo):
    patron = patrones.get(tipo)
    return validar_formato(entrada, patron)
