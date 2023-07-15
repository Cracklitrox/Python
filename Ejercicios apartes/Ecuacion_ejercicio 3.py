from asyncio import open_connection
import os
from time import process_time
from unittest import result

print("|x**2+3x+1|");
print("|---------|");
print("|    4    |");
print("");
x=int(input("Ingrese un valor para X: "));
result= (x**2+3+x+1)/4;
print("");
print(f"El resultado de la ecuación es: {result}");