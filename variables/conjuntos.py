

conjunto = set(["christian", "eduardo"])
conjunto2 = {"hola", "como estan"}
#verificando si es un subconjunto

resultado = conjunto.issubset(conjunto2) #o tambien se puede <= no es una resta y poara los superset es >

print(resultado)


conjunto4 = frozenset(["hola1","hola2"])
conjunto5 = {conjunto4, "holaaaaa"}

print(conjunto5)
