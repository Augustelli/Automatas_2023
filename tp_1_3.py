
entrada = input('Entrada de cadena de numeros: ')
global index
index = 0
digitos = {'0','1','2','3','4','5','6','7','8','9','.','E'}


def est_0(entrada, index):
    if entrada[index] == '+' or entrada[index] == '-':
        index += 1
        est_1(entrada, index)
    elif entrada[index] in digitos:
        index += 1
        est_2(entrada, index)
    else:
        error(entrada, index)


def est_1(entrada, index):
    if entrada[1] in digitos:
        est_2(entrada, index)
    else:
        error(entrada, index)

def est_2(entrada, index):
    for i in range(index,len(entrada)+1):
        if entrada[i] in digitos:
            index += 1
            continue
        elif entrada[i] == '.':
            est_3(entrada, index)
        elif entrada[i] == 'E':
            est_5(entrada, index)
        elif index == len(entrada) + 1:
            est_8(entrada, index)
        else:
            error(entrada, index)


def est_3(entrada, index):
    if entrada[index+1] in digitos:
        index += 1
        est_4(entrada, index)


def est_4(entrada, index):
    for i in range(index,len(entrada)+1):
        if entrada[i] in digitos:
            index += 1
            continue
        elif entrada[i] == 'E':
            est_5(entrada, index)
        elif index == len(entrada):
            est_8(entrada, index)
        else:
            error(entrada, index)


def est_5(entrada, index):
    if entrada[index] == '+'or entrada[index] == '-':
        index += 1
        est_6(entrada, index)
    elif entrada[index] in digitos:
        est_7(entrada, index)
    else:
        error(entrada, index)


def est_6(entrada, index):
    if entrada[index] in digitos:
        index += 1
        est_7(entrada, index)
    else:
        error(entrada, index)
def est_7(entrada, index):
    for i in range(index, len(entrada)+1):
        if entrada[i] in digitos:
            index += 1
            continue
        if index == len(entrada) + 1:
            est_8(entrada,index)
        else:
            error(entrada, index)
        
def est_8(entrada, index):
    print(f'La cadena: {entrada} es correcta')


def error(entrada, index):
    print(f'La cadena {entrada} tiene error en la posición {index}')


est_0(entrada, index)