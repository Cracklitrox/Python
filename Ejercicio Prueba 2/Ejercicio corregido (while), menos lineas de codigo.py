from multiprocessing.sharedctypes import Value
from re import M
from statistics import mode
from tracemalloc import stop
cont_user=0;
cont_fecha=0;
Flag=True
while Flag == True:
    print('.................\n  Opciones Duoc\n.................\n\n(1). registrar\n(2). consultar\n(3). fechas\n(4). salir\n\n.................\n\n');
    try:
        op=int(input("Seleccione una opción: "));
        print();
        if op == 1:
            if cont_user == 0:
                while Flag == True:
                    cont=0;
                    cont1=0;
                    try:
                        print('Ingrese 6 caracteres en su patente (3 numeros y 3 letras)\n\n');
                        patente=input('Ingrese su patente: ');
                        print();
                        if len(patente) == 6:
                            for x in patente:
                                if x.isalpha() == True:
                                    cont+=1
                                elif x.isalnum() == True:
                                    cont1+=1
                            if cont == 3 and cont1 == 3:
                                break
                            else:
                                print('Ingrese 3 letras y 3 numeros, de lo contrario, no se registrara su patente.\n\n');
                        else:
                            print('Ingrese solamente 6 caracteres\n\n');
                    except ValueError:
                        print('Digite correctamente.\n\n');
                while Flag == True:
                    try:
                        marca=input("Ingrese la marca de su automovil: ");
                        print();
                        break
                    except ValueError:
                        print('Ingrese correctamente la marca de su automovil.\n\n');
                while Flag == True:
                    try:
                        modelo=input("Ingrese el modelo de su automovil: ");
                        print();
                        break
                    except ValueError:
                        print('Ingrese correctamente el modelo de su automovil.\n\n');
                while Flag == True:
                    try:
                        año_vehiculo=int(input("Ingrese el año de fabricación de su vehiculo: "));
                        print();
                        if año_vehiculo >= 1900 and año_vehiculo <= 2020:
                            break
                        else:
                            print(f'El año ingresado: {año_vehiculo} no es valido dentro del sistema, por favor ingrese correctamente el año.\n\n');
                    except ValueError:
                        print('Ingrese correctamente el año de fabricación de su automovil.\n\n');
                while Flag == True:
                    try:
                        tipo=input("Ingrese el tipo de vehiculo al cual pertenece (b,d,e,h): ");
                        print();
                        if tipo == 'b' or tipo == 'B' or tipo == 'd' or tipo == 'D' or tipo == 'e' or tipo == 'E' or tipo == 'h' or tipo == 'H':
                            print('Se ha registrado correctamente los datos ingresados\n\nSera rediccionado al menu de inicio.\n\n');
                            cont_user+=1
                            break
                        else:
                            print(f'El caracter digitado: {tipo} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n');
                    except ValueError:
                        print('Ingrese correctamente el tipo de vehiculo.\n\n');
            else:
                print('Ya existe un usuario registrado, por favor, seleccione otras opciones.\n\n');
        elif op == 2:
            if cont_user == 0:
                print('No se ha registrado ninguna patente dentro del sistema, por favor, seleccione la opción 1.\n\n');
            else:
                if cont_fecha == 0:
                    while Flag == True:
                        try:
                            patente_verificacion=input("Ingrese su patente: ");
                            print();
                            if patente_verificacion == patente:
                                break
                            else:
                                print(f'La patente ingresada: {patente_verificacion} no se encuentra registrada dentro del sistema, intentelo nuevamente\n\n');
                        except ValueError:
                            print('Ingrese correctamente la patente.\n\n');
                    fecha_inicio=input("Ingrese la fecha de su revisión: ");
                    print();
                    revicion_inicial=input("Ingrese los cambios hechos: ");
                    print();
                    print("----------------------------------------------------------------------------");
                    print(f"La primera revición fue en la fecha:\t{fecha_inicio}\n\nEl registro de la revicion fue:\t{revicion_inicial}");
                    print("----------------------------------------------------------------------------\n\n");
                    cont_fecha+=1
                else:
                    while Flag == True:
                        try:
                            patente_verificacion=input("Ingrese su patente: ");
                            print();
                            if patente_verificacion == patente:
                                break
                            else:
                                print(f'La patente ingresada: {patente_verificacion} no se encuentra registrada dentro del sistema, intentelo nuevamente\n\n');
                        except ValueError:
                            print('Ingrese correctamente la patente.\n\n');
                    fecha_final=input("Ingrese la fecha de su revisión: ");
                    print();
                    revicion_final=input("Ingrese los cambios hechos: ");
                    print();
                    print("----------------------------------------------------------------------------");
                    print(f"El ingreso la primera revision fue:\t{fecha_inicio}\n\nEl registro de la revicion inicial fue:\t{revicion_inicial}\n\nLa ultima fecha de la revicion fue:\t{fecha_final}\n\nEl registro de la revicion fue:\t{revicion_final}");
                    print("----------------------------------------------------------------------------\n\n");
                    cont_fecha+=1
        elif op == 3:
            if cont_user == 0:
                print('No se ha registrado ninguna patente dentro del sistema, por favor, seleccione la opción 1.\n\n');
            else:
                while Flag == True:
                    try:
                        patente_verificacion=input("Ingrese su patente: ");
                        print();
                        if patente_verificacion == patente:
                            break
                        else:
                            print(f'La patente ingresada: {patente_verificacion} no se encuentra registrada dentro del sistema, intentelo nuevamente\n\n');
                    except ValueError:
                        print('Ingrese correctamente la patente.\n\n');
                print(f"----------------------------------------------------------------------------\n                           Datos Cliente                                    \n\nSu patente es:\t{patente}\n\nLa marca de su auto es:\t{marca}\n\nEl modelo de su automovil es:\t{modelo}\n\nEl año de fabricación de su carro es:\t{año_vehiculo}\n\nEl tipo de gasolina que usa su vehiculo es:\t{tipo}\n----------------------------------------------------------------------------\n\n");
        elif op == 4:
            if cont_user == 0:
                print('No se ha registrado ninguna patente dentro del sistema, aun asi lo dejare salir, vuelva pronto');
                Flag=False;
            else:
                print('Cerrando seción.');
                Flag=False;
        else:
            print(f'El digito ingresado: {op} no se encuentra entre las opciones del sistema, por favor, intentelo nuevamente.\n\n');
    except ValueError:
        print('Digite correctamente.\n\n');