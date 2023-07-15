from unittest import result


def convertidor(a,b):
    resultado=a+b
    return (resultado);
while True:
    print("------------------------------\n    Convertir temperaturas    \n------------------------------\n");
    print("(1) Grados a Kelvin\n(2) Kelvin a Grados\n(3) Salir\n");
    try:
        op=int(input("Seleccione una opción:\t"));
        print();
        if op == 1:
            while True:
                try:
                    grados=int(input("Ingrese los grados que desea convertir:\t"));
                    print();
                    print(f"La cantidad de {grados} grados a kelvin son:\t{convertidor(grados,b=273.15)}\n");
                    break
                except ValueError:
                    print("\nSolo digite numeros\n");
        elif op == 2:
            while True:
                try:
                    kelvin=int(input("Ingrese la temperatura kelvin que desea convertir:\t"));
                    print();
                    print(f"La cantidad de {kelvin} kelvin a grados son:\t{convertidor(kelvin,b=-273.15)}\n");
                    break
                except ValueError:
                    print("\nSolo digite numeros\n");
        elif op == 3:
            print("Cerrando aplicación\n");
            break
        else:
            print(f"La opción ingresada:\t{op} no es valido en el rango del sistema, intentelo nuevamente\n");
    except ValueError:
        print("\nSolo digite numeros\n");