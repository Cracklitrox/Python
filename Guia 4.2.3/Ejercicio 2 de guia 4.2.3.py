import numpy as np
matriz=np.zeros((10,4));
i=0
for x in range(len(matriz)):
    for z in range(4):
        i+=1
        matriz[x][z]=i
print(f"Los asientos del bus son los siguientes\n");
print(matriz);