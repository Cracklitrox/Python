from concurrent.futures import BrokenExecutor
import numpy as np
matriz=np.full((4,4),' ');
for x in range(4):
    for z in range(4):
        matriz[x][z]=' ';
cont=0;
cont1=0;
cont2=0;
cont3=0;
cont_vocales=0;
while True:
    try:
        caracter=input("Ingrese un caracter (sin numeros): ");
        if caracter.isalpha() == True and len(caracter) == 1:
            for x in range(1):
                for z in range(4):
                    if matriz[0][3] != ' ' and matriz[1][3] == ' ' and matriz[2][3] == ' ' and matriz[3][3] == ' ':
                        matriz[1][z+cont1]=caracter
                        cont1+=1
                        break
                    elif matriz[0][3] != ' ' and matriz[1][3] != ' ' and matriz[2][3] == ' ' and matriz[3][3] == ' ':
                        matriz[2][z+cont2]=caracter
                        cont2+=1
                        break
                    elif matriz[0][3] != ' ' and matriz[1][3] != ' ' and matriz[2][3] != ' ' and matriz[3][3] == ' ':
                        matriz[3][z+cont3]=caracter
                        cont3+=1
                        break
                    else:
                        matriz[x][z+cont]=caracter
                        cont+=1
                        break
            if cont == 4 and cont1 == 4 and cont2 == 4 and cont3 == 4:
                for x in range(4):
                    for z in range(4):
                        if matriz[x][z] == 'a' or matriz[x][z] == 'A' or matriz[x][z] == 'e' or matriz[x][z] == 'E' or matriz[x][z] == 'i' or matriz[x][z] == 'I' or matriz[x][z] == 'o' or matriz[x][z] == 'O' or matriz[x][z] == 'u' or matriz[x][z] == 'U':
                            cont_vocales+=1
                        else:
                            continue
                print();
                break
            else:
                print();
                continue
        else:
            print(f"Lo digitado: '{caracter}' no es valido, solo escriba un caracter sin numeros.");
    except ValueError:
        print("nada")
print(f"La cantidad total de vocales en la matriz son:\t{cont_vocales}\n");