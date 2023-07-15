print("-----------------------------------------------------------");
print("         |Empresa XY|          ");
nom=input("Ingrese su usuario: ");
con=str(input("Ingrese su contraseña: "));
print("");
if nom == 'pedro' or nom == 'Pedro' and con == '1234':
    print(f"Bienvenido {nom}");
elif nom == 'angel' and con == 'a4s1':
    print(f"Bienvenido {nom}");
else:
    print("Se ha equivocado en el usuario o contraseña, intente nuevamente.");
print("-----------------------------------------------------------");