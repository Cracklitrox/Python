import numpy as np
nombre_cliente=[];
rut_cliente=[];
telefono_cliente=[];
banco_cliente=[];
asiento_cliente=[];
i=0;
asientos=np.full((7,6),'  ');
for x in range(7):
    for z in range(6):
        i+=1;
        asientos[x][z]=i
matriz_clientes=(nombre_cliente,rut_cliente,telefono_cliente,banco_cliente,asiento_cliente);
def opcion2():
    while True:
        try:
            nombre=input(f"Ingrese su nombre:\t");
            print();
            rut=int(input(f"Ingrese su rut (Sin puntos ni digito verificador):\t"));
            print();
            telefono=int(input(f"Ingrese su número de telefono (limite de 8 digitos):\t(+56) 9 "));
            print();
            banco=int(input(f"-------------------\nSeleccione su banco\n-------------------\n\n(1) Banco Estado\n(2) Banco Falabella\n(3) Banco Santander\n(4) Banco Duoc\n\nSeleccione una opción:\t"));
            print();
            if nombre.isalpha() == True:
                if rut >= 1000000 and rut <= 99999999:
                    if telefono >= 10000000 and telefono <= 99999999:
                        if banco >= 1 and banco <= 4:
                            nombre_cliente.append(nombre);
                            rut_cliente.append(rut);
                            telefono_cliente.append(telefono);
                            banco_cliente.append(banco);
                            precio_asiento();
                            break
                        else:
                            print(f"El número de banco ingresado:\t{banco} no es valido, intentelo nuevamente\n");
                    else:
                        print(f"El telefono ingresado:\t{telefono} no es valido, intentelo nuevamente\n");
                else:
                    print(f"El rut ingresado:\t{rut} no es valido, intentelo nuevamente\n");
            else:
                print(f"El nombre ingresado:\t{nombre} no es valido, intentelo nuevamente\n");
        except ValueError:
            print(f"\nSolo digite números\n");
def precio_asiento():
    normal=78900
    vip=240000
    while True:
        p=0;
        m=0;
        print(f"Los asientos son los siguientes ('X' = ocupado , '1,2,3,4...,42' = disponible)\n");
        print(asientos);
        print();
        try:
            eleccion=int(input(f"Seleccione el asiento que desea:\t"));
            print();
            for x in range(7):
                for z in range(6):
                    m+=1
                    if m == eleccion:
                        num1=x;
                        num2=z;
                        break
            if asientos[num1][num2] == 'X':
                print("Asiento ocupado, intentelo nuevamente\n");
            else:
                if eleccion >= 1 and eleccion <= 42:
                    if eleccion >= 1 and eleccion <= 30:
                        op2=input(f"El precio del asiento {eleccion} es de ${normal}, ¿Desea comparlo?:\t");
                        print();
                        if op2 == 'Si' or op2 == 'si' or op2 == 'SI' or op2 == 's' or op2 == 'S':
                            for x in range(7):
                                for z in range(6):
                                    p+=1
                                    if p == eleccion:
                                        print("Asiento registrado\n");
                                        asiento_cliente.append(eleccion);
                                        asientos[x][z] = 'X';
                                        break
                            pago(normal);
                            break
                        elif op2 == 'No' or op2 == 'no' or op2 == 'NO' or op2 == 'n' or op2 == 'N':
                            print(f"Ok, se volvera a indicar los asientos disponibles\n");
                        else:
                            print(f"El caracter ingresado:\t{op2} no es valido en el sistema, intentelo nuevamente\n");
                    else:
                        op2=input(f"El precio del asiento {eleccion} es de ${vip}, ¿Desea comprarlo?:\t");
                        print();
                        if op2 == 'Si' or op2 == 'si' or op2 == 'SI' or op2 == 's' or op2 == 'S':
                            for x in range(7):
                                for z in range(6):
                                    p+=1;
                                    if p == eleccion:
                                        print("Asiento registrado\n");
                                        asiento_cliente.append(eleccion);
                                        asientos[x][z] = 'X';
                                        break
                            pago(vip);
                            break
                        elif op2 == 'No' or op2 == 'no' or op2 == 'NO' or op2 == 'n' or op2 == 'N':
                            print(f"Ok, se volvera a indicar los asientos disponibles\n");
                        else:
                            print(f"El caracter ingresado:\t{op2} no es valido en el sistema, intentelo nuevamente\n");
                else:
                    print(f"El número de asiento ingresado:\t{eleccion} no es valido, intentelo nuevamente\n");
        except ValueError:
            print("\nSolo digite números\n");
def pago(b):
    while True:
        try:
            if banco_cliente[-1] == [4]:
                descuento=int(b-(b * 0.15));
                print(f"Felicidades, por ser cliente del Banco Duoc obtiene 15% en el total de su pasaje, el total a pagar es de:\t{descuento}\n");
                pago=int(input(f"Ingrese el monto:\t"));
                print();
                if pago >= 1:
                    if pago >= descuento:
                        vuelto=pago-descuento;
                        print(f"Asiento y datos registrados, gracias por comprar con nosotros, tenga su vuelto:\t{vuelto}\n");
                        break
                    else:
                        print(f"El monto ingresado:\t{pago} es menor al precio requerido, intentelo nuevamente\n");
                else:
                    print(f"El monto ingresado:\t{pago} es menor o igual a 0, por favor, ingrese correctamente el pago\n");
            else:
                pago=int(input(f"Ingrese el monto:\t"));
                print();
                if pago >= 1:
                    if pago >= b:
                        vuelto=pago-b;
                        print(f"Asiento y datos registrados, gracias por comprar con nosotros, tenga su vuelto:\t{vuelto}\n");
                        break
                    else:
                        print(f"El monto ingresado:\t{pago} es menor al precio requerido, intentelo nuevamente\n");
                else:
                    print(f"El monto ingresado:\t{pago} es menor o igual a 0, por favor, ingrese correctamente el pago\n");
        except ValueError:
            print("\nSolo digite números\n");
def opcion3():
    while True:
        b=0;
        try:
            rut_comprobacion=int(input(f"Ingrese su rut (Sin puntos ni digito verificador):\t"));
            print();
            if rut_comprobacion in rut_cliente:
                for h in range(len(rut_cliente)):
                    if rut_cliente[h] == rut_comprobacion:
                        break
                    else:
                        continue
                nombre_cliente.pop(h);
                rut_cliente.pop(h);
                telefono_cliente.pop(h);
                banco_cliente.pop(h);
                for x in range(7):
                    for z in range(6):
                        b+=1
                        if b == asiento_cliente[h]:
                            asientos[x][z] = b;
                            break
                asiento_cliente.pop(h);
                print("Datos y asiento borrado\n");
                break
            else:
                print(f"El rut ingresado:\t{rut_comprobacion} no se encuentra registrado en el sistema, intentelo nuevamente\n");
        except ValueError:
            print(f"\nSolo digite números\n");
def opcion4():
    while True:
        try:
            asiento_comprobacion=int(input(f"Ingrese uno de los asientos que usted tiene:\t"));
            print();
            rut_comprobacion=int(input(f"Ingrese su rut (Sin puntos ni digito verificador):\t"));
            print();
            if asiento_comprobacion in asiento_cliente:
                if rut_comprobacion in rut_cliente:
                    while True:
                        for h in range(len(rut_cliente)):
                            if rut_cliente[h] == rut_comprobacion:
                                break
                            else:
                                continue
                        print(f".......................\n    Modificar Datos    \n.......................\n")
                        print(f"(1) Cambiar Nombre\n(2) Cambiar Número de telefono\n(3) Salir\n");
                        try:
                            op3=int(input("Seleccione una opción:\t"));
                            print();
                            if op3 == 1:
                                nombre_cambio=input(f"Ingrese su nombre:\t");
                                print();
                                if nombre_cambio.isalpha() == True:
                                    nombre_cliente[h] = nombre_cambio;
                                    print("Nombre registrado exitosamente\n");
                                    break
                                else:
                                    print(f"El nombre ingresado es erroneo, intentelo nuevamente\n");
                            elif op3 == 2:
                                telefono_cambio=int(input(f"Ingrese su número de telefono (limite de 8 digitos):\t(+56) 9 "));
                                print();
                                if telefono_cambio >= 10000000 and telefono_cambio <= 99999999:
                                    telefono_cliente[h] = telefono_cambio;
                                    print("Numero de telefono cambiado exitosamente\n");
                                    break
                                else:
                                    print(f"El telefono ingresado:\t{telefono_cambio} no es valido, intentelo nuevamente\n");
                            elif op3 == 3:
                                print("Cerrando menú\n");
                                break
                            else:
                                print(f"La opción ingresada:\t{op3} no es valido en el sistema, intentelo nuevamente\n");
                        except ValueError:
                            print(f"\nSolo digite números\n");
                    break
                else:
                    print(f"El rut ingresado:\t{rut_comprobacion} no se encuentra registrado en el sistema, intentelo nuevamente\n");
            else:
                print(f"El asiento ingresado:\t{asiento_comprobacion} no se encuentra registrado en el sistema, intentelo nuevamente\n");
        except ValueError:
            print(f"\nSolo digite números\n");
def despedida():
    return print(f"Cerrando aplicación\nAplicacion creada por Cracklitrox\n");