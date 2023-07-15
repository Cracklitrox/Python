
# Funcion sin argumentos y sin retorno, solo se muestra el mensaje si se llama la funcion

import re


def saludos():
    print("Saludando a mis estudiantes");
print();
saludos();
print();

# Funcion sin argumentos y con retorno, solo se muestra el mensaje si se llama la funcion, funciona en un print o cadena.

def saludo():
    return("Buenas tardes");
print(f"\nQue tal alumnos, {saludo()}\n");

# Funcion sin argumentos y con retorno, solo se muestra el mensaje de la suma si se llama a la funcion, funciona en un print o cadena.

def sumar():
    num1 = 3
    num2 = 5
    return(num1+num2);
print(f"\nLa suma es:\t{sumar()}\n");

# Funcion con argumentos y sin retorno, se define las variables y el mensaje final dentro de la funcion, fuera de la funcion se pide los elementos que seran las variables, para despues llamar a la funcion remplazando la variable 'a' por 'num1' y la variable 'b' por 'num2', de esta forma, se realiza la funcion y nos mostrara el mensaje final, el cual, es la suma de ambos elementos

def sumas(a,b):
    suma=a+b
    print(f"La suma de los argumentos es:\t{suma}\n");
num1=int(input("Ingrese primer numero:\t"));
print();
num2=int(input("Ingrese segundo numero:\t"));
print();
sumas(num1,num2)

# Funcion con argumentos y con retorno, se define las variables y la operacion, fuera de la funcion se pide los elementos de las variables, para despues imprimir el resultado pero llamando a la funcion dentro del print, siendo que, la variable 'c' es remplazado por 'num3' y la variable 'd' por 'num4', de esta forma, se llama a la funcion, realiza la operacion y muestra el resultado.

def resta(c,d):
    total=c-d
    return(total);
num3=int(input("Ingrese primer numero:\t"));
print();
num4=int(input("Ingrese segundo numero:\t"));
print();
print(f"El resultado de la resta es:\t{resta(num3,num4)}\n");

# Invertir las variables y generar un resultado diferente, solo definiendo que la variable 'c' es ahora 'num4' y la variable 'd' es 'num3', seguira haciendo la misma operación por que la funcion resta la seguimos llamando, mostrando el resultado final.

print(f"El resultado de la resta es:\t{resta(c=num4,d=num3)}\n");

# Para evitar un error cuando falte o se equivoque el ingreso de valores, usar un while cuando se pida los numeros

def paramentros(e = None, f = None):
    multiplicacion=e*f
    return(multiplicacion);
while True:
    try:
        num5=int(input("Ingrese primer numero:\t"));
        print();
        num6=int(input("Ingrese segundo numero:\t"));
        print();
        print(f"El resultado de la multiplicación es:\t{paramentros(num5,num6)}\n");
        break
    except ValueError:
        print("\nDigite solo numeros\n");

#  Funcion para varios valores, el '*args' representa que recibe una lista dinámica de argumentos, eso significa que solo cadenas, numeros o booleanos, se llama en resumen: Recibir parametros indeterminados por posición.

def varios_valores(*args):
    # Aca se muestran los elementos que ingresamos, de forma decendente y total.
    for x in args:
        print(x);
varios_valores(999,9.31,'q tal',[1,2,3,4,5,5,6,]);
print();

# Funcion para mostrar valores, la unica diferencia es que no recibe parametros, pero si los retorna, en resumen se llama: Retorno Multiple

def mostrar_valores():
    return(999,9.31,'q tal',[1,2,3,4,5,5,6,]);
print(f"Los valores son los siguientes:\t{mostrar_valores()}\n");