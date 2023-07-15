from multiprocessing.sharedctypes import Value


Flag=True
cont=0;
cont1=0;
nom=input("Ingrese un nombre de juego: ");
print("");
print("--------------------");
print("      Juegos Duoc   ");
print("--------------------\n");
palabra=input("Ingrese una palabra: ");
print("");
for caracter in palabra:
    if caracter == 'A' or caracter == 'a' or caracter == 'E' or caracter == 'e' or caracter == 'I' or caracter == 'i' or caracter == 'O' or caracter == 'o' or caracter == 'U' or caracter == 'u':
        cont=cont+1
    else:
        cont1=cont1+1
if cont <= 2:
    print(f"Mal jugado {nom}, usted ha atinado {cont} vocales, por lo cual pierde el juego.\n");
elif cont >= 3 and cont <= 5:
    print(f"Mala suerte {nom}, usted ha atinado {cont} vocales, casi ganas el juego¡\n");
else:
    print(f"Bien jugado {nom}, usted ha atinado {cont} vocales, has ganado el juego¡\n");