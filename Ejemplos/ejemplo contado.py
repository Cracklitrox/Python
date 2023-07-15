cont = 0;
num1 = int(input("Ingrese primer numero: "));
if num1 % 3 == 0:
    cont = cont + 1
num2 = int(input("Ingrese segundo numero: "));
if num2 % 3 == 0:
    cont = cont + 1
num3 = int (input("Ingrese tercer numero: "));
if num3 % 3 == 0:
    cont = cont + 1
print("");
print(f"La cantidad de numeros impares es {cont}");