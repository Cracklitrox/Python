from re import T
def fibonacci(r):
    a=0;
    b=1;
    c=0;
    num=[];
    for n in range(r):
        a=b;
        b=c;
        c=a+b;
        num.append(c);
    return num
while True:
    print("-----------------------\n    Serie Fibonacci    \n-----------------------\n");
    try:
        tamaño=int(input("Indique cuántos números considerara la serie:\t"));
        print();
        if tamaño >= 1:
            print(f"Los numeros son los siguientes:\t{fibonacci(tamaño)}\n");
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
            print(f"El número ingresado para el tamaño de la serie fibonacci:\t{tamaño} no es valido, intentelo con números mayores a 0\n");
    except ValueError:
        print("\nSolo digite números\n");