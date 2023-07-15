from Funciones_ejercicio import *
while True:
    print(f"-------------------\n    Vuelos Duoc    \n-------------------\n");
    print(f"(1) Ver asientos disponibles\n(2) Comprar asiento\n(3) Anular vuelo\n(4) Modificar datos de pasajero\n(5) Salir\n(6) mostrar datos pasajeros\n");
    try:
        op=int(input(f"Seleccione una opción:\t"));
        print();
        if op == 1:
            print(f"Los asientos son los siguientes ('X' = ocupado , '1,2,3,4...,42' = disponible)\n");
            print(asientos);
            print();
        elif op == 2:
            if np.all(asientos == 'X'):
                print(f"Ya se ocuparon todos los asientos del avion\n")
            else:
                print();
                opcion2();
        elif op == 3:
            if len(rut_cliente[0]) == 0:
                print(f"No se ha registrado ningun usuario aún, elija la opción 2 para continuar\n");
            else:
                opcion3();
                print();
        elif op == 4:
            if len(rut_cliente[0]) == 0:
                print(f"No se ha registrado ningun usuario aún, elija la opción 2 para continuar\n");
            else:
                opcion4();
                print();
        elif op == 5:
            despedida();
            break
        elif op == 6:
            if len(rut_cliente[-1]) == 0:
                print(f"No hay datos registrados, seleccione la opción 2 para continuar\n");
            else:
                print(f"Los datos son los siguientes\nNombre:\t{nombre_cliente}\nRut:\t{rut_cliente}\nTelefono:\t{telefono_cliente}\nBanco:\t{banco_cliente}\nAsiento:\t{asiento_cliente}");
                print(f"Los datos de la matriz son los siguientes:\t{matriz_clientes}\n");
        else:
            print(f"El número ingresado:\t{op} no se encuentra entre las opciones del sistema, intentelo denuevo\n");
    except ValueError:
        print(f"\nSolo digite números\n");