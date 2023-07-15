from enum import Flag
from sys import flags


Flag=True
while Flag == True:
    print("                     ----------------------");
    print("                    |      Estadio Duoc    |");
    print("                     ----------------------");
    print("");
    print("---------------------------------------------------------------");
    print("|   Cliente    | |           Intervalos              | |Precio|");
    print("|              | |                                   | |      |");
    print("|   Menores    | | Mayores a 7 años y menores que 12 | |$4.000|");
    print("|   Adulto     | |  Desde los 12 años hasta los 65   | |$7.000|");
    print("| Adulto Mayor | |         Desde los 65 años         | |$3.000|");
    print("---------------------------------------------------------------");
    print("");
    op=input("¿Desea comprar boletos?: ");
    print("");
    cont=0;
    sum=0;
    cont1=0;
    sum1=0;
    cont2=0;
    sum2=0;
    try:
        if op == 'Si' or op == 'si' or op == 'Bueno' or op == 'bueno' or op == 'Vale' or op == 'vale' or op == 'OK' or op == 'Ok' or op == 'ok':
            num=int(input("¿Cuantos boletos desea comprar?: "));
            print("");
            if num <= 0:
                print(f"{num} no es un numero valido dentro del sistema, por favor intentelo nuevamente\n\n");
            elif num >= 1:
                x=range(num);
                for n in x:
                    num1=int(input("Ingrese la edad del cliente para su boleta: "));
                    print("");
                    if num1 >= 7 and num1 <= 11:
                        cont=cont+1
                        sum=sum+4000
                    elif num1 >= 12 and num1 <= 65:
                        cont1=cont1+1
                        sum1=sum1+7000
                    elif num1 >= 66:
                        cont2=cont2+1
                        sum2=sum2+3000
                    elif num1 <=6 and num1 >=1:
                        print(f"{num1} no es valido dentro del sistema, por favor ingrese los valores que se les indica.\n\n");
                    else:
                        print(f"{num1} no es un numero valido dentro del sistema, por favor intentelo nuevamente.\n\n");
                result=sum+sum1+sum2
                print("Compra");
                print("");
                print("---------------------------------------");
                print(f"{cont} Menor(s):         ${sum}");
                print(f"{cont1} Adulto(s):        ${sum1}");
                print(f"{cont2} Adulto Mayor(s):  ${sum2}");
                print("---------------------------------------");
                print("");
                print(f"Total:              ${result}");
                print("");
                op2=input("¿Desea comprar mas boletos o desea salir del sistema?: ");
                print("");
                if op2 == 'Si' or op2 == 'si' or op2 == 'Bueno' or op2 == 'bueno' or op2 == 'Vale' or op2 == 'vale' or op2 == 'OK' or op2 == 'Ok' or op2 == 'Comprar mas' or op2 == 'comprar mas' or op2 == 'Comprar Mas' or op2 == 'Mas' or op2 == 'mas':
                    print("Se le mostrara el menu nuevamente para hacer sus compras de 0.\n\n");
                elif op2 == 'No' or op2 == 'no' or op2 == 'No gracias' or op2 == 'no gracias' or op2 == 'No Gracias ' or op2 == 'Salir' or op2 == 'salir':
                    print("Gracias por usar nuestro programa, vuelva otro dia :D")
                    Flag=False
                else:
                    print(f"{op2} no esta dentro del sistema, por favor intentelo nuevamente.\n\n")
            else:
                print(f"{num} no es un caracter valido dentro del sistema, por favor intentelo nuevamente.\n\n");
        elif op == 'No' or op == 'no' or op == 'No gracias' or op == 'no gracias' or op == 'No Gracias ':
            print("Gracias por usar nuestro programa, vuelva otro dia :D");
            Flag=False
        else:
            print(f"{op} no se encuentra registrado dentro del sistema, por favor intentelo nuevamente.\n\n");
    except:
        print("");
        print(f"El ultimo caracter digitalizado es incorrecto, por favor intentelo nuevamente.");
        print("");