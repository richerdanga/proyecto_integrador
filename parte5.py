import os
import random
from typing import List, Tuple
from readchar import readkey, key

class Juego:
    def __init__(self, mapa: List[List[str]], inicio: Tuple[int, int], fin: Tuple[int, int]):
        self.mapa= mapa
        self.inicio= inicio
        self.fin = fin
    
    def convertir_mapa_a_matriz(laberinto: str) -> List[List[str]]:
        return [list(fila) for fila in laberinto.split("\n")]
    
    def mostrar_mapa(mapa: List[List[str]]):
     os.system('cls' if os.name == 'nt' else 'clear')
     for fila in mapa:
         print(''.join(fila))
    
    def main_loop(self):
       px, py = self.inicio
       self.mapa[px][py] = 'P'

       while (px, py) != self.fin:
            self.mostrar_mapa()
            movimiento = readkey()

            nueva_px, nueva_py = px, py
            if movimiento == key.UP:
                nueva_px -= 1
            elif movimiento == key.DOWN:
                nueva_px += 1
            elif movimiento == key.LEFT:
                nueva_py -= 1
            elif movimiento == key.RIGHT:
                nueva_py += 1

            if 0 <= nueva_px < len(self.mapa) and 0 <= nueva_py < len(self.mapa[0]) and self.mapa[nueva_px][nueva_py] != '#':
                self.mapa[px][py] = '.'
                px, py = nueva_px, nueva_py
                self.mapa[px][py] = 'P'

class JuegoArchivo(Juego):
    
    def __init__(self, path_a_mapas: str):
       
        archivo_mapa = self.elegir_mapa_aleatorio(path_a_mapas)
        mapa, inicio, fin = self.leer_datos_mapa(archivo_mapa)
        super().__init__(mapa, inicio, fin)

    
    def elegir_mapa_aleatorio(self, path: str) -> str:
        archivos = os.listdir(path)
        nombre_archivo = random.choice(archivos)
        return f"{path}/{nombre_archivo}"

    
    def leer_datos_mapa(self, archivo_mapa: str) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
        with open(archivo_mapa, 'r') as file:
            lineas = file.readlines()
        
        
        coords = lineas[0].strip().split()
        inicio = (int(coords[0]), int(coords[1]))
        fin = (int(coords[2]), int(coords[3]))
        laberinto = ''.join(lineas[1:]).strip()

       
        mapa = self.convertir_mapa_a_matriz(laberinto)
        return mapa, inicio, fin

def main():
    
    juego = JuegoArchivo("./mapas")
    juego.main_loop()

if __name__ == "__main__":
    main()
