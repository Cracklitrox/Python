from concurrent.futures import BrokenExecutor
import random


arreglo_1=[];
for i in range(10):
    arreglo_1.append(random.randrange(0,100));
print(f"Los números del arreglos son: {arreglo_1}\n\n");
cont=0;
for z in range(len(arreglo_1)):
    if arreglo_1[z] % 2 == 0:
        cont+=1
print(f"Hay {cont} numeros pares en el arreglo.\n\n");
for x in range(len(arreglo_1)):
    for n in range(2,arreglo_1[x]):
        if arreglo_1[x] % n == 0:
            print(f"El numero {arreglo_1[x]} no es primo, es divisor.\n");
            break
        else:
            print(f"El numero {arreglo_1[x]} es primo.");
            break