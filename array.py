"""Ejercicio 8)

Sumamos elementos
Haga un programa que, liste 50 números comenzando en 23 (veintitrés) mostrando al final del listado la suma de los números pares.
"""
suma = 0
array = []
for i in range(23, 74, 1):
        array.append(i)
        if i % 2 == 0:
            suma += i

print(array)
print("La suma de los pares es: ",suma)
    


         


        

