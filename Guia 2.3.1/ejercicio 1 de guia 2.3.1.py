suma= 0;
cont= 0;
num1=int(input("Ingrese primer numero: "));
if num1 > 0 and num1 % 2 == 0:
    suma= suma + num1
else:
    cont= cont + 1
num2=int(input("Ingrese segundo numero: "));
if num2 > 0 and num2 % 2 == 0:
    suma= suma + num2
else:
    cont= cont + 1
num3=int(input("Ingrese tercer numero: "));
if num3 > 0 and num3 % 2 == 0:
    suma= suma + num3
else:
    cont= cont + 1
print(f"La suma de los numeros mayores a 0 y par es: {suma}\n");
print(f"La cantidad de numeros menores a 0, impares e iguales a 0 son: {cont}");