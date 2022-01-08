#diccionarios

equipo = {10: "Lucas Battista", 11: "Rocio", 7: "Juan", 13: "Pedro", 36: "Javier"}

print(equipo)
print(equipo[10])
print(equipo.get(22,"No existe "))
print(equipo.get(36,"No existe "))

print(22 in equipo) 
print(equipo.keys()) #devuelve una lista con las claves
print(equipo.values()) #devuelve una lista
print(equipo.pop(36)) #elimina el elemento y devuelve el valor
print(equipo.items()) #devuelve una tupla con los pares clave-valor
print(len(equipo)) #devuelve el numero de elementos

equipo.clear() #borra todos los elementos