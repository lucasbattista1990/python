
""" 
Ejercicio 1)
En una tienda de ropa tienen una promoción de llevarse tres remeras por el precio de las dos más baratas.
Haga un programa que, dados los tres precios de las remeras, me indique la cantidad a pagar.
"""

mi_array = []
final = 0

print("Ingrese el valor de las 3 remeras que compro")
for i in range(3):
    print("remera n°", i + 1 )
    mi_array.append(int(input("")))
for j in range(2):
    aux = mi_array[j]
    for n in range(len(mi_array)):
        if (aux > mi_array[n]):
            aux = mi_array[n]
    final += aux
    mi_array.remove(aux)

print("El precio final es: ", final)

