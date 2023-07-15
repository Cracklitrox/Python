x=range(1);
for n in x:
    num=int(input("Ingrese un numero mayor a 0: "));
    print("");
    if num <= 0:
        print(f"{num} no es un numero valido, por favor intente nuevamente.");
    else:
        result=num%2
if num == 2 or result == 1:
    print(f"{num} es un numero primo.");
else:
    print(f"{num} es un numero compuesto.");