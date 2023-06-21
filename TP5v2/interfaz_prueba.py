import re
import pandas as pd
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import radiolist_dialog, checkboxlist_dialog, input_dialog, message_dialog


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


def show_main_menu():

    # Definir las opciones para el menú principal
    main_menu_choices = [
        ('Filtrar CSV', 'filter'),
        ('Mostrar CSV filtrados', 'show'),
        ('Salir', 'exit')
    ]
    main_menu_selection = radiolist_dialog(
        title='Menú Principal',
        text='Seleccione una opción:',
        values=main_menu_choices
    ).run()

    return main_menu_selection


def get_csv_file():
    csv_file = input_dialog(
        title='Archivo CSV',
        text='Ingrese el nombre del archivo CSV a cargar:'
    ).run()
    return csv_file

def run_filtering(data_filter):
    # Obtener la fecha de inicio de la búsqueda
    date_start = input_dialog(
        title='Fecha de inicio',
        text='Ingrese la fecha de inicio de la búsqueda (YYYY-MM-DD): '
    ).run()

    # Obtener la fecha de fin de la búsqueda
    date_end = input_dialog(
        title='Fecha de fin',
        text='Ingrese la fecha de fin de la búsqueda (YYYY-MM-DD): '
    ).run()

    # Resto del código para validar las fechas y realizar el filtrado
    if date_start <= date_end:
        message_dialog(
            title='Fechas correctas',
            text='Fecha de inicio y fin correctas'
        ).run()

        # Realizar el filtrado
        data_filtered = data_filter[(data_filter['Inicio_de_Conexión_Dia'] >= date_start) & (data_filter['FIN_de_Conexión_Dia'] <= date_end)]

        # Mostrar los resultados en la interfaz
        message_dialog(
            title='Resultados',
            text=str(data_filtered)
        ).run()

        # Preguntar si desea exportar los datos
        export_response = message_dialog(
            title='Exportar datos',
            text='Desea exportar los datos? (Y/N):'
        ).run()

        if export_response.lower() == 'y':
            export_format = input_dialog(
                title='Formato de exportación',
                text='Desea exportar los datos en formato CSV o Excel? (CSV/Excel):'
            ).run()

            if export_format.lower() == 'csv':
                filename = input_dialog(
                    title='Nombre de archivo',
                    text='Ingrese el nombre del archivo CSV: '
                ).run()
                filename_csv = f'./TP5v2/export/{filename}.csv'
                data_filtered.to_csv(filename_csv, index=False)
                message_dialog(
                    title='Exportación exitosa',
                    text=f'Los datos han sido exportados a {filename_csv}'
                ).run()

            elif export_format.lower() == 'excel':
                filename = input_dialog(
                    title='Nombre de archivo',
                    text='Ingrese el nombre del archivo Excel: '
                ).run()
                filename_excel = f'./TP5v2/export/{filename}.xlsx'
                data_filtered.to_excel(filename_excel, index=False)
                message_dialog(
                    title='Exportación exitosa',
                    text=f'Los datos han sido exportados a {filename_excel}'
                ).run()

            else:
                message_dialog(
                    title='Opción incorrecta',
                    text='Opción de formato de exportación incorrecta'
                ).run()

    else:
        message_dialog(
            title='Fechas incorrectas',
            text='Fecha de inicio y/o fin incorrectas, volver a intentar'
        ).run()


def run_selection(data_filter):
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

    while True:
        columnas_a_aniadir = checkboxlist_dialog(
            title='Campos de la tabla',
            text='Seleccione los campos para la tabla:',
            values=[(num, opc) for num, opc in opciones_columnas.items()]
        ).run()

        if columnas_a_aniadir:
            for opcion in columnas_a_aniadir:
                lista_columnas.append(opciones_columnas[opcion])

            break

    data_filter_finally = data_filter[lista_columnas]
    print('\n')
    print(data_filter_finally)
    print('\n')
    export(data_filter_finally)


def main():
    csv_file = get_csv_file()

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
        'MAC_AP': r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}:HCDD$',
        'MAC_Cliente': r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
        # Razon de terminacion de sesioncon
    }

    data = pd.read_csv(csv_file, low_memory=False, usecols=expresiones_regulares.keys())
    data_filter = data

    for columna, patron in expresiones_regulares.items():
        regex = re.compile(patron)
        data_filter = data_filter[data_filter[columna].astype(str).str.match(regex)]

    while True:
        main_menu_selection = show_main_menu()

        if main_menu_selection == 'filter':
            data_filter = run_filtering(data_filter)
        elif main_menu_selection == 'select':
            run_selection(data_filter)
        elif main_menu_selection == 'show':
            print('Opción de Mostrar seleccionada')
        elif main_menu_selection == 'exit':
            break

        rta3 = prompt('¿Desea volver a consultar? (Y/N): ').lower()
        if rta3 != 'y':
            break

    print('Gracias por usar el programa')


if __name__ == '__main__':
    main()