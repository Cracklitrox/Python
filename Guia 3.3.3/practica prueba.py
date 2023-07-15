Flag=True
cont=0;
cont1=0;
while Flag==True:
    print("---------------------------------------\n");
    print("(1). Registrar Cliente\n(2). Suscripción\n(3). Consultar Datos Cliente\n(4). Salir\n");
    print("---------------------------------------\n");
    sw=1;
    try:
        op=int(input("Seleccione una opción: "));
        print("");
        if op == 1:
            if cont == 0:
                while sw == 1:
                    try:
                        cont_correo=0;
                        cont_mal=0;
                        rut=int(input("Ingrese su rut (Sin digito verificador ni puntos): "));
                        print("");
                        nombre=input("Ingrese su nombre: ");
                        print("");
                        direccion=input("Ingrese su dirección (Sin numeros): ");
                        print("");
                        numero_direccion=int(input("Ingrese el numero de su dirección: "));
                        print("");
                        comuna=input("Ingrese su comuna: ");
                        print("");
                        correo=input("Ingrese su correo: ");
                        print("");
                        edad=int(input("Ingrese su edad: "));
                        print("");
                        genero=input("Ingrese su genero (M o F): ");
                        print("");
                        celular=int(input("Ingrese su numero de celular (9 digitos): (+56) "));
                        print("");
                        print("-----------------------------------------\n");
                        print("Tenemos disponibles las siguiente cuentas\n");
                        print("Premium\nGold\nSilver\n\n");
                        print("-----------------------------------------\n\n");
                        cuenta=input("Ingrese el tipo de cuenta que desea: ");
                        print("");
                        if rut >= 4000000 and rut <= 99999999:
                            if all(x.isalnum() or x.isspace() for x in nombre):
                                if all(x.isalnum() or x.isspace() for x in direccion):
                                    if numero_direccion >= 1 and numero_direccion <= 99999999:
                                        if all(x.isalnum() or x.isspace() for x in comuna):
                                            for caracter in correo:
                                                if caracter == '@':
                                                    cont_correo+=1
                                                else:
                                                    cont_mal+=1
                                            if cont_correo == 1:
                                                if edad >= 0 and edad <= 110:
                                                    if all(x.isalnum() or x.isspace() for x in genero):
                                                        if genero == 'M' or genero == 'm' or genero == 'F' or genero == 'f':
                                                            if celular >= 100000000 and celular <= 999999999:
                                                                if all(x.isalnum() or x.isspace() for x in cuenta):
                                                                    if cuenta == 'Premium' or cuenta == 'PREMIUM' or cuenta == 'premium' or cuenta == 'Gold' or cuenta == 'GOLD' or cuenta == 'gold' or cuenta == 'Silver' or cuenta == 'SILVER' or cuenta == 'silver':
                                                                        print(f"Gracias {nombre}, su cuenta ha sido registrada exitosamente.\nVolvera al menu de inicio\n\n");
                                                                        cont+=1
                                                                        sw=0
                                                                    else:
                                                                        print(f"El tipo de cuenta ingresada: {cuenta} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                                                else:
                                                                    print(f"El tipo de cuenta ingresada: {cuenta} contiene numeros, por favor, abstenganse de usar digitos en selección de cuenta\nIntentelo nuevamente.\n\n");
                                                            else:
                                                                print(f"El numero ingresado: {celular} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                                        else:
                                                            print(f"El genero ingresado: {genero} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                                    else:
                                                        print(f"El genero ingresado: {genero} contiene numeros, por favor, abstenganse de usar digitos en el genero\nIntentelo nuevamente.\n\n");
                                                else:
                                                    print(f"La edad ingresada: {edad} no es valida dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                            elif cont_correo >= 2:
                                                print(f"El correo ingresado: {correo} tiene mas de un '@', por favor, intentelo nuevamente.\n\n");
                                            else:
                                                print(f"El correo ingresado: {correo} le falta un '@', por favor, intentelo nuevamente.\n\n");
                                        else:
                                            print(f"La comuna ingresada: {comuna} contiene numeros, por favor, abstenganse de usar digitos en la comuna\nIntentelo nuevamente.\n\n");
                                    else:
                                        print(f"El numero de su dirección: {numero_direccion} no existe dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                else:
                                    print(f"La dirección ingresada: {direccion} contiene numeros, por favor, abstenganse de usar digitos en su dirección\nIntentelo nuevamente.\n\n");
                            else:
                                print(f"El nombre ingresado: {nombre} contiene numero, por favor, abstenganse de usar digitos en su nombre\nIntentelo nuevamente.\n\n");
                        else:
                            print(f"El rut ingresado: {rut} no es valido dentro del sistema, por favor intentelo nuevamente.\n\n");
                            op1=input("Desea volver al menu principal, o desea continuar intentandolo \n\n(1) Salir\n(2) Continuar\n\nSeleccione su opción: ");
                            print("");
                            if op1 == '1' or op1 == 'Salir' or op1 == 'salir' or op1 == 'SALIR':
                                print("Ok, siga intentandolo\n\n");
                                sw=0
                            elif op1 == '2' or op1 == 'Continuar' or op1 == 'CONTINUAR' or op1 == 'continuar':
                                print("Esta bien, sera devuelo al menu de inicio\n\n");
                            else:
                                print(f"El caracter ingresado: {op1} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                    except ValueError:
                        print("\n\nUsted digito mal lo que se le pedia, por favor intentelo nuevamente.\n\n");
            else:
                print("Ya existe una cuenta dentro del sistema, por favor, elija las demás opciones del sistema.\n\n");
        elif op == 2:
            if cont == 0:
                print("No hay una cuenta registrada dentro del sistema, por favor, elija la opción 1 para crear una cuenta.\n\n");
            else:
                if cont1 == 0:
                    while sw == 1:
                        try:
                            rut_verificador=int(input("Ingrese su rut (Sin puntos ni digitador verificador): "));
                            print("");
                            if rut >= 4000000 and rut <= 99999999:
                                if rut_verificador == rut:
                                    while sw == 1:
                                        try:
                                            dia=int(input("Ingrese el dia: "));
                                            print("");
                                            mes=input("Ingrese el mes: ");
                                            print("");
                                            año=int(input("Ingrese el año: "));
                                            print("");
                                            if dia >= 1 and dia <= 31:
                                                if mes.isalpha() == True:
                                                    if año >= 1 and año <= 9999:
                                                        print(f"Se ha registrado el primer inicio de sección de su cuenta: {dia} de {mes} del año {año}\n\n");
                                                        sw=0;
                                                        cont1+=1
                                                    else:
                                                        print(f"El año ingresado: {año} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                                else:
                                                    print(f"El mes ingresado: {mes} contiene numeros, por favor, abstengase de usar digitos\nIntentelo nuevamente.\n\n");
                                            else:
                                                print(f"El dia ingresado: {dia} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                        except ValueError:
                                            print("\n\nUsted ha digito mal lo que se le pedia, por favor, intentelo nuevamente.\n\n");
                                else:
                                    print(f"El rut ingresado: {rut_verificador} no es igual al que esta registrado dentro del sistema, por favor, intentelo nuevamente.\n\n");
                            else:
                                print(f"El rut ingresado: {rut_verificador} no es valido dentro del sistema, por favor intentelo nuevamente.\n\n");
                        except ValueError:
                            print("\n\nUsted ha digito mal lo que se le pedia, por favor, intentelo nuevamente.\n\n");
                else:
                    while sw == 1:
                        try:
                            rut_verificador=int(input("Ingrese su rut (Sin puntos ni digitador verificador): "));
                            print("");
                            if rut >= 4000000 and rut <= 99999999:
                                if rut_verificador == rut:
                                    while sw == 1:
                                        try:
                                            dia1=int(input("Ingrese el dia: "));
                                            print("");
                                            mes1=input("Ingrese el mes: ");
                                            print("");
                                            año1=int(input("Ingrese el año: "));
                                            print("");
                                            if dia1 >= 1 and dia1 <= 31:
                                                if mes1.isalpha() == True:
                                                    if año1 >= 1 and año <= 9999:
                                                        print(f"Se ha registrado el primer inicio de sección de su cuenta: {dia} de {mes} del año {año}\n\n");
                                                        print(f"La ultima fecha ingresada en la aplicacion fue: el dia {dia1} de {mes1} del año {año1}\n\n");
                                                        sw=0;
                                                        cont1+=1
                                                    else:
                                                        print(f"El año ingresado: {año} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                                else:
                                                    print(f"El mes ingresado: {mes} contiene numeros, por favor, abstengase de usar digitos\nIntentelo nuevamente.\n\n");
                                            else:
                                                print(f"El dia ingresado: {dia} no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
                                        except ValueError:
                                            print("\n\nUsted ha digito mal lo que se le pedia, por favor, intentelo nuevamente.\n\n");
                                else:
                                    print(f"El rut ingresado: {rut_verificador} no es igual al que esta registrado dentro del sistema, por favor, intentelo nuevamente.\n\n");
                            else:
                                print(f"El rut ingresado: {rut_verificador} no es valido dentro del sistema, por favor intentelo nuevamente.\n\n");
                        except ValueError:
                            print("\n\nUsted ha digito mal lo que se le pedia, por favor, intentelo nuevamente.\n\n");
        elif op == 3:
            if cont == 0:
                print("No hay una cuenta registrada dentro del sistema, por favor, elija la opción 1 para crear una cuenta.\n\n");
            else:
                while sw == 1:
                    try:
                        rut_verificador=int(input("Ingrese su rut (Sin puntos ni digitador verificador): "));
                        print("");
                        if rut >= 4000000 and rut <= 99999999:
                            if rut_verificador == rut:
                                print(f"Se mostraran los datos del cliente\n");
                                print("-----------------------------------------------------------------------");
                                print(f"Su rut es:\t{rut}\n\nSu nombre es:\t{nombre}\n\nSu dirección es:\t{direccion} {numero_direccion}\n\nSu comuna es:\t{comuna}\n\nSu correo es:\t{correo}\n\nSu edad es:\t{edad}\n\nSu genero es:\t{genero}\n\nSu numero de celular es:\t{celular}\n\nEl tipo de cuenta que tiene es:\t{cuenta}\n\n");
                                print("-----------------------------------------------------------------------");
                                sw=0;
                            else:
                                print(f"El rut ingresado: {rut_verificador} no es igual al que esta registrado dentro del sistema, por favor, intentelo nuevamente.\n\n");
                        else:
                            print(f"El rut ingresado: {rut_verificador} no es valido dentro del sistema, por favor intentelo nuevamente.\n\n");
                    except ValueError:
                        print("\n\nUsted digito mal lo que se le pedia, por favor, intentelo nuevamente.\n\n")
        elif op == 4:
            if cont == 0:
                print("Usted no ha registrado ninguna cuenta, pero igual lo dejo salir de la aplicación, denada\n\n");
                Flag=False;
            else:
                print(f"Gracias por suscribirse a la App de Juan Maestro, {nombre}");
                Flag=False;
        else:
            print("Ingrese una opcion valida");
    except ValueError:
        print("\n\nUsted digito mal lo que se le pedia, por favor, intentelo nuevamente.\n\n");