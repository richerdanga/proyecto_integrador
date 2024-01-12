import os
from typing import List, Tuple
from readchar import readkey, key

def convertir_mapa_a_matriz(laberinto: str) -> List[List[str]]:
    return [list(fila) for fila in laberinto.split("\n")]
    

def mostrar_mapa(mapa: List[List[str]]):
     os.system('cls' if os.name == 'nt' else 'clear')
     for fila in mapa:
         print(''.join(fila))

def main_loop(mapa: List[List[str]], inicio: Tuple[int, int], final: Tuple[int, int]):
    px, py = inicio
    mapa[px][py] = 'P'

    while (px, py) != final:
        mostrar_mapa(mapa)
        movimiento=readkey()
        nueva_px, nueva_py = px, py
        if movimiento == key.UP:
            nueva_px -= 1
        elif movimiento == key.DOWN:
            nueva_px += 1
        elif movimiento == key.LEFT:
            nueva_py -= 1
        elif movimiento == key.RIGHT:
            nueva_py += 1
        if(0 <= nueva_px < len(mapa) and 0 <= nueva_py < len(mapa[0]) and mapa[nueva_px][nueva_py] != '#'):
            mapa[px][py] = '.'    #  restaura la posicion del jugador
            px, py = nueva_px, nueva_py   # Actualiza la posicion
            mapa[px][py] = 'P'
print("Llegaste al final :", end='')      
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

mapa=convertir_mapa_a_matriz(laberinto)  
inicio=(0,0)
fin=((len(mapa)-1, len(mapa[0])-1)) 

main_loop(mapa,inicio,fin)
   