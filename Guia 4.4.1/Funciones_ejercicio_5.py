numeros_parte=[];
nombre_parte=[];
precio_producto=[];
descripcion_producto=[];
def opcion1():
    while True:
        try:
            num_parte=int(input("Ingrese el número de parte (minimo 10 números):\t"));
            print();
            if num_parte >= 10:
                numeros_parte.append(num_parte);
                break
            else:
                print(f"El número de parte ingresado:\t'{num_parte}' es incorrecto, intentelo nuevamente\n");
        except ValueError:
            print(f"\nSolo digite números\n")
    while True:
        try:
            nom_producto=input("Ingrese el nombre del producto (minimo 6 caracteres):\t");
            print();
            if nom_producto.isalpha() == True:
                if len(nom_producto) >= 6:
                    nombre_parte.append(nom_producto);
                    break
                else:
                    print(f"El nombre del producto ingresado:\t'{nom_producto}' debe tener minimo 6 caracteres, intentelo nuevamente\n");
            else:
                print(f"El nombre del producto ingresado:\t'{nom_producto}' no es valido, solo digite caracteres\n");
        except ValueError:
            print(f"\nSolo digite caracteres\n");
    while True:
        try:
            descripccion=input("Ingrese una breve descripccion del producto:\t");
            print();
            if descripccion.isalpha() == True:
                descripcion_producto.append(descripccion);
                break
            else:
                print(f"La descripcion ingresada:\t'{descripccion}' no es valida, solo digite caracteres\n");
        except ValueError:
            print(f"\nSolo digite caracteres\n");
    while True:
        try:
            precio=int(input("Ingrese el precio del producto:\t"));
            print();
            if precio >= 1:
                precio_producto.append(precio);
                break
            else:
                print(f"El precio del producto ingresado:\t'{precio}' debe ser mayor a 0, intentelo nuevamente\n");
        except ValueError:
            print(f"\nSolo digite números\n");
def opcion2():
    while True:
        try:
            buscar=int(input(f"Ingrese el número de la parte del producto (minimo 10 números):\t"));
            print();
            if buscar >= 10:
                if buscar in numeros_parte:
                    a=numeros_parte.index(buscar);
                    if precio_producto[a] >= 500:
                        print(f"El producto es:\t{numeros_parte[a]}-{nombre_parte[a]} con un precio de $ {precio_producto[a]} y su descripción es:\t{descripcion_producto[a]}\n");
                        break
                    else:
                        print(f"Producto sin stock\n");
                        break
                else:
                    print(f"El número de parte del producto ingresado:\t'{buscar}' no se encuentra registrado en el sistema, intentelo nuevamente\n");
            else:
                print(f"El número de parte del producto ingresado:\t'{buscar}' es incorrecto, intentelo nuevamente\n");
        except ValueError:
            print(f"\nSolo digite números\n");
def opcion3():
    i=1;
    print(f"A continuación se mostraran los productos registrados dentro del sistema\n");
    for x in range(len(descripcion_producto)):
        print(f"({i}) El producto es:\t{numeros_parte[x]}-{nombre_parte[x]} con un precio de $ {precio_producto[x]} y su descripción es:\t{descripcion_producto[x]}\n");
        i+=1;
def opcion4():
    print(f"Cerrando aplicación\tCreada por Carlos Gacitúa\tVersion 1.0\n");