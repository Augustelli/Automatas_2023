import re
import pandas as pd

expresiones_regulares = {
    'ID': r'^\d{6,7}$',
    'ID_Sesion': r'^[A-F0-9]{8}-[A-F0-9]{8}$',
    'Usuario': r'^[a-zA-Z-]{3,25}$',
    'Inicio_de_Conexión_Dia': r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$',
    'Inicio_de_Conexión_Hora': r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
    'FIN_de_Conexión_Dia': r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$',
    'FIN_de_Conexión_Hora': r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
    'Session_Time': r'^\d+(\.\d+)?$'
}

csv_file = './TP5v2/file/export-2019-to-now-v4.csv'
data = pd.read_csv(csv_file, low_memory=False, usecols=expresiones_regulares.keys())

data_filter = data
for columna, patron in expresiones_regulares.items():
    regex = re.compile(patron)
    data_filter = data_filter[data_filter[columna].astype(str).str.match(regex)]

print(data_filter)








# import re 
# import pandas as pd
# import tabulate

# # Expresiones regulares para cada columna
# expresiones_regulares = {
#     'ID': r'^\d{6,7}$',
#     'ID_Sesion': r'^[A-F0-9]{8}-[A-F0-9]{8}$',
#     # 'ID_Conexión_unico': r'^[a-f0-9]{16}$',
#     'Usuario': r'^[a-zA-Z-]{3,25}$',
#     # 'IP_NAS_AP': r'^192\.168\.247\.[0-9]{2}$',
#     'Inicio_de_Conexión_Dia': r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$',
#     'Inicio_de_Conexión_Hora': r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
#     'FIN_de_Conexión_Dia': r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$',
#     'FIN_de_Conexión_Hora': r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
#     'Session_Time': r'^\d+(\.\d+)?$'
#     # 'MAC_AP':  r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}:HCDD$',
#     # 'MAC_Cliente': r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
# }



# # Cargar el archivo CSV como un DataFrame en Pandas utilizando multiprocessing
# # def cargar_csv(path):
# #     data=pd.read_csv(path,low_memory=False,usecols=expresiones_regulares.keys())
# #     return data

# # Ruta y nombre de tu archivo CSV
# csv_file = './TP5v2/file/export-2019-to-now-v4.csv'

# data=pd.read_csv(csv_file,low_memory=False,usecols=expresiones_regulares.keys())


# # data_filter=data[data['ID'].str.contains(r'^\d{6,7}$') &
# #                 data['ID_Sesion'].str.contains(r'^[A-F0-9]{8}-[A-F0-9]{8}$') &
# #                 data['Usuario'].str.contains(r'^[a-zA-Z-]{3,25}$') &
# #                 data['Inicio_de_Conexión_Dia'].str.contains(r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$') &
# #                 data['Inicio_de_Conexión_Hora'].str.contains(r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$') &
# #                 data['FIN_de_Conexión_Dia'].str.contains(r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$') &
# #                 data['FIN_de_Conexión_Hora'].str.contains(r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$') &
# #                 data['Session_Time'].str.contains(r'^\d+(\.\d+)?$')]


# data_filter = data[data['ID'].astype(str).str.contains(r'^\d{6,7}$') &
#                    data['ID_Sesion'].astype(str).str.contains(r'^[A-F0-9]{8}-[A-F0-9]{8}$') &
#                    data['Usuario'].astype(str).str.contains(r'^[a-zA-Z-]{3,25}$') &
#                    data['Inicio_de_Conexión_Dia'].astype(str).str.contains(r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$') &
#                    data['Inicio_de_Conexión_Hora'].astype(str).str.contains(r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$') &
#                    data['FIN_de_Conexión_Dia'].astype(str).str.contains(r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$') &
#                    data['FIN_de_Conexión_Hora'].astype(str).str.contains(r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$') &
#                    data['Session_Time'].astype(str).str.contains(r'^\d+(\.\d+)?$')]


# print(data_filter)

