from Funciones import *
while opcion != "5":
    print("Opciones\n(1) Grabar\n(2) Buscar\n(3) Imprimir\n(4) Salir\n");
    opcion=input("Ingrese una opcion:\t");
    if opcion not in listaopciones:
        print("Opcion erroneao\n");
        input("Precione Enter para volver a intentarlo...\n");
    if opcion == "4":
        print("Usted a salido del programa.\n");
        break
    if opcion == "1":
        opcion1(NDP,j);
        j+=1
        print(NDP,j);
    if opcion == "2":
        if NDP[0,j-1] == "":
            print("No se ha registrado ninguna NDP, por favor seleccione la opcion 1\n");
        else:
            opcion2(NDP);
    if opcion == "3":
        if NDP[0,j-1] == "":
            print("No se ha registrado ninguna NDP, por favor seleccione la opcion 1\n");
        else:
            opcion3(NDP);