suma = 0;
num1 = int(input("Ingrese primer numero: "));
if num1 % 2 == 0:
    suma= suma + num1
num2 = int(input("Ingrese segundo numero: "));
if num2 % 2 == 0:
    suma= suma + num2
num3 = int(input("Ingrese tercer numero: "));
if num3 % 2 == 0:
    suma= suma + num3
print(f"El resultado de la suma de los numeros pares es: {suma}");