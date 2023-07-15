sw=1;
nom=input("Ingrese su nombre de juego: ");
print("");
while sw == 1:
    result=0
    print("--------------------");
    print("     Magia Duoc     ");
    print("--------------------");
    print("");
    op=input("¿Desea ver un truco de magia?: ");
    print("");
    try:
        if op == 'Si' or op == 'si' or op == 'OK' or op == 'Ok' or op == 'ok' or op == 'Vale' or op == 'vale' or op == 'Bueno' or op == 'bueno':
            num=int(input(f"Ingrese un numero entero positivo mayor a 0 {nom}: "));
            print("");
            if num <= 0:
                print(f"El numero {num} no es valido {nom}, intente nuevamente");
                print("");
            else:
                print(f"La suma de estos numeros daran el cuadrado de {num}, {nom}");
                print("");
                x=range(1,num*2,2)
                print("--------------------------------------");
                for n in x:
                    print(f"|{n}|");
                    result=result+n
                print("--------------------------------------");
                print("");
                print(f"El cuadrado de {num} es: {result}")
                print("");
                op1=input(f"¿Desea repetir la magia {nom}?: ");
                print("");
                if op1 == 'Si' or op1 == 'si' or op1 == 'OK' or op1 == 'Ok' or op1 == 'ok' or op1 == 'Vale' or op1 == 'vale' or op1 == 'Bueno' or op1 == 'bueno':
                    print("");
                elif op1 == 'No' or op1 == 'no' or op1 == 'No gracias' or op1 == 'no gracias' or op1 == 'No Gracias':
                    print(f"Gracias por jugar {nom} :D");
                    sw=0;
                else:
                    print(f"{op1} no esta registrado en el sistema {nom}, se mostrara el menu de inicio nuevamente.");
        elif op == 'No' or op == 'no' or op == 'No gracias' or op == 'no gracias' or op == 'No Gracias':
            print(f"Gracias por jugar {nom} :D");
            sw=0;
        else:
            print(f"{op} no esta registrado en el sistema, se mostrara el menu de inicio nuevamente.");
    except:
        print("");
        print(f"{nom} ha escrito mal lo ultimo que digito, por favor intente nuevamente.");