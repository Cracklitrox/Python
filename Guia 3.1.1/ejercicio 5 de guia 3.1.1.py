i=0;
multi=0;
x=range(1,11,1);
for n in x:
    i=i+1;
    print("");
    print(f"La tabla de {i}");
    print("");
    for z in x:
        tabla=i;
        resultado=i*z;
        print(f"La tabla de {i} * {tabla} es: {resultado}");