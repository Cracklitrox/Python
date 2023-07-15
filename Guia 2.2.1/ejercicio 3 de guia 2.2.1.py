import sys
print("---------------------------------------");
not1=float(input("Ingrese su primera nota (1.0 a 7.0): "));
if not1 <= 0.9 or not1 >= 7.1:
    print("Ingrese un valor valido");
    print("---------------------------------------");
    print (sys.exit());
else:
    not2=float(input("Ingres su segunda nota (1.0 a 7.0): "));
    if not2 <= 0.9 or not2 >= 7.1:
        print("Ingrese un valor valido");
        print("---------------------------------------");
        print (sys.exit());
    else:
        not3=float(input("Ingrese su tercera nota (1.0 a 7.0): "));
        if not3 <= 0.9 or not2 >= 7.1:
            print("Ingrese un valor valido");
            print("---------------------------------------");
            print (sys.exit());
result=(not1+not2+not3)/3;
print("");
if result >= 4.0:
    print(f"Felicidades, aprobaste el curso\nTu promedio fue de: {result}");
    print("---------------------------------------");
else:
    print(f"Desafortunadamente, desaprobaste el curso\nTu promedio fue de: {result}");
    print("---------------------------------------");