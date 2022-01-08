"""Realizar la codificación necesaria en lenguaje “python” utilizando las herramientas brindadas por la cátedra. 

Ejercicio:

Se requiere implementar un software para administrar una agencia de venta de automotores.

El Sistema principal cuenta con un menú cíclico con las siguientes opciones:
    • 0: Salir
    • 1: Armar pedido
    • 2: Listar pedido
    • 3: Borrar pedido


Cualquier otra opción ingresada deberá ser informada como incorrecta y volver a solicitar al usuario ingresar una nueva acción.


Detalle de acciones
Armar pedido

Se solicitara al usuario el Nro de Motor de los automotores con los cuales armar el archivo de Pedidos. 

El pedido se forma copiando a un nuevo archivo binario de “pedidos” [pedidos.dat] el auto existente en el archivo de automotores 
[automotores.dat] que se corresponda con el Nro de motor ingresado por el usuario.

La búsqueda del nro de motor deberá realizarse sobre un archivo de índices de automotores [automotores.inx] y NO sobre el archivo original.
Si el Nro de motor ingresado NO EXISTE debe informar al usuario la leyenda: Nro de motor existente.


Listar pedido

Deberá mostrarse por pantalla el listado de autos que conforman el pedido armado. En caso de no existir ningún auto en el pedido deberá 
informarse al usuario que debe generar un pedido.
	
Formato de salida

Total de Autos en el pedido: ##  (cantidad de autos en el pedido)

Borrar pedido

Eliminar el contenido del archivo de pedidos [pedidos.dat]

Consideraciones


    • Para aprobar el sistema deberá compilar (poder ejecutarse)
"""



import time

def main():
    """
    Función principal del programa.
    """
    print("Bienvenido al sistema de administración de pedidos de autos")
    print("Por favor ingrese una opción:")
    print("1: Armar pedido")
    print("2: Listar pedido")
    print("3: Borrar pedido")
    print("0: Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        armar_pedido()
    elif opcion == "2":
        listar_pedido()
    elif opcion == "3":
        borrar_pedido()
    elif opcion == "0":
        sys.exit()
    else:
        print("Opción incorrecta")
        main()


def armar_pedido():
    """
    Función que permite armar un pedido.
    """
    print("Armar pedido")
    print("Ingrese el número de motor del auto que desea armar el pedido")
    nro_motor = input("Nro de motor: ")
    archivo_autos = open("automotores.dat", "wb")
    archivo_pedidos = open("pedidos.dat", "wb")
    archivo_indice = open("automotores.inx", "wb")
    archivo_indice.seek(0)
    posicion = archivo_indice.read(4)
    while posicion != b"":
        archivo_autos.seek(int(posicion))
        auto = archivo_autos.read(32)
        archivo_pedidos.write(auto)
        posicion = archivo_indice.read(4)
    archivo_indice.close()
    archivo_autos.close()
    archivo_pedidos.close()
    print("Pedido armado correctamente")
    time.sleep(2)
    main()

def listar_pedido():
    """
    Función que permite listar los autos que conforman el pedido.
    """
    print("Listar pedido")
    archivo_pedidos = open("pedidos.dat", "rb")
    print("Total de autos en el pedido: ", archivo_pedidos.seek(0, 2) / 32)
    archivo_pedidos.close()
    time.sleep(2)
    main()

def borrar_pedido():
    """
    Función que permite borrar el contenido del archivo de pedidos.
    """
    print("Borrar pedido")
    archivo_pedidos = open("pedidos.dat", "wb")
    archivo_pedidos.close()
    print("Pedido borrado correctamente")
    time.sleep(2)
    main()


if __name__ == "__main__":
    main()
