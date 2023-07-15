def resta(a,b):
    return a - b
print(f"El primer resultado de la actividad es:\t{resta(30,10)}\n");
print(f"El segundo resultado de la actividad es:\t{resta(b=30,a=10)}\n");

def funcion():
    return 'Bienvenidos a Python'
frase=funcion();
print(frase)
print();

def resta1(c=None,d=None):
    if c == None or d == None:
        print("Error, falta parámetros a la función\n");
        return
    return c - d
print(f"La operación:\t{resta1()}\n");

def calculo(precio, descuento):
    print(precio)
    print(descuento)
    return precio - (precio * descuento / 100)
datos=[10000,10];
print(f"El monto final a pagar es:\t{calculo(*datos)}\n");

# Preguntar para que sirve el '*' en '*datos'

def saludo(nombre, mensaje='Python'):
    print(mensaje, nombre);
    # El mensaje es remplazado por 'Buen dia' y el nombre ya que estaba vacio ahora es 'Pedro'
saludo(mensaje='Buen dia', nombre='Pedro');