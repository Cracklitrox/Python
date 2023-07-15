import numpy as np
i=0;
asientos=np.full((7,6),'  ');
for x in range(7):
    for z in range(6):
        i+=1;
        asientos[x][z]=i;
while True:
    print("-------------------\n    Vuelos Duoc    \n-------------------\n");
    print(f"(1) Ver asientos disponibles\n(2) Comprar asiento\n(3) Anular vuelo\n(4) Modificar datos de pasajero\n(5) Salir\n");
    try:
        op=int(input("Seleccione una opción:\t"));
        print();
        if op == 1:
            print(f"Los asientos son los siguientes ('X' = ocupado , '1,2,3,4...,42' = disponible)\n");
            print(asientos);
            print();
        elif op == 2:
            if np.all(asientos == 'X'):
                print(f"Ya se encuentran ocupados todos los asientos\n");
        elif op == 3:
            continue
        elif op == 4:
            continue
        elif op == 5:
            continue
        else:
            print(f"El número ingresado:\t{op} no es valido, intentelo nuevamente\n");
    except ValueError:
        print("\nSolo Digite Numeros\n");