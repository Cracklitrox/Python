from tkinter import Y


cont=0;
cont1=0;
sw=1;
while sw == 1:
    print("-------------");
    print("(1) Opcion 1");
    print("");
    print("(2) Opcion 2");
    print("");
    print("(3) Opcion 3");
    print("-------------");
    print("");
    try:
        print("------------------------");
        op=int(input("Seleccione una opcion: "));
        print("------------------------");
        print("");
        if op > 0 and op < 4:
            if op == 1:
                print("Usted a seleccionado la opcion 1");
                print("");
                print(f"La opcion {op} es impar.");
                print("");
                conti=input("¿Desea salir de la aplicacion? (Si o No): ");
                print("");
                if conti == 'Si' or conti == 'si':
                    print("Gracias por usar nuestra aplicacion");
                    sw=0
                elif conti == 'No' or conti == 'no':
                    print("Se le mostrara nuevamente el menu:");
                    print("");
                else:
                    print(f"{conti} no es un caracter valido, se mostrara el menu de inicio.");
                    print("");
            elif op == 2:
                print("Usted a seleccionado la opcion 2.");
                print("");
                num1=int(input("Ingrese un numero mayor o igual a 0: "));
                print("");
                if num1 >= 0:
                    print(f"Se le mostrara los primeros 10 numeros de la serie Fibonacci del numero {num1}");
                    print("");
                    x=range(1,11,1)
                    a=0;
                    b=1;
                    c=num1;
                    for n in x:
                        a=b;
                        b=c;
                        c=a+b;
                        print(f"({n}) {c}");
                    print("");
                    conti=input("¿Desea salir de la aplicacion? (Si o No): ");
                    print("");
                    if conti == 'Si' or conti == 'si':
                        print("Gracias por usar nuestra aplicacion");
                        sw=0
                    elif conti == 'No' or conti == 'no':
                        print("Se le mostrara nuevamente el menu:");
                        print("");
                    else:
                        print(f"{conti} no es un caracter valido, se mostrara el menu de inicio.");
                        print("");
                else:
                    print("Valor incorrecto, se mostrara el menu de inicio");
                    print("");
            elif op == 3:
                print("Usted a seleccionado la opcion 3.");
                print("");
                print("Usted saldra del sistema");
                print("");
                print("Gracias por usar nuestra aplicacion.");
                sw=0
            else:
                print(f"La opcion {op} no esta dentro del sistema");
                print("");
                print("Se mostrara el menu nuevamente.");
                print("");
        else:
            print(f"La opcion {op} no esta dentro del sistema");
            print("");
            print("Se mostrara el menu nuevamente.");
            print("");
    except ValueError:
        print("");
        print(f"Por favor: {op} no es una opcion valido dentro del sistema, por favor intentelo nuevamente.");
        print("");