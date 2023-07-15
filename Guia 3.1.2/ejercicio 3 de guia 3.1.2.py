num=int(input("Ingrese desde que numero desea imprimir: "));
print("");
num1=int(input("Ingrese hasta que numero desea imprimir: "));
print("");
x=range(num,num1+1,1)
for n in x:
    if num < num1:
        print(f"{n}");
if num < num1:
    print("Gracias por usar el programa.")
else:
    print("Usted coloco mal los numeros.");