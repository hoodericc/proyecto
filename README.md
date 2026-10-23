# Proyecto
Github para mi proyecto de Fundamentos de la Programación (Grupo 601)

## Sistema de Taquería
Este proyecto consiste en desarrollar un sistema sencillo de pedidos para una taquería de la esquina utilizando Python 3.
El programa permitirá al usuario visualizar un menú con diferentes productos, seleccionar los alimentos que desea ordenar, indicar la cantidad de cada producto y calcular el costo total de la compra.
A lo largo del proyecto utilizaré diferentes conceptos de programación en Python, como por ejemplo operadores, funciones y ciclos.
El objetivo principal es aplicar mis conocimientos vistos en clase dentro de un programa organizado y fácil de utilizar.
## Funciones principales
Mostrar el menú 
Seleccionar diferentes tipos de tacos o comida y bebidas
Indicar la cantidad de productos deseados
Calcular el precio de cada producto
Calcular el precio total de la orden
Validar las opciones ingresadas por el usuario
Permitir agregar varios productos a un mismo pedido
Mostrar el resumen de la compra

## Pseudocódigo

```
INICIO
Definir constantes del menu:
-NOMBRES_PRODUCTOS: lista con el nomber de cada producto
-PRECIOS_PRODUCTOS: lista con el precio de cada producto

Funcion valida_opcion(opcion, total_productos):
  if opcion es un numero:
    if el numero esta entre el 1 y el total de productos:
      return true
  return false

Funcion valida_cantidad(cantidad):
  If cantidad es un numero:
    If cantidad > 0:
      return true
  return false

Funcion calcula_subtotal(precio, cantidad):
  return precio * cantidad

Funcion muestra_menu(nombres, precios):
  for cada producto de la lista:
    mostrar su numero, nombre y precio

Funcion muestra_resumen(pedido, total):
  for cada producto del pedido:
    Mostrar el producto
  Mostrar el total a pagar

Funcion toma_pedido(nombres, precios):
  Pedido = lista vacia
  total = 0
  seguir = "s"
  while seguir sea "s":
    mostrar el menu
    pedir opcion al usuario
    if la opcion es valida:
      pedir cantidad al usuario
      if la cantidad es valida:
        subtotal = calcula_subtotal(precio, cantidad)
        total = total + subtotal
        agregar el producto al pedido
      elif:
        mostrar "cantidad invalida"
    elif:
      mostrar "opcion invalida"
    preguntar si desea agregar otro producto
  return pedido, total

PROGRAMA PRINCIPAL:
  pedido, total = toma_pedido(NOMBRES_PRODUCTOS, PRECIOS_PRODUCTOS)
  muestra_resumen(pedido, total)
  Mostrar mensaje de despedida (¡Provecho!, Gracias por su pedido, etc.)
FIN
```
