import os
from time import process_time
os.system('cls')

import sys
print("-------------------------------------------");
print("    Bienvenidos a la ruleta de preguntas   ");
print("");
nom=input("Ingrese su nombre: ");
print("");
print("Comenzaremos con la sección de preguntas");
print("");
print("Primera pregunta");
print("");
print("¿Cuál es el deporte mas popular del mundo?");
print("");
print("(1) Basquetbol\n(2) Futbol americano\n(3) Futbol\n(4) Tenis");
basquetbol=1;
Futbol_americano=2;
Futbol=3;
Tenis=4;
print("");
option1=int(input("Seleccione la alternativa correcta: "));
print("");
if option1 <= 0 or option1 >= 5:
    print("Valor incorrecto\nSeleccione una opcion correcta");
    print("-------------------------------------------");
    print (sys.exit());
else:
    if option1 == 3:
        print("!Alternativa correcta¡\nHas ganado 10 puntos.");
        print("");
    elif option1 == 1:
        print("!Alternativa erronea¡, pero te daremos puntos por lastima\nObtienes 5 puntos.");    
        print("");
    elif option1 == 2 or option1 == 4:
        print("!Alternativa incorrecta, ganas 0 puntos");
        print("");
print("Segunda pregunta");
print("");
print("¿2 elevado a 5 es:");
print("");
print("(1) 16\n(2) 4\n(3) 32\n(4) 64");
a=1;
b=2;
c=3;
d=4;
print("");
option2=int(input("Seleccione la alternativa correcta: "));
print("");
if option2 <= 0 or option2 >= 5:
    print("Valor incorrecto\nSeleccione una opcion correcta");
    print("-------------------------------------------");
    print (sys.exit());
else:
    if option2 == 3:
        print("!Alternativa correcta¡\nHas ganado 10 puntos.");
        print("");
    elif option2 == 1:
        print("!Alternativa erronea¡, pero te daremos puntos por lastima\nObtienes 5 puntos.");    
        print("");
    elif option2 == 2 or option2 == 4:
        print("!Alternativa incorrecta, ganas 0 puntos");
        print("");
print("Tercera y ultima pregunta");
print("");
print("Pablito clavó un clavito en la calva\nde un calvito. Un clavito clavó\nPablito en la calva de un calvito.");
print("")
print("¿Cuantos clavitos clavo pablito?");
print("");
print("(1) 2\n(2) 3\n(3) 1\n(4) 4");
e=1;
f=2;
g=3;
h=4;
print("");
option3=int(input("Seleccione la alternativa correcta: "));
print("");
if option3 <= 0 or option3 >= 5:
    print("Valor incorrecto\nSeleccione una opcion correcta");
    print("-------------------------------------------");
    print (sys.exit());
else:
    if option3 == 3:
        print("!Alternativa correcta¡\nHas ganado 10 puntos.");
        print("");
    elif option3 == 1:
        print("!Alternativa erronea¡, pero te daremos puntos por lastima\nObtienes 5 puntos.");    
        print("");
    elif option3 == 2 or option3 == 4:
        print("!Alternativa incorrecta, ganas 0 puntos");
        print("");
if option1 == 3 and option2 == 3 and option3 == 3:
    print(f"Excelente {nom}, has acertado las 3 preguntas\nHas obtenido 30 puntos.");
    print("-------------------------------------------");
elif option1 == 3 and option2 == 3 and option3 == 1:
    print(f"Bien jugado {nom}, has fallado 1 pregunta, estuviste cerca del 100%\nObtiones 25 puntos.");
    print("-------------------------------------------");
elif option1 == 1 and option2 == 3 and option3 == 3:
    print(f"Bien jugado {nom}, has fallado 1 pregunta, estuviste cerca del 100%\nObtiones 25 puntos.");
    print("-------------------------------------------");
elif option1 == 3 and option2 == 1 and option3 == 3:
    print(f"Bien jugado {nom}, has fallado 1 pregunta, estuviste cerca del 100%\nObtiones 25 puntos.");
    print("-------------------------------------------");
elif option1 == 3 and option2 == 4 or option2 == 2 and option3 == 3:
    print(f"Bien jugado {nom}, has fallado 1 pregunta\nObtienes 20 puntos.");
    print("-------------------------------------------");
elif option1 == 4 or option1 == 2 and option2 == 3 and option3 == 3:
    print(f"Bien jugado {nom}, has fallado 1 pregunta\nObtienes 20 puntos.");
    print("-------------------------------------------");
elif option1 == 3 and option2 == 3 and option3 == 2 or option3 == 4:
    print(f"Bien jugado {nom}, has fallado 1 pregunta\nObtienes 20 puntos.");
    print("-------------------------------------------");
elif option1 == 3 and option2 == 1 and option3 == 1:
    print(f"Bien jugado {nom}, has acertado 1 pregunta y estuviste cerca en 2\nObtienes 20 puntos.");
    print("-------------------------------------------");
elif option1 == 1 and option2 == 3 and option3 == 1:
    print(f"Bien jugado {nom}, has acertado 1 pregunta y estuviste cerca en 2\nObtienes 20 puntos.");
    print("-------------------------------------------");
elif option1 == 1 and option2 == 1 and option3 == 3:
    print(f"Bien jugado {nom}, has acertado 1 pregunta y estuviste cerca en 2\nObtienes 20 puntos.");
    print("-------------------------------------------");
elif option1 == 1 and option2 == 1 and option3 == 1:
    print(f"Bien jugado {nom}, has fallado las 3 preguntas, pero estuviste cerca\nHas obtenido 15 puntos.");
    print("-------------------------------------------");
elif option1 == 3 and option2 == 1 and option3 == 2 or option3 == 4:
    print(f"Bien jugado {nom}, has acertado 1 y estuviste cerca en 2\nObtienes 15 puntos.");
    print("-------------------------------------------");
elif option1 == 2 or option1 == 4 and option2 == 3 and option3 == 1:
    print(f"Bien jugado {nom}, has acertado 1 y estuviste cerca en 2\nObtienes 15 puntos.");
    print("-------------------------------------------");
elif option1 == 1 and option2 == 2 or option2 == 4 and option3 == 3:
    print(f"Bien jugado {nom}, has acertado 1 y estuviste cerca en 2\nObtienes 15 puntos.");
    print("-------------------------------------------");
elif option1 == 3 and option2 == 2 and option3 == 4 or option3 == 1:
    print(f"Bien jugado {nom}, has acertado 1 y estuviste cerca en 2\nObtienes 15 puntos.");
    print("-------------------------------------------");
elif option1 == 2 or option1 == 4 and option2 == 1 and option3 == 3:
    print(f"Bien jugado {nom}, has acertado 1 y estuviste cerca en 2\nObtienes 15 puntos.");
    print("-------------------------------------------");
elif option1 == 1 and option2 == 3 and option3 == 2 or option3 == 4:
    print(f"Bien jugado {nom}, has acertado 1 y estuviste cerca en 2\nObtienes 15 puntos.");
    print("-------------------------------------------");
elif option1 == 3 and option2 == 2 or option2 == 4 and option3 == 2 or option3 == 4:
    print(f"Cerca del 0%, pero tuviste 1 buena\nObtienes 10 puntos.");
    print("-------------------------------------------");
elif option1 == 2 or option1 == 4 and option2 == 3 and option3 == 2 or option3 == 4:
    print(f"Cerca del 0%, pero tuviste 1 buena\nObtienes 10 puntos.");
    print("-------------------------------------------");
elif option1 == 2 or option1 == 4 and option2 == 2 or option2 == 4 and option3 == 3:
    print(f"Cerca del 0%, pero tuviste 1 buena\nObtienes 10 puntos.");
    print("-------------------------------------------");
elif option1 == 1 and option2 == 1 and option3 == 2 or option3 == 4:
    print (f"Cerca del 0%, pero estuviste cerca de 2 preguntas y fallaste 1\nPor lastima, obtienes 10 puntos.");
    print("-------------------------------------------");
elif option1 == 2 or option1 == 4 and option2 == 1 and option3 == 1:
    print (f"Cerca del 0%, pero estuviste cerca de 2 preguntas y fallaste 1\nPor lastima, obtienes 10 puntos.");
    print("-------------------------------------------");
elif option1 == 1 and option2 == 2 or option2 == 4 and option3 == 1:
    print (f"Cerca del 0%, pero estuviste cerca de 2 preguntas y fallaste 1\nPor lastima, obtienes 10 puntos.");
    print("-------------------------------------------");
elif option1 == 1 and option2 == 2 or option2 == 4 and option3 == 2 or option3 == 4:
    print(f"Estuviste cerca del 0% {nom}, has tenido 3 malas pero en 1 estuviste cerca\nPor lastima te daremos 5 puntos.");
    print("-------------------------------------------");
elif option1 == 2 or option1 == 4 and option2 == 1 and option3 == 2 or option3 == 4:
    print(f"Estuviste cerca del 0% {nom}, has tenido 3 malas pero en 1 estuviste cerca\nPor lastima te daremos 5 puntos.");
    print("-------------------------------------------");
elif option1 == 2 or option1 == 4 and option2 == 2 or option2 == 4 and option3 == 1:
    print(f"Estuviste cerca del 0% {nom}, has tenido 3 malas pero en 1 estuviste cerca\nPor lastima te daremos 5 puntos.");
    print("-------------------------------------------");
elif option1 == 2 or option1 == 4 and option2 == 2 or option2 == 4 and option3 == 2 or option3 == 4:
    print(f"¿Jugaste encerio?, has fallado las 3 preguntas, ni cerca estuviste\nObtienes 0 puntos.");
    print("-------------------------------------------");