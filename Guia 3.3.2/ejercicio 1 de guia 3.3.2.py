num=int(input("Ingrese un numero entero: "));
print("");
num_list=[num];
num_list.extend([num*2,num*3,num*4,num*5,num*6,num*7,num*8,num*9,num*10]);
print(f"Su numero multiplicado en orden de menor a mayor es: {num_list}");