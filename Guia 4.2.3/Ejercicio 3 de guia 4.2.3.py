import random
import numpy as np
matriz=np.zeros((4,5));
for x in range(len(matriz)):
    for z in range(5):
        a=random.randrange(0,100);
        matriz[x][z]=a
print(f"La suma de los elementos de la fila 0 son:\t{matriz[0,:].sum()}\nLa suma de los elementos de la fila 1 son:\t{matriz[1,:].sum()}\nLa suma de los elementos de la fila 2 son:\t{matriz[2,:].sum()}\nLa suma de los elementos de la fila 3 son:\t{matriz[3,:].sum()}\n\n");
print(f"La suma de los elementos de la columna 0 son:\t{matriz[:,0].sum()}\nLa suma de los elementos de la columna 1 son:\t{matriz[:,1].sum()}\nLa suma de los elementos de la columna 2 son:\t{matriz[:,2].sum()}\nLa suma de los elementos de la columna 3 son:\t{matriz[:,3].sum()}\nLa suma de los elementos de la columna 4 son:\t{matriz[:,4].sum()}\n\n");
print(f"La suma de los elementos de la diagonal principal son:\t{matriz.diagonal().sum()}\n\n");
cont=0;
for x in range(len(matriz)):
    for z in range(5):
        if matriz[x][z] % 2 == 0:
            continue
        else:
            cont+=1
print(f"La cantidad de elementos impares en la matriz son:\t{cont}\n");