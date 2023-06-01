global entrada, index
entrada = input('Cadena de numeros: ')
index = 0
digitos = {'0','1','2','3','4','5','6','7','8','9','.','E'}

print(index)
def estado_0(entrada, index):
    if entrada[index] == '+' or entrada[index] == '-':
       
        index += 1 
        
        estado_1(entrada, index)
    elif entrada[index] in digitos:
        
        index += 1
        
        estado_2(entrada, index)
    else:
       
        error(entrada, index)


def estado_1(entrada, index):
    if entrada[index] in digitos:
        
        index += 1
       
        estado_2(entrada, index)
    else:
        
        error(entrada, index)


def estado_2(entrada, index):
    
    for caracter in entrada:
        if index == len(entrada):
            
            esatdo_8(entrada, index)
            
        elif  caracter == '.':
           
            index += 1
           
            estado_3(entrada,index)
        elif caracter == 'E':
            
            index += 1
            
            estado_5(entrada, index)
        elif (caracter in digitos) and ((caracter != '.') or (caracter != 'E')):
           
            index += 1
        else:
            
            error(entrada, index)


def estado_3(entrada, index):
    if entrada[index] in digitos:
        
        index += 1
      
        estado_4(entrada, index)
    else:
        
        error(entrada, index)

def estado_4(entrada, index):

    for caracter in entrada:
        if index == len(entrada):
            
            esatdo_8(entrada, index)
        
        elif caracter == 'E':
           
            index += 1
            
            estado_5(entrada, index)
        elif (caracter in digitos) and (caracter != 'E'):
            
            index += 1
         
        else:
            
            error(entrada, index)


def estado_5(entrada, index):
    if entrada[index] == '+' or entrada[index] == '-':
       
        index += 1 
       
        estado_6(entrada, index)
    elif entrada[index] in digitos:
        
        index += 1

        estado_7(entrada, index)
    else:
        
        error(entrada, index)



def estado_6(entrada, index):
    if entrada[index] in digitos:
       
        index += 1
       
        estado_7(entrada, index)
    else:
        
        error(entrada, index)


def estado_7(entrada, index):
    for caracter in entrada:
        if index == len(entrada):
            
            esatdo_8(entrada, index)
        
        elif (caracter in digitos) and (caracter != 'E'):
            index += 1
        else:
            error(entrada, index)

def esatdo_8(entrada, index):
    print(f'ESTADO FINAL, el número {entrada} está correctamente escrito')
    #Estado final -> "correcto"

def error(entrada, index):
    #Si el número posee algún error
    print(f'ERROR, el número {entrada} posee un error de escritura en la posción {index+1}')


estado_0(entrada, index)