num_list=[]
result=0;
x=range(10);
for n in x:
    num=int(input("Ingrese un numero entero: "));
    print("");
    num_list.append(num);
    result=result+num;
result1=result/10;
print(f"La suma de los numeros ingresados es: {result}");
print("");
print(f"El promedio de {result} es: {result1}");