import numpy as np
i=0;
asientos=np.full((7,6),'  ');
for x in range(7):
    for z in range(6):
        i+=1;
        asientos[x][z]=i;
nombre_cliente=[];
rut_cliente=[];
telefono_cliente=[];
banco_cliente=[];
asiento_cliente=[];
def opcion2():
    while True:
        try:
            nom=input(f"Ingrese su nombre:\t");
            print();
            if nom.isalpha() == True:
                nombre_cliente.append(nom);
                break
            else:
                print(f"El nombre ingresado:\t{nom} contiene numeros o espacios, solo ingrese su nombre\n");
        except ValueError:
            print("\nSolo digite caracteres\n");
    while True:
        try:
            rut=int(input("Ingrese su rut (Sin puntos ni digito verificador):\t"));
            print();
            if rut >= 1000000 and rut <= 99999999:
                rut_cliente.append(rut);
                break
            else:
                print(f"El rut ingresado:\t{rut} no es valido, intentelo nuevamente\n");
        except ValueError:
            print("\nSolo digite numeros\n");
    while True:
        try:
            telefono=int(input("Ingrese su número de telefono (8 digitos maximo):\t(+56) 9 "));
            print();
            if telefono >= 10000000 and telefono <= 99999999:
                telefono_cliente.append(telefono);
                break
            else:
                print(f"El número ingresado:\t{telefono} no es valido, intentalo nuevamente\n");
        except ValueError:
            print("\nSolo digite numeros\n");
    while True:
        print(f"--------------------------\n    Bancos Disponibles    \n--------------------------\n");
        print("(1) Banco Santander\n(2) Banco Falabella\n(3) Banco BBVA\n(4) Banco Duoc\n");
        try:
            op1=int(input("Seleccione una opción:\t"));
            print();
            if op1 >= 1 and op1 <= 4:
                banco_cliente.append(op1);
                break
            else:
                print(f"El número ingresado:\t{op} no es valido, intentelo nuevamente\n");
        except ValueError:
            print("\nSolo digite numeros\n");
    asientos();
def asientos():
    while True:
        cont=0;
        cont1=0;
        normal=78900;
        vip=240000;
        print("Los asientos son los siguientes ('X' = ocupado ; '1,2,3,...42' = Disponible)\n");
        print(asientos);
        print();
        try:
            eleccion=int(input("Ingrese el número del asiento que desea:\t"));
            print();
            for x in range(7):
                for z in range(6):
                    cont+=1;
                    if cont == eleccion:
                        num1=x;
                        num2=z;
                        break
                    else:
                        continue
            if asientos[num1][num2] == 'X':
                print(f"El asiento {eleccion} ya se encuentra ocupado, intente seleccionando otro asiento\n");
            else:
                if eleccion >= 1 and eleccion <= 42:
                    if eleccion >= 1 and eleccion <= 30:
                        for x in range(7):
                            for z in range(6):
                                cont1+=1;
                                if cont1 == eleccion:
                                    asientos[x][z]='X';
                                    asiento_cliente.append(eleccion);
                                    break
                                else:
                                    continue
                        pago(normal)
                        break
                    else:
                        for x in range(7):
                            for z in range(6):
                                cont1+=1;
                                if cont1 == eleccion:
                                    asientos[x][z]='X';
                                    asiento_cliente.append(eleccion);
                                    break
                                else:
                                    continue
                        pago(vip);
                        break
                else:
                    print(f"El número ingresado:\t{eleccion} no es valido, intentelo nuevamente\n");
        except ValueError:
            print("\nSolo digite numeros\n");
def pago(a):
    while True:
        if banco_cliente[0] == [4]:
            descuento=int(a-(a*0.15));
            print(f"Felicidades, por ser cliente del Banco Duoc obtiene 15% en el total de su pasaje, el total a pagar es de:\t{descuento}\n");
            pago=int(input(f"Ingrese el monto:\t"));
            print();
            if pago >= descuento:
                print("Pago cancelado, datos y asiento registrado\n");
                break
            else:
                print(f"El monto ingresado:\t${pago} es menor a ${descuento}, por favor, intentelo nuevamente\n");
        else:
            print(f"Felicidades, por ser cliente del Banco Duoc obtiene 15% en el total de su pasaje, el total a pagar es de:\t{descuento}\n");
            pago=int(input(f"Ingrese el monto:\t"));
            print();
            if pago >= a:
                print("Pago cancelado, datos y asiento registrado\n");
                break
            else:
                print(f"El monto ingresado:\t${pago} es menor a ${a}, por favor, intentelo nuevamente\n");
def opcion3():
    while True:
        cont=0;
        try:
            rut_comprobacion=int(input("Ingrese su rut (Sin puntos ni digito verificador:\t"));
            print();
            if rut_comprobacion >= 1000000 and rut_comprobacion <= 99999999:
                for x in range(len(rut_cliente)):
                    if rut_comprobacion == rut_cliente[x]:
                        break
                    else:
                        continue
                nombre_cliente.pop(x);
                rut_cliente.pop(x);
                telefono_cliente.pop(x);
                banco_cliente.pop(x);
                for c in range(7):
                    for z in range(6):
                        cont+=1;
                        if cont == asiento_cliente[x]:
                            asiento_cliente.pop(x);
                            asientos[c][z]=cont
                            break
                        else:
                            continue
                break
            else:
                print(f"El rut ingresado:\t{rut_comprobacion} es incorrecto, intentelo nuevamente\n");
        except ValueError:
            print("\nSolo digite numeros\n");
def opcion4():
    while True:
        cont=0;
        try:
            rut_comprobacion=int(input("Ingrese su rut (Sin puntos ni digito verificador:\t"));
            print();
            asiento_comprobacion=int(input("Ingrese el asiento que tiene asignado:\t"));
            print();
            if rut_comprobacion >= 1000000 and rut_comprobacion <= 99999999:
                for x in range(len(rut_cliente)):
                    if rut_comprobacion == rut_cliente[x]:
                        num1=x;
                        break
                    else:
                        continue
                if asiento_comprobacion == asiento_cliente[x]:
                    submenu(x);
                    break
                else:
                    print(f"El asiento ingresado:\t{asiento_comprobacion} no concuerda con el suyo registrado, intentelo nuevamente\n");
            else:
                print(f"El rut ingresado:\t{rut_comprobacion} es incorrecto, intentelo nuevamente\n");
        except ValueError:
            print("\nSolo digite numeros\n");
def submenu(rango):
    while True:
        print("-----------------------\n    Modificar datos    \n-----------------------\n");
        print("(1) Cambiar Nombre\n(2) Cambiar Número de Telefono\n(3) Salir\n");
        try:
            op=int(input("Seleccione una opción:\t"));
            print();
            if op == 1:
                nom=input("Ingrese su nombre:\t");
                print();
                if nom.isalpha() == True:
                    nombre_cliente[rango]=nom;
                    print("Nombre cambiado exitosamente\n");
                else:
                    print(f"El nombre ingresado:\t{nom} contiene numeros o espacios, solo ingrese su nombre\n");
            elif op == 2:
                telefono=int(input("Ingrese su número de telefono (8 digitos maximo):\t(+56) 9 "));
                print();
                if telefono >= 10000000 and telefono <= 99999999:
                    telefono_cliente[rango]=telefono;
                    print("Número de telefono cambiado exitosamente\n");
                else:
                    print(f"El número de telefono ingresado:\t{telefono} es incorrecto, intentelo nuevamente\n");
            elif op == 3:
                print("Cerrando submenú\n");
                break
            else:
                print(f"El número ingresado:\t{op} es incorrecto, intentalo nuevamente\n");
        except ValueError:
            print("\nSolo digite numeros\n");
def despedida():
    return print(f"Cerrando aplicación\nAplicacion creada por Cracklitrox\nVersion 1.0\n");
while True:
    print(f"-------------------\n    Vuelos Duoc    \n-------------------\n");
    print(f"(1) Ver asientos disponibles\n(2) Comprar asiento\n(3) Anular vuelo\n(4) Modificar datos de pasajero\n(5) Salir\n");
    try:
        op=int(input("Seleccione una opción:\t"));
        print();
        if op == 1:
            print("Los asientos son los siguientes ('X' = ocupado ; '1,2,3,...42' = Disponible)\n");
            print(asientos);
            print();
        elif op == 2:
            opcion2();
        elif op == 3:
            opcion3();
        elif op == 4:
            opcion4();
        elif op == 5:
            despedida();
            break
        else:
            print(f"El número ingresado:\t{op} no es valido, intentelo nuevamente\n");
    except ValueError:
        print(f"\nSolo digite numeros\n");