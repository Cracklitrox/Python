import random
import numpy as np

# Ejercicio 1 de guia 4.2.1

matriz=np.zeros((3,3));
for x in range(len(matriz)):
    for z in range(0,3):
        r=random.randrange(0,100);
        matriz[x][z]=r
print();
print(f"Los elementos de la matriz son\n");
print(matriz);
print();

# Ejercicio 2 de guia 4.2.1

print(f"El promedio de los elementos de la matriz es:\t{matriz.mean()}\n");
print(f"La suma de los elementos de la matriz es:\t{matriz.sum()}\n");
print(f"El elemento mayor de la matriz es:\t{matriz.max()}\n");
print(f"El elemento menor de la matriz es:\t{matriz.min()}\n");
print(f"Los elementos de la diagonal principal son:\t{matriz.diagonal()}\n");