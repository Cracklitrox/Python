import numpy as np
NDP=np.array ([["","","",""]], dtype = ("U",16));
j=0;
opcion=0;
listaopciones=("1","2","3","4");
def opcion1(NDP,j):
    while True:
        ndp=input("Ingrese el MPN:\t");
        print();
        if ndp.isnumeric() == True:
            NDP[0,j]=ndp
            print(f"NDP agregada. {NDP [0,j]}");
            break
        else:
            print("Ingrese correctamente el ndp.");
            input("Precione Enter para volver a intentarlo...\n");
def opcion2(NDP):
    while True:
        ndp_comprobacion=input("Ingrese el MPN:\t");
        print();
        if ndp_comprobacion.isnumeric() == True:
            if ndp_comprobacion in NDP:
                print(f"El NDP se encuentra dentro del sistema:\t{ndp_comprobacion}\nVolviendo al menu de inicio\n");
                break
            else:
                print(f"El NDP ingresado:\t{ndp_comprobacion} no se encuentra en el sistema, intentelo nuevamente\n");
        else:
            print("Ingrese correctamente el ndp.");
            input("Precione Enter para volver a intentarlo...\n");
def opcion3(NDP):
    while True:
        ndp_comprobacion=input("Ingrese el MPN:\t");
        print();
        if ndp_comprobacion.isnumeric() == True:
            if ndp_comprobacion in NDP:
                print(f"El NDP se encuentra dentro del sistema:\t{ndp_comprobacion}, se encuentra en la posicion {np.where(NDP == ndp_comprobacion)}\nVolviendo al menu de inicio\n");
                break
            else:
                print(f"El NDP ingresado:\t{ndp_comprobacion} no se encuentra en el sistema, intentelo nuevamente\n");
        else:
            print("Ingrese correctamente el ndp.");
            input("Precione Enter para volver a intentarlo...\n");