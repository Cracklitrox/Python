import random
import numpy as np
matriz=np.zeros(10);
for x in range(len(matriz)):
    r=random.randrange(0,101);
    matriz[x]=r;
print(matriz)
i=0;
while True:
    a=0;
    b=0;
    print("----------------------\n    Acierto Letras    \n----------------------\n");
    try:
        if i == 10:
            break
        else:
            num=int(input("Ingrese un número:\t"));
            print();
            for x in range(10):
                if matriz[x] == num:
                    b+=1
                    break
                else:
                    a+=1
                    continue
            if b == 1:
                print("Pertenece\n");
                op=input("¿Desea volverlo a intentar?:\t");
                print();
                if op == 'Vale' or op == 'vale' or op == 'VALE' or op == 'ok' or op == 'OK' or op == 'Ok' or op == 'Si' or op == 'si' or op == 'SI' or op == 'Bueno' or op == 'bueno' or op == 'BUENO':
                    continue
                elif op == 'No' or op == 'no' or op == 'NO':
                    print("Cerrando aplicación\n");
                    break
                else:
                    print("Ingrese correctamente lo que escriba, intentelo nuevamente\n");
            else:
                print("No pertenece\n");
                op=input("¿esea volverlo a intentar?:\t");
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