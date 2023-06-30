from funciones import expresiones_regulares, guardar_DataFrame, last_conection
import pandas as pd
import re

csv_file = './TP5v2/file/export-2019-to-now-v4.csv'
data = pd.read_csv(csv_file, low_memory=False, usecols=expresiones_regulares.keys())

data_filter = data
data_total = data
data_filter_erronea = pd.DataFrame()  # Crear un DataFrame vacío para almacenar los datos filtrados
ubicacion_errores = pd.DataFrame()


# Devuelve los valores correctos junto a donde se encuentran los errores (TRue , False) -> Todos
for columna, patron in expresiones_regulares.items():
    regex = re.compile(patron)
    data_filter = data_filter[data_filter[columna].astype(str).str.match(regex)]  # Listo
    
    filter_mask = data[columna].astype(str).str.match(regex)  # Máscara booleana para los valores que cumplen con la expresión regular
    ubicacion_errores = ubicacion_errores._append(filter_mask)  # Agregar los datos filtrados al DataFrame
    
data_filter_correcta = data_filter

for columna, patron in expresiones_regulares.items():
    filtered_data = data[~filter_mask]  # Usar ~ para negar la máscara y obtener los valores que no cumplen
    data_filter_erronea = data_filter_erronea._append(filtered_data)  # Agregar los datos filtrados al DataFrame


ubicacion_errores = ubicacion_errores.T
        
ubicacion_errores_final = ubicacion_errores.loc[~(ubicacion_errores==True).all(axis=1)]

numero_fila = ubicacion_errores_final.index

tabla_errores = data_total[data_total.index.isin(numero_fila)]

tabla1=tabla_errores.reset_index(drop=True)
tabla2=ubicacion_errores_final.reset_index(drop=True)
tabla_unida_errores = pd.concat([tabla1, tabla2], axis=1)


continuar = True
while continuar is True:
    last_conection(data_filter_correcta)
    rta4 = input('Desea guardar los errores encontrados en un archivo? (Y/N): ').lower()
    if rta4 == 'y':
        guardar_DataFrame(tabla_unida_errores)

    rta7 = input('¿Desea volver a consultar? (Y/N):\nRespuesta: ').lower()
    if rta7 == 'y':
        pass
    elif rta7 == 'n':
        continuar = False
    else:
        print(' Opción incorrecta, volver a ingresar')
    
