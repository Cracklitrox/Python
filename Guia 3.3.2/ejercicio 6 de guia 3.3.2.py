Flag=True
cont=0;
vocal=0;
consonante=0;
while Flag == True:
    op=str(input("¿Desea ingresar algun nombre?: "));
    print("");
    try:
        if op == 'Si' or op == 'si' or op == 'Vale' or op == 'vale' or op == 'OK' or op == 'ok' or op == 'Ok' or op == 'Vale' or op == 'vale':
            nom=str(input("Ingrese el nombre: "));
            print("");
            if nom != str:
                print("ta mal");
            else:
                cont=cont+1
                for caracter in nom:
                    if caracter == 'A' or caracter == 'a' or caracter == 'E' or caracter == 'e' or caracter == 'I' or caracter == 'i' or caracter == 'O' or caracter == 'o' or caracter == 'U' or caracter == 'u':
                        vocal=vocal+1
                    else:
                        consonante=consonante+1
        elif op == 'No' or op == 'no' or op == 'No gracias' or op == 'no gracias':
            print("OK, se mostraran los nombres ingresados, pero se eliminara el nombre con menos caracteres.\n");
            if cont == 0:
                print("Usted no ha ingresado ningun nombre aun, por lo cual se le mostrara el menu de inicio.\n\n");
                Flag=False
            else:
                print("Aca se mostraria los nombres ingresados");
                print("");
                print("Y aca los nombres, menos el que tenia menos caracteres.");
        else:
            print(f"{op} no se encuentra registrado dentro del sistema, por favor intentelo nuevamente.");
    except:
        print("Nose, no deberia darme este mensaje");