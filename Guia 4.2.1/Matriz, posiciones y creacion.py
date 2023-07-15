import numpy as np

# ARREGLO BIDIMENCIONAL (MATRIZ)

# la lista tiene 2 listas
lista=[[1,2,3],[4,5,6]];
print(lista)
print();
# la lista ahora se convierte en una matriz (lista de listas)
matriz=np.array(lista);
print(matriz)
print();
# imprimiria el elemento encontrada en la fila 0 que contiene (1,2,3) y de la columna 1, el cual seria (2)
print(matriz[0,1]);
print();
# se crea un arreglo sin la necesidad de crear una lista de listas antes
matriz1=np.array([[1,2,3],[4,5,6]]);
print(matriz1)
print();
# la forma tradicional de imprimar los elementos de los indices en una matriz
for x in range(len(matriz1)):
    # se entiende que la x sera la ubicacion de las filas de la matriz, en este caso 0 (1,2,3) y 1 (4,5,6)
    for z in range(0,3):
        # imprime las 2 filas, en este caso 0 que representaria (1,2,3) y 1 que representaria (4,5,6)
        # el rango se entiende que son la cantidad total de los elementos de un arreglo, en este caso 3
        print(matriz1[(x),(z)]);

# MOSTRAR UNO/VARIOS ELEMENTO/S DE LA MATRIZ

print();
# imprimiria el elemento encontrada en la fila 1 que contiene (4,5,6) y de la columna 1, el cual seria (5)
print(matriz1[1,1]);
print();
# imprimiria los elementos de la fila 0, el cual contiene (1,2,3) y el ':' representa que imprimira todos los elementos de esa fila.
print(matriz1[0,:]);
print();
# imprimiria los elementos de la fila 1, el cual contiene (4,5,6) y el ':' representa que imprimira todos los elementos de esa fila.
print(matriz1[1,:]);
print();
# imprimira todos los elementos de la columna 1 de la matriz
print(matriz1[:,1]);
print();
# imprimira todos los elementos de la fila 0, el cual contiene (1,2,3) y el ':-1' representa que imprimira todos los elementos de esa fila exceptuando el elemento ubicado en el -1, el cual seria '3'
print(matriz1[0,:-1]);
print();
# imprimira todos los elementos de la fila 0, el cual contiene (1,2,3) y el ':-2' representa que imprimira todos los elementos de esa fila exceptuando el elemento ubicado en el -2, el cual seria '2', pero tambien, los elementos a la derecha no se imprimiran, se toma como el limite del rango a imprimir
print(matriz[0,:-2]);
print();
# imprimira todos los elementos de la fila 0, el cual contiene (1,2,3) y el ':3' representa que imprimira todos los elementos de esa fila hasta el indice 3, el cual, como no hay elementos, imprimira todos los elementos de esa fila
print(matriz1[0,:3]);
print();
# imprimira todos los elementos de la fila 1, el cual contiene (4,5,6) y el '::-1' ni idea que representa, preguntar eso.
print(matriz[1,::-1]);