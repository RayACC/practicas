
vocal = ["a", "e", "i", "o", "u"]
salir = ""

while salir != "fin":
    frase = input("introduce tu frase:     ")
    vocales = []

    for x in frase:
        if x in vocal:
            vocales.append(x)


    salir = input("Si deseas terminar escribe fin:   ")
    salir = salir.lower()
print("Estas son las vocales: {}".format(vocales))