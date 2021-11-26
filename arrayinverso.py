"""Ejercicio 9)

Restamos elementos
Haga un programa que, liste los anteriores 50 números comenzando en 127 y muestre al final 
el resultado de restarle al valor 253 los números impares.
"""

array = []
suma = 0
resultado = 0
for i in range(127, 76, -1):
        array.append(i)
        
        if i % 2 != 0:
            suma += i
            resultado = suma -253 
print(array)
print("impares - 253 es:", resultado)