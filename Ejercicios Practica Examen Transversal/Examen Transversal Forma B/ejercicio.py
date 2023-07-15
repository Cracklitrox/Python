from funciones import *
while True:
    print(f"------------------\n    Casa Feliz    \n------------------\n");
    print(f"(1) Comprar departamento\n(2) Mostrar departamentos disponibles\n(3) Ver listado de compradores\n(4) Mostrar ganacias totales\n(5) Salir\n");
    try:
        op=int(input("Seleccione una opción:\t"));
        print();
        if op == 1:
            opcion1();
        elif op == 2:
            opcion2();
        elif op == 3:
            opcion3();
        elif op == 4:
            opcion4();
        elif op == 5:
            opcion5();
            break
        else:
            print(f"La opción ingresada:\t{op} no es valida, intente entre las 5 opciones del sistema\n");
    except ValueError:
        print(f"\nSolo digite números\n");