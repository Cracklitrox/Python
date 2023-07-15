cont=0;
cont1=0;
cont2=0;
x=range(5);
for n in x:
    num=int(input("Ingrese numero: "));
    print("");
    if num > 0:
        cont=cont+1
    elif num < 0:
        cont1=cont1+1
    elif num == 0:
        cont2=cont2+1
print(f"La cantidad de numeros mayores a 0 es: {cont}");
print("");
print(f"La cantidad de numeros menores a 0 es: {cont1}");
print("");
print(f"La cantidad de numeros iguales a 0 es: {cont2}");