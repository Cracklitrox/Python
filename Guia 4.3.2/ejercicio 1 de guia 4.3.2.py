from math import factorial
from mimetypes import init
def opcion_1(a):
    if a == 2 or a == 3 or a == 5 or a == 7 or a == 11 or a == 13:
        return print(f"El número:\t{num} es primo\n");
    return print(f"El número:\t{num} no es primo\n");
def opcion_2(b):
    if b == 0 or b == 1:
        resultado = 1
    elif b >= 2:
        resultado = b * factorial(b-1);
    return resultado
def opcion_3(c):
    i=0;
    f=len(c)-1
    while c[i] == c[f]:
        if i >= f:
            return True
        i+=1
        f-=1
    return False
def opcion_4():
    return ("Aplicación creada por Cracklitrox");
while True:
    cont=0;
    cont1=0;
    print("----------------------------\n     Numeros especiales     \n----------------------------\n");
    print("(1) Número Primo\n(2) Factorial\n(3) Palíndrome\n(4) Salir\n");
    try:
        op=int(input("Seleccione una opción:\t"));
        print();
        if op == 1:
            while True:
                print("Ingrese un número entre 1 y 15\n");
                try:
                    num=int(input("Ingrese el número:\t"));
                    print();
                    if num >= 1 and num <= 15:
                        print(opcion_1(num));
                        break
                    else:
                        print(f"El número ingresado:\t{num} no esta dentro del rango requerido, intentelo nuevamente\n");
                except ValueError:
                    print("\nSolo digite número\n");
        elif op == 2:
            while True:
                print("Ingrese un número entre 3 y 10\n");
                try:
                    num=int(input("Ingrese el número:\t"));
                    print();
                    if num >= 3 and num <= 10:
                        print(f"El factorial de {num} es:\t{opcion_2(num)}\n");
                        break
                    else:
                        print(f"El número ingresado:\t{num} no esta dentro del rango requerido, intentelo neuvamente\n");
                except ValueError:
                    print(f"El número:\t{num} no es primo\n");
        elif op == 3:
            while True:
                try:
                    palabra=input("Ingrese una palabra:\t");
                    print();
                    if palabra.isalpha() == True and len(palabra) >= 1:
                        if opcion_3(palabra):
                            print(f"La palabra:\t{palabra} es palíndromo\n");
                            break
                        else:
                            print(f"La palabra:\t{palabra} no es palíndromo\n");
                            break
                    else:
                        print(f"La palabra ingresada:\t{palabra} contiene números o no contiene caracteres, intentelo nuevamente\n");
                except ValueError:
                    print("\nDigite solo caracteres\n");
        elif op == 4:
            print(f"Cerrando aplicación\n{opcion_4()}\n");
            break
        else:
            print(f"El número ingresado:\t{op} no es valido dentro del rango del sistema, intentelo nuevamente\n");
    except ValueError:
        print("\nSolo digite número\n");