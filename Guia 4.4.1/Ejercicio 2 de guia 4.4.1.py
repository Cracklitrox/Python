import random
import numpy as np
while True:
    try:
        num1=int(input("Ingrese un número (Entre 3 y 6):\t"));
        print()
        num2=int(input("Ingrese un número (Entre 3 y 6):\t"));
        print();
        if num1 <= 2 and num1 >= 7 and num2 <= 2 and num2 >= 7:
            print("Número mal ingresado, intentelo nuevamente\n");
            break
        else:
            matriz=np.zeros((num1,num2));
            for x in range(num1):
                for z in range(num2):
                    r=random.randrange(0,999);
                    matriz[x][z]=r
            print("Los elementos del arreglo son los siguientes\n");
            print(matriz);
            print();
            for x in range(num1):
                print(f"La suma de los elementos de la fila {x+1} es:\t{matriz[x,:].sum()}\n");
            for z in range(num2):
                print(f"El promedio de los elementos de la columna {z+1} es:\t{matriz[:,z].mean()}\n");
            op=input("¿Desea volverlo a intentar?:\t");
            print();
            if op == 'Vale' or op == 'vale' or op == 'VALE' or op == 'ok' or op == 'OK' or op == 'Ok' or op == 'Si' or op == 'si' or op == 'SI' or op == 'Bueno' or op == 'bueno' or op == 'BUENO':
                continue
            elif op == 'No' or op == 'no' or op == 'NO':
                print("Cerrando aplicación\n");
                break
            else:
                print("Ingrese correctamente lo que escriba, intentelo nuevamente\n");
    except ValueError:
        print("\nSolo digite numeros\n");