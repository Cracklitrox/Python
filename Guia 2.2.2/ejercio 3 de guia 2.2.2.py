cont=0;
sum=0;
print("---------------------------------------------------------");
print("     Convertidor de dinero de DuocUC a peso chileno      ");
print("---------------------------------------------------------");
print("");
print("Bienvenido usuario");
print("");
print("(1) Dólar australiano esta a: $603.05 pesos chilenos\n(2) Peso Argentino esta a: $7.36 pesos chilenos\n(3) Yen esta a: $6.58 pesos chilenos");
print("");
dolar_australiano=1;
peso_argentino=2;
yen=3;
usuario=int(input("Por favor, eliga su tipo de moneda: "));
print("");
if usuario <= 0 or usuario >= 4:
    print(f"{usuario} no es un numero valido, por favor correctamente entre las opciones dentro del sistema.");
if usuario == 1:
    num=int(input("Elija la cantidad de dolares australianos desea convertir a peso chileno: "));
    print("");
    if num >= 1:
        cont=cont+num
        result=num*603.05
        print(f"La cantidad de ${num} dolares australianos a sido convertido\nUsted tiene ${result} pesos chilenos.");
        print("");
        print("Gracias por cambiar su moneda con nosotros.");
    else:
        print(f"{num} no es un valor correcto, por favor ingrese un numero mayor a 1.");
elif usuario == 2:
    num=int(input("Elija la cantidad de pesos argentinos desea convertir a pesos chilenos: "));
    print("");
    if num >= 1:
        cont=cont+num
        result=num*7.36
        print(f"La cantidad de ${num} pesos argentinos a sido convertido\nUsted tiene ${result} pesos chilenos.");
        print("");
        print("Gracias por cambiar su moneda con nosotros.");
    else:
        print(f"{num} no es un valor correcto, por favor ingrese un numero mayor a 1.");
elif usuario == 3:
    num=int(input("Elija la cantidad de pesos argentinos desea convertir a pesos chilenos: "));
    print("");
    if num >= 1:
        cont=cont+num
        result=num*6.58
        print(f"La cantidad de ${num} yen a sido convertido\nUsted tiene ${result} pesos chilenos.");
        print("");
        print("Gracias por cambiar su moneda con nosotros.");
    else:
        print(f"{num} no es un valor correcto, por favor ingrese un numero mayor a 1.");