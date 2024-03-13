'''Implementar una función que reciba el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres.
Utiliza el siguiente mapa:
    laberinto = """..###################
    ....#...............#
    #.#.#####.#########.#
    #.#...........#.#.#.#
    #.#####.#.###.#.#.#.#
    #...#.#.#.#.....#...#
    #.#.#.#######.#.#####
    #.#...#.....#.#...#.#
    #####.#####.#.#.###.#
    #.#.#.#.......#...#.#
    #.#.#.#######.#####.#
    #...#...#...#.#.#...#
    ###.#.#####.#.#.###.#
    #.#...#.......#.....#
    #.#.#.###.#.#.###.#.#
    #...#.#...#.#.....#.#
    ###.#######.###.###.#
    #.#.#.#.#.#...#.#...#
    #.#.#.#.#.#.#.#.#.#.#
    #.....#.....#.#.#.#.#
    ###################.."""
    Pasos a seguir.
    Los puntos inicial y final deben ser dados al crear el juego, usar las coordenadas (0,0) para el inicio y (len(mapa)-1, len(mapa[0])-1) para el final.
    
    Recuerdo: Para separar por filas usar split("\n") y para convertir una cadena a una lista de caracteres usar list(cadena).
    
    Escribir una función que limpie la pantalla y muestre la matriz (recibe el mapa en forma de matriz)

    Implementar el main loop en una función (recibe el mapa en forma de matriz)

    recibir: mapa List[List[str]], posicion inicial Tuple[int, int], posicion final Tuple[int, int].

    definir dos variavles px y py que contienen las coordenadas del jugador, iniciar como los valores de la posición incial
    procesar mientras (px, py) no coincida con la coordenada final.
    
    asignar el caracter P en el mapa a las coordenadas (px, py) en todo momento.
    
    leer del teclado las teclas de flechas, antes de actualizar la posición, verificar si esta posición tentativa:
    No se sale del mapa
    No es una pared
    Si la nueva posición es válida, actualizar (px, py), poner el caracter P en esta nueva coordenada y restaurar la anterior a .
    mostrar
'''

# Librerias
import os
from typing import List, Tuple
import readchar
from readchar import readkey, key


# Mapa que utilizaremos
laberinto = """..###################
    ....#...............#
    #.#.#####.#########.#
    #.#...........#.#.#.#
    #.#####.#.###.#.#.#.#
    #...#.#.#.#.....#...#
    #.#.#.#######.#.#####
    #.#...#.....#.#...#.#
    #####.#####.#.#.###.#
    #.#.#.#.......#...#.#
    #.#.#.#######.#####.#
    #...#...#...#.#.#...#
    ###.#.#####.#.#.###.#
    #.#...#.......#.....#
    #.#.#.###.#.#.###.#.#
    #...#.#...#.#.....#.#
    ###.#######.###.###.#
    #.#.#.#.#.#...#.#...#
    #.#.#.#.#.#.#.#.#.#.#
    #.....#.....#.#.#.#.#
    ###################.."""

print('Bienvenido al mapa del laberinto.')
name_user = input('Cual es tu nombre: ')
print(f'{name_user} El mapa esta por comenzar, ponte listo!.')
name_user = input('Presiona enter para comenzar ')

# Funciones
def convertir_a_matriz(laberinto):
    # Dividir el laberinto en filas
    filas = laberinto.split('\n    ')

    # Crear la matriz de caracteres
    matriz = [list(fila) for fila in filas]

    return matriz

mapa = convertir_a_matriz(laberinto)

# Punto inicial y final
punto_inicial = (0, 0)
punto_final = (len(mapa)-1, len(mapa[0])-1)

# Funcion que muestra el mapa
def mapa_visual(mapa):
    clear_terminal()
    for fila in mapa:
        print(''.join(fila))

# ocupamos limpiar la pantalla de la terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funcion main loop 
def main_loop(mapa: List[List[str]], punto_inicial: Tuple[int, int], punto_final: Tuple[int, int]):
    
    eje_x, eje_y = punto_inicial

    # mostar el mapa con la letra p 
    def mostrar_mapa():
        mapa[eje_x][eje_y] = 'P'
        mapa_visual(mapa)

    # funcion para mostrar mapa
    mostrar_mapa()

    # Bucle que ejecuta cuenta con las siguientes carcteristicas
    # 1. Se acaba solo cuando los valores de posicion del eje_x y eje_y son iguales cordenada final del mapa (punto_final)
    # 2. Captura la tecla presionada y si corresponde a las teclas ↑ ↓ ← → de tu teclado realiza un cambio de posicion de la letra 'P'
    while (eje_x, eje_y) != punto_final:

        # obtener el valor de tela presionada y guardarlo en la variable pressed_key.
        pressed_key = readchar.readkey()

        # variable para nuevas coordenadas con el ultomo valor de eje x y eje y
        nuevo_eje_x, nuevo_eje_y = eje_x, eje_y

        # Flujo de control para realizar actualizacion de la coordenada depediendo de la tecla presionada
        if pressed_key == key.UP and eje_x > 0 and mapa[eje_x - 1][eje_y] != '#':
            nuevo_eje_x -= 1
        elif pressed_key == key.DOWN and eje_x < len(mapa) - 1 and mapa[eje_x + 1][eje_y] != '#':
            nuevo_eje_x += 1
        elif pressed_key == key.LEFT and eje_y > 0 and mapa[eje_x][eje_y - 1] != '#':
            nuevo_eje_y -= 1
        elif pressed_key == key.RIGHT and eje_y < len(mapa[0]) - 1 and mapa[eje_x][eje_y + 1] != '#':
            nuevo_eje_y += 1

        # Restaura la posición anterior a '.'
        mapa[eje_x][eje_y] = '.'
        eje_x, eje_y = nuevo_eje_x, nuevo_eje_y

        # Mostrar nuevamente con la nueva posicion de la letra 'p'
        mostrar_mapa()

# Llama a la función principal con el mapa y los puntos iniciales y finales para inicializar el juego.
main_loop(mapa, punto_inicial, punto_final)

print(f'{name_user} Enhorabuena! Completaste el mapa.')
