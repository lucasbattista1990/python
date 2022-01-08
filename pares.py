'''Hacer programa que pida 2 numeros y se de cuenta cual de ellos es par, o si ambos lo son.'''

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if num1 % 2 == 0 and num2 % 2 == 0:
     print("Ambos numeros son pares")
elif num1 % 2 != 0 and num2 % 2 == 0:
    print("El primer numero es impar y el segundo es par")
elif num1 % 2 == 0 and num2 % 2 != 0:
    print("El primer numero es par y el segundo es impar")
else:
    print("Ambos numeros son impares")
