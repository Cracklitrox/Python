import numpy as np
import random
matriz1=np.zeros((3,3));
matriz2=matriz1[:].copy();
for x in range(len(matriz1)):
    for z in range(0,3):
        r=random.randrange(0,100);
        matriz1[x][z]=r
        r=random.randrange(0,100);
        matriz2[x][z]=r
print(f"Los elementos de la matriz 1 son\n");
print(matriz1);
print();
print(f"Los elementos de la matriz 2 son\n");
print(matriz2);
print();
matrices=np.zeros((3,3));
for x in range(3):
    for z in range(3):
        matrices[x][z]=matriz1[x][z]*matriz2[x][z]
print(f"La multiplicacion entre la matriz 1 y 2 son:\n");
print(matrices)