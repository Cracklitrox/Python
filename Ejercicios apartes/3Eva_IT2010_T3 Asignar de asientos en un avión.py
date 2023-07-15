from concurrent.futures import BrokenExecutor
from operator import contains
import numpy as np
asientos_avion=np.zeros((10,4));
codigo_asientos_avios=asientos_avion[:].copy();
cedulas=np.zeros((10,4));
nombres=np.full((10,4),input);
i=1;
cont=0;
print(f".........................\n     Aerolinea Duoc     \n.........................\n");
while True:
    print(f"---------------------------------\n     {41-i} asientos disponibles     \n---------------------------------\n");
    print("--------------------------\n     Menu de opciones     \n--------------------------\n(1) Comprar Boleto\n(2) Asignar asiento\n(3) Mostrar ocupación de asientos\n(4) Lista de Pasajeros en el vuelo\n(5) Salir\n");
    try:
        op=int(input("Seleccione una opción: "));
        print();
        if op == 1:
            if cont == 40:
                print("Ya se registraron todos los asientos del avion¡\n");
            else:
                while True:
                    try:
                        cedula_registro=int(input("Ingrese su cedula de identidad sin puntos ni digito verificador: "));
                        print();
                        nombre_registro=input("Ingrese su nombre: ");
                        print();
                        if cedula_registro >=  4000000 and cedula_registro <= 99999999:
                            if nombre_registro.isalpha() == True:
                                print("Cedula y nombre registrado\n");
                                cont+=1
                                for f in range(10):
                                    for c in range(4):
                                        if cedulas[f][c] == 0:
                                            cedulas[f][c]=cedula_registro
                                            nombres[f][c]=nombre_registro
                                            break
                                        else:
                                            continue
                                    break
                                break
                            else:
                                print(f"El nombre ingresado:\t'{nombre_registro}' contiene numeros, digite correctamente\n");
                        else:
                            print(f"La cedula ingresada:\t'{cedula_registro}' no es valida dentro del sistema, intentelo nuevamente\n");
                    except ValueError:
                        print("\nDigite solo caracteres o números\n");
        elif op == 2:
            if cont == 0:
                print("Compre un boleto al menos para asignar un asiento.\n");
            elif i == 41:
                print("Ya se registraron todos los asientos del avion¡\n");
            else:
                while True:
                    try:
                        print("--------------------------------------------------------\n    Solo se puede comprar 1 boleto por cada pasajero    \n--------------------------------------------------------\n")
                        cedula_comprobacion=int(input("Ingrese su cedula de identidad sin puntos ni digito verificador: "));
                        print();
                        print("Se mostraran las ubicaciones de los asientos del avios (0 = disponibles; 1,2,3,4,...40 = ocupado)\n");
                        print(f"{asientos_avion}\n");
                        fila_elegida=int(input("Ingrese en que fila desea ubicarse: "));
                        print();
                        columna_elegida=int(input("Ingrese en que columna desea ubicarse: "));
                        print();
                        if cedula_comprobacion >=  4000000 and cedula_comprobacion <= 99999999:
                            for x in range(10):
                                for z in range(4):
                                    if cedula_comprobacion == cedulas[x][z]:
                                        break
                                    else:
                                        continue
                                break
                            if fila_elegida >= 1 and fila_elegida <= 10 and columna_elegida >= 1 and columna_elegida <= 4:
                                if asientos_avion[fila_elegida-1][columna_elegida-1] == 0:
                                    for z in range (10):
                                        for x in range(4):
                                            if codigo_asientos_avios[z][x] != 0:
                                                continue
                                            else:
                                                codigo_asientos_avios[z][x] = i
                                                asientos_avion[fila_elegida-1][columna_elegida-1] = i
                                                i+=1
                                                break
                                        break
                                    break
                                else:
                                    print(f"El asiento de la fila {fila_elegida} y columna {columna_elegida} ya esta ocupado, intentelo nuevamente\n");
                            else:
                                print("La fila o columna escogida no se encuentra dentro del rando, por favor, intentelo nuevamente\n");
                        else:
                            print(f"La cedula ingresada:\t'{cedula_comprobacion}' no es valida dentro del sistema, intentelo nuevamente\n");
                    except ValueError:
                        print("\nDigite solo números\n");
        elif op == 3:
            print("Los asientos ocupados y vacios son los siguientes (0 = disponibles ; 1,2,3,4,...40 = ocupado)\n");
            print(f"{asientos_avion}\n");
        elif op == 4:
            if i == 1:
                print("No hay asientos registrados\n");
            else:
                print(f"La información de cada pasajero con asiento confirmado son los siguientes\n");
                for x in range(10):
                    for z in range(4):
                        if codigo_asientos_avios[x][z] == 0:
                            continue
                        else:
                            print(f"Cedula:\t{cedulas[x][z]}\nNombre:\t{nombres[x][z]}\nNumero del asiento:\t{codigo_asientos_avios[x][z]}\n");
        elif op == 5:
            print("Cerrando aplicación\n");
            break
        else:
            print(f"La numero ingresado:\t'{op}' no es valido dentro del sistema, ingrese un valor desde la opción 1 hasta la 5\n");
    except ValueError:
        print(f"\nDigite solo números\n");
# Preguntar como hacer una validación para que un pasajero solo compre un boleto, sin necesidad de contenedores