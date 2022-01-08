'''hacer un programa que pida 3 numeros y determine cual es mayor'''

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese otro numero: "))

if num1 > num2 and num1 > num3:
    print("El primer numero es mayor")
elif num2 > num1 and num2 > num3:
    print("El segundo numero es mayor")
elif num3 > num1 and num3 > num2:
    print("El tercer numero es mayor")
else:
    print("Los numeros son iguales")
    