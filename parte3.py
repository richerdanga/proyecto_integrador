import os
def borrar():
     os.system('cls' if os.name=='nt' else 'clear')
     print(contador)


contador=0
while contador <= 50:
    borrar()
    n=input("presiona la tecla n: ")
    contador+=1

print("finaliza la ejecucion del programa")