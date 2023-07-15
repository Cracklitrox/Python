from multiprocessing.sharedctypes import Value


Flag=True
while Flag == True:
    try:
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
        print(f"El primer nombre del usuario es: {nom_list[0]} y el segundo apellido es: {ape_list[0]}\n");
        print(f"El primer nombre del usuario es: {nom_list[1]} y el segundo apellido es: {ape_list[1]}\n");
        print(f"El primer nombre del usuario es: {nom_list[2]} y el segundo apellido es: {ape_list[2]}\n");
        Flag=False
    except ValueError:
        print(f"Intento nuevamente.\n\n")