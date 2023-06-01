import re
print('Qué expresión regular desea verificar?')
print('1: validación de fecha\n'
      '2: validación de número real\n'
      '3: validación de ID de video de Youtube\n'
      '4: validación de mail de la universidad\n'
      '5: validación de número de celular argentino\n'
      '6: validación de CUIL\n'
      '7: validación de contraseña')


opcion = int(input('Ingrese el número de la opción: '))




def validacion_fecha(fecha):
    patron = re.compile(r'^(0[1-9]|[1-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])(\/|-)\d{4}$')
   
    if patron.match(fecha):
        print('La fecha ingresada es correcta')
    else:
        print('La fecha ingresada es incorrecta')






def num_real(numero):
    patron=re.compile(r'^-?(?:(?:\d{1,3},)*\d{1,3}|\d+)(?:\.\d{2})?$')
    if patron.match(numero):
        print('El número ingresado es correcto')
    else:
        print('El numero ingresado es incorrecto')


def video_youtube(string):
    patron=re.compile(r'^[a-zA-Z0-9_-]{11}$')
    if patron.match(string):
        print('El ID ingresado es correcto')
    else:
        print('El ID ingresado es incorrecto')






def mail_uni(mail):
    patron=re.compile(r'^[a-z]{2}\.[a-z]+@(alumno\.um\.edu\.ar)$')
    if patron.match(mail):
        print('El mail ingresado es correcto')
    else:
        print('El mail ingresado es incorrecto')






def telefono_arg(cel):
    patron=re.compile(r'^54[9](11|[2368][1-9])15[0-9]{7}$')
    if patron.match(cel):
        print('El celular ingresado es correcto')
    else:
        print('El  celular es incorrecto')






def Cuil(cuil_usr):
    patron=re.compile(r'[0-9]{2}(-)[0-9]{8}(-)[0-9]{1}$')
    if patron.match(cuil_usr):
        print('El CUIL ingresado es correcto')
    else:
        print('El  CUIL es incorrecto')




def password(contraseña):
    patron=re.compile(r'^(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*()-_+=])(?!.*\s).{8,16}$')
    if patron.match(contraseña):
        print('La contraseña ingresada es correcta')
    else:
        print('La contraseña ingresada es incorrecta')






if opcion == 1:
    fecha = input('Ingrese una fecha (dd/mm/aaaa) o (dd-mm-aaaa): ')
    verificacion=validacion_fecha(fecha)
elif opcion == 2:
   
    numero = input('Ingrese un número real con dos decimales(punto) y separador de miles(coma) positivo o negativo ')
    verificacion1=num_real(numero)
elif opcion == 3:
    string=input('Ingrese el ID de Youtube')
    verificacion2=video_youtube(string)
elif opcion == 4:
    mail=input('Ingrese su mail de la universidad')
    verificacion3=mail_uni(mail)
elif opcion == 5:
    cel=input('Ingrese el numero de celular con código de pais (54), de provincia (ej 11 BsAS, 26 Mendoza) seguido de 15(numero de celular)  ')
    verificacion4=telefono_arg(cel)
elif opcion == 6:
   
    cuil_usr=input('Ingrese el cuil (nn-dni-verficicador):  ')
    verificacion5=Cuil(cuil_usr)
elif opcion == 7:
    contraseña=input()
    verificacion5=password(contraseña)
else:
    print('Opción incorrecta')
