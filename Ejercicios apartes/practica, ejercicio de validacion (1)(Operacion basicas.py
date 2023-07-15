from ast import Raise, type_ignore
from decimal import DivisionByZero
from importlib import invalidate_caches


sw=1;
while sw == 1:
    print("---------------------------------------------------");
    print("(1) Adiccion\n(2) Sustraccion\n(3) Multiplicacion\n(4) Divicion\n(5) Salir");
    print("---------------------------------------------------");
    print("");
    try:
        option=int(input("Eliga una opción: "));
        print("");
        if option > 0 and option < 5:
            num=int(input("Ingrese un numero: "));
            print("");
            num1=int(input("Ingrese un segundo valor: "));
            print("");
            if option == 1:
                result=num+num1
                print(f"El resultado de {num}+{num1} es: {result}");
                print("");
                op=input("¿Desea salir de la aplicacion?: ");
                print("");
                if op == 'Si' or op == 'si':
                    print("Gracias por usar el programa.");
                    sw=0
                elif op == 'No' or op == 'no':
                    print("Se le mostrara el menu nuevamente");
                    print("");
                else:
                    print(f"{op} no esta dentro del sistema, se le mostrara el menu de inicio nuevamente.\n\n")
            elif option == 2:
                result1=num-num1
                print(f"El resultado de {num}-{num1} es: {result1}");
                print("");
                op=input("¿Desea salir de la aplicacion?: ");
                print("");
                if op == 'Si' or op == 'si':
                    print("Gracias por usar el programa.");
                    sw=0
                elif op == 'No' or op == 'no':
                    print("Se le mostrara el menu nuevamente");
                    print("");
                else:
                    print(f"{op} no esta dentro del sistema, se le mostrara el menu de inicio nuevamente.\n\n")
            elif option == 3:
                result2=num*num1
                print(f"El resultado de {num}*{num1} es: {result2}");
                print("");
                op=input("¿Desea salir de la aplicacion?: ");
                print("");
                if op == 'Si' or op == 'si':
                    print("Gracias por usar el programa.");
                    sw=0
                elif op == 'No' or op == 'no':
                    print("Se le mostrara el menu nuevamente");
                    print("");
                else:
                    print(f"{op} no esta dentro del sistema, se le mostrara el menu de inicio nuevamente.\n\n")
            elif option == 4:
                    result3=num/num1
                    print(f"El resultado de {num}/{num1} es: {result3}");
                    print("");
                    op=input("¿Desea salir de la aplicacion?: ");
                    print("");
                    if op == 'Si' or op == 'si':
                        print("Gracias por usar el programa.");
                        sw=0
                    elif op == 'No' or op == 'no':
                        print("Se le mostrara el menu nuevamente");
                        print("");
                    else:
                        print(f"{op} no esta dentro del sistema, se le mostrara el menu de inicio nuevamente.\n\n")
        elif option == 5:
                print("Gracias por usar el programa.");
                sw=0;
        else:
            print(f"La opcion {option} no esta dentro del sistema");
            print("");
            print("Se mostrara el menu nuevamente, intente nuevamente.");
            print("");
    except ValueError:
        print("");
        print(f"Lo que usted digito no esta dentro del sistema\n\nPor favor intente nuevamente.");
        print("");