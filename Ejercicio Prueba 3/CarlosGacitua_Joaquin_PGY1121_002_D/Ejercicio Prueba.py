from funciones import *
while True:
    print(f"------------------\n    AutoSeguro    \n------------------\n");
    print("(1) Grabar\n(2) Buscar\n(3) Imprimir certificados\n(4) Salir\n");
    try:
        op=int(input("Seleccione una opción:\t"));
        print();
        if op == 1:
            opcion1();
        elif op == 2:
            if len(patentes) == 0:
                print(f"No hay datos registrados, seleccione la opción 1 para continuar\n");
            else:
                opcion2();
        elif op == 3:
            if len(patentes) == 0:
                print(f"No hay datos registrados, seleccione la opción 1 para continuar\n");
            else:
                opcion3();
        elif op == 4:
            despedida();
            break
        else:
            print(f"El numero ingresado\t{op} es incorrecto, intentelo nuevamente\n");
    except ValueError:
        print("\nSolo digite numeros\n");