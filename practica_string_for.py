vocal = ["a","e","i","o","u"]
salir=""
while fin != "fin" 
  frase = input("introduce tu frase")
 
  vocales = 0
  consonantes = 0

  for x in frase:
  
    if x in vocal 
        vocales += 1
    else
        consonantes += 1

  print("Numero de vocales:  {} ".format(vocales))  
  print("Numero de consonantes: {}".format(consonantes))
  salir=input("Si deseas terminar escribe fin:")
  salir= salir.lower()
  
print("fin del programa ")
