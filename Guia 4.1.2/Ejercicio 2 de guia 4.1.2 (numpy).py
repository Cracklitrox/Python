import numpy as np
import random
arreglo_1=np.arange(10);
for x in range(10):
    arreglo_1[x]=random.randrange(0,1000);
print(f"Los elementos del arreglos son:\t{arreglo_1}\n");
cont=0;
sum=0;
for z in range(len(arreglo_1)):
    if arreglo_1[z] % 2 == 0:
        cont+=1
    else:
        sum=sum+arreglo_1[z]
print(f"La cantidad de elementos pares del arreglo son:\t{cont}\n");
print(f"La suma de los elementos impares del arreglo es:\t{sum}\n");
def primo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    for x in range(2,int(numero/2)):
        if numero % x == 0:
            return False
    return True
print(primo);
for x in range(len(arreglo_1)):
    if arreglo_1[x] == primo:
        print(f"El numero {arreglo_1[x]} es primo.\n");
    else:
        continue