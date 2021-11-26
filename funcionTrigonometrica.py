"""Ejercicio 6)

Trigonometría y clasificación de  ángulos.
Haga el programa que dado un ángulo calcule y muestre su Seno (sin) y Coseno (cos) y Tangente (tan) con una presión de 
4 decimales además de indicar si el mismo es agudo (0>°<90) u obtuso (90>°<180).
"""

import math
angulo = float(input("Ingrese un ángulo: "))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"Seno: {seno:.4f}")
print(f"Coseno: {coseno:.4f}")
print(f"Tangente: {tangente:.4f}")

if angulo > 0 and angulo < 90:
    print("El ángulo es agudo")
elif angulo > 90 and angulo < 180:
    print("El ángulo es obtuso")
else:
    print("El ángulo es recto")
