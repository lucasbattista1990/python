"""Ejercicio 7)

Pitágoras
Haga el programa que, dado 2 lados o 1 lado y su hipotenusa, calcule y muestre la longitud del lado restante. 
Deberá solicitar al usuario que indique “L” o “H” para identificar el lado y su longitud con 2 decimales.
"""
import math
print("ingrese L o H para identificar el lado")
lado = input("Lado: ")
lado = lado.upper()
if lado == "L":
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    hipotenusa = math.sqrt(lado1**2 + lado2**2)
    print("La hipotenusa es: {:.2f}".format(hipotenusa))
elif lado == "H":
    lado1 = float(input("Lado 1: "))
    hipotenusa = float(input("Hipotenusa: "))
    lado2 = math.sqrt(hipotenusa**2 - lado1**2)
    print("El lado 2 es: {:.2f}".format(lado2))
else:
    print("No se reconoce el lado")


