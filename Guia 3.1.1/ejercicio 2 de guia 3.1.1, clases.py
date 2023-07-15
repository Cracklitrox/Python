i=0;
cont=0;
cont1=0;
while i < 10:
    i=i+1
    letra=input("Ingrese una letra: ");
    print("");
    if letra == 'a' or letra == 'A' or letra == 'e' or letra == 'E' or letra == 'i' or letra == 'I' or letra == 'o' or letra == 'O' or letra == 'u' or letra == 'U':
        cont=cont+1
    else:
        cont1=cont1+1
print(f"El total de letras vocales es: {cont}");
print("");
print(f"El total de letras consonantes es: {cont1}");