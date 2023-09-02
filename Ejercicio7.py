#Ejercicio7

correo = input("Ingrese su correo eletronico: ")
correo_cambiado = correo.find('@')
print(correo[: correo_cambiado] + '@ceu.es')

