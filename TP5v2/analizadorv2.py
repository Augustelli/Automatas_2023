import re
import pandas as pd
import pdb
import ciso8601
from concurrent.futures import ThreadPoolExecutor


def last_conection(data_filter):
    correcto = True
    seguir = True
    lista_columnas = []
    opciones_columnas = {
        '1': 'ID',
        '2': 'ID_Sesion',
        '3': 'ID_Conexión_unico',
        '4': 'Usuario',
        '5': 'IP_NAS_AP',
        '6': 'Inicio_de_Conexión_Dia',
        '7': 'Inicio_de_Conexión_Hora',
        '8': 'FIN_de_Conexión_Dia',
        '9': 'FIN_de_Conexión_Hora',
        '10': 'Session_Time',
        '11': 'MAC_AP',
        '12': 'MAC_Cliente',
    }
    date_start = input('Ingrese la fecha de inicio de la busqueda (YYYY-MM-DD): ')
    date_end = input('Ingrese la fecha de fin de la busqueda (YYYY-MM-DD): ')
    patron_start = re.compile(r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$')
    patron_end = re.compile(r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$')

    if (patron_start.match(date_start) and patron_end.match(date_end)) and (date_start <= date_end):
        print('Fecha de inicio y fin correctas')
        while correcto is True:
            rta2 = input(' Desea ver:\n\
                        1. los usuarios que han iniciado y finalizado su conexión en el intervalo de tiempo \n\
                        2.  Su conexión haya terminado en el intervalo de tiempo\n\
                        Respuesta : ')
            if rta2 == '1':
                correcto = False
                data_filter = data_filter[(data_filter['Inicio_de_Conexión_Dia'] >= date_start) & (data_filter['FIN_de_Conexión_Dia'] <= date_end)]
            elif rta2 == '2':
                correcto = False
                data_filter = data_filter[(data_filter['FIN_de_Conexión_Dia'] >= date_start) & (data_filter['FIN_de_Conexión_Dia'] <= date_end)]
            else:
                print(f'Opción {rta2} incorrecta, intente denuevo. ')

        while seguir:
            columnas_a_aniadir = input('''Seleccione los campos para la tabla:\n
                    1: ID
                    2: ID_Sesion
                    3: ID_Conexión_unico
                    4: Usuario
                    5: IP_NAS_AP
                    6: Inicio_de_Conexión_Dia
                    7: Inicio_de_Conexión_Hora
                    8: FIN_de_Conexión_Dia
                    9: FIN_de_Conexión_Hora
                    10: Session_Time
                    11: MAC_AP
                    12: MAC_Cliente
                    E: Salir\nRespuesta:  ''')
            if columnas_a_aniadir in opciones_columnas.keys():
                lista_columnas.append(opciones_columnas[columnas_a_aniadir])
            else:
                seguir = False
        data_filter_finally = (data_filter[lista_columnas])
        print('\n')
        print(data_filter_finally)
        print('\n')
        export(data_filter_finally)
    else:
        print('Fecha de inicio y/o fin incorrectas, volver a intentar')
        last_conection(data_filter)


def export(data_filter_finally):
    rta = input('Desea exportar los datos? (Y/N):').lower()
    if rta == 'y':
        rta1 = input('Desea exportar los datos en formato CSV o Excel? (CSV/Excel):').lower()
        if rta1 == 'csv':
            nombre_archivo = input('Nombre del archvo: ')
            ruta_csv = f'./TP5v2/export/{nombre_archivo}.csv'
            data_filter_finally.to_csv(ruta_csv, index=False)
        if rta1 == 'excel':
            nombre_archivo = input('Nombre del archvo: ')
            ruta_excel = f'./TP5v2/export/{nombre_archivo}.xlsx'
            data_filter_finally.to_excel(ruta_excel, index=False)
    else:
        print('Gracias por usar el programa')

def guardar_DataFrame(dataframe):
    pd.set_option('display.width', None)  # Desactivar el ajuste automático del ancho
    pd.set_option('display.max_columns', None)  # Mostrar todas las columnas

    # Guardar el DataFrame en un archivo CSV
    dataframe.to_csv('output.csv', index=False)

    # Restaurar la configuración predeterminada de Pandas
    pd.reset_option('display.width')
    pd.reset_option('display.max_columns')
    

expresiones_regulares = {
    'ID': r'^\d{6,7}$',
    'ID_Sesion': r'^[A-F0-9]{8}-[A-F0-9]{8}$',
    'ID_Conexión_unico': r'^[a-f0-9]{16}$',
    'Usuario': r'^[a-zA-Z-]{3,25}$',
    'IP_NAS_AP': r'^192\.168\.247\.[0-9]{2}$',
    'Inicio_de_Conexión_Dia': r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$',
    'Inicio_de_Conexión_Hora': r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
    'FIN_de_Conexión_Dia': r'^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]|3[01])$',
    'FIN_de_Conexión_Hora': r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$',
    'Session_Time': r'^\d+(\.\d+)?$',
    'MAC_AP':  r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}:HCDD$',
    'MAC_Cliente': r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    # Razon de terminacion de sesioncon
}

csv_file = './TP5v2/file/export-2019-to-now-v4.csv'
data = pd.read_csv(csv_file, low_memory=False, usecols=expresiones_regulares.keys())

data_filter = data
data_filter_erronea = pd.DataFrame()  # Crear un DataFrame vacío para almacenar los datos filtrados
ubicacion_errores = pd.DataFrame()

for columna, patron in expresiones_regulares.items():
    regex = re.compile(patron)
    data_filter = data_filter[data_filter[columna].astype(str).str.match(regex)]
    
    filter_mask = data[columna].astype(str).str.match(regex)  # Máscara booleana para los valores que cumplen con la expresión regular
    ubicacion_errores = ubicacion_errores._append(filter_mask)  # Agregar los datos filtrados al DataFrame
    
    filtered_data = data[~filter_mask]  # Usar ~ para negar la máscara y obtener los valores que no cumplen
    data_filter_erronea = data_filter_erronea._append(filtered_data)  # Agregar los datos filtrados al DataFrame

# print(data_filter_erronea)
# print(ubicacion_errores.T)


ubicacion_errores = ubicacion_errores.T
# Suponiendo que ya tienes el DataFrame `df`

# Establecer la configuración para la escritura en CSV

guardar_DataFrame(data_filter_erronea)
guardar_DataFrame(ubicacion_errores)

# tabla1=data_filter_erronea.reset_index(drop=True)

# # print(len(ubicacion_errores))  # Trae todos los registros 

# df_filtered = ubicacion_errores[~ubicacion_errores.all(axis=1)]
# # ubicacion_errores = ubicacion_errores.drop(ubicacion_errores.index[ubicacion_errores.all(axis=1)])  #  SOlo los registros que tienen al menos un error
# print(len(df_filtered))
# print(len(data_filter_erronea))
# tabla2=ubicacion_errores.reset_index(drop=True)
# ubicacion_errores_final = pd.concat([tabla1,tabla2], axis=1)
# ubicacion_errores_final = pd.concat([data_filter_erronea,ubicacion_errores], axis=1)
# ruta_csv_error= f'./TP5v2/export/error.csv'
# ubicacion_errores_final.to_csv(ruta_csv_error, index=False)


# mask_elim = ubicacion_errores.all(axis=1)
# culo=ubicacion_errores.drop(ubicacion_errores[mask_elim].index)
# print(len(culo))

# data_filter = data

# for columna, patron in expresiones_regulares.items():
#     regex = re.compile(patron)
#     data_filter = data_filter[data_filter[columna].astype(str).str.match(regex)]
# # print(data_filter)
# data_filter_correcta = data_filter
# continuar = True
# while continuar is True:
#     last_conection(data_filter)
#     rta3 = input('¿Desea volver a consultar? (Y/N):\nRespuesta: ').lower()
#     if rta3 == 'y':
#         pass
#     elif rta3 == 'n':
#         continuar = False
#     else:
#         print(' Opción incorrecta, volver a ingresar')

