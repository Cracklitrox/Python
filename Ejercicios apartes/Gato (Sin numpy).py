from calendar import c
from concurrent.futures import BrokenExecutor
from doctest import BLANKLINE_MARKER
import random
cont=0;
cont1=0;
cont2=0;
while True:
    z=0;
    turno=1;
    tablero=['1', '2', '3', '4', '5', '6', '7', '8', '9'];
    jugadas_jugador=[];
    jugadas_maquina=[];
    print("----------------------");
    print("       Juego Duoc     ");
    print("----------------------\n\n");
    print("(1) Jugar contra PC\n(2) Ver marcadores\n(3) Salir\n");
    try:
        op=int(input("Seleccione una opción: "));
        print();
        if op == 1:
            print("Bueno, se le mostrara el tablero a continuación\n");
            while True:
                print(".....................\n");
                print(" "*4,f" {tablero[0]} | {tablero[1]} | {tablero[2]} ");
                print(" "*4,"---+---+---");
                print(" "*4,f" {tablero[3]} | {tablero[4]} | {tablero[5]} ");
                print(" "*4,"---+---+---");
                print(" "*4,f" {tablero[6]} | {tablero[7]} | {tablero[8]} ");
                print("");
                print(".....................\n");
                try:
                    if turno == 1 or turno == 3 or turno == 5 or turno == 7:
                        seleccion=int(input("Seleccione un numero (1-9): "));
                        print();
                        if seleccion >= 1 and seleccion <= 9:
                            a=seleccion-1
                            if jugadas_maquina.count(a) or a in jugadas_jugador:
                                print("Ya esta ocupado por el rival¡¡\n");
                            else:
                                tablero.pop(a);
                                jugadas_jugador.append(a);
                                tablero.insert(a,'X');
                                turno+=1
                                if len(jugadas_jugador) >= 3:
                                    if (0 in jugadas_jugador and 1 in jugadas_jugador and 2 in jugadas_jugador) or (3 in jugadas_jugador and 4 in jugadas_jugador and 5 in jugadas_jugador) or (6 in jugadas_jugador and 7 in jugadas_jugador and 8 in jugadas_jugador) or (0 in jugadas_jugador and 3 in jugadas_jugador and 6 in jugadas_jugador) or (1 in jugadas_jugador and 4 in jugadas_jugador and 7 in jugadas_jugador) or (2 in jugadas_jugador and 5 in jugadas_jugador and 8 in jugadas_jugador) or (0 in jugadas_jugador and 4 in jugadas_jugador and 8 in jugadas_jugador) or (6 in jugadas_jugador and 4 in jugadas_jugador and 2 in jugadas_jugador):
                                        print(".....................\n");
                                        print(" "*4,f" {tablero[0]} | {tablero[1]} | {tablero[2]} ");
                                        print(" "*4,"---+---+---");
                                        print(" "*4,f" {tablero[3]} | {tablero[4]} | {tablero[5]} ");
                                        print(" "*4,"---+---+---");
                                        print(" "*4,f" {tablero[6]} | {tablero[7]} | {tablero[8]} ");
                                        print("");
                                        print(".....................\n");
                                        print("Ganaste.\n\n");
                                        cont+=1
                                        break
                        else:
                            print(f"El numero: '{seleccion}' no es valido dentro del tablero, intentelo nuevamente.\n\n");
                    elif turno == 2 or turno == 4 or turno == 6 or turno == 8:
                        for x in range(100):
                            jugadas_maquina.append(random.randrange(0,9));
                            if jugadas_jugador.count(jugadas_maquina[z]):
                                jugadas_maquina.pop();
                            else:
                                break
                        if  jugadas_maquina.count(jugadas_maquina[z]) >= 2:
                            jugadas_maquina.pop();
                        else:
                            tablero.pop(jugadas_maquina[z]);
                            tablero.insert(jugadas_maquina[z],'O');
                            turno+=1
                            z+=1
                            if len(jugadas_maquina) >= 3:
                                if (0 in jugadas_maquina and 1 in jugadas_maquina and 2 in jugadas_maquina) or (3 in jugadas_maquina and 4 in jugadas_maquina and 5 in jugadas_maquina) or (6 in jugadas_maquina and 7 in jugadas_maquina and 8 in jugadas_maquina) or (0 in jugadas_maquina and 3 in jugadas_maquina and 6 in jugadas_maquina) or (1 in jugadas_maquina and 4 in jugadas_maquina and 7 in jugadas_maquina) or (2 in jugadas_maquina and 5 in jugadas_maquina and 8 in jugadas_maquina) or (0 in jugadas_maquina and 4 in jugadas_maquina and 8 in jugadas_maquina) or (6 in jugadas_maquina and 4 in jugadas_maquina and 2 in jugadas_maquina):
                                    print(".....................\n");
                                    print(" "*4,f" {tablero[0]} | {tablero[1]} | {tablero[2]} ");
                                    print(" "*4,"---+---+---");
                                    print(" "*4,f" {tablero[3]} | {tablero[4]} | {tablero[5]} ");
                                    print(" "*4,"---+---+---");
                                    print(" "*4,f" {tablero[6]} | {tablero[7]} | {tablero[8]} ");
                                    print("");
                                    print(".....................\n");
                                    print("Perdiste, te gano la consola .-.\n\n");
                                    cont1+=1
                                    break
                    elif turno == 9:
                        seleccion=int(input("Seleccione un numero (1-9): "));
                        print();
                        if seleccion >= 1 and seleccion <= 9:
                            a=seleccion-1
                            if jugadas_maquina.count(a) or a in jugadas_jugador:
                                break
                            else:
                                tablero.pop(a);
                                jugadas_jugador.append(a);
                                tablero.insert(a,'X');
                                if len(jugadas_jugador) >= 3:
                                    if (0 in jugadas_jugador and 1 in jugadas_jugador and 2 in jugadas_jugador) or (3 in jugadas_jugador and 4 in jugadas_jugador and 5 in jugadas_jugador) or (6 in jugadas_jugador and 7 in jugadas_jugador and 8 in jugadas_jugador) or (0 in jugadas_jugador and 3 in jugadas_jugador and 6 in jugadas_jugador) or (1 in jugadas_jugador and 4 in jugadas_jugador and 7 in jugadas_jugador) or (2 in jugadas_jugador and 5 in jugadas_jugador and 8 in jugadas_jugador) or (0 in jugadas_jugador and 4 in jugadas_jugador and 8 in jugadas_jugador) or (6 in jugadas_jugador and 4 in jugadas_jugador and 2 in jugadas_jugador):
                                        print(".....................\n");
                                        print(" "*4,f" {tablero[0]} | {tablero[1]} | {tablero[2]} ");
                                        print(" "*4,"---+---+---");
                                        print(" "*4,f" {tablero[3]} | {tablero[4]} | {tablero[5]} ");
                                        print(" "*4,"---+---+---");
                                        print(" "*4,f" {tablero[6]} | {tablero[7]} | {tablero[8]} ");
                                        print("");
                                        print(".....................\n");
                                        print("Ganaste.\n\n");
                                        cont+=1
                                        break
                                print(".....................\n");
                                print(" "*4,f" {tablero[0]} | {tablero[1]} | {tablero[2]} ");
                                print(" "*4,"---+---+---");
                                print(" "*4,f" {tablero[3]} | {tablero[4]} | {tablero[5]} ");
                                print(" "*4,"---+---+---");
                                print(" "*4,f" {tablero[6]} | {tablero[7]} | {tablero[8]} ");
                                print("");
                                print(".....................\n");
                                print("Empate");
                                cont2+=1
                                break
                        else:
                            print(f"El numero: '{seleccion}' no es valido dentro del tablero, intentelo nuevamente.\n\n");
                except ValueError:
                    print("Solo digite numeros.\n\n");
        elif op == 2:
            print(f"     Tabla de puntuación    \n----------------------------------\n\nVeces ganadas por el jugador:\t{cont}\n\nVeces ganadas por la consola:\t{cont1}\n\nVeces empatadas:\t{cont2}\n----------------------------------\n\n");
        elif op == 3:
            print("Bueno, cerrando juego.");
            break
        else:
            print("Lo digitado no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");
    except ValueError:
        print(f"Lo digitado: '{op}' no es valido dentro del sistema, por favor, intentelo nuevamente.\n\n");