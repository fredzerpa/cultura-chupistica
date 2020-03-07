def menu():
    opcion_valida = False
    while not opcion_valida:
        print("Bienvenido a Cultura Chupistica")
        print()
        print("Por favor escoja una opcion")
        print("1. Comenzar partida.")
        print("2. Reglas")
        print("3. Salir del Juego.")
        opcion_seleccionada = int(input("Opcion: "))
        if opcion_seleccionada == 1:
            opcion_valida = True
        elif opcion_seleccionada == 2:
            print()
            reglas()
            print()
        elif opcion_seleccionada == 3:
            exit() # Finalizar Programa
        else:
            print("\"Escoja una opcion valida\"")


def reglas():
    print("Reglas del Juego:")
    print("    1. En cada turno debe escribirse las palabras ya usadas en los turnos anteriores y una palabra nueva.")
    print("    2. No se puede añadir mas de una palabra por turno.")
    print("    3. No pueden repetirse las palabras en una misma partida.")
    print("    4. Deben escribirse todas las palabras separadas por un espacio \" \".")
    input("Presione ENTER para continuar")

while True: # La funcion exit() termina el programa
    print()
    menu()
    lista_palabras_usadas = []
    contador_de_turnos = 0

    salir_partida = False
    while not salir_partida:

        contador_de_turnos += 1
        palabras_en_string = input(f"Turno {contador_de_turnos}: ")
        palabras_en_list = palabras_en_string.split(" ") # Crea una lista con las palabras usadas

        # Misma cantidad de palabras ya usadas mas la nueva palabra
        if len(palabras_en_list) == len(lista_palabras_usadas) + 1:

            # Si no es el primer turno
            if contador_de_turnos > 1:

                # La palabra no sea repetida
                es_repetida = False
                for palabra in lista_palabras_usadas:

                    # Chequear palabra por palabra de las palabras ya usadas
                    if palabras_en_list[-1] == palabra:
                        es_repetida = True

                # Verificar si la palabra ya existe
                if es_repetida:
                    salir_partida = True
                else:
                    lista_palabras_usadas.append(palabras_en_list[-1])

            else: # Si es el primer turno
                lista_palabras_usadas.append(palabras_en_list[-1])

            # Guia para revisar como continua el juego
            # Comenta las siguientes 2 lineas para jugar sin la guia
            print(f"Palabras escritas: {palabras_en_list}")
            print(f"Palabras Usadas: {lista_palabras_usadas}")

            # Las palabras sean las mismas y en orden
            for i in range(contador_de_turnos):
                if not palabras_en_list[i] == lista_palabras_usadas[i]:
                    print("Has perdido!")
                    print("El orden estuvo mal.")
                    salir_partida = True
                    break

        else:
            if len(palabras_en_list) < len(lista_palabras_usadas) + 1:
                print("Has perdido!")
                print(f"Han faltado {(len(lista_palabras_usadas) + 1) - len(palabras_en_list)} palabra's.")
                salir_partida = True
                input("Presione ENTER para continuar")

            else:
                print("Has perdido!")
                print(f"Te pasaste con mas de {len(palabras_en_list) - (len(lista_palabras_usadas) + 1)} palabra's.")
                salir_partida = True
                input("Presione ENTER para continuar")