import numpy as np,time
patentes=[];
marcas=[];
precios=[];
montos=[];
dias=[];
meses=[];
años=[];
nombres=[];
matriz=np.array(patentes,marcas);
matriz1=np.array(precios,montos);
matriz2=np.array(dias,meses);
matriz3=np.array(años,nombres);
def opcion1():
    while True:
        print("Ingrese 6 letras\n");
        try:
            patente=input("Ingrese su patente:\t");
            print();
            if len(patente) == 6:
                if patente.isalpha() == True:
                    patentes.append(patente);
                    break
                else:
                    print(f"La patente ingresada contiene numeros o espacios, solo digite lo necesario, intentelo nuevamente\n");
            else:
                print(f"La patente ingresada debe ser de 6 de largo, intentelo nuevamente\n");
        except ValueError:
            print(f"\nDigite solo palabras y numeros\n");
    while True:
        print(f"Ingrese entre 2 y 15 caracteres\n");
        try:
            marca=input("Ingrese la marca de su automovil:\t");
            print();
            if len(marca) >= 2 and len(marca) <= 15:
                marcas.append(marca);
                break
            else:
                print(f"La marca ingresada:\t{marca} no cumple la condición pedida, intentelo nuevamente\n");
        except ValueError:
            print(f"\nSolo digite caracteres\n");
    while True:
        print(f"El precio del vehiculo debe ser mayor a $5.000.000\n");
        try:
            precio=int(input("Ingrese el precio del vehiculo:\t"));
            print();
            if precio >= 5000000:
                precios.append(precio);
                break
            else:
                print(f"El precio ingresado:\t{precio} es menor al requerido, intentelo nuevamente\n");
        except ValueError:
            print("\nSolo digite numeros\n");
    while True:
        try:
            validacion=input(f"¿El auto tiene alguna multa? (Si o No):\t");
            print();
            if validacion == 'Si' or validacion == 'si' or validacion == 'SI' or validacion == 'S' or validacion == 's':
                monto=int(input("Ingrese el valor de la multa (Desde $1.500 hasta $3.500):\t"));
                print();
                dia=int(input("Ingrese el dia en que tuvo su multa:\t"));
                print();
                mes=int(input("-------------\n    Meses    \n-------------\n(1) Enero\n(2) Febrero\n(3) Marzo\n(4) Abril\n(5) Mayo\n(6) Junio\n(7) Julio\n(8) Agosto\n(9) Septiembre\n(10) Octubre\n(11) Noviembre\n(12) Diciembre\n\nIngrese el número en que tuvo su multa:\t"));
                print();
                año=int(input("Ingrese el año en que tuvo su multa (Desde 1900 hasta 2023):\t"));
                print();
                if monto >= 1500 and monto <= 3500:
                    if dia >= 1 and dia <= 31:
                        if mes >=1 and mes <= 12:
                            if año >= 1900 and año <= 2023:
                                montos.append(monto);
                                dias.append(dia);
                                meses.append(mes);
                                años.append(año);
                                break
                            else:
                                print(f"El año ingresado:\t{año} no es valido, intentelo nuevamente\n");
                        else:
                            print(f"El mes ingresado:\t{mes} no es valido, intentelo nuevamente\n");
                    else:
                        print(f"El dia ingresado:\t{dia} no es valido, intentelo nuevamente\n");
                else:
                    print(f"El monto ingresado:\t{monto} es menor o mayor al rango requerido, intentelo nuevamente\n");
            elif validacion == 'NO' or validacion == 'no' or validacion == 'No' or validacion == 'n' or validacion == 'N':
                montos.append(0);
                dias.append(0);
                meses.append(0);
                años.append(0);
                break
            else:
                print(f"Lo ingresado:\t{validacion} no se encuentra registrado en el sistema, intentelo nuevamente\n");
        except ValueError:
            print(f"\nIngrese solo palabras y numeros\n");
    while True:
        try:
            nombre=input("Ingrese el nombre del dueño del automovil:\t");
            print();
            if nombre.isalpha() == True:
                print(f"Los datos fueron registrados exitosamente\n");
                nombres.append(nombre);
                break
            else:
                print(f"El nombre ingresado:\t{nombre} no es valido, intentelo nuevamente\n");
        except ValueError:
            print("\nSolo digite palabras\n");
def opcion2():
    while True:
        print("Ingrese 6 letras\n");
        try:
            patente_comprobacion=input("Ingrese su patente:\t");
            print();
            if len(patente_comprobacion) == 6:
                if patente_comprobacion.isalpha() == True:
                    if patente_comprobacion in patentes:
                        a=patentes.index(patente_comprobacion);
                        if montos[a] == 0:
                            time.sleep (1)
                            print(f"-----------------------------\n    Los datos del cliente {nombres[a]} son    \n-----------------------------\n\nSu patente es:\t{patentes[a]}\nLa marca de su automovil es:\t{marcas[a]}\nEl precio de su automovil es:\t{precios[a]}\n");
                            break
                        else:
                            time.sleep (1)
                            print(f"-----------------------------\n    Los datos del cliente {nombres[a]} son    \n-----------------------------\nSu patente es:\t{patentes[a]}\nLa marca de su automovil es:\t{marcas[a]}\nEl precio de su automovil es:\t{precios[a]}\nEl monto de su multa es:\t{montos[a]}\nLa fecha de su multa es:\t{dias[a]}/{meses[a]}/{años[a]}\n");
                            break
                    else:
                        print(f"La patente ingresada no esta registrado en la base de datos, intentelo nuevamente\n");
                else:
                    print(f"La patente ingresada contiene numeros o espacios, solo digite lo necesario, intentelo nuevamente\n");
            else:
                print(f"La patente ingresada debe ser de 6 de largo, intentelo nuevamente\n");
        except ValueError:
            print(f"\nDigite solo palabras y numeros\n");
def opcion3():
    while True:
        print("Ingrese 6 letras\n");
        try:
            patente_comprobacion=input("Ingrese su patente:\t");
            print();
            if len(patente_comprobacion) == 6:
                if patente_comprobacion.isalpha() == True:
                    if patente_comprobacion in patentes:
                        b=patentes.index(patente_comprobacion);
                        funcion_op3(b);
                        break
                    else:
                        print(f"La patente ingresada no esta registrado en la base de datos, intentelo nuevamente\n");
                else:
                    print(f"La patente ingresada contiene numeros o espacios, solo digite lo necesario, intentelo nuevamente\n");
            else:
                print(f"La patente ingresada debe ser de 6 de largo, intentelo nuevamente\n");
        except ValueError:
            print(f"\nDigite solo palabras y numeros\n");
def funcion_op3(a):
    while True:
        print("--------------------\n    Certificados    \n--------------------\n");
        print("(1) Emisión de contaminantes\n(2) Anotaciones vigentes\n(3) Multas\n(4) Salir\n");
        try:
            op1=int(input("Seleccione una opción:\t"));
            print();
            if op1 == 1:
                time.sleep (1)
                print(f"Certificado de emisión de contaminantes\nLa patente es:\t{patentes[a]}\nEl nombre del dueño es:\t{nombres[a]}\n");
                break
            elif op1 == 2:
                time.sleep (1)
                print(f"Certificado de anotaciones vigentes\nLa patente es:\t{patentes[a]}\nEl nombre del dueño es:\t{nombres[a]}\n");
                break
            elif op1 == 3:
                time.sleep (1)
                print(f"Certificado de multa\nEl valor de la multa fue de:\t${montos[a]}\nLa patente es:\t{patentes[a]}\nEl nombre del dueño es:\t{nombres[a]}\n");
                break
            elif op1 == 4:
                break
            else:
                print(f"La opcion ingresada:\t{op1} no es valida, intentelo nuevamente\n");
        except ValueError:
            print("\nSolo digite numeros\n");
def despedida():
    return print(f"Cerrando aplicacion\nCreado por Carlos Gacitúa y Joaquin Calderón\nVersion 1.0\n");