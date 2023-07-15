import numpy as np
hotel=np.empty((10,5),dtype=('U16'));
detalles1=np.empty(shape=(1,2),dtype=('U16'));
detalles2=np.empty(shape=(1,5),dtype=('U16'));
detalles1[0,0]='|Piso|';
detalles1[0,1]='----Tipos----';
detalles2[0,0]='|    |';
detalles2[0,1]='A';
detalles2[0,2]='B';
detalles2[0,3]='C';
detalles2[0,4]='D';
h=10;
for x in range(10):
    if h == 10:
        hotel[x,0]=f'| {h} |';
        h-=1;
    else:
        hotel[x,0]=f'|  {h} |';
        h-=1;
Ruts=[];
cont_tipos=[];
def opcion1():
    while True:
        try:
            Rut=int(input("Ingrese su Rut (Sin puntos, guion ni digito verificador):\t"));
            print();
            if Rut >= 1000000 and Rut <= 99999999:
                Ruts.append(Rut);
                break
            else:
                print(f"El Rut ingresado:\t{Rut} no es valido, el rango es de 7 a 8 numeros de largo, intentelo nuevamente\n");
        except ValueError:
            print(f"\nSolo digite numeros\n");
    while True:
        j=0;
        try:
            piso=int(input(f"Ingrese el número del piso que desea (1-10):\t"));
            print();
            tipo=input(f"Ingrese el tipo de departamento que desea (A,B,C o D):\t");
            print();
            if piso >= 1 and piso <= 10:
                if tipo == 'A' or tipo == 'a' or tipo == 'B' or tipo == 'b' or tipo == 'C' or tipo == 'c' or tipo == 'D' or tipo == 'd':
                    for x in range(10):
                        j+=1;
                        if j == piso and tipo == 'A' or tipo == 'a':
                            a=x-piso;
                            b=1;
                            break
                        elif j == piso and tipo == 'B' or tipo == 'b':
                            a=x-piso;
                            b=2;
                            break
                        elif j == piso and tipo == 'C' or tipo == 'c':
                            a=x-piso;
                            b=3;
                            break
                        elif j == piso and tipo == 'D' or tipo == 'd':
                            a=x-piso;
                            b=4;
                            break
                        else:
                            continue
                    if hotel[a,b] == '':
                        cont_tipos.append(tipo);
                        hotel[a,b]='X';
                        opcion1_pago(tipo)
                        break
                    else:
                        print(f"No está disponible, intentelo nuevamente\n");
                else:
                    print(f"El piso ingresado:\t{piso} no es valido, intentelo nuevamente\n");
            else:
                print(f"El número del piso ingresado:\t{piso} no es valido, intentelo nuevamente\n");
        except ValueError:
            print(f"\nSolo digite números o caracteres\n");
def opcion1_pago(x):
    while True:
        if x == 'A' or 'a':
            pago=int(input(f"El valor del departamento es de 3.800 UF\n\nCancele el trato (El pago es en UF):\t"));
            print();
            if pago >= 3800:
                vuelto=pago-3800
                print(f"Transmite realizado exitosamente, tenga su vuelto:\t{vuelto} UF\n");
                break
            else:
                print(f"El monto ingresado es insuficiente para el pago total, por favor intentelo nuevamente\n");
        elif x == 'B' or 'b':
            pago=int(input(f"El valor del departamento es de 3.000 UF\n\nCancele el trato (El pago es en UF):\t"));
            print();
            if pago >= 3000:
                vuelto=pago-3000
                print(f"Transmite realizado exitosamente, tenga su vuelto:\t{vuelto} UF\n");
                break
            else:
                print(f"El monto ingresado es insuficiente para el pago total, por favor intentelo nuevamente\n");
        elif x == 'C' or x == 'c':
            pago=int(input(f"El valor del departamento es de 2.800 UF\n\nCancele el trato (El pago es en UF):\t"));
            print();
            if pago >= 2800:
                vuelto=pago-2800
                print(f"Transmite realizado exitosamente, tenga su vuelto:\t{vuelto} UF\n");
                break
            else:
                print(f"El monto ingresado es insuficiente para el pago total, por favor intentelo nuevamente\n");
        elif x == 'D' or x == 'd':
            pago=int(input(f"El valor del departamento es de 3.500 UF\n\nCancele el trato (El pago es en UF):\t"));
            print();
            if pago >= 3500:
                vuelto=pago-3500
                print(f"Transmite realizado exitosamente, tenga su vuelto:\t{vuelto} UF\n");
                break
            else:
                print(f"El monto ingresado es insuficiente para el pago total, por favor intentelo nuevamente\n");
def opcion2():
    print(f"Los departamentos ocupados se marcaran con una X y los vacios en ''\n")
    print(detalles1);
    print(detalles2)
    print(hotel);
def opcion3():
    print(f"El listado de los compradores de los departamentos son los siguientes (De menor a mayor)\n");
    for x in range(len(Ruts)):
        op3=sorted(Ruts);
        print(f"Rut:\t{op3[x]}\n");
def opcion4():
    cont_a=0;
    cont_b=0;
    cont_c=0;
    cont_d=0;
    for x in range(len(cont_tipos)):
        if cont_tipos[x] == 'A' or cont_tipos[x] == 'a':
            cont_a+=1;
        elif cont_tipos[x] == 'B' or cont_tipos[x] == 'b':
            cont_b+=1;
        elif cont_tipos[x] == 'C' or cont_tipos[x] == 'c':
            cont_c+=1;
        elif cont_tipos[x] == 'D' or cont_tipos[x] == 'd':
            cont_d+=1;
    print(f"Las ventas totales hasta ahora son las siguientes\n");
    print(f"-----------------------------------------------------");
    print(f"|  Tipo de Departamento  |  Cantidad  |    Total    |");
    print(f"-----------------------------------------------------");
    print(f"|  Tipo A 3.800 UF       |      {cont_a}     |   {cont_a*3800} UF   |");
    print(f"|  Tipo B 3.000 UF       |      {cont_b}     |   {cont_b*3000} UF   |");
    print(f"|  Tipo C 2.800 UF       |      {cont_c}     |   {cont_c*2800} UF   |");
    print(f"|  Tipo D 3.500 UF       |      {cont_d}     |   {cont_d*3500} UF   |");
    print(f"|  TOTAL                 |      {cont_a+cont_b+cont_c+cont_d}     |   {(cont_a*3800)+(cont_b*3000)+(cont_c*2800)+(cont_d*3500)} UF   |");
    print(f"-----------------------------------------------------\n");
def opcion5():
    print(f"Saliendo de la aplicacion\tCreada por Carlos Gacitúa\tVersion 1.0\n");