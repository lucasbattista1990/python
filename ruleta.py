"""Ejercicio 2)

Vamos al casino y decidimos jugar a la Ruleta.
Haga un programa que, ingresando el número que salió en la ruleta nos indique con un mensaje si corresponde a la 1ra, 
2da o 3er docena. Si el número que salió es 0 (cero) debe mostrar el mensaje: Banca Gana.
"""
import random

asd = input("Aprete una tecla para empezar el juego")
valor = random.randint(0,37)

print("El numero es: ", valor)
if (valor == 0):
    print("Banca gana")

elif (valor < 13):
    print("Corresponde a la primer docena.")
elif (valor < 25):
    print("Corresponde a la segunda docena.")
elif (valor < 37):
    print("Corresponde a la tercera docena.")


