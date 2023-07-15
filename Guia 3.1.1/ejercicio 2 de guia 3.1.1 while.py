num=int(input("Ingrese un numero positivo entre 103 y 987: "));
print("");
if num < 103 and num > 987:
    print(f"El numero {num} no esta entre las opciones del sistema, por favor intente nuevamente.");
else:
    result=int(num/10);
    modulo=(num%10)*10;
    result1=int(result/10);
    modulo1=result%10;
    todo=(modulo+modulo1)*10;
    result2=int(result1/10);
    modulo2=result1%10;
    todo1=(todo+modulo2);
    print(f"{todo1} es su numero dado vuelta.");