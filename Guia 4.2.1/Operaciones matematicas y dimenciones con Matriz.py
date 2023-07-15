from array import array
import numpy as np

# Operaciones con matriz

matriz=np.array([(1,2,3),(4,5,6)]);
# Muestra la suma de todos los elementos de la matriz
print(matriz.sum());
print();
# Muestra la suma de todos los elementos de la fila 0 de la matriz
print(matriz[0,:].sum());
print();
# Muestra la suma de todos los elementos de la fila 1 de la matriz
print(matriz[1,:].sum());
print();
# Muestra las dimenciones de la matriz
print(matriz.ndim);
print();
# Muestra la cantidad de filas y columnas de la matriz
print(matriz.shape);
print();
# Muestra la cantidad de elementos contenidos en la matriz
print(matriz.size);
print();
# Muestra las 2 matrices seguidas, preguntar para que es el axis
m2=np.array([(7,8,9),(10,11,12)]);
print(np.concatenate((matriz,m2), axis=0));
print();
# Muestra la suma de todos los elementos de la fila 0 de ambas matrices
m=np.concatenate((matriz,m2), axis=0);
print(m[0,:].sum());
print();
# Muestra la suma de todos los elementos de la columna 0 de ambas matrices, ya que esta definida por m, se saltara el paso
print(m[:,0].sum());