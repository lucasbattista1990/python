# bucle while
import math

numero = int(input("Introduce un número: "))

while numero < 0:
    print("El número debe ser positivo")
    numero = int(input("Introduce un número: "))

print(f"\n Su raiz cuadrada es: {(math.sqrt(numero)):.2f}")
