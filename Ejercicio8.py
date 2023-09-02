#Ejercicio 8

precio_producto = input("Introduzca el precio del producto con dos decimales")
precio_cambiado = precio_producto.find(".")
print(precio_producto[: precio_cambiado], 'euros y', precio_producto[precio_cambiado + 1:], "céntimos.")
