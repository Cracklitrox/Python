Flag=True
list_num=[];
while Flag == True:
    num=int(input("Ingrese un numero: "));
    if num == 0:
        Flag=False;
        print(list_num);
    else:
        list_num.append(num);