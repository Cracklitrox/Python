import numpy as np
import random
arreglo=np.arange(10);
for x in range(10):
    arreglo[x]=random.randrange(0,100);
copia_arreglo=arreglo;
print(f"El elemento mayor del arreglo es:\t{copia_arreglo.max()}\nEl elemento menor del arreglo es:\t{copia_arreglo.min()}\nLa suma de todos los elementos del arreglo es:\t{copia_arreglo.sum()}\nEl promedio de los elementos del arreglo es:\t{copia_arreglo.mean()}\nLos elementos del arreglo son:\t{copia_arreglo}\n");