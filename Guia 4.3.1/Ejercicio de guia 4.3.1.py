from FuncionesEjercicio import *
while True:
    print("-----------------\n     Menu Duoc    \n-----------------\n");
    print("(1) Calcular Iva\n(2) Descuento\n(3) Calcular Imc\n(4) Salir\n");
    try:
        op=int(input("Seleccione una opción:\t"));
        print();
        if op == 1:
            opcion1()
        elif op == 2:
            opcion2()
        elif op == 3:
            opcion3()
        elif op == 4:
            print("Cerrando aplicación\n");
            break
        else:
            print(f"La opción ingresada:\t{op} no es valida en el rango del sistema, intentelo del 1 al 4\n");
    except ValueError:
        print("\nSolo digite números\n");