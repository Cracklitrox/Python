from turtle import pos
import numpy as np
matriz=np.empty(shape=(10,10),dtype=('U10'));
i=1;
for x in range(10):
    for z in range(10):
        matriz[x,z]=i;
        i+=1;
Ruts=[];
op4=[];
def opcion2():
    print(f"Los asientos ocupados se mostraran con una X y los desocupados son los números\n\n                ESCENARIO    \n");
    print(matriz);
    print();
def opcion1_pago(x):
    while True:
        try:
            if x >= 1 and x <= 20:
                pago=int(input(f"Usted ha seleccionado una entrada Platinum, el monto total es de $120.000\nIngrese el monto a pagar:\t"));
                print();
                if pago >= 120000:
                    vuelto=pago-120000;
                    if vuelto == 0:
                        print(f"Asiento registrado\n");
                        break
                    else:
                        print(f"Asiento registrado, tenga su vuelto:\t$ {vuelto}\n");
                        break
                else:
                    print(f"El monto ingresado:\t'{pago}' es menor al requerido, por favor, intentelo nuevamente\n");
            elif x >= 21 and x <= 50:
                pago=int(input(f"Usted ha seleccionado una entrada Gold, el monto total es de $80.000\nIngrese el monto a pagar:\t"));
                print();
                if pago >= 80000:
                    vuelto=pago-80000;
                    if vuelto == 0:
                        print(f"Asiento registrado\n");
                        break
                    else:
                        print(f"Asiento registrado, tenga su vuelto:\t$ {vuelto}\n");
                        break
                else:
                    print(f"El monto ingresado:\t'{pago}' es menor al requerido, por favor, intentelo nuevamente\n");
            elif x >= 51 and x <= 100:
                pago=int(input(f"Usted ha seleccionado una entrada Silver, el monto total es de $50.000\nIngrese el monto a pagar:\t"));
                print();
                if pago >= 50000:
                    vuelto=pago-50000;
                    if vuelto == 0:
                        print(f"Asiento registrado\n");
                        break
                    else:
                        print(f"Asiento registrado, tenga su vuelto:\t$ {vuelto}\n");
                        break
                else:
                    print(f"El monto ingresado:\t'{pago}' es menor al requerido, por favor, intentelo nuevamente\n");
        except ValueError:
            print(f"\nSolo digite números\n");
def opcion1():
    while True:
        try:
            rut=int(input("Ingrese su Rut (Sin guion, digito verificador ni puntos):\t"));
            print();
            if rut >= 1000000 and rut <= 99999999:
                Ruts.append(rut);
                break
            else:
                print(f"El Rut ingresado:\t'{rut}' no es valido, intentelo nuevamente\n");
        except ValueError:
            print(f"\nSolo digite números\n");
    while True:
        try:
            cantidad=int(input("Ingrese la cantidad de entredas que desea (1-3):\t"));
            print();
            if cantidad >= 1 and cantidad <= 3:
                for x in range(cantidad):
                    while True:
                        p=0;
                        opcion2();
                        try:
                            posicion=int(input("Ingrese el número del asiento que desea:\t"));
                            print();
                            if posicion >= 1 and posicion <= 100:
                                for x in range(10):
                                    for z in range(10):
                                        p+=1;
                                        if p == posicion:
                                            a=x;
                                            b=z;
                                            break
                                        else:
                                            continue
                                if matriz[a,b] != 'X':
                                    matriz[a,b]='X';
                                    op4.append(posicion);
                                    opcion1_pago(posicion);
                                    break
                                else:
                                    print(f"No está disponible, intente con otra posición\n");
                            else:
                                print(f"La posicion ingresada:\t'{posicion}' no es valida, intentelo nuevamente\n");
                        except ValueError:
                            print(f"\nSolo digite números\n");
                break
            else:
                print(f"La cantidad ingresada:\t'{cantidad}' no es valida, intentelo nuevamente\n");
        except ValueError:
            print(f"\nSolo digite números\n");
def opcion3():
    print(f"A continuación se mostraran los Ruts registrados en el sistema, de menor a mayor\n");
    for x in range(len(Ruts)):
        orden=sorted(Ruts);
        print(f"Rut:\t{orden[x]}");
        print();
def opcion4():
    cont_a=0;
    cont_b=0;
    cont_c=0;
    for x in range(len(op4)):
        if op4[x] >= 1 and op4[x] <= 20:
            cont_a+=1;
        elif op4[x] >= 21 and op4[x] <= 50:
            cont_b+=1;
        elif op4[x] >= 51 and op4[x] <= 100:
            cont_c+=1;
    multiplicacion_a=cont_a*120000;
    multiplicacion_b=cont_b*80000;
    multiplicacion_c=cont_c*50000;
    suma_total=cont_a+cont_b+cont_c;
    total=multiplicacion_a+multiplicacion_b+multiplicacion_c;
    print(f"|--------------------------------------------------|");
    print(f"|      Tipo Entrada     |   Cantidad   |   Total   |");
    print(f"|--------------------------------------------------|");
    print(f"|   Platinum $120.000   |      {cont_a}       |   $ {multiplicacion_a}     |");
    print(f"|--------------------------------------------------|");
    print(f"|   Gold     $ 80.000   |      {cont_b}       |   $ {multiplicacion_b}     |");
    print(f"|--------------------------------------------------|");
    print(f"|   Silver   $ 50.000   |      {cont_c}       |   $ {multiplicacion_c}     |");
    print(f"|--------------------------------------------------|");
    print(f"|   TOTAL               |      {suma_total}       |   $ {total}     |");
    print(f"|--------------------------------------------------|\n");
def opcion5():
    print(f"Aplicación creada por Carlos Gacitúa\t14/07-2022\n");