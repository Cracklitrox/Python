import numpy as np
import random
arregloA=np.arange(100);
for x in range(100):
    arregloA[x]=random.randrange(0,500);
print(f"Los elementos contenidos en los indice pares son:\t{arregloA[np.mod(arregloA,2) == 0.0]}");
print(f"El elemento mayor del arreglo es:\t{arregloA.max()}\n");
print(f"El indice del elemento mayor del arreglo es:\t{arregloA.argmax()}\n");
print(f"El elemento menor del arreglo es:\t{arregloA.min()}\n");
copia_arregloA=arregloA[:].copy();
copia_arregloA=copia_arregloA*3
print(f"Los elementos del segundo arreglo multiplicado por 3 son:\t{copia_arregloA}\n");
print(f"La suma de los elementos del segundo arreglo es:\t{copia_arregloA.sum()}\n");
print(f"El promedio de los elementos del segundo arreglo es:\t{copia_arregloA.mean()}\n");