def el_mayor(lista_de_numeros):
  numero_prueba=0
  for numero in lista_de_numeros:
    
    if numero > numero_prueba:
      numero_prueba = numero
  
  return (numero_prueba)
  

numero = input("Escribe la lista de numeros que quieras conocer su numero mayor: ")
mayor = el_mayor(numero)
print("El numero mayor es: {} ".format(mayor))
  
  
  
    
