nom=input("Ingrese su nombre: ");
print("");
nom_list=[nom];
nom2=input("Ingrese su apellido: ");
print("");
ape_list=[nom2];
x=range(2);
for n in x:
    nom1=input("Ingrese su nombre: ");
    print("");
    nom4=input("Ingrese su apellido: ");
    print("");
    nom_list.append(nom1);
    ape_list.append(nom4);
print(nom_list);
print(ape_list);
a=nom_list.pop(0);
a2=ape_list.pop(0);
c=nom_list.pop(1);
c2=ape_list.pop(1);
b=nom_list.pop(-1);
b2=ape_list.pop(-1);
print(f"El primer nombre ingresado es: {a} y el apellido es: {a2}\n");
print(f"El segundo nombre ingresado es: {b} y el apellido es: {b2}\n");
print(f"El ultimo nombre ingresado es: {c} y el apellido es: {c2}\n");