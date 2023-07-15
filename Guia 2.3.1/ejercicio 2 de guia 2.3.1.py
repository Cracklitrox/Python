num1=int(input("Ingrese un numero: "));
if num1 >= -9 and num1 <= 9:
    print(f"El numero {num1} tiene 1 digito");
elif num1 >= -99 and num1 <= 99:
    print(f"El numero {num1} tiene 2 digitos");
elif num1 >= -999 and num1 <= 999:
    print(f"El numero {num1} tiene 3 digitos");