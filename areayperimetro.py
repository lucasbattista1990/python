"""Ejercicio 5)

Calculamos Área y Perímetro 
Haga un programa que, solicite al usuario los 2 lados de un rectángulo. Calcular mostrar su área y perímetro.
 """

lado1=float(input("Introduce el primer lado: "))
lado2=float(input("Introduce el segundo lado: "))
 
area = lado1 * lado2
perimetro = 2 * (lado1 + lado2)

print("El área del rectángulo es: ", area)
print("El perímetro del rectángulo es: ", perimetro)