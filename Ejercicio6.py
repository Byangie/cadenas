#Ejercicio 6

frase = input("Ingrese una frase: ")
vocal = input("Ingrese una vocal: ")
vocal_mayuscula = vocal.upper()
frase_vocal = frase.replace(vocal, vocal_mayuscula)

print(frase_vocal)

