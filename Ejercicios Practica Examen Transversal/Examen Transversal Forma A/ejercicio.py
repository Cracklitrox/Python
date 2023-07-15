from Funciones import *
while True:
    print(f"-----------------------------\n    Concierto Michael Jam    \n-----------------------------\n");
    print(f"(1) Comprar entradas\n(2) Mostrar ubicaciones disponibles\n(3) Ver listado de asistentes\n(4) Mostrar ganancias totales\n(5) Salir\n");
    try:
        op=int(input("Seleccione una opción:\t"));
        print();
        if op == 1:
            opcion1();
        elif op == 2:
            opcion2();
        elif op == 3:
            if len(Ruts) == 0:
                print(f"No se ha registrado ningun Rut en el sistema aún, por favor, seleccione la opcion 1 para habilitar esta opción\n");
            else:
                opcion3();
        elif op == 4:
            opcion4();
        elif op == 5:
            opcion5();
            break
        else:
            print(f"La número de la opción ingresada:\t'{op}' no es valida, intentelo nuevamente\n");
    except ValueError:
        print(f"\nSolo digite números\n");