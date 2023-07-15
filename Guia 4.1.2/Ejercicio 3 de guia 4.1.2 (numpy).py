import numpy as np
import random
arregloA=np.arange(10);
arregloB=np.arange(10);
for x in range(10):
    arregloA[x]=random.randrange(0,300);
    arregloB[x]=random.randrange(0,300);
print(f"La suma de los elementos del arreglo A es:\t{arregloA.sum()}\n\nLa suma de los elementos del arreglo B es:\t{arregloB.sum()}\n");
print(f"La suma de los elementos de ambos arreglos es:\t{arregloA.sum()+arregloB.sum()}\n");
enumeracion=np.arange(1,11);
for z in range(len(arregloB)):
    if arregloB[z] % 2 == 0:
        continue
    else:
        print(f"La tabla de multiplicar de {arregloB[z]}\n");
        for x in range(10):
            print(f"{enumeracion[x]}) {arregloB[z]} x {enumeracion[x]} = {arregloB[z]*enumeracion[x]}");
        print();