Flag=True
cont=0;
cont3=0;
while Flag == True:
    print("-----------------------------");
    print("       Juan Maestro App      ");
    print("-----------------------------\n");
    print("(1). Registrar Cliente       ");
    print("(2). Suscripción             ");
    print("(3). Consultar Datos Cliente ");
    print("(4). Salir                   \n");
    print("-----------------------------");
    cont1=0;
    cont2=0;
    try:
        op=int(input("Seleccione una opción: "));
        print("");
        if op == 1:
            if cont == 0:
                rut=int(input("Ingrese su rut (Sin dígito verificador ni puntos): "));
                print("");
                if rut >= 4000000 and rut <= 99999999:
                    nom=input("Ingrese su nombre de usuario: ");
                    print("");
                    # Preguntar al profesor como hacer la distincion para que sea mas de una letra: 'a' y que sea valido si yo ingreso mas de 2 letras: 'ze' #
                    dirrecion=input("Ingrese su direción: ");
                    print("");
                    # Preguntar al profesor como hacer la distincion para que sea mas de una letra: 'a' y que sea valido si yo ingreso mas de 2 letras: 'miraflores' o 'mi' #
                    dirrecion_num=int(input("Ingrese el numero de su dirección: "));
                    print("");
                    if dirrecion_num >= 1 and dirrecion_num <= 999999:
                        comuna=input("Ingrese su comuna: ");
                        print("");
                        # Preguntar al profesor como hacer la distincion para que sea mas de una letra: 'a' y que sea valido si yo ingreso mas de 2 letras: 'Puerto Montt' o 'PM' #
                        correo=input("Ingrese su correo: ");
                        print("");
                        # Preguntar al profesor a que se refiere el problema en que use 'cadena de caracteres', como se hace eso? #
                        for caracter in correo:
                            if caracter == '@':
                                cont1=cont1+1
                            else:
                                cont2=cont2+1
                        if cont1 == 1:
                            edad=int(input("Ingrese su edad: "));
                            print("");
                            if edad >= 0 and edad <= 110:
                                genero=input("Ingrese su genero (M o F): ");
                                print("");
                                # Preguntar al profesor si esta bien con 'input' o tengo que usar 'chr' obligatoriamente #
                                if genero == 'M' or genero == 'm' or genero == 'F' or genero == 'f':
                                    celular=int(input("Ingrese su numero de celular (Hasta 9 digitos): "));
                                    print("");
                                    if celular >= 100000000 and celular <= 999999999:
                                        print("-------------------------------------------------------");
                                        print("Tenemos en disposición los siguientes tipos de cuentas  \n");
                                        print("Premium\nGold\nSilver\n");
                                        print("-----------------------------------------------------\n");
                                        tipo=input("Ingrese el tipo de cuenta que desea: ");
                                        print("");
                                        if tipo == 'Premium' or tipo == 'PREMIUM' or tipo == 'premium' or tipo == 'Gold' or tipo == 'GOLD' or tipo == 'gold' or tipo == 'Silver' or tipo == 'SILVER' or tipo == 'silver':
                                            print(f"Gracias {nom}, su cuenta ha sido registrada exitosamente\n\nSera rediccionado al menu de inicio.\n\n");
                                            cont=cont+1
                                        else:
                                            print(f"El caracter digitalizado: {tipo} no se encuentra disponible entre las opciones dentro del sistema, por favor intentelo nuevamente\nSera enviado al menu de inicio-\n\n");
                                    else:
                                        print(f"El numero ingresado: {celular} no es valido dentro del sistema, por favor intentelo nuevamente, sera enviado al menu de inicio.\n\n");
                                else:
                                    print(f"El caracter ingresado: {genero} no es valido dentro del sistema, por favor intentelo nuevamente, sera enviado al menu de inicio.\n\n");
                            else:
                                print(f"La edad ingresada: {edad} no es valido dentro del sistema, por favor intentelo nuevamente, sera enviado al menu de inicio.\n\n");
                        else:
                            print(f"El correo ingresado: {correo} le falta un '@' al menos, por favor intentelo nuevamente, sera enviado al menu del inicio.\n\n");
                    else:
                        print(f"El numero de la dirección ingresada: {dirrecion_num} no es valido dentro del sistema, por favor, intentelo nuevamente.\nSera devuelto al menu de inicio\n\n");
                else:
                    print(f"El rut ingresado: {rut} no es valido dentro del sistema, por favor intentelo nuevamente.\n\n");
            else:
                print(f"Ya existe un usuario registrado dentro del sistema, su nombre es: {nom}, por favor elija las demás opciones.\n\n");
        elif op == 2:
            if cont == 0:
                print("Para poder entrar a esta opción, necesita registrar un usuario, por favor elija la opción 1\n\n");
            else:
                if cont3 == 0:
                    rut_verificador=int(input("Ingrese su rut (Sin dígito verificador ni puntos): "));
                    print("");
                    if rut_verificador == rut:
                        dia=int(input(f"Bienvenido {nom}, por favor ingrese el dia en que inicio seción: "));
                        print("");
                        if dia >= 1 and dia <= 31:
                            fecha_lista=[dia];
                            mes=input("Ingrese el mes: ");
                            print("");
                            if mes == 'Enero' or mes == 'enero' or mes == 'ENERO' or mes == 'Febrero' or mes == 'FEBRERO' or mes == 'febrero' or mes == 'Marzo' or mes == 'MARZO' or mes == 'marzo' or mes == 'Abril' or mes == 'abril' or mes == 'ABRIL' or mes == 'Mayo' or mes == 'mayo' or mes == 'MAYO' or mes == 'Junio' or mes == 'JUNIO' or mes == 'junio' or mes == 'Julio' or mes == 'JULIO' or mes == 'julio' or mes == 'Agosto' or mes == 'agosto' or mes == 'AGOSTO' or mes == 'Septiembre' or mes == 'SEPTIEMBRE' or mes == 'septiembre' or mes == 'Octubre' or mes == 'octubre' or mes == 'OCTUBRE' or mes == 'Noviembre' or mes == 'noviembre' or mes == 'NOVIEMBRE' or mes == 'Diciembre' or mes == 'diciembre' or mes == 'DICIEMBRE':
                                fecha_lista.append(mes);
                                año=int(input("Ingrese el año: "));
                                print("");
                                if año >= 1 and año <= 9999:
                                    fecha_lista.append(año);
                                    print(f"Bienvenido {nom}, su primera fecha de ingreso fue el dia {fecha_lista[0]} de {fecha_lista[1]} del año {fecha_lista[2]}.\n\n");
                                    cont3=cont3+1
                                else:
                                    print(f"El año ingresado: {año} no es valido dentro del sistema, por favor intentelo nuevamente.\n\n");
                            else:
                                print(f"El mes ingresado: {mes} no es valido dentro del sistema, por favor intentelo nuevamente.\n\n");
                        else:
                            print(f"El dia ingresado: {dia} no es valido dentro del sistema, por favor intentelo nuevamente.\n\n");
                    else:
                        print(f"El rut ingresado: {rut_verificador} no coincide con el registrado dentro del sistema, por favor intentelo nuevamente.\n\n");
                else:
                    rut_verificador=int(input("Ingrese su rut (Sin dígito verificador ni puntos): "));
                    print("");
                    if rut_verificador == rut:
                        dia1=int(input(f"Bienvenido {nom}, por favor ingrese el dia en que inicio seción: "));
                        print("");
                        if dia1 >= 1 and dia1 <= 31 and dia1 > dia:
                            fecha_lista1=[dia1];
                            mes1=input("Ingrese el mes: ");
                            print("");
                            if mes1 == 'Enero' or mes1 == 'enero' or mes1 == 'ENERO' or mes1 == 'Febrero' or mes1 == 'FEBRERO' or mes1 == 'febrero' or mes1 == 'Marzo' or mes1 == 'MARZO' or mes1 == 'marzo' or mes1 == 'Abril' or mes1 == 'abril' or mes1 == 'ABRIL' or mes1 == 'Mayo' or mes1 == 'mayo' or mes1 == 'MAYO' or mes1 == 'Junio' or mes1 == 'JUNIO' or mes1 == 'junio' or mes1 == 'Julio' or mes1 == 'JULIO' or mes1 == 'julio' or mes1 == 'Agosto' or mes1 == 'agosto' or mes1 == 'AGOSTO' or mes1 == 'Septiembre' or mes1 == 'SEPTIEMBRE' or mes1 == 'septiembre' or mes1 == 'Octubre' or mes1 == 'octubre' or mes1 == 'OCTUBRE' or mes1 == 'Noviembre' or mes1 == 'noviembre' or mes1 == 'NOVIEMBRE' or mes1 == 'Diciembre' or mes1 == 'diciembre' or mes1 == 'DICIEMBRE':
                                fecha_lista1.append(mes1);
                                año1=int(input("Ingrese el año: "));
                                print("");
                                if año1 >= 1 and año1 <= 9999 and año1 >= año:
                                    fecha_lista1.append(año1);
                                    print(f"Bienvenido {nom}, su primera fecha de ingreso fue el dia {fecha_lista[0]} de {fecha_lista[1]} del año {fecha_lista[2]}.\n\n");
                                    # Preguntar al profesor como hacer la distincion si el usuario puso en su fecha inicial: 2 de marzo del 2020 y luego cuando pongo : 1 de marzo del 2020; Que se pueda hacer una distincion en caso de que yo ingrese un dia anterior o que el mes sea igual o anterior, ya que, ya hay una excepcion para cuando el año es menor al inicial #
                                    print(f"Su ultimo inicio de seción fue el dia {fecha_lista1[0]} de {fecha_lista1[1]} del año {fecha_lista1[2]}.\n\n");
                                elif año1 < año:
                                    print(f"Hay algo raro aqui, su año ingresado {año1} es diferente del año {año} de su fecha inicial, por favor, digite correctamente sus fechas.\n\n")
                                else:
                                    print(f"El año ingresado: {año} no es valido dentro del sistema, por favor intentelo nuevamente.\n\n");
                            else:
                                print(f"El mes ingresado: {mes} no es valido dentro del sistema, por favor intentelo nuevamente.\n\n");
                        else:
                            print(f"El dia ingresado: {dia} no es valido dentro del sistema, por favor intentelo nuevamente.\n\n");
                    else:
                        print(f"El rut ingresado: {rut_verificador} no coincide con el registrado dentro del sistema, por favor intentelo nuevamente.\n\n");
        elif op == 3:
            if cont == 0:
                print("Para poder entrar a esta opción, necesita registrar un usuario, por favor elija la opción 1\n\n");
            else:
                rut_verificador=int(input("Ingrese su rut (Sin dígito verificador ni puntos): "));
                print("");
                if rut_verificador == rut:
                    print(f"Bienvenido {nom} a continuacion se mostraran sus datos de forma ordenada\n\nSu rut es:\t{rut}\nSu nombre de usuario es:\t{nom}\nSu dirección es:\t{dirrecion} {dirrecion_num}\nSu comuna es:\t{comuna}\nSu correo electronico es:\t{correo}\nSu edad es:\t{edad}\nSu genero es:\t{genero}\nSu numero telefonico es:\t{celular}\nEl tipo de cuenta que tiene registrado es:\t{tipo}\n\nEstos son sus datos {nom}, sera reenviado al menu de inicio\n\n");
                else:
                    print(f"El rut escrito: {rut_verificador} no coincide con el registrado en el sistema, por favor intentelo nuevamente.\n\n");
        elif op == 4:
            if cont == 0:
                print("No ha registrado ninguna cuenta, recuerde que Juan Maestro me paga por cada usuario registrado, pero lo dejare salir por ahora, adios. :D\n\n");
                Flag=False
            else:
                print(f"Gracias por suscribirse a la App de Juan Maestro {nom}, vuelva pronto :D\n\n");
                Flag=False
        else:
            print(f"La opcion elegida: {op} no se encuentra dentro del sistema, por favor, seleccione una de las 4 opciones disponibles.\n\n");
    except ValueError:
        print("\n\nEl valor digitalizado es erroneo, por favor escriba correctamente.\n\n");