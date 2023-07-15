import os
from time import process_time
os.system('cls')

suma=0;
print("-------------------------------");
print("        Supermercado Duoc      ");
print("-------------------------------");
print("");
print("---------------------------------------");
cliente=input("Usted es cliente preferencial (V o F): ");
if cliente == 'F' or cliente == 'f':
    print("");
    print("---------------------------------------------------------");
    print("La lista de productos son los siguientes: ");
    print("");
    print("(1) Agua: $600\n(2) Azúcar: $1200\n(3) Aceite: $1500\n(4) Arroz: $1250\n(5) Fideos: $790\n(6) Bebida: $1780\n(7) Chocolate: $2500\n(8) Pan molde: $1340");
    print("---------------------------------------------------------");
    agua=600;
    azucar=1200;
    aceite=1500;
    arroz=1250;
    fideos=790;
    bebida=1780;
    chocolate=2500;
    pan_molde=1340;
    print("");
    decision=input("¿Desea comprar algun producto?\t(Si o No): ");
    print("");
    if decision == 'Si' or decision == 'si':
        decision1=input("¿Desea comprar agua?\n(Si o No): ");
        print("");
        if decision1 == 'Si' or decision1 == 'si':
            num=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num == 1:
                cont=0+num
                suma= suma+(num*agua)
                print(f"Usted lleva {cont} producto de agua, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num > 1:
                cont=0+num
                suma= suma+(num*agua)
                print(f"Usted lleva {cont} productos de agua, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar azúcar? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num1=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num1 == 1:
                cont1=0+num1
                suma= suma+(num1*azucar)
                print(f"Usted lleva {cont1} producto de azúcar, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num1 > 1:
                cont1=0+num1
                suma= suma+(num1*azucar)
                print(f"Usted lleva {cont1} productos de azúcar, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num1} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar aceite? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num2=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num2 == 1:
                cont2=0+num2
                suma= suma+(num2*aceite)
                print(f"Usted lleva {cont2} producto de aceite, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num2 > 1:
                cont2=0+num2
                suma= suma+(num2*aceite)
                print(f"Usted lleva {cont2} productos de aceite, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num2} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar arroz? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num3=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num3 == 1:
                cont3=0+num3
                suma= suma+(num3*arroz)
                print(f"Usted lleva {cont3} producto de arroz, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num3 > 1:
                cont3=0+num3
                suma* suma+(num3*arroz)
                print(f"Usted lleva {cont3} productos de arroz, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num3} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar fideos? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num4=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num4 == 1:
                cont4=0+num4
                suma= suma+(num4*fideos)
                print(f"Usted lleva {cont4} producto de fideo, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num4 > 1:
                cont4=0+num4
                suma= suma+(num4*fideos)
                print(f"Usted lleva {cont4} productos de fidelos, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num4} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar bebida? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num5=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num5 == 1:
                cont5=0+num5
                suma= suma+(num5*bebida)
                print(f"Usted lleva {cont5} producto de bebida, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num5 > 1:
                cont5=0+num5
                suma= suma+(num5*bebida)
                print(f"Usted lleva {cont5} productos de bebida, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num5} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar chocolate? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num6=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num6 == 1:
                cont6=0+num6
                suma= suma+(num6*chocolate)
                print(f"Usted lleva {cont6} producto de chocolate, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num6 > 1:
                cont6=0+num6
                suma= suma+(num6*chocolate)
                print(f"Usted lleva {cont6} productos de chocolates, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num6} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar pan molde? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num7=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num7 == 1:
                cont7=0+num7
                suma= suma+(num7*pan_molde)
                print(f"Usted lleva {cont7} producto de pan de molde, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num7 > 1:
                cont7=0+num7
                suma= suma+(num7*pan_molde)
                print(f"Usted lleva {cont7} productos de pan de molde, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num7} no es un caracter valido, por favor digite bien los valores a elegir.");
        print(f"En total, usted debera pagar: ${suma}");
        print("");
        paga=int(input("Ingrese valor a pagar: "));
        print("");
        if paga == suma:
            print("Gracias por comprar con nosotros");
            print("");
            print("Su vuelto es: $0");
        elif paga > suma:
            result=paga-suma
            print(f"Gracias por comprar con nosotros");
            print("");
            print(f"Su vuelto es de: ${result}");
        else:
            print(f"Su monto ${paga} no alcanza a pagar todos los productos\nPor lo tanto, dinero insuficiente, Guardias!");
    elif decision == 'No' or decision == 'no':
        print("")
        print("Entonces vayase, no moleste (-.-)");
    else:
        print(f"{decision} no es un caracter valido, por favor digite bien.");
elif cliente == 'V' or cliente == 'v':
    print("");
    print("---------------------------------------------------------");
    print("La lista de productos son los siguientes: ");
    print("");
    print("(1) Agua: $600\n(2) Azúcar: $1200\n(3) Aceite: $1500\n(4) Arroz: $1250\n(5) Fideos: $790\n(6) Bebida: $1780\n(7) Chocolate: $2500\n(8) Pan molde: $1340");
    print("---------------------------------------------------------");
    agua=600;
    azucar=1200;
    aceite=1500;
    arroz=1250;
    fideos=790;
    bebida=1780;
    chocolate=2500;
    pan_molde=1340;
    print("");
    decision=input("¿Desea comprar algun producto?\t(Si o No): ");
    print("");
    if decision == 'Si' or decision == 'si':
        decision1=input("¿Desea comprar agua?\n(Si o No): ");
        print("");
        if decision1 == 'Si' or decision1 == 'si':
            num=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num == 1:
                cont=0+num
                suma= suma+(num*agua)
                print(f"Usted lleva {cont} producto de agua, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num > 1:
                cont=0+num
                suma= suma+(num*agua)
                print(f"Usted lleva {cont} productos de agua, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar azúcar? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num1=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num1 == 1:
                cont1=0+num1
                suma= suma+(num1*azucar)
                print(f"Usted lleva {cont1} producto de azúcar, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num1 > 1:
                cont1=0+num1
                suma= suma+(num1*azucar)
                print(f"Usted lleva {cont1} productos de azúcar, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num1} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar aceite? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num2=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num2 == 1:
                cont2=0+num2
                suma= suma+(num2*aceite)
                print(f"Usted lleva {cont2} producto de aceite, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num2 > 1:
                cont2=0+num2
                suma= suma+(num2*aceite)
                print(f"Usted lleva {cont2} productos de aceite, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num2} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar arroz? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num3=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num3 == 1:
                cont3=0+num3
                suma= suma+(num3*arroz)
                print(f"Usted lleva {cont3} producto de arroz, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num3 > 1:
                cont3=0+num3
                suma* suma+(num3*arroz)
                print(f"Usted lleva {cont3} productos de arroz, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num3} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar fideos? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num4=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num4 == 1:
                cont4=0+num4
                suma= suma+(num4*fideos)
                print(f"Usted lleva {cont4} producto de fideo, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num4 > 1:
                cont4=0+num4
                suma= suma+(num4*fideos)
                print(f"Usted lleva {cont4} productos de fidelos, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num4} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar bebida? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num5=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num5 == 1:
                cont5=0+num5
                suma= suma+(num5*bebida)
                print(f"Usted lleva {cont5} producto de bebida, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num5 > 1:
                cont5=0+num5
                suma= suma+(num5*bebida)
                print(f"Usted lleva {cont5} productos de bebida, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num5} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar chocolate? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num6=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num6 == 1:
                cont6=0+num6
                suma= suma+(num6*chocolate)
                print(f"Usted lleva {cont6} producto de chocolate, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num6 > 1:
                cont6=0+num6
                suma= suma+(num6*chocolate)
                print(f"Usted lleva {cont6} productos de chocolates, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num6} no es un caracter valido, por favor digite bien los valores a elegir.");
        a=input("¿Desea comprar pan molde? (Si o No): ");
        print("");
        if a == 'Si' or a == 'si':
            num7=int(input("¿Cuantos productos desea comprar?: "));
            print("");
            if num7 == 1:
                cont7=0+num7
                suma= suma+(num7*pan_molde)
                print(f"Usted lleva {cont7} producto de pan de molde, con un valor total hasta ahora de: ${suma}");
                print("");
            elif num7 > 1:
                cont7=0+num7
                suma= suma+(num7*pan_molde)
                print(f"Usted lleva {cont7} productos de pan de molde, con un valor total hasta ahora de: ${suma}");
                print("");
            else:
                print(f"{num7} no es un caracter valido, por favor digite bien los valores a elegir.");
        print("---------------------------------------------------------");
        print(f"En total, usted debera pagar: ${suma}");
        print("");
        print("Felicidades, por ser cliente preferencial obtienes 25%");
        print("");
        descuento=int;
        descuento=suma-(suma*0.25)
        print(f"El monto total a pagar ahora es de: {descuento}");
        print("");
        print("---------------------------------------------------------");
        paga=int(input("Ingrese valor a pagar: "));
        print("");
        if paga == descuento:
            print("Gracias por comprar con nosotros");
            print("---------------------------------------------------------");
        elif paga > descuento:
            result=paga-descuento
            print(f"Gracias por comprar con nosotros\nSu vuelto es de: ${result}");
            print("---------------------------------------------------------");
        else:
            print(f"Su monto ${paga} no alcanza a pagar todos los productos\nPor lo tanto, dinero insuficiente, Guardias!");
            print("---------------------------------------------------------");
    elif decision == 'No' or decision == 'no':
        print("")
        print("Entonces vayase, no moleste (-.-)");
        print("---------------------------------------------------------");
    else:
        print(f"{decision} no es un caracter valido, por favor digite bien.");
        print("---------------------------------------------------------");
else:
    print(f"{cliente} no es un caracter valido, por favor digite bien.");
    print("---------------------------------------------------------");