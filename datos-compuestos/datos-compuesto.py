

#creando una lista si se puede modificar
lista = ["christian", "eduardo", 1, True]
tuple = ("christian", "eduardo", 1, True) # crando lista con tupla que no se pueden modificar


lista[0] = "hanna"
#tupla[1] = "baker" error porque no se pueden modificar las tuplas
#creando un conjunto (set)

conjunto = {"christian", "eduardo"}
# no se pueden acceder por el indixe y no permite repetir valores
conjunto = {"eduardo", "barillas"} #solo se pueden redefinir pero no alterar sus indices
#son como las tuplas que es un conjunto de datos pero aqui solo se pueden redifinir la el conjunto de datos

print(lista[2])
print(tuple[2]) 


#ultimo dato compuesto son los diccionarios (dict) la estructura es key-value

diccionario = {
    
    "nombre" : "christian",
    "edad" : 24
}

print (diccionario["nombre"])

 