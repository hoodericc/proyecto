"""
Proyecto Taqueria
Sistema de pedidos para una taqueria.
El programa muestra un menu de productos, permite al usuario agregar varios
productos a un mismo pedido, valida lo que el usuario captura y al final
muestra un resumen de la compra con el total a pagar.
"""

# constantes del menu
NOMBRES_PRODUCTOS = ["Taco de pastor", "Taco de bistec", "Quesadilla",
                     "Refresco", "Agua fresca"]
PRECIOS_PRODUCTOS = [15, 18, 20, 20, 15]

"""
================== funciones de validacion  =================================
"""


def valida_opcion(opcion, total_productos):
    """
    (uso de funciones, condicionales)
    recibe: opcion cadena de texto, total_productos entero
    revisa que la opcion sea un numero entre 1 y total_productos
    devuelve: True si la opcion es valida, False si no lo es
    """
    if opcion.isdigit():
        numero = int(opcion)
        if numero >= 1 and numero <= total_productos:
            return True
    return False


def valida_cantidad(cantidad):
    """
    (uso de funciones, condicionales)
    recibe: cantidad cadena de texto
    revisa que la cantidad sea un numero entero mayor a 0
    devuelve: True si la cantidad es valida, False si no lo es
    """
    if cantidad.isdigit():
        if int(cantidad) > 0:
            return True
    return False


"""
================== funciones de calculo  ====================================
"""


def calcula_subtotal(precio, cantidad):
    """
    (uso de operadores, uso de funciones)
    recibe: precio valor numerico, cantidad valor numerico
    multiplica el precio de un producto por la cantidad pedida
    devuelve: subtotal numerico
    """
    return precio * cantidad


"""
================== funciones de pantalla  ===================================
"""


def muestra_menu(nombres, precios):
    """
    (uso de funciones, listas, ciclos)
    recibe: nombres lista de cadenas, precios lista de enteros
    imprime en pantalla cada producto con su numero y su precio
    """
    print("\n----- Menu de la Taqueria -----")
    for i in range(len(nombres)):
        numero = i + 1
        print(numero, ". ", nombres[i], " - $", precios[i], sep="")


def muestra_resumen(pedido, total):
    """
    (uso de funciones, listas, ciclos)
    recibe: pedido lista de cadenas, total valor numerico
    imprime en pantalla cada producto del pedido y el total a pagar
    """
    print("\n----- Resumen de tu pedido -----")
    for producto in pedido:
        print(producto)
    print("Total a pagar: $", total, sep="")


"""
================== funcion de integracion  ==================================
"""


def toma_pedido(nombres, precios):
    """
    (uso de funciones, condicionales, ciclos, listas)
    recibe: nombres lista de cadenas, precios lista de enteros
    funcion de integracion, repite el menu hasta que el usuario ya no quiera
    agregar productos. Valida cada opcion y cantidad capturada y acumula el
    total del pedido.
    devuelve: pedido lista de cadenas, total valor numerico
    """
    pedido = []
    total = 0
    seguir = "s"

    while seguir == "s":
        muestra_menu(nombres, precios)
        opcion = input("\nElige el numero del producto: ")

        if valida_opcion(opcion, len(nombres)):
            cantidad = input("Cantidad: ")

            if valida_cantidad(cantidad):
                indice = int(opcion) - 1
                subtotal = calcula_subtotal(precios[indice], int(cantidad))
                total = total + subtotal
                descripcion = (cantidad + " x " + nombres[indice]
                               + " = $" + str(subtotal))
                pedido.append(descripcion)
                print("Agregado:", descripcion)
            else:
                print("Cantidad invalida, debe ser un numero mayor a 0")
        else:
            print("Opcion invalida, elige un numero del menu")

        seguir = input("\n¿Deseas agregar otro producto? s/n ").lower()

    return pedido, total


"""
========  parte principal del programa ======================================
"""

pedido_final, total_final = toma_pedido(NOMBRES_PRODUCTOS, PRECIOS_PRODUCTOS)
muestra_resumen(pedido_final, total_final)
print("\n¡Gracias por tu compra! Buen provecho")
