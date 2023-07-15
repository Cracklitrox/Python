from cmath import pi
from re import A


def area_de_un_circulo(a):
    r=int(pi*a**2)
    return print(f"El area del circulo es:\t{r} (Aproximado a la decima)\n");
def perimetro_de_un_cuadrado(a):
    c=a+a+a+a
    return print(f"El perimetro del cuadrado es:\t{c}\n");
def opcion1():
    while True:
        try:
            num=int(input("Ingrese el radio de su circulo:\t"));
            print();
            if num >= 1:
                area_de_un_circulo(num);
                break
            else:
                print("Ingrese valores mayores a 0 para calcular el area del circulo\n");
        except ValueError:
            print("\nSolo digite un numero\n");
def opcion2():
    while True:
        try:
            num=int(input("Ingrese el lado de su cuadrado:\t"));
            print();
            if num >= 1:
                perimetro_de_un_cuadrado(num);
                break
            else:
                print("Ingrese valores mayores a 0 para calcular el perimetro de su cuadrado\n");
        except ValueError:
            print("\nSolo digite numeros\n");
while True:
    print("-----------------\n    Geometria    \n-----------------\n");
    print("(1) Área de un circulo\n(2) Perímetro de un cuadrado\n(3) Salir\n");
    try:
        op=int(input("Seleccione una opción:\t"));
        print();
        if op == 1:
            opcion1();
        elif op == 2:
            opcion2();
        elif op == 3:
            print("Cerrando aplicación\n");
            break
        else:
            print(f"El número ingresado:\t{op} no es valido en el sistema, intentelo nuevamente\n");
    except ValueError:
        print("\nSolo digite un numero\n");