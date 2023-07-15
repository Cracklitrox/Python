edad=int(input("Ingrese su edad: "));
if edad >= 18:
    print(f"Su edad es: {edad}\nUsted es mayor de edad");
elif edad <= 0:
    print(f"Su edad es: {edad}\nIngrese un valor valido");
else:
    print(f"Su edad es: {edad}\nUsted es menor de edad");