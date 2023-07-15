Flag=True;
cont=0;
cont1=0;
cont2=0;
while Flag == True:
    print("-------------------------");
    print("   App ServiExpress  ");
    print("-------------------------\n");
    print("(1). Registrar  automóvil\n(2). Registro Mantenimiento\n(3). Consultar Automóvil\n(4). Salir\n");
    print("-------------------------\n");
    sw=1;
    try:
        op=int(input("Seleccione una opción: "));
        print("");
        if op == 1:
            if cont == 0:
                while sw == 1:
                    cont_vocal=0;
                    cont_consonante=0;
                    try:
                        patente=input("Ingrese su patente (Sin numeros y al menos 3 caracteres): ");
                        print("");
                        numero_patente=int(input("Ingrese los numeros de su patente (Al menos 3 numeros): "));
                        print("");
                        marca=input("Ingrese la marca de su automovil: ");
                        print("");
                        modelo=input("Ingrese el modelo de su vehiculo: ");
                        print("");
                        año_fabricacion=int(input("Ingrese el año de fabricación de su automovil (A partir del año 1900 hasta 2021): "));
                        print("");
                        tipo_vehiculo=input("Ingrese el tipo de vehiculo al cual pertenece (b,d,e,h): ");
                        print("");
                        if patente.isalpha() == True:
                            for caracter in patente:
                                if caracter == 'a' or caracter == 'A' or caracter == 'e' or caracter == 'E' or caracter == 'i' or caracter == 'I' or caracter == 'O' or caracter == 'o' or caracter == 'U' or caracter == 'u':
                                    cont_vocal+=1
                                else:
                                    cont_consonante+=1
                            cont_palabras=cont_vocal+cont_consonante;
                            if cont_palabras >= 3:
                                if numero_patente >= 100 and numero_patente <= 999:
                                    if all(x.isspace() or x.isalpha() for x in marca):
                                        if all(x.isspace() or x.isalpha() for x in modelo):
                                            if año_fabricacion >= 1900 and año_fabricacion <= 2021:
                                                if tipo_vehiculo.isalpha() == True:
                                                    if tipo_vehiculo == 'b' or tipo_vehiculo == 'B' or tipo_vehiculo == 'd' or tipo_vehiculo == 'D' or tipo_vehiculo == 'e' or tipo_vehiculo == 'E' or tipo_vehiculo == 'h' or tipo_vehiculo == 'H':
                                                        print(f"Gracias usuario, su vehiculo fue registrado exitosamente.\n\n");
                                                        sw=0;
                                                        cont+=1
                                                    else:
                                                        print(f"El caracter ingresado: {tipo_vehiculo} no es valido dentro del sistenma, por favor, intentelo nuevamente.\n\n");
                                                else:
                                                    print(f"El caracter ingresado: {tipo_vehiculo} contiene numeros o no digito nada, por favor, intentelo nuevamente.\n\n");
                                            else:
                                                print(f"El año ingresado: {año_fabricacion} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                        else:
                                            print(f"El modelo ingresado: {modelo} contiene numeros o no digito nada, por favor, intentelo nuevamente.\n\n");
                                    else:
                                        print(f"La marca ingresada: {marca} contiene numeros o no digito nada, por favor, intentelo nuevamente.\n\n");
                                else:
                                    print(f"Los numeros ingresados de su patente: {numero_patente} no son validos dentro del sistema, por favor, intentelo nuevamente.\n\n");
                            else:
                                print(f"La patente ingresada: {patente} no contiene las suficientes letras que se requiere, por favor intentelo nuevamente.\n\n");
                        else:
                            print(f"El patente ingresado: {patente} contiene numeros o no digito nada, por favor, digite correctamente.\n\n");
                    except ValueError:
                        print("\n\nEl caracter digitado no es valido, por favor, intentelo nuevamente.\n\n");
            else:
                print("Ya se encuentra registrado los datos de un vehiculo en el sistema\nPor favor seleccione las demas opciones.\n\n");
        elif op == 2:
            if cont == 0:
                print("No se ha registrada ningun vehiculo dentro del sistema, por favor, intentelo nuevamente.\n\n");
            else:
                if cont2 == 0:
                    while sw == 1:
                        try:
                            cont_vocal1=0;
                            cont_consonante1=0;
                            patente_verificador_nombre=input("Ingrese su patente (Sin numeros y al menos 3 caracteres): ");
                            print("");
                            patente_verificadro_numero=int(input("Ingrese los numeros de su patente (Al menos 3 numeros): "));
                            print("");
                            if patente_verificador_nombre.isalpha() == True:
                                for caracter in patente_verificador_nombre:
                                    if caracter == 'a' or caracter == 'A' or caracter == 'e' or caracter == 'E' or caracter == 'i' or caracter == 'I' or caracter == 'O' or caracter == 'o' or caracter == 'U' or caracter == 'u':
                                        cont_vocal1+=1
                                    else:
                                        cont_consonante1+=1
                                cont_palabras1=cont_vocal1+cont_consonante1;
                                if cont_palabras1 >= 3:
                                    if patente_verificadro_numero >= 1 and patente_verificadro_numero <= 999:
                                        if patente_verificador_nombre == patente and patente_verificadro_numero == numero_patente:
                                            dia=int(input("Ingrese la fecha: "));
                                            print("");
                                            mes=input("Ingrese el mes: ");
                                            print("");
                                            año=int(input("Ingrese el año: "));
                                            print("");
                                            if dia >= 1 and dia <= 31:
                                                if mes.isalpha() == True:
                                                    if año >= 1 and año <= 2500:
                                                        print(f"Se ha registrado correctamente la fecha ingresada: {dia} de {mes} del año {año}");
                                                        sw=0;
                                                        cont2+=1
                                                    else:
                                                        print(f"El año ingresado: {año} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                                else:
                                                    print(f"El mes ingresado: {mes} contiene numeros o no digito nada, por favor, intentelo nuevamente.\n\n");
                                            else:
                                                print(f"El dia ingresado: {dia} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                        else:
                                            print(f"La patente ingresada es incorrecta con el registrada en el sistema, por favor, intentelo nuevamente.\n\n");
                                    else:
                                        print(f"Los numeros ingresados de su patente: {patente_verificadro_numero} no son validos dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                else:
                                    print(f"La patente ingresada: {patente_verificador_nombre} no contiene las suficientes letras que se requiere, por favor intentelo nuevamente.\n\n");
                            else:
                                print(f"El patente ingresado: {patente_verificador_nombre} contiene numeros o no digito nada, por favor, digite correctamente.\n\n");
                        except ValueError:
                            print("\n\nEl caracter digitado no es valido, por favor, intentelo nuevamente.\n\n");
                else:
                    while sw == 1:
                        try:
                            cont_vocal3=0;
                            cont_consonante3=0;
                            patente_verificador_nombre=input("Ingrese su patente (Sin numeros y al menos 3 caracteres): ");
                            print("");
                            patente_verificadro_numero=int(input("Ingrese los numeros de su patente (Al menos 3 numeros): "));
                            print("");
                            if patente_verificador_nombre.isalpha() == True:
                                for caracter in patente_verificador_nombre:
                                    if caracter == 'a' or caracter == 'A' or caracter == 'e' or caracter == 'E' or caracter == 'i' or caracter == 'I' or caracter == 'O' or caracter == 'o' or caracter == 'U' or caracter == 'u':
                                        cont_vocal3+=1
                                    else:
                                        cont_consonante3+=1
                                cont_palabras3=cont_vocal3+cont_consonante3;
                                if cont_palabras3 >= 3:
                                    if patente_verificadro_numero >= 1 and patente_verificadro_numero <= 999:
                                        if patente_verificador_nombre == patente and patente_verificadro_numero == numero_patente:
                                            dia1=int(input("Ingrese la fecha: "));
                                            print("");
                                            mes1=input("Ingrese el mes: ");
                                            print("");
                                            año1=int(input("Ingrese el año: "));
                                            print("");
                                            if dia1 >= 1 and dia1 <= 31:
                                                if mes1.isalpha() == True:
                                                    if año1 >= 1 and año1 <= 2500:
                                                        print(f"Su primera fecha de ingreso fue: {dia} de {mes} del año {año}");
                                                        print("");
                                                        print(f"Se ha registrado correctamente la ultima fecha ingresada: {dia1} de {mes1} del año {año1}");
                                                        print("");
                                                        sw=0;
                                                        cont2+=1
                                                    else:
                                                        print(f"El año ingresado: {año1} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                                else:
                                                    print(f"El mes ingresado: {mes1} contiene numeros o no digito nada, por favor, intentelo nuevamente.\n\n");
                                            else:
                                                print(f"El dia ingresado: {dia1} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                        else:
                                            print(f"La patente ingresada es incorrecta con el registrada en el sistema, por favor, intentelo nuevamente.\n\n");
                                    else:
                                        print(f"Los numeros ingresados de su patente: {patente_verificadro_numero} no son validos dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                else:
                                    print(f"La patente ingresada: {patente_verificador_nombre} no contiene las suficientes letras que se requiere, por favor intentelo nuevamente.\n\n");
                            else:
                                print(f"El patente ingresado: {patente_verificador_nombre} contiene numeros o no digito nada, por favor, digite correctamente.\n\n");
                        except ValueError:
                            print("\n\nEl caracter digitado no es valido, por favor, intentelo nuevamente.\n\n");
        elif op == 3:
            if cont == 0:
                print("No se ha registrada ningun vehiculo dentro del sistema, por favor, intentelo nuevamente.\n\n");
            else:
                while sw == 1:
                    try:
                        cont_vocal2=0;
                        cont_consonante2=0;
                        patente_verificador_nombre=input("Ingrese su patente (Sin numeros y al menos 3 caracteres): ");
                        print("");
                        patente_verificadro_numero=int(input("Ingrese los numeros de su patente (Al menos 3 numeros): "));
                        print("");
                        if patente_verificador_nombre.isalpha() == True:
                            for caracter in patente_verificador_nombre:
                                if caracter == 'a' or caracter == 'A' or caracter == 'e' or caracter == 'E' or caracter == 'i' or caracter == 'I' or caracter == 'O' or caracter == 'o' or caracter == 'U' or caracter == 'u':
                                    cont_vocal2+=1
                                else:
                                    cont_consonante2+=1
                            cont_palabras2=cont_vocal2+cont_consonante2;
                            if cont_palabras2 >= 3:
                                if patente_verificadro_numero >= 1 and patente_verificadro_numero <= 999:
                                    if patente_verificador_nombre == patente and patente_verificadro_numero == numero_patente:
                                        print("------------------------------------------------------");
                                        print(f"Sus datos son:\n\nSu patente es:\t{patente} {numero_patente}\n\nSu marca de auto es:\t{marca}\n\nSu modelo de automovil es:\t{modelo}\n\nEl año de fabricacion de su vehiculo es:\t{año_fabricacion}\n\nEl tipo de vehiculo de su auto (en solo un caracter) es:\t{tipo_vehiculo}\n\n");
                                        print("------------------------------------------------------");
                                        print("");
                                        sw=0;
                                    else:
                                        print(f"La patente ingresada es incorrecta con el registrada en el sistema, por favor, intentelo nuevamente.\n\n");
                                else:
                                    print(f"Los numeros ingresados de su patente: {patente_verificadro_numero} no son validos dentro del sistema, por favor, intentelo nuevamente.\n\n");
                            else:
                                print(f"La patente ingresada: {patente_verificador_nombre} no contiene las suficientes letras que se requiere, por favor intentelo nuevamente.\n\n");
                        else:
                            print(f"El patente ingresado: {patente_verificador_nombre} contiene numeros o no digito nada, por favor, digite correctamente.\n\n");
                    except ValueError:
                        print("\n\nEl caracter digitado no es valido, por favor, intentelo nuevamente.\n\n");
        elif op == 4:
            if cont == 0:
                print("Uste no ha registrado ningun vehiculo, pero lo dejare salir de todos modos\n\n");
                Flag=False
            else:
                print("Cerrando sesión");
                Flag=False
        else:
            print(f"El numero digitado: {op} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
    except ValueError:
        print("\n\nEl caracter digitado no es valido, por favor, intentelo nuevamente.\n\n");