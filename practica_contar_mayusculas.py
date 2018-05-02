salir = 0

while salir != "fin":
    y = False

    cont = 0
    frase = input("introduce tu frase:     ")

    for x in frase:
        y = x.isupper()
        if y is True:
            cont +=1

    print("Numero de Mayusculas: {} ".format(cont))

    salir = input("Si deseas terminar escribe fin:   ")
    salir = salir.lower()

print("fin del programa ")
