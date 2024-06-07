import time
import os
import csv


print('Bienvenido a la App Champs LoL!')
time.sleep(1)
os.system('cls')

titulos = ['Identificador', 'Nombre', 'Anio de lanzamiento']
try:
    with open('lol_champs.csv', 'x', newline='') as archive:
        escritor = csv.writer(archive)
        escritor.writerow(titulos)
except:
    pass
opciones = (1, 2, 3)
matriz = []

while True:
    time.sleep(1)
    os.system('cls')
    while True:
        print('\tMénu\n\t1. Agregar campeón\n\t2. Ver información de campeones\n\t3. Salir')
        try:
            opc = int(input('\tIngrese una opción: '))
            if opc in opciones:
                break
            else:
                print('ERROR! debe ingresar una opción valida, opciones validas(1,2,3)!')
            time.sleep(1)
            os.system('cls')
        except:
            print('ERROR! debe ingresar un número entero!')

    if opc == 1:
        print('Agregar campeón!')
        time.sleep(1)
        os.system('cls')
        while True:
            try:
                identificador = int(input('Ingrese un id: '))
                if identificador >= 1 and identificador <= 168:
                    print('Id registrado!')
                    time.sleep(1)
                    os.system('cls')
                    break
                else:
                    print('ERROR! debe ingresar un ID que este dentro de 1 a 168!')
                time.sleep(1)
                os.system('cls')
            except:
                print('ERROR! debe ingresar un número entero!')

        with open('lol_champs.csv', 'a+', newline='') as archive:
            lector = csv.reader(archive)
            band = False
            for fila in lector:
                if fila[0] == identificador:
                    print('EL ID YA SE ENCUENTRA REGISTRADO!')
                    time.sleep(1)
                    band = True

        if band == True:
            print('EL ID YA SE ENCUENTRA REGISTRADO!')
            time.sleep(1)
            continue

        while True:
            nombre = str(input('Ingrese el nombre del campeón: '))
            if len(nombre.strip()) >= 2:
                print('Nombre registrado!')
                time.sleep(1)
                os.system('cls')
                break
            else:
                print('ERROR! el nombre debe contener al menos 2 letras!')
            time.sleep(1)
            os.system('cls')

        while True:
            try:
                anio = int(
                    input('Ingrese el año de lanzamiento del campeón: '))
                if anio >= 2009 and anio <= 2024:
                    print('Año de lanzamiento registrado!')
                    time.sleep(1)
                    os.system('cls')
                    break
                else:
                    print(
                        'ERROR! debe ingresar un año valido, el año debe estar dentro de los años 2009 a 2024!')
                time.sleep(1)
                os.system('cls')
            except:
                print('ERROR! debe ingresar números enteros!')

        campeon_agregar = [identificador, nombre, anio]

        with open('lol_champs.csv', 'r+', newline='') as archive:
            lector = csv.reader(archive)
            for campeon in lector:
                matriz.append(campeon)
            matriz.append(campeon_agregar)

            escritor = csv.writer(archive)
            escritor.writerows(matriz)
        print('CAMPEON AGREGADO!')

    elif opc == 2:
        print('Información de campeones!')
        time.sleep(1)
        os.system('cls')
        while True:
            with open('lol_champs.csv', 'r', newline='') as archive:
                lector = csv.reader(archive)
                for x in lector:
                    print(x)
            mensaje = str(
                input('¿Deseas salir? Ingrese ("S":Salir)("N":Redirigir): '))
            if mensaje.upper() in ("S", "N"):
                if mensaje.upper() == "S":
                    print('Saliendo.')
                    time.sleep(1)
                    os.system('cls')
                    break
                elif mensaje.upper() == "N":
                    print('Redirigiendo.')
                    time.sleep(1)
                    os.system('cls')
                else:
                    print(
                        'ERROR! debe ingresar una opción valida, opciones validas("S" o "N")!')
                time.sleep(1)
                os.system('cls')
    else:
        for t in range(1, 4):
            print('Saliendo de champs lol', ('.'*t))
            time.sleep(1)
            os.system('cls')
        break
