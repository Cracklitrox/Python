print("----------------------------");
print("        Delivery Duoc       ");
print("----------------------------");
print("");
print("(1) Pan Amasado: $1.500\n(2) Pan Molde: $1.000\n(3) Pan Baguette: $2.000\n(4) Pan Integral: $3.000");
print("");
i=0;
cont=0;
cont1=0;
cont2=0;
cont3=0;
result=0;
result1=0;
while i < 1:
    i=i+1
    num=int(input("¿Cuantos panes amasados desea llevar?: "));
    print("");
    cont=(num+1500)-num
    num1=int(input("¿Cuantos panes de molde desea llevar?: "));
    print("");
    cont1=(num1+1000)-num1
    num2=int(input("¿Cuantos panes baguette desea llevar?: "));
    print("");
    cont2=(num2+2000)-num2
    num3=int(input("¿Cuantos panes integrales desea llevar: "));
    print("");
    cont3=(num3+3000)-num3
result=cont+cont1+cont2+cont3
if result >= 5000:
    print(f"Felicidades, por compras mayores a $5.000 obtiene envio gratuito\nGracias por comprar con nosotros.\nSu volar total a pagar es de: {result}")
else:
    result1=(result*0.1)+result
    print(f"Gracias por comprar con nosotros, por comprar menores a $5.000 se le aplicara un '10%' adicional a su boleta\nSu valor total es: {result1}");