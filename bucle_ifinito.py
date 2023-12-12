from readchar import readkey, key
while True:
    print("ingresa una tecla:",end=" ")
    tecla=readkey()
    print(tecla)
    if tecla== key.UP:
        print("presionaste la tecla UP")
        break
