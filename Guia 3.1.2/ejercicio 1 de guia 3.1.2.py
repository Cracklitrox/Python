cont=0;
cont1=0;
cont2=0;
sum=0;
sum1=0;
sum2=0

print("-----------------------------");
print("        Transporte Duoc      ");
print("-----------------------------");
print("");
print("-------------------------------");
print("|  Kilos  | |Categoria| | Valor |");
print("| 0 - 5   | | Liviano | |$1.000 |");
print("| 6 - 10  | | Normal  | |$4.500 |");
print("| 11 - 20 | | Pesado  | |$8.000 |");
print("-------------------------------");
print("");
num=int(input("¿Cuantos paquetes desea enviar: "));
print("");
if num <= 0:
    print(f"{num} no es un numero valido, por favor intente nuevamente.");
else:
    x=range(num)
    for n in x:
        num1=int(input("¿Cuanto pesa su producto?: "));
        print("");
        if num1 >= 0 and num1 <= 5:
            cont=cont+1
            sum=sum+1000
        elif num1 >= 6 and num1 <= 10:
            cont1=cont1+1
            sum1=sum1+4500
        elif num1 >= 11 and num1 <= 20:
            cont2=cont2+1
            sum2=sum2+8000
        else:
            print(f"{num1} no es un valor valido dentro del sistema.");
result=sum+sum1+sum2
print("               Encomiendas             ");
print("---------------------------------------");
print(f"{cont} bulto LIVIANO: ${sum}");
print(f"{cont1} bulto NORMAL: ${sum1}");
print(f"{cont2} bulto PESADO: ${sum2}");
print("---------------------------------------");
print("");
print(f"El total a pagar es de: {result}");