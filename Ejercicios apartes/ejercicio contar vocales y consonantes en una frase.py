letra=input("Ingrese una frase: ");
print("");
cont=0;
cont1=0;
cont2=0;
for caracter in letra:
    if caracter == 'A' or caracter == 'a' or caracter == 'E' or caracter == 'e' or caracter == 'I' or caracter == 'i' or caracter == 'O' or caracter == 'o' or caracter == 'U' or caracter == 'u':
        cont+=1
    elif caracter == ' ' or caracter == '_' or caracter == '-' or caracter == ':' or caracter == ',' or caracter == ';' or caracter == '.' or caracter == '#':
        cont1+=1
    else:
        cont2+=1
print(f"La cantidad de vocales son: {cont}\n\nLa cantidad de consonantes son: {cont2}");