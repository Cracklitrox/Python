user_list=[];
contra_list=[];
cont=0
while True:
    print("\n-------------Sistema Duoc UC-------------\n\n(1) Iniciar Sesión\n(2) Registrar Usuario\n(3) Salir\n\n");
    try:
        op=int(input("Seleccione una opción: "));
        print();
        if op == 1:
            if cont == 0:
                print("No existe ningun usuario registrado, por favor, seleccione la opcion 2.\n\n");
            else:
                while True:
                    try:
                        decision=input("Desea ingresar usuario o desea volver al menu del inicio (Ingresar o Volver): ");
                        print();
                        if decision == 'Ingresar' or decision == 'INGRESAR' or decision == 'ingresar':
                            user_comprobacion=input("Ingrese su usuario: ");
                            print();
                            contra_comprobacion=input("Ingrese su contraseña: ");
                            print();
                            if len(user_list) == 1 and len(contra_list) == 1:
                                if user_comprobacion == user_list[0] and contra_comprobacion == contra_list[0]:
                                    print(f"Bienvenido {user_comprobacion}\n\n");
                                    print("------------Opciones usuario------------\n");
                                    while True:
                                        print("\n\n(1) Realizar llamada\n(2) Enviar correo electronico\n(3) Cerrar sesión.\n\n");
                                        try:
                                            op1=int(input("Seleccion una opción: "));
                                            print();
                                            if op1 == 1:
                                                while True:
                                                    celular=int(input("Ingrese el numero: 9"));
                                                    print();
                                                    if celular >= 10000000 and celular <= 99999999:
                                                        print("Numero registrado correctamente.\n\n");
                                                        break
                                                    else:
                                                        print("Ingrese correctamente el numero, intentelo nuevamente.\n\n");
                                            elif op1 == 2:
                                                while True:
                                                    cont_correo=0;
                                                    cont_mal=0;
                                                    try:
                                                        correo=input("Ingrese el correo: ");
                                                        print();
                                                        for x in correo:
                                                            if x == '@':
                                                                cont_correo+=1
                                                            else:
                                                                cont_mal+=1
                                                        if cont_correo == 1:
                                                            print("Correo registrado exitosamente.\n");
                                                            mensaje=input("Redacte el mensaje que tendra el correo: ");
                                                            print();
                                                            print("Mensaje enviado exitosamente.\n\n");
                                                            break
                                                        else:
                                                            print(f"El correo ingresado: '{correo}' necesita tan solo un @, vuelva a intentarlo.\n\n");
                                                    except ValueError:
                                                        print("Digite correctamente, vuelva a intentarlo.\n\n");
                                            elif op1 == 3:
                                                print("Ok, sera devuelto al menu de inicio.\n\n");
                                                break                                    
                                            else:
                                                print(f"La opcion ingresada: '{op1}' no se encuentra entre las opciones del sistema, por favor, intentelo nuevamente.\n\n");
                                        except ValueError:
                                            print("Digite correctamente, vuelva a intentarlo\n\n");
                                else:
                                    print("El usuario o contraseña ingresada no coincide con los registrados dentro del sistema, por favor, intentelo nuevamente.\n\n");
                            elif len(user_list) == 2 and len(contra_list) == 2:
                                if (user_comprobacion == user_list[0] and contra_comprobacion == contra_list[0]) or (user_comprobacion == user_list[1] and contra_comprobacion == contra_list[1]):
                                    print(f"Bienvenido {user_comprobacion}\n\n");
                                    print("------------Opciones usuario------------\n");
                                    while True:
                                        print("\n\n(1) Realizar llamada\n(2) Enviar correo electronico\n(3) Cerrar sesión.\n\n");
                                        try:
                                            op1=int(input("Seleccion una opción: "));
                                            print();
                                            if op1 == 1:
                                                while True:
                                                    celular=int(input("Ingrese el numero: 9"));
                                                    print();
                                                    if celular >= 10000000 and celular <= 99999999:
                                                        print("Numero registrado correctamente.\n\n");
                                                        break
                                                    else:
                                                        print("Ingrese correctamente el numero, intentelo nuevamente.\n\n");
                                            elif op1 == 2:
                                                while True:
                                                    cont_correo=0;
                                                    cont_mal=0;
                                                    try:
                                                        correo=input("Ingrese el correo: ");
                                                        print();
                                                        for x in correo:
                                                            if x == '@':
                                                                cont_correo+=1
                                                            else:
                                                                cont_mal+=1
                                                        if cont_correo == 1:
                                                            print("Correo registrado exitosamente.\n");
                                                            mensaje=input("Redacte el mensaje que tendra el correo: ");
                                                            print();
                                                            print("Mensaje enviado exitosamente.\n\n");
                                                            break
                                                        else:
                                                            print(f"El correo ingresado: '{correo}' necesita tan solo un @, vuelva a intentarlo.\n\n");
                                                    except ValueError:
                                                        print("Digite correctamente, vuelva a intentarlo.\n\n");
                                            elif op1 == 3:
                                                print("Ok, sera devuelto al menu de inicio.\n\n");
                                                break                                    
                                            else:
                                                print(f"La opcion ingresada: '{op1}' no se encuentra entre las opciones del sistema, por favor, intentelo nuevamente.\n\n");
                                        except ValueError:
                                            print("Digite correctamente, vuelva a intentarlo\n\n");
                                else:
                                    print("El usuario o contraseña ingresada no coincide con los registrados dentro del sistema, por favor, intentelo nuevamente.\n\n");
                            elif len(user_list) == 3 and len(contra_list) == 3:
                                if (user_comprobacion == user_list[0] and contra_comprobacion == contra_list[0]) or (user_comprobacion == user_list[1] and contra_comprobacion == contra_list[1]) or (user_comprobacion == user_list[2] and contra_comprobacion == contra_list[2]):
                                    print(f"Bienvenido {user_comprobacion}\n\n");
                                    print("------------Opciones usuario------------\n");
                                    while True:
                                        print("\n\n(1) Realizar llamada\n(2) Enviar correo electronico\n(3) Cerrar sesión.\n\n");
                                        try:
                                            op1=int(input("Seleccion una opción: "));
                                            print();
                                            if op1 == 1:
                                                while True:
                                                    celular=int(input("Ingrese el numero: 9"));
                                                    print();
                                                    if celular >= 10000000 and celular <= 99999999:
                                                        print("Numero registrado correctamente.\n\n");
                                                        break
                                                    else:
                                                        print("Ingrese correctamente el numero, intentelo nuevamente.\n\n");
                                            elif op1 == 2:
                                                while True:
                                                    cont_correo=0;
                                                    cont_mal=0;
                                                    try:
                                                        correo=input("Ingrese el correo: ");
                                                        print();
                                                        for x in correo:
                                                            if x == '@':
                                                                cont_correo+=1
                                                            else:
                                                                cont_mal+=1
                                                        if cont_correo == 1:
                                                            print("Correo registrado exitosamente.\n");
                                                            mensaje=input("Redacte el mensaje que tendra el correo: ");
                                                            print();
                                                            print("Mensaje enviado exitosamente.\n\n");
                                                            break
                                                        else:
                                                            print(f"El correo ingresado: '{correo}' necesita tan solo un @, vuelva a intentarlo.\n\n");
                                                    except ValueError:
                                                        print("Digite correctamente, vuelva a intentarlo.\n\n");
                                            elif op1 == 3:
                                                print("Ok, sera devuelto al menu de inicio.\n\n");
                                                break                                    
                                            else:
                                                print(f"La opcion ingresada: '{op1}' no se encuentra entre las opciones del sistema, por favor, intentelo nuevamente.\n\n");
                                        except ValueError:
                                            print("Digite correctamente, vuelva a intentarlo\n\n");
                                else:
                                    print("El usuario o contraseña ingresada no coincide con los registrados dentro del sistema, por favor, intentelo nuevamente.\n\n");
                        elif decision == 'Volver' or decision == 'VOLVER' or decision == 'volver':
                            print("Ok, sera devuelto al menu de inicio.\n\n");
                            break
                        else:
                            print(f"Lo digitado: '{decision}' no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                    except ValueError:
                        print("Digite correctamente lo que se le pide.\n\n");
        elif op == 2:
            if cont >= 0 and cont <= 2:
                while True:
                    try:
                        user=input("Ingrese su nombre de usuario: ");
                        print();
                        contraseña=input("Ingrese su contraseña: ");
                        print();
                        user_list.append(user);
                        contra_list.append(contraseña);
                        cont+=1;
                        break;
                    except ValueError:
                        print("Ingrese correctamente los datos que se le piden.\n\n");
            else:
                print("Ya existen 3 usuario registrados dentro del sistema, por favor, seleccione otras opciones.\n\n");
        elif op == 3:
            print("Cerrando sesión.\n");
            break
        else:
            print(f"La opcion ingresada: '{op}' no es valido dentro del sistema.");
    except ValueError:
        print(f"La que usted digito no es valida dentro del sistema, por favor, intentelo nuevamente.\n\n");