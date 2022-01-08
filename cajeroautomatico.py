'''hacer un programa que simule un cajero automaticvo con un saldo inicial de 1000 y tendra el siguiente menu}
1. ingresar dinero en la cuenta
2. retirar dinero
3. mostrar dinero disponible
4. salir'''

dinero = 1000
opcion = 0
while opcion != 4:
    print("1. ingresar dinero en la cuenta")
    print("2. retirar dinero")
    print("3. mostrar dinero disponible")
    print("4. salir\n")
    opcion = int(input("ingrese una opcion: "))
    if opcion == 1:
        dinero = dinero + int(input("\ningrese dinero: \n"))
    elif opcion == 2:
        dinero = dinero - int(input("\ningrese cantidad que desea retirar: \ns"))
    elif opcion == 3:
        print("\nsaldo: ", dinero)
    elif opcion == 4:
        print("\ngracias por su visita")
    else:
        print("\n opcion no valida")
