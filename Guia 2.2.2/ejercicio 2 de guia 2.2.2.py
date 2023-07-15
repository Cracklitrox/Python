cont=0;
sum=0;
print("--------------------------");
print("     Zapateria DuocUc     ");
print("--------------------------");
print("");
print("Bienvenido usuario");
print("Tenemos a la venta zapatos para hombres con un valor de $20.000");
print("");
usuario=input("¿Desea comprar zapatos para hombres? (Si o No): ");
print("");
if usuario == 'Si' or usuario == 'si':
    num=int(input("¿Cuantos zapatos desea comprar?: "));
    print("");
    if num == 1:
        result=20000+3000
        print(f"El valor total a pagar es: ${result} más el envio");
        print("");
        print("Gracias por comprar con nosotros.");
    elif num >1:
        result=20000*num
        print(f"El valor total a pagar es: ${result}");
        print("");
        print("Su compra es mayor a $40.000, por lo tanto tiene envío gratis");
        print("");
        print("Gracias por comprar con nosotros.");
elif usuario == 'No' or usuario == 'no':
    print("Esta bien, vuelva proximamente.");
else:
    print(f"{usuario} no es un caracter correcto, por favor digite correctamente.")