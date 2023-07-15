sw=1;
nom=input("Ingrese su nombre de juego: ");
print("");
while sw == 1:
    cont=0;
    cont1=0;
    cont2=0;
    print("-----------------------");
    print("       Juego Duoc      ");
    print("-----------------------");
    print("");
    try:
        letra=input("Ingrese una frase: ");
        print("");
        for caracter in letra:
            if caracter == 'A' or caracter == 'a' or caracter == 'E' or caracter == 'e' or caracter == 'I' or caracter == 'i' or caracter == 'O' or caracter == 'o' or caracter == 'U' or caracter == 'u':
                cont+=1
            elif caracter == ' ' or caracter == '_' or caracter == '-' or caracter == ':' or caracter == ',' or caracter == ';' or caracter == '.' or caracter == '#':
                cont1+=1
            else:
                cont2+=1
        if cont > 0 and cont < 3:
            print(f"Mala suerte {nom}, perdio el juego, solo ingreso {cont} vocales.");
            print("");
            op=input("¿Desea jugar nuevamente?: ");
            print("");
            if op == 'Si' or op == 'si' or op == 'OK' or op == 'Ok' or op == 'ok' or op == 'Vale' or op == 'vale' or op == 'Bueno' or op == 'bueno':
                print("");
            elif op == 'No' or op == 'no' or op == 'No gracias' or op == 'no gracias' or op == 'No Gracias':
                print("Gracias por jugar :D");
                sw=0;
            else:
                print(f"{op} no esta dentro del sistema, pero se le devolvera al menu inicial.");
                print("");
        elif cont >= 3 and cont <= 5:
            print(f"Felicidades {nom}, casi gana el juego, usted ingreso {cont} vocales.");
            print("");
            op=input("¿Desea jugar nuevamente?: ");
            print("");
            if op == 'Si' or op == 'si' or op == 'OK' or op == 'Ok' or op == 'ok' or op == 'Vale' or op == 'vale' or op == 'Bueno' or op == 'bueno':
                print("");
            elif op == 'No' or op == 'no' or op == 'No gracias' or op == 'no gracias' or op == 'No Gracias':
                print("Gracias por jugar :D");
                sw=0;
            else:
                print(f"{op} no esta dentro del sistema, pero se le devolvera al menu inicial.");
                print("");
        elif cont > 5:
            print(f"Felicidades {nom}, haz ganado el juego, usted a ingresado {cont} vocales.");
            print("");
            op=input("¿Desea jugar nuevamente?: ");
            print("");
            if op == 'Si' or op == 'si' or op == 'OK' or op == 'Ok' or op == 'ok' or op == 'Vale' or op == 'vale' or op == 'Bueno' or op == 'bueno':
                print("");
            elif op == 'No' or op == 'no' or op == 'No gracias' or op == 'no gracias' or op == 'No Gracias':
                print("Gracias por jugar :D");
                sw=0;
            else:
                print(f"{op} no esta dentro del sistema, pero se le devolvera al menu inicial.");
                print("");
        else:
            print(f"No ingreso ninguna frase {nom}, es necesiario escribir algo para jugar\n\nIntentelo nuevamente");
            print("");
    except ValueError:
        print(f"{letra} no se encuetra dentro del sistema, se le enviara al menu nuevamente.");