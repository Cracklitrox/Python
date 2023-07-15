from Funciones_ejercicio_5 import *
while True:
    print("-------------------------\n     Número de parte     \n-------------------------\n");
    print("(1) Grabar\n(2) Buscar\n(3) Imprimir\n(4) Salir\n");
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
            break
        else:
            print(f"El número ingresado\t{op} no es valido en el sistema, intente desde las opciones 1-4\n");
    except ValueError:
        print("\nSolo digite números\n");