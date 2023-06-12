import pandas as pd
import re

# Carga el csv como una tabla
data_frame = pd.read_csv('./files/export-2019-to-now-v4.csv')

expresiones_regulares={
    'ID': r'^\d{6,7}$',
    'ID_Sesion' : r'^[A-F0-9]{8}-[A-F0-9]{8}$',
    'ID_Conexión_unico': r'^[a-f0-9]{16}$',
    'Usuario' : r'^(?=.*[a-z])(?=.*[A-Z])(?=.*-)[a-zA-Z-]{1,25}$',
    'IP_NAS_AP': r'^192\.168\.274\.[0-9]{2}$',
    'Inicio_de_Conexión_Dia': r'^(?:19|20)\d\d-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$', #(r'^(0[1-9]|[1-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])(\/|-)\d{4}$')
    'Inicio_de_Conexión_Hora': r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
    'FIN_de_Conexión_Dia': r'^(?:19|20)\d\d-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$',
    'FIN_de_Conexión_Hora':  r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
    'Session_Time': r'^\d+(\.\d+)?$',
    'MAC_AP': r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$',
    'MAC_Cliente': r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    # 'Razon_de_Terminación_de_Sesión'  
    # 'Input_Octects',  
    # 'Output_Octects',  
    # 'Tipo__conexión',  
}



registros_validos = pd.DataFrame(columns=data_frame.columns)
registros_no_validos = pd.DataFrame(columns=data_frame.columns)
 

for indice, fila in data_frame.iterrows():
    registo_valido = True

    for columna in data_frame.columns:
        if columna in expresiones_regulares:
            patron = expresiones_regulares[columna]
            valor = str(fila[columna])

            if not re.match(patron, valor):
                registros_valido = False
                break

    if registo_valido:
        registros_validos = registros_validos.append(fila)
    else:
        registros_no_validos = registros_no_validos.append(fila)

registros_validos.reset_index(drop=True, inplace=True)
registros_no_validos.reset_index(drop=True, inplace=True)

#ID,
# ID_Sesion,
# ID_Conexión_unico,
# Usuario,
# IP_NAS_AP,
# Tipo__conexión,
# Inicio_de_Conexión_Dia,
# Inicio_de_Conexión_Hora,
# FIN_de_Conexión_Dia,
# FIN_de_Conexión_Hora,
# Session_Time,
# Input_Octects,
# Output_Octects,
# MAC_AP,
# MAC_Cliente,
# Razon_de_Terminación_de_Sesión,
#603877,5AA0184E-000001CA,d6104707df0cd315,invitado-deca,192.168.247.11,Wireless-802.11,2019-02-07,19:46:08,2019-03-13,11:27:57,25,39517,505219,DC-9F-DB-12-F3-EA:HCDD,DC-BF-E9-1A-B5-D0,User-Request,,
#1616268
