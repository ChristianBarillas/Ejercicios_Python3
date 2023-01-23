cadena1 = "christian"
cadena2 = "eduardo"

#convierte a mayuculas

resultado = cadena1.upper()

#convierte a minuscula este metodo

resultado1 = cadena1.lower()

#convierte solo la primera en mayuscula pero convierte en minuscuka antes

resultado2 = cadena1.capitalize()


#busqueda

resultado3 = cadena2.find("d")


#si no hay una concidencia tira una exepcion

# resultado4 = cadena2.index("6")

#detecta si hay numeros incluso si la cadena es string (fase or true)
resultado5 = cadena2.isnumeric()


# detecta si es alpha numerico, no detecta los caracteres especiales como las comas, espacios, simbolos, numeros, etc
resultado6 = cadena2.isalpha()



# podemos buscar si se repite palabras y contar el numero de sus repeticiones, es decir devulve cuantas repeticiones existen en la variable con el dato que le pasemos
resultado7 = cadena2.count("e")



#compruena si la cadena comienza con el dato que le pasamos y devuelve falso o verdadero dependiendo si existe la coincidencia al principio

resultado8 = cadena2.startswith("d")



# lo mismo que la anterior pero comprueba el ultimo valor de la cadena devolviendo true or false

resultado9 = cadena2.endswith("y")




#podemos cambiar el valor de una cadena con el metodo replace ojo que debe concidir exactamente con lo que queremos remplazar sino no funcionara


resultado10 = cadena1.replace("christian", "ordonez")


#ojo me separa donde yo le indico, si no le indico nada no me separa nada y me crea la lista con el unico elemento de la cadena, pero si le indico una letra o palabra entonces me la comienza a separar desde ese lugar ojo no incluye esas palabras o letras sino que las borra y en su lugar es remplazada por la sepacion que es puesta en una lista(dato compuesto llamado lista cuyo tiene un indixe es decir una posicion) 

resultado11 = cadena2.split("e")

print(resultado3)