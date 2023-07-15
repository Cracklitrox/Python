import random
from re import A
from tkinter import N


arregloA=[];
for i in range(100):
    arregloA.append(random.randrange(0,500));
print(f"Los numeros del arreglo son: {arregloA}\n\n");
for x in range(len(arregloA)):
    if x == 0:
        continue
    else:
        if x % 2 == 0:
            print(f"El numero en la posición {x} es: {arregloA[x]}\n\n");
print(f"El número maximo del arreglo es: {max(arregloA)}\n\n");
print(f"La posición que ocupa {max(arregloA)} en el arreglo es: {arregloA.index(max(arregloA))}\n");
print(f"El número menor del arreglo es: {min(arregloA)}\n\n");
sum=0;
copia_arregloA=list(arregloA);
for z in range(len(copia_arregloA)):
    print(f"La multiplicacion de {copia_arregloA[z]} por 3 es: {copia_arregloA[z]*3}\n");
    sum=sum+copia_arregloA[z]*3;
print(f"\nLa suma de los numeros multiplicados por 3 es: {sum}\n\n");
print(f"El promedio de los numeros multiplicados es: {sum/100}");