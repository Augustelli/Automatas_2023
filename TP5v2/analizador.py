'''ESTE NO FUNCAAAAAAAAAAAA'''



# import pandas as pd
# import re
# from multiprocessing import Pool
# import tabulate

# # Expresiones regulares para cada columna
# expresiones_regulares = {
#     'ID': r'^\d{6,7}$',
#     'ID_Sesion': r'^[A-F0-9]{8}-[A-F0-9]{8}$',
#     'ID_Conexión_unico': r'^[a-f0-9]{16}$',
#     'Usuario': r'^[a-zA-Z-]{3,25}$',
#     'IP_NAS_AP': r'^192\.168\.247\.[0-9]{2}$',
#     'Inicio_de_Conexión_Dia': r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$',
#     'Inicio_de_Conexión_Hora': r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
#     'FIN_de_Conexión_Dia': r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$',
#     'FIN_de_Conexión_Hora': r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
#     'Session_Time': r'^\d+(\.\d+)?$'
#     # 'MAC_AP':  r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}:HCDD$',
#     # 'MAC_Cliente': r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
# }

# def table():
#     table=[[f'{key}',f'{value}'] for key,value in expresiones_regulares.items()]
#     headers=['Columna','Expresión Regular']
#     table_final=tabulate(table,headers,tablefmt='fancy_grid')
#     print(table_final)



# # Cargar el archivo CSV como un DataFrame en Pandas utilizando multiprocessing
# def cargar_csv(path):
#     data=pd.read_csv(path,low_memory=False,usecols=expresiones_regulares.keys())
    
#     return data




# # Ruta y nombre de tu archivo CSV
# csv_file = './TP5v2/file/export-2019-to-now-v4.csv'

# # Cargar el archivo CSV utilizando multiprocessing
# with Pool() as pool:
#     data_frame = pd.concat(pool.map(cargar_csv, [csv_file]))

# # Crear DataFrames para los registros válidos e inválidos
# registros_validos = pd.DataFrame(columns=data_frame.columns)
# registros_invalidos = pd.DataFrame(columns=data_frame.columns)


# # Función para validar un registro
# def validar_registro(registro):
#     valido = True
#     for columna, valor in registro.items():
#         expresion_regular = expresiones_regulares.get(columna)
#         if expresion_regular:
#             if not re.match(expresion_regular, str(valor)):
#                 valido = False
#                 break
#     return valido


# # Validar cada registro del DataFrame utilizando multiprocessing
# with Pool() as pool:
#     resultados = pool.map(validar_registro, data_frame.to_dict('records'))

# # Dividir los registros válidos e inválidos
# for index, registro in enumerate(data_frame.iterrows()):
#     if resultados[index]:
#         registros_validos = pd.concat([registros_validos, registro[1]])
#     else:
#         registros_invalidos = pd.concat([registros_invalidos, registro[1]])

# # Mostrar los primeros 100 registros válidos
# primeros_registros_validos = registros_validos.head(100)
# print(primeros_registros_validos)
# ###
