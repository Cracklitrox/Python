import sys
print("-------------------------------------------------");
print("Bienvenido al siguiente juego");
print("");
print("¿Cuál de los siguientes animales vive en el agua?");
print("");
print("(1) Perro\n(2) Cocodrilo\n(3) Conejo\n(4) Tiburón");
print("")
option=int(input("Ingrese la alternativa correcta: "));
print("");
if option <= 0 or option >= 5:
    print("Valor incorrecto\nPor favor, ingrese un valor valido");
    print("-------------------------------------------------");
    print (sys.exit());
else:
    if option == 4:
        print("!Es correcto¡\nUsted ha ganado 1 punto");
        print("-------------------------------------------------");
    elif option == 2:
        print("!Estuviste cerca¡\nUsted ha ganado 0.5 puntos");
        print("-------------------------------------------------");
    else:
        print("!No es correcto¡\nDesafortunadamente, no gano puntos");
        print("-------------------------------------------------");