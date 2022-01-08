'''construir un programa que simule el funcionamiento de una calculadora que puede realizar 
las cuatro operaciones aritmeticas basicas (suma, resta , nmultiplicacion y division).
el usuario debe especificar la operacion con el primer caracter del nombre de la operacion'''
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
print("Seleccione una operacion: ")
print("S. Suma")
print("R. Resta")
print("M. Multiplicacion")
print("D. Division")
opcion = input("Marque la opcion deseada: ").upper()

if opcion == "S":
    suma = numero1 + numero2
    print(f"La suma es : {suma}")
elif opcion == "R":
    resta = numero1 - numero2
    print(f"La resta es : {resta}")
elif opcion == "M":
    multiplicacion = numero1 * numero2
    print(f"La multiplicacion es : {multiplicacion}")
elif opcion == "D":
    division = numero1 / numero2
    print(f"La division es : {division:.2f}")
else:
    print("Opcion no valida")
