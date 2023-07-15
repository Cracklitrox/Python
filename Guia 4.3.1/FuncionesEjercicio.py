def iva(a):
    return a*0.19
def descuento(b,c):
    return b - (b * c / 100)
def imc(d,e):
    return d / e ** 2
def opcion1():
    while True:
        try:
            precio=int(input("Ingrese el precio del producto:\t"));
            print();
            if precio >= 0:
                print(f"El iva del producto con valor {precio} es:\t{iva(precio)}\n");
                break
            else:
                print(f"El precio ingresado:\t{precio} es menor a 0, no se puede hacer la operacion, intentelo con valores mayores a 0\n");
        except ValueError:
            print("\nSolo digite números\n");
def opcion2():
    while True:
        try:
            precio=int(input("Ingrese el precio del producto:\t"));
            print();
            des=int(input("Ingrese el descuento: "));
            print();
            if precio >= 0:
                if des >= 1 and des <= 99:
                    print(f"El resultado del descuento aplicado al producto es:\t{descuento(precio,des)}\n");
                    break
                else:
                    print(f"El descuento ingresado:\t{des} no es valido en el rango de 1-100, intentelo nuevamente.\n");
            else:
                print(f"El precio ingresado:\t{precio} es menor a 0, intentelo con numeros mayores a 0\n");
        except ValueError:
            print("\nSolo digite números\n");
def opcion3():
    while True:
        try:
            peso=int(input("Ingrese su peso (Sin decimales):\t"));
            print();
            altura=float(input("Ingrese su altura (Con decimales):\t"));
            print();
            if peso >= 1 and peso <= 500:
                if altura >= 0.000 and altura <= 3.00:
                    if imc(peso,altura) <= 18.5:
                        print(f"Su indice de masa corporal es:\t{imc(peso,altura)}\nUsted tiene bajo peso\n");
                        break
                    elif imc(peso,altura) >= 18.5 and imc(peso,altura) <= 24.9:
                        print(f"Su indice de masa corporal es:\t{imc(peso,altura)}\nUsted tiene un peso adecuado\n");
                        break
                    elif imc(peso,altura) >= 25.0 and imc(peso,altura) <= 29.9:
                        print(f"Su indice de masa corporal es:\t{imc(peso,altura)}\nUsted tiene sobrepeso\n");
                        break
                    elif imc(peso,altura) >= 30.0 and imc(peso,altura) <= 34.9:
                        print(f"Su indice de masa corporal es:\t{imc(peso,altura)}\nUsted tiene obesidad grado 1\n");
                        break
                    else:
                        print(f"Su indice de masa corporal es:\t{imc(peso,altura)}\nUsted tiene obesidad grado 2\n");
                        break
                else:
                    print(f"La altura ingresada:\t{altura} no es valido dentro del rango del sistema, intentelo nuevamente\n");
            else:
                print(f"El peso ingresado:\t{peso} no es valido dentro del rango del sistema, intentelo nuevamente\n");
        except ValueError:
            print("\nSolo digite números\n");