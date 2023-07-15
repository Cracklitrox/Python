import random
import numpy as np
cont=0;
cont1=0;
cont2=0;
cont_jugador_1=0;
cont_jugador_2=0;
cont_jugador_empate=0;
cont_jugadores=0;
while True:
    turn=1;
    print("----------------------");
    print("       Juego Duoc     ");
    print("----------------------\n\n");
    print("(1) Jugar contra PC\n(2) Jugar contra otro jugador\n(3) Ver marcadores\n(4) Salir\n");
    try:
        op=int(input("Seleccione una opción: "));
        print();
        if op == 1:
            jugadas=np.full(9,' ');
            while True:
                print(".......................\n");
                print(" "*4,f" {jugadas[0]}  | {jugadas[1]}  | {jugadas[2]} ");
                print(" "*4,"----+----+----");
                print(" "*4,f" {jugadas[3]}  | {jugadas[4]}  | {jugadas[5]} ");
                print(" "*4,"----+----+----");
                print(" "*4,f" {jugadas[6]}  | {jugadas[7]}  | {jugadas[8]} ");
                print("");
                print(".......................\n");
                try:
                    if (jugadas[0] == 'X' and jugadas[1] == 'X' and jugadas[2] == 'X') or (jugadas[3] == 'X' and jugadas[4] == 'X' and jugadas[5] == 'X') or (jugadas[6] == 'X' and jugadas[7] == 'X' and jugadas[8] == 'X') or (jugadas[0] == 'X' and jugadas[3] == 'X' and jugadas[6] == 'X') or (jugadas[1] == 'X' and jugadas[4] == 'X' and jugadas[7] == 'X') or (jugadas[2] == 'X' and jugadas[5] == 'X' and jugadas[8] == 'X') or (jugadas[0] == 'X' and jugadas[4] == 'X' and jugadas[8] == 'X') or (jugadas[2] == 'X' and jugadas[4] == 'X' and jugadas[6] == 'X'):
                        print("ganaste\n\n");
                        cont+=1
                        break
                    elif (jugadas[0] == 'O' and jugadas[1] == 'O' and jugadas[2] == 'O') or (jugadas[3] == 'O' and jugadas[4] == 'O' and jugadas[5] == 'O') or (jugadas[6] == 'O' and jugadas[7] == 'O' and jugadas[8] == 'O') or (jugadas[0] == 'O' and jugadas[3] == 'O' and jugadas[6] == 'O') or (jugadas[1] == 'O' and jugadas[4] == 'O' and jugadas[7] == 'O') or (jugadas[2] == 'O' and jugadas[5] == 'O' and jugadas[8] == 'O') or (jugadas[0] == 'O' and jugadas[4] == 'O' and jugadas[8] == 'O') or (jugadas[2] == 'O' and jugadas[4] == 'O' and jugadas[6] == 'O'):
                        print("perdiste\n\n")
                        cont1+=1
                        break
                    else:
                        if turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9:
                            print("Turno del jugador X\n");
                            selecccion=int(input("Seleccione un numero (1-9): "));
                            print();
                            if selecccion >= 1 and selecccion <= 9:
                                if jugadas[selecccion-1] == 'O' or jugadas[selecccion-1] == 'X':
                                    print("repetido");
                                else:
                                    jugadas[selecccion-1]='X';
                                    turn+=1
                            else:
                                print(f"El número ingresado: '{selecccion}' no es valido dentro del rango, intentelo nuevamente.\n");
                        elif turn == 2 or turn == 4 or turn == 6 or turn == 8:
                            print("Turno de la consola O\n");
                            for x in range(100):
                                aleatorio=random.randrange(0,9);
                                if jugadas[aleatorio] == 'X' or jugadas[aleatorio] == 'O':
                                    continue
                                elif jugadas[aleatorio] == ' ':
                                    jugadas[aleatorio]='O'
                                    break
                            turn+=1;
                        elif turn == 10:
                            print("Empate\n\n");
                            cont2+=1
                            break
                except ValueError:
                    print("Digite solo numeros.\n");
        elif op == 2:
            while True:
                salir=input("¿Desea jugar de verdad?: ");
                print();
                if salir == 'Si' or salir == 'SI' or salir == 'si' or salir == 'OK' or salir == 'ok' or salir == 'Ok':
                    jugador1=input("Ingrese el nombre del primer jugador: ");
                    print();
                    jugador2=input("Ingrese el nombre del segundo jugador: ");
                    print();
                    if len(jugador1) <= 3 or len(jugador2) <= 3:
                        print("Ingrese al menos 3 caracteres en su nombre de juego.\n");
                    else:
                        if random.randint(0,100) % 2 == 0:
                            print(f"Empezara el jugador:\t'{jugador2}'\n");
                            print(f"El jugador:\t'{jugador2}' tendra asignado 'X'\nEl jugador:\t'{jugador1}' tendra asignado 'O'\n");
                            jugadas=np.full(9,' ');
                            while True:
                                print(".......................\n");
                                print(" "*4,f" {jugadas[0]}  | {jugadas[1]}  | {jugadas[2]} ");
                                print(" "*4,"----+----+----");
                                print(" "*4,f" {jugadas[3]}  | {jugadas[4]}  | {jugadas[5]} ");
                                print(" "*4,"----+----+----");
                                print(" "*4,f" {jugadas[6]}  | {jugadas[7]}  | {jugadas[8]} ");
                                print("");
                                print(".......................\n");
                                try:
                                    if (jugadas[0] == 'X' and jugadas[1] == 'X' and jugadas[2] == 'X') or (jugadas[3] == 'X' and jugadas[4] == 'X' and jugadas[5] == 'X') or (jugadas[6] == 'X' and jugadas[7] == 'X' and jugadas[8] == 'X') or (jugadas[0] == 'X' and jugadas[3] == 'X' and jugadas[6] == 'X') or (jugadas[1] == 'X' and jugadas[4] == 'X' and jugadas[7] == 'X') or (jugadas[2] == 'X' and jugadas[5] == 'X' and jugadas[8] == 'X') or (jugadas[0] == 'X' and jugadas[4] == 'X' and jugadas[8] == 'X') or (jugadas[2] == 'X' and jugadas[4] == 'X' and jugadas[6] == 'X'):
                                        print(f"gano el jugador:\t'{jugador2}'\n\n");
                                        cont_jugador_2+=1
                                        cont_jugadores+=1
                                        break
                                    elif (jugadas[0] == 'O' and jugadas[1] == 'O' and jugadas[2] == 'O') or (jugadas[3] == 'O' and jugadas[4] == 'O' and jugadas[5] == 'O') or (jugadas[6] == 'O' and jugadas[7] == 'O' and jugadas[8] == 'O') or (jugadas[0] == 'O' and jugadas[3] == 'O' and jugadas[6] == 'O') or (jugadas[1] == 'O' and jugadas[4] == 'O' and jugadas[7] == 'O') or (jugadas[2] == 'O' and jugadas[5] == 'O' and jugadas[8] == 'O') or (jugadas[0] == 'O' and jugadas[4] == 'O' and jugadas[8] == 'O') or (jugadas[2] == 'O' and jugadas[4] == 'O' and jugadas[6] == 'O'):
                                        print(f"gano el jugador:\t'{jugador1}'\n\n");
                                        cont_jugador_1+=1
                                        cont_jugadores+=1
                                        break
                                    else:
                                        if turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9:
                                            print("Turno del jugador 'X'\n");
                                            selecccion=int(input("Seleccione un numero (1-9): "));
                                            print();
                                            if selecccion >= 1 and selecccion <= 9:
                                                if jugadas[selecccion-1] == 'O' or jugadas[selecccion-1] == 'X':
                                                    print("repetido");
                                                else:
                                                    jugadas[selecccion-1]='X';
                                                    turn+=1
                                            else:
                                                print(f"El número ingresado: '{selecccion}' no es valido dentro del rango, intentelo nuevamente.\n");
                                        elif turn == 2 or turn == 4 or turn == 6 or turn == 8:
                                            print("Turno del jugador 'O'\n");
                                            selecccion=int(input("Seleccione un numero (1-9): "));
                                            print();
                                            if selecccion >= 1 and selecccion <= 9:
                                                if jugadas[selecccion-1] == 'O' or jugadas[selecccion-1] == 'X':
                                                    print("repetido");
                                                else:
                                                    jugadas[selecccion-1]='O';
                                                    turn+=1
                                            else:
                                                print(f"El número ingresado: '{selecccion}' no es valido dentro del rango, intentelo nuevamente.\n");
                                        elif turn == 10:
                                            print("Empate\n\n");
                                            cont_jugador_empate+=1
                                            cont_jugadores+=1
                                            break
                                except ValueError:
                                    print("Digite solo numeros.\n");
                        else:
                            print(f"Empezara el jugador:\t'{jugador1}'\n");
                            print(f"El jugador:\t'{jugador1}' tendra asignado 'X'\nEl jugador:\t'{jugador2}' tendra asignado 'O'\n");
                            jugadas=np.full(9,' ');
                            while True:
                                print(".......................\n");
                                print(" "*4,f" {jugadas[0]}  | {jugadas[1]}  | {jugadas[2]} ");
                                print(" "*4,"----+----+----");
                                print(" "*4,f" {jugadas[3]}  | {jugadas[4]}  | {jugadas[5]} ");
                                print(" "*4,"----+----+----");
                                print(" "*4,f" {jugadas[6]}  | {jugadas[7]}  | {jugadas[8]} ");
                                print("");
                                print(".......................\n");
                                try:
                                    if (jugadas[0] == 'X' and jugadas[1] == 'X' and jugadas[2] == 'X') or (jugadas[3] == 'X' and jugadas[4] == 'X' and jugadas[5] == 'X') or (jugadas[6] == 'X' and jugadas[7] == 'X' and jugadas[8] == 'X') or (jugadas[0] == 'X' and jugadas[3] == 'X' and jugadas[6] == 'X') or (jugadas[1] == 'X' and jugadas[4] == 'X' and jugadas[7] == 'X') or (jugadas[2] == 'X' and jugadas[5] == 'X' and jugadas[8] == 'X') or (jugadas[0] == 'X' and jugadas[4] == 'X' and jugadas[8] == 'X') or (jugadas[2] == 'X' and jugadas[4] == 'X' and jugadas[6] == 'X'):
                                        print(f"gano el jugador:\t'{jugador1}'\n\n");
                                        cont_jugador_1+=1
                                        cont_jugadores+=1
                                        break
                                    elif (jugadas[0] == 'O' and jugadas[1] == 'O' and jugadas[2] == 'O') or (jugadas[3] == 'O' and jugadas[4] == 'O' and jugadas[5] == 'O') or (jugadas[6] == 'O' and jugadas[7] == 'O' and jugadas[8] == 'O') or (jugadas[0] == 'O' and jugadas[3] == 'O' and jugadas[6] == 'O') or (jugadas[1] == 'O' and jugadas[4] == 'O' and jugadas[7] == 'O') or (jugadas[2] == 'O' and jugadas[5] == 'O' and jugadas[8] == 'O') or (jugadas[0] == 'O' and jugadas[4] == 'O' and jugadas[8] == 'O') or (jugadas[2] == 'O' and jugadas[4] == 'O' and jugadas[6] == 'O'):
                                        print(f"gano el jugador:\t'{jugador2}'\n\n");
                                        cont_jugador_2+=1
                                        cont_jugadores+=1
                                        break
                                    else:
                                        if turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9:
                                            print("Turno del jugador 'X'\n");
                                            selecccion=int(input("Seleccione un numero (1-9): "));
                                            print();
                                            if selecccion >= 1 and selecccion <= 9:
                                                if jugadas[selecccion-1] == 'O' or jugadas[selecccion-1] == 'X':
                                                    print("repetido");
                                                else:
                                                    jugadas[selecccion-1]='X';
                                                    turn+=1
                                            else:
                                                print(f"El número ingresado: '{selecccion}' no es valido dentro del rango, intentelo nuevamente.\n");
                                        elif turn == 2 or turn == 4 or turn == 6 or turn == 8:
                                            print("Turno del jugador 'O'\n");
                                            selecccion=int(input("Seleccione un numero (1-9): "));
                                            print();
                                            if selecccion >= 1 and selecccion <= 9:
                                                if jugadas[selecccion-1] == 'O' or jugadas[selecccion-1] == 'X':
                                                    print("repetido");
                                                else:
                                                    jugadas[selecccion-1]='O';
                                                    turn+=1
                                            else:
                                                print(f"El número ingresado: '{selecccion}' no es valido dentro del rango, intentelo nuevamente.\n");
                                        elif turn == 10:
                                            print("Empate\n\n");
                                            cont_jugador_empate+=1
                                            cont_jugadores+=1
                                            break
                                except ValueError:
                                    print("Digite solo numeros.\n");
                else:
                    print("Volviendo al menu de inicio.\n");
                    break
        elif op == 3:
            while True:
                print("     Tabla de puntuaciones     \n");
                print("."*35);
                print();
                print("(1) Marcadores contra PC\n(2) Marcadores 1 vs 1\n(3) Salir\n");
                print("."*35);
                print();
                try:
                    op1=int(input("Seleccione una opción: "));
                    print();
                    if op1 == 1:
                        print("     Tabla de puntuaciones contra la consola     \n");
                        print("."*55);
                        print();
                        print(f"Veces ganadas por el jugador:\t{cont}\nVeces ganadas por la consola:\t{cont1}\nVeces empatadas:\t{cont2}\n");
                        print("."*55);
                        print();
                    elif op1 == 2:
                        if cont_jugadores == 0:
                            print("Aun no ha jugado un 1 vs 1 contra otro jugador, intentalo y se desbloqueara el marcador.\n");
                        else:
                            print("     Tabla de puntuaciones 1 vs 1     \n");
                            print("."*40);
                            print();
                            print(f"Veces ganadas por el jugador '{jugador1}':\t{cont_jugador_1}\nVeces ganadas por el jugador '{jugador2}':\t{cont_jugador_2}\nVeces empatas:\t{cont_jugador_empate}\n");
                            print("."*40);
                            print();
                    elif op1 == 3:
                        print("Volviendo al menu de inicio.\n");
                        break
                    else:
                        print(f"La opcion ingresada:\t'{op1}' no es valido, use solo lo que esta en el rango disponible (1-3).\n\n");
                except ValueError:
                    print("Solo digite numeros\n\n");
        elif op == 4:
            print("Cerrando juego");
            break
        else:
            print(f"La opcion ingresada: '{op}' no es valido dentro del sistema, intentelo nuevamente.\n");
    except ValueError:
        print("Digite solo numeros.\n");