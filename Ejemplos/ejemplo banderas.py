from operator import truediv


flag = False;
num = int(input("Ingrese un numero: "));
if num % 2 == 0:
    flag = True
if flag:
    print(f"El numero {num} es par");
else:
    print(f"El numero {num} es impar");