def comprobacion(a):
    if a.isalpha() == True:
        if len(a) == 1 and a == 'k' or a == 'K':
            return print(f"El rut ingresado:\t{rut}{dv_rut} es valido\n");
        else:
            return print(f"El rut ingresado:\t{rut}{dv_rut} no es valido, intentalo nuevamente\n");
    elif a.isalnum() == True:
        b=int(a)
        if len(a) == 1 and b >= 0 and b <= 9:
            return print(f"El rut ingresado:\t{rut}{dv_rut} es valido\n");
        else:
            return print(f"El rut ingresado:\t{rut}{dv_rut} no es valido, intentalo nuevamente\n");
while True:
    print("-------------------------\n     Verificador Rut     \n-------------------------\n");
    try:
        rut=input("Ingrese su rut (sin digito verificador):\t");
        print();
        dv_rut=input("Ingrese su digito verificador:\t");
        print();
        if rut.isdigit() == True and len(rut) >= 7 and len(rut) <= 8:
            print(comprobacion(dv_rut));
            op=input("\nDesea intentarlo nuevamente?:\t");
            print();
            if op == 'Si' or op == 'si' or op == 'SI' or op == 'Vale' or op == 'vale' or op == 'VALE' or op == 'ok' or op == 'OK' or op == 'Ok' or op == 'Bueno' or op == 'bueno' or op == 'BUENO':
                continue
            elif op == 'No' or op == 'NO' or op == 'no' or op == 'No gracias' or op == 'NO GRACIAS' or op == 'no gracias':
                print("Cerrando aplicación\n");
                break
            else:
                print(f"La palabra ingresada:\t{op} no es valida dentro del sistema, intentelo nuevamente\n");
        else:
            print(f"El rut ingresado:\t{rut} contiene letras, no es valido en el sistema, intentelo nuevamente\n");
    except ValueError:
        print("\nSolo caracteres y numeros\n");