" obtener los tipo de datos en una lista "


lista_datos = [1,2,3, "asd",False,[],True,123,2.1 ]
lista_tipos = []


for dato in lista_datos:
    lista_tipos.append(type(dato))


print(lista_tipos)