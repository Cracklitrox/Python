from statistics import mode


print("-------Bienvenido a ServiExpress-------\n");
listaAutos=[];
listaRegistro=[];

while True:
    print("Elija una opción");
    print("1.- Registrar automóvil.");
    print("2.- Registrar mantenimiento.");
    print("3.- Consultar automóvil.");
    print("4.- Salir.");
    try:
        opcion=int(input("Opcion elegida: "));
        if opcion>0 and opcion<5:
            if opcion==1:
                print("Eligió la opción 1: ");
                while True:
                    try:
                        patente=input("Ingrese una patente: ");
                        if len(patente)==6 and patente.isalnum():
                            listaAutos.append(patente);
                            break;
                        else:
                            print("Ingrese una patente válida.");
                    except ValueError:
                        print("Valor inválido.")
                while True:
                    agno=int(input("Ingrese la año de fabricación: "));
                    if agno>=1900 and agno<=2021:
                        listaAutos.append(agno);
                        break;
                    else:
                        print("ingrese un año válido");
                while True:
                    tipo_vehiculo=input("Ingrese el tipo de vehículo (d/b/h/e): ");
                    if tipo_vehiculo=='d' or tipo_vehiculo=='b' or tipo_vehiculo=='h' or tipo_vehiculo=='e':
                        listaAutos.append(tipo_vehiculo);
                        break;
                    else:
                        print("ingrese un tipo válido.");
                while True:
                    marca=input("Ingrese la marca: ")
                    if len(marca)>=2:
                        listaAutos.append(marca);
                        break;
                    else:
                        print("No puede estar vacío. Ingrese una marca.");
                while True:        
                    modelo=input("Ingrese la modelo: ")
                    if len(modelo)>=2:
                        listaAutos.append(modelo);
                        break;
                    else:
                        print("No puede estar vacío. Ingrese un modelo.");
                listaAutos.append(modelo);
            if opcion==2:
                while True:
                    print("Eligió opción 2:\n");
                    patente2=input("Ingrese patente para ingresar mantenimiento: ");
                    if patente2==listaAutos[0]:
                        #Deben validar el ingreso de la fecha y una observación, que no esté vacía.
                        fecha=input("Ingrese la fecha: ");
                        observacion=input("ingrese la observación: ");
                        listaRegistro.append(fecha);
                        listaRegistro.append(observacion);
                        listaAutos.extend(listaRegistro);
                        print("Se registró exitosamente.")
                        break;
                    else:
                        print("Ingrese una patente válida");
            if opcion==3:
                while True:
                    print("Eligió la opción 3: ")
                    patente3=input("Ingrese patente para consultar: ");
                    if patente3==listaAutos[0]:
                        print("Los datos del automóvil son los siguientes: ", listaAutos);
                        break;
                    else:
                        print("La patente no existe. Vuelva a intentarlo.")
            if opcion==4:
                print("------Cerrando sesión------\n")
                break;
        else:
            print("ingrese una opcion válida");
    except ValueError:
        print("Ingresó un caracter. Vuelva a intertarlo.")