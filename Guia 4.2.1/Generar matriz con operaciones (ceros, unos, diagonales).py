import numpy as np

# GENERAR MATRIZES CON OPERACIONES

# generar matriz con ceros en filas y columnas
matriz=np.zeros((3,3));
print(matriz);
print();
# imprimir los elementos de la matriz
for x in range(len(matriz)):
    for z in range(0,3):
        print(matriz[x][z]);
print();
# generar matriz con unos en filas y columnas
matriz_1=np.ones((3,3));
print(matriz_1);
print();
# imprimir los elementos de la matriz
for x in range(len(matriz_1)):
    for z in range(0,3):
        print(matriz_1[x][z]);
print();
# generar matriz con diagonal principal con 1
# genera una matriz donde 'np.diag([1,1,1])' representa que en la fila 0, columna 0, el numero sera 1. Luego, en la fila 1, columna 1, el numero sera 1. Finalmente, en la fila 2, columna 2, el numero sera 1
matriz_diagonal=np.diag([1,1,1]);
print(matriz_diagonal);
print();
# imprimir los elementos de la matriz
for x in range(len(matriz_diagonal)):
    for z in range(0,3):
        print(matriz_diagonal[x][z]);
print();
# generar matriz con diagonal principal con cadenas
# genera una matriz donde 'np.dia([' ','X',9])' representa que en la fila 0, columna 0, el elemento sera ' ' (basicamente, esta vacio). Luego, en la fila 1, columna 1, el elemento sera 'X'. Finalmente, en la fila 2, columna 2, el numero sera 9
matriz_diagonal_cadena=np.diag([' ','X',9]);
print(matriz_diagonal_cadena);
print();
# imprimir los elementos de la matriz
for x in range(len(matriz_diagonal_cadena)):
    for z in range(0,3):
        print(matriz_diagonal_cadena[x][z]);
print();