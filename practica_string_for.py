vocal = ["a","e","i","o","u"]
fin=""
while != "fin" 
  frase = input("introduce tu frase")
  indice= 0
  vocales = 0
  consonantes = 0

  for frase:
  
    if frase[indice] in vocal 
        vocales += 1
    else
        consonantes += 1

  print("Numero de vocales:  {} ".format(vocales))  
  print("Numero de consonantes: {}".format(consonantes))
  fin=input("Si deseas terminar escribe fin:")
 
print("fin del programa ")
