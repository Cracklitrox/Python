def opcion1():
    while True:
        print(".................................\n    ¿Cuantos cafes desea comprar?    \n.................................\n");
        try:
            cantidad=int(input("Digite la cantidad que desea comprar:\t"));
            print();
            if cantidad >= 1:
                cafes(cantidad)
                break
            else:
                print(f"La cantidad ingresada:\t{cantidad} no es valido, elija aun que sea 1 cafe\n");
        except ValueError:
            print("\nSolo digite numeros\n");
def cafes(a):
    i=0;
    cantidad_cafes=[];
    while i < a:
        print("-----------------------------------------\n     Tenemos las siguientes opciones     \n-----------------------------------------\n");
        print("(1) Espresso = $1.500\n(2) Capuchino = $1.800\n(3) Latte = $1.600\n(4) Moca = $1.700\n");
        try:
            eleccion=int(input("Elija el cafe que desea:\t"));
            print();
            if eleccion >= 1 and eleccion <= 4:
                print("Cafe registrado\n");
                cantidad_cafes.append(eleccion);
                i+=1;
            else:
                print(f"El número ingresado:\t{eleccion} no se encuentra en el menú, por favor intentelo nuevamente\n");
        except ValueError:
            print("\nSolo digite numeros\n");
    calculo(cantidad_cafes);
def calculo(a):
    total=0;
    for x in range(len(a)):
        if a[x] == 1:
            total=total+1500;
        elif a[x] == 2:
            total=total+1800;
        elif a[x] == 3:
            total=total+1600;
        elif a[x] == 4:
            total=total+1700;
    while True:
        descuento=0;
        try:
            if total >= 3000:
                descuento=total-(total*0.1);
                print(f"Felicidades, por compras superiores o iguales a $3.000 se le otorga un 10% en el total de su compra\nTotal a pagar:\t${descuento}\n");
                pago=int(input("Ingrese el monto a pagar:\t"));
                print();
                if pago < descuento:
                    print("El monto ingresado es insuficiente para cancelar los cafes, intentelo nuevamente\n");
                elif pago >= descuento:
                    vuelto=pago-descuento
                    print(f"Gracias por su compra, tenga su vuelto:\t${vuelto}\n");
                    break
            else:
                print(f"Total a pagar:\t${total}\n");
                pago=int(input("Ingrese el monto a pagar:\t"));
                print();
                if pago < total:
                    print("El monto ingresado es insuficiente para cancelar el cafe, intentelo nuevamente\n");
                elif pago >= total:
                    vuelto=pago-total
                    print(f"Gracias por su compra, tenga su vuelto:\t${vuelto}\n");
                    break
        except ValueError:
            print("\nSolo digite numeros\n");
while True:
    print("----------------------\n    Cafeteria Duoc    \n----------------------\n");
    print("(1) Comprar cafes\n(2) Salir\n");
    try:
        op=int(input("Seleccione una opción:\t"));
        print();
        if op == 1:
            opcion1();
        elif op == 2:
            print("Cerrando aplicación\n");
            break
        else:
            print(f"El número ingresado:\t{op} no es valido en el sistema, eliga entre la opción 1 o 2\n");
    except ValueError:
        print("\nSolo digite numeros\n");