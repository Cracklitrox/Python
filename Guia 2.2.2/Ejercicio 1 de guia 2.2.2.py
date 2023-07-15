import os
from time import process_time
os.system('cls')

cont=0;
cont1=0;
cont2=0;
while True:
    print("------------------------------------")
    print("           Cine duocUC              ");
    print("------------------------------------")
    print("");
    usuario=input("Pertenece a Duoc (Si o No): ");
    print("");
    try: 
        if usuario == 'Si' or usuario == 'si':
            print("Tenemos a la venta las siguientes entradas");
            print("");
            print("(1) Estreno: $4.800\n(2) Normal: $2.900");
            estreno=1;
            normal=2;
            print("");
            opcion=int(input("Ingrese que tipo de entrada desea (1 o 2): "));
            print("");
            if opcion == 1:
                num=int(input("Cuanto boletos desea comprar: "));
                print("");
                cont=4800*num
                if num <= 0:
                    print(f"{num} no es un valor correcto, por favor digite correctamente.");
                else:
                    palomita=input("Desea comprar palomitas (Si o No): ");
                    print("");
                    if palomita == 'Si' or palomita == 'si':
                        print("Tenemos las siguientes opciones");
                        print("");
                        print("(1) Palomitas pequeñas: $2.500\n(2) Palomitas medianas: $4.500\n(3) Palomitas Grandes: $7.800");
                        palomita_pequeña=1;
                        palomita_mediana=2;
                        palomita_grande=3;
                        print("");
                        num1=int(input("Elija que opcion desea (1,2 o 3): "));
                        print("");
                        if num1 == 1:
                            num2=int(input("Cuantas palomitas pequeñas desea: "));
                            cont1=2500*num2
                            print("");
                            if num2 >= 1:
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    descuento=cont-(cont*0.3)
                                    result=descuento+cont1
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                            else:
                                print(f"{num2} no es un valor correcto, por favor elige correctamente.");
                        elif num1 == 2:
                            num2=int(input("Cuantas palomitas medianas desea: "));
                            cont1=4500*num2
                            print("");
                            if num2 >= 1:
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    descuento=cont-(cont*0.3)
                                    result=descuento+cont1
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                        elif num1 == 3:
                            num2=int(input("Cuantas palomitas grandes desea: "));
                            cont1=7800*num2
                            print("");
                            if num2 >= 1:
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    descuento=cont-(cont*0.3)
                                    result=descuento+cont1
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                            else:
                                print(f"{num2} no es un valor correcto, por favor elige correctamente.");
                        else:
                            print(f"{num1} no es un valor correcto, por favor elige correctamente.");
                    elif palomita == 'No' or palomita == 'no':
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    descuento=cont-(cont*0.3)
                                    result=descuento
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                    else:
                        print(f"{palomita} no es un caracter valido, por favor, digite correctamente.");
            elif opcion == 2:
                num=int(input("Cuanto boletos desea comprar: "));
                print("");
                cont=2900*num
                if num <= 0:
                    print(f"{num} no es un valor correcto, por favor digite correctamente.");
                else:
                    palomita=input("Desea comprar palomitas (Si o No): ");
                    print("");
                    if palomita == 'Si' or palomita == 'si':
                        print("Tenemos las siguientes opciones");
                        print("");
                        print("(1) Palomitas pequeñas: $2.500\n(2) Palomitas medianas: $4.500\n(3) Palomitas Grandes: $7.800");
                        palomita_pequeña=1;
                        palomita_mediana=2;
                        palomita_grande=3;
                        print("");
                        num1=int(input("Elija que opcion desea (1,2 o 3): "));
                        print("");
                        if num1 == 1:
                            num2=int(input("Cuantas palomitas pequeñas desea: "));
                            cont1=2500*num2
                            print("");
                            if num2 >= 1:
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    descuento=cont-(cont*0.3)
                                    result=descuento+cont1
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                            else:
                                print(f"{num2} no es un valor correcto, por favor elige correctamente.");
                        elif num1 == 2:
                            num2=int(input("Cuantas palomitas medianas desea: "));
                            cont1=4500*num2
                            print("");
                            if num2 >= 1:
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    descuento=cont-(cont*0.3)
                                    result=descuento+cont1
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                        elif num1 == 3:
                            num2=int(input("Cuantas palomitas grandes desea: "));
                            cont1=7800*num2
                            print("");
                            if num2 >= 1:
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    descuento=cont-(cont*0.3)
                                    result=descuento+cont1
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                            else:
                                print(f"{num2} no es un valor correcto, por favor elige correctamente.");
                        else:
                            print(f"{num1} no es un valor correcto, por favor elige correctamente.");
                    elif palomita == 'No' or palomita == 'no':
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            descuento=cont-(cont*0.3)
                                            result=descuento+cont+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    descuento=cont-(cont*0.3)
                                    result=descuento
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    print("Felicidades, por ser perteneciente a Duoc se le aplico un descuento del '30%' a sus entradas");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                    else:
                        print(f"{palomita} no es un caracter valido, por favor, digite correctamente.");
        elif usuario == 'No' or usuario == 'no':
            print("Tenemos a la venta las siguientes entradas");
            print("");
            print("(1) Estreno: $4.800\n(2) Normal: $2.900");
            estreno=1;
            normal=2;
            print("");
            opcion=int(input("Ingrese que tipo de entrada desea (1 o 2): "));
            print("");
            if opcion == 1:
                num=int(input("Cuanto boletos desea comprar: "));
                print("");
                cont=4800*num
                if num <= 0:
                    print(f"{num} no es un valor correcto, por favor digite correctamente.");
                else:
                    palomita=input("Desea comprar palomitas (Si o No): ");
                    print("");
                    if palomita == 'Si' or palomita == 'si':
                        print("Tenemos las siguientes opciones");
                        print("");
                        print("(1) Palomitas pequeñas: $2.500\n(2) Palomitas medianas: $4.500\n(3) Palomitas Grandes: $7.800");
                        palomita_pequeña=1;
                        palomita_mediana=2;
                        palomita_grande=3;
                        print("");
                        num1=int(input("Elija que opcion desea (1,2 o 3): "));
                        print("");
                        if num1 == 1:
                            num2=int(input("Cuantas palomitas pequeñas desea: "));
                            cont1=2500*num2
                            print("");
                            if num2 >= 1:
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    result=cont+cont1
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                            else:
                                print(f"{num2} no es un valor correcto, por favor elige correctamente.");
                        elif num1 == 2:
                            num2=int(input("Cuantas palomitas medianas desea: "));
                            cont1=4500*num2
                            print("");
                            if num2 >= 1:
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    result=cont+cont1
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                        elif num1 == 3:
                            num2=int(input("Cuantas palomitas grandes desea: "));
                            cont1=7800*num2
                            print("");
                            if num2 >= 1:
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    result=cont+cont1
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                            else:
                                print(f"{num2} no es un valor correcto, por favor elige correctamente.");
                        else:
                            print(f"{num1} no es un valor correcto, por favor elige correctamente.");
                    elif palomita == 'No' or palomita == 'no':
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    result=cont
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                    else:
                        print(f"{palomita} no es un caracter valido, por favor, digite correctamente.");
            elif opcion == 2:
                num=int(input("Cuanto boletos desea comprar: "));
                print("");
                cont=2900*num
                if num <= 0:
                    print(f"{num} no es un valor correcto, por favor digite correctamente.");
                else:
                    palomita=input("Desea comprar palomitas (Si o No): ");
                    print("");
                    if palomita == 'Si' or palomita == 'si':
                        print("Tenemos las siguientes opciones");
                        print("");
                        print("(1) Palomitas pequeñas: $2.500\n(2) Palomitas medianas: $4.500\n(3) Palomitas Grandes: $7.800");
                        palomita_pequeña=1;
                        palomita_mediana=2;
                        palomita_grande=3;
                        print("");
                        num1=int(input("Elija que opcion desea (1,2 o 3): "));
                        print("");
                        if num1 == 1:
                            num2=int(input("Cuantas palomitas pequeñas desea: "));
                            cont1=2500*num2
                            print("");
                            if num2 >= 1:
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    result=cont+cont1
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                            else:
                                print(f"{num2} no es un valor correcto, por favor elige correctamente.");
                        elif num1 == 2:
                            num2=int(input("Cuantas palomitas medianas desea: "));
                            cont1=4500*num2
                            print("");
                            if num2 >= 1:
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    result=cont+cont1
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                        elif num1 == 3:
                            num2=int(input("Cuantas palomitas grandes desea: "));
                            cont1=7800*num2
                            print("");
                            if num2 >= 1:
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont1+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    result=cont+cont1
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                            else:
                                print(f"{num2} no es un valor correcto, por favor elige correctamente.");
                        else:
                            print(f"{num1} no es un valor correcto, por favor elige correctamente.");
                    elif palomita == 'No' or palomita == 'no':
                                bebida=input("Desea agregar bebida a su pedido (Si o No): ");
                                print("");
                                if bebida == 'Si' or bebida == 'si':
                                    print("Tenemos las siguientes opciones");
                                    print("");
                                    print("(1) Bebidas pequeñas: $1.000\n(2) Bebidas medianas: $1.250\n(3) Bebidas grandes: $2.000");
                                    bebida_pequeña=1;
                                    bebida_mediana=2;
                                    bebida_grande=3;
                                    print("");
                                    num3=int(input("Elija que opcion desea (1,2 o 3): "));
                                    print("");
                                    if num3 == 1:
                                        num4=int(input("Cuantas bebidas pequeñas desea: "));
                                        cont2=1000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 2:
                                        num4=int(input("Cuantas bebidas medianas desea: "));
                                        cont2=1250*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    elif num3 == 3:
                                        num4=int(input("Cuantas bebidas grandes desea: "));
                                        cont2=2000*num4
                                        print("");
                                        if num4 >=1:
                                            result=cont+cont2
                                            print(f"El total a pagar es de: ${result}");
                                            print("");
                                            num5=int(input("Ingrese valor a pagar: "));
                                            print("");
                                            if num5 == result:
                                                print("Gracias por su compra, su vuelto es: $0");
                                            elif num5 > result:
                                                vuelto=num5-result
                                                print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                            else:
                                                print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                        else:
                                            print(f"{num4} no es un valor correcto, por favor elije correctamente.");
                                    else:
                                        print(f"{num3} no es un valor correcto, por favor elije correctamente.");
                                elif bebida == 'No' or bebida == 'no':
                                    result=cont
                                    print(f"El total a pagar es de: ${result}");
                                    print("");
                                    num5=int(input("Ingrese valor a pagar: "));
                                    print("");
                                    if num5 == result:
                                        print("Gracias por su compra, su vuelto es: $0");
                                    elif num5 > result:
                                        vuelto=num5-result
                                        print(f"Gracias por su compra, su vuelto es: ${vuelto}");
                                    else:
                                        print(f"Su dinero ${num5} es insuficiente para el valor total ${result}\nSi no puede pagar, por favor, retirese.");
                                else:
                                    print(f"{bebida} no es un caracter valido, por favor, digite correctamente.");
                    else:
                        print(f"{palomita} no es un caracter valido, por favor, digite correctamente.");
        else:
            print(f"{usuario} es un caracter incorrecto, por favor escriba correctamente.");
    except ValueError:
        print("\nSolo digite numeros o caracteres\n");