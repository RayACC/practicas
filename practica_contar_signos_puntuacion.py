punto = ["."]
coma = [","]
espacio = [" "]
salir = ""

while salir != "fin":
    frase = input("introduce tu frase:     ")

    puntos = 0
    comas = 0
    espacios = 0

    for x in frase:

        if x in punto:
            puntos += 1
        if x in coma:
            comas += 1
        if x in espacio:
            espacios += 1



    print("Numero de puntos: {} ".format(puntos))
    print("Numero de comas: {}".format(comas))
    print("Numero de espacios: {}".format(espacios))
    salir = input("Si deseas terminar escribe fin:   ")
    salir = salir.lower()

print("fin del programa ")
