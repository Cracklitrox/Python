from asyncio import open_connection
import os
from time import process_time
from unittest import result
os.system('cls')

import sys
print("---------------------------------------------------")
print("(1) Adiccion\n(2) Sustraccion\n(3) Multiplicacion\n(4) Divicion")
print("---------------------------------------------------")
adiccion=1;
sustraccion=2;
multiplicacion=3;
divicion=4;
option=int(input("Eliga que operacion quiere realizar: "))
print("")
if option <= 0 or option >= 5:
    print("La opcion elegida no se encuentra en el sistema\nPor favor elija una opcion correcta");
    print (sys.exit())
num=int(input("Ingrese un numero: "));
print("");
num1=int(input("Ingrese un segundo valor: "));
print("");
if option == 1:
    result = num + num1
    print(f"El resultado es: {result}");
elif option == 2:
    result1= num - num1
    print(f"El resultado es: {result1}");
elif option == 3:
    result2= num * num1
    print(f"El resultado es: {result2}");
elif option == 4:
    result3= num / num1
    print(f"El resultado es: {result3}");