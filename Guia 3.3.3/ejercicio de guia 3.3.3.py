from calendar import c
from re import M

cont2=0;
cont3=0;
Flag=True
while Flag == True:
    print("-----------------------------");
    print("     App Juan Maestro   ");
    print("-----------------------------\n");
    print("(1). Registrar Cliente       ");
    print("(2). Suscripción             ");
    print("(3). Consultar Datos Cliente ");
    print("(4). Salir                   ");
    print("");
    cont=0;
    cont1=0;
    sexo='M'
    sexo1='m'
    sexo2='F'
    sexo3='f'
    try:
        op=int(input("Ingrese una opción: "));
        print("");
        if op == 1:
            if cont2 == 0:
                print("Se le pediran los siguientes datos");
                print("");
                rut=int(input("Ingrese su rut(Sin dígito verificador ni puntos): "));
                print("")
                if rut >= 4000000 and rut <= 99999999:
                    print(f"El rut: {rut}, ha sido registrado.\n")
                    print("");
                    rut_list=[rut]
                    nom=input("Ingrese su nombre: ");
                    print("");
                    # Hacer una distincion con if para verificar que sea caracter el "nom" #
                    nom_list=[nom]
                    dirre=input("Ingrese su dirreccion: ");
                    print("");
                    # No es necesario hacer una distincion #
                    dirre_list=[dirre]
                    comu=input("Ingrese su comuna: ");
                    print("");
                    # Hacer una distincion con if para verificar que sea caracter en "comu" #
                    comu_list=[comu]
                    correo=input("Ingrese su correo: ");
                    print("");
                    for caracter in correo:
                        if caracter == '@':
                            cont=cont+1
                        else:
                            cont1=cont1+1
                    if cont == 1:
                        print(f"El correo: {correo}, ha sido registrado.\n");
                        correo_list=[correo]
                        edad=int(input("Ingrese su edad: "));
                        print("");
                        if edad >= 1 and edad <= 110:
                            print(f"Su edad de {edad} años ha sido registrada\n");
                            edad_list=[edad]
                            genero=input("Ingrese su genero (M o F): ");
                            print("");
                            if genero == sexo or genero == sexo1 or genero == sexo2 or genero == sexo3:
                                print(f"Su genero ha sido registrado.\n");
                                genero_list=[genero]
                                celular=int(input("Ingrese su numero: "));
                                print("");
                                if celular >= 100000000 and celular <= 999999999:
                                    print(f"Su numero: {celular}, ha sido registrado.\n");
                                    celular_list=[celular]
                                    print("------------------------------------------");
                                    print("Tenemos disponibles las siguientes cuentas:\n\nPremium\nGold\nSilver\n");
                                    print("------------------------------------------\n");
                                    tipo=input("Ingrese el tipo de cuenta que desea: ")
                                    print("");
                                    if tipo == 'Premium' or tipo == 'PREMIUM' or tipo == 'premium':
                                        print(f"Su cuenta {tipo} ha sido registrada.\n");
                                        cont2=cont2+1
                                        tipo_list=[tipo]
                                    elif tipo == 'Gold' or tipo == 'GOLD' or tipo == 'gold':
                                        print(f"Su cuenta {tipo} ha sido registrada.\n");
                                        cont2=cont2+1
                                        tipo_list=[tipo]
                                    elif tipo == 'Silver' or tipo == 'SILVER' or tipo == 'silver':
                                        print(f"Su cuenta {tipo} ha sido registrada.\n");
                                        cont2=cont2+1
                                        tipo_list=[tipo]
                                else:
                                    print(f"El numero: {celular}, no se ha podido registrar, por favor digite correctamente.");
                            else:
                                print(f"El digito ingresado: {genero} no se encuentra valido dentro del sistema, por favor intentelo nuevamente.\n\n");
                        else:
                            print(f"El numero {edad} años no se puede registrar dentro del sistema, debido a que no es valido, por favor intentelo nuevamente.\n\n");
                    else:
                        print(f"El correo: {correo}, no ha sido registrado, debido a que uso mas de una vez '@' o falto usar '@'\n");
                else:
                    print(f"El rut: {rut} esta mal digitalizado, por favor intentelo nuevamente.\n\n");
            elif cont2 == 1:
                print(f"\nYa se ha registrado un usuario en el sistema, por ahora solo se admite un usuario.\nSe le mostrara el menu de inicio.\n\n");
        elif op == 2:
            if cont2 == 0:
                print("Usted aun no se ha registrado, por favor seleccione la opcion 1.\n\n");
            elif cont2 == 1:
                rut_verificador=int(input("Ingrese su rut(Sin dígito verificador ni puntos): "));
                print("");
                if rut_verificador == rut:
                    print(f"Bienvenido {nom}.\n");
                    if cont3 == 0:
                        num2=input("Ingrese la fecha de su inicio de secion: ");
                        print("");
                        fecha_lista=[num2];
                        cont3=cont3+1;
                        print(f"Usted ha ingresado el dia: {fecha_lista}");
                    else:
                        num3=input("Ingrese la fecha de su inicio de secion: ");
                        print("");
                        fecha_lista.append(num3);
                        print(f"Usted ha ingresado en los dias: {fecha_lista}");  
                        cont3=cont3+1
                else:
                    print(f"El rut que usted ingreso: {rut_verificador}, no se encuentra registrado dentro del sistema, por favor intentelo nuevamente.\n\n");
        elif op == 3:
            if cont2 == 0:
                print("Usted aun no se ha registrado, por favor seleccione la opcion 1.\n\n");
            else:
                rut_verificador=int(input("Ingrese su rut(Sin dígito verificador ni puntos): "));
                print("");
                if rut_verificador == rut:
                    print(f"Bienvenido {nom}.\n");
                    print(f"Se mostraran los datos del cliente\n\nSu rut es:\t{rut}\nSu nombre es:\t{nom}\nSu dirreccion es:\t{dirre}\nSu comuna es:\t{comu}\nSu correo es:\t{correo}\nSu edad es:\t{edad}\nSu genero es:\t{genero}\nSu celular es:\t{celular}\nSu tipo de cuenta es:\t{tipo}\n\nSe le enviara al menu de inicio.\n\n");
                else:
                    print(f"El rut que usted ingreso: {rut_verificador}, no se encuentra registrado dentro del sistema, por favor intentelo nuevamente.\n\n");    
        elif op == 4:
            if cont2 == 0:
                print("Usted aun no se ha registrado, pero aun asi lo dejare salir de la aplicacion.\n\n");
                Flag=False
            else:
                print("Gracias por suscribirse a la App de Juan Maestro");
                Flag=False
    except ValueError:
        print("");
        print("El caracter digitalizado es erroneo, por favor intentelo nuevamente.\n\n");