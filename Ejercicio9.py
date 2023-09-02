#Ejercicio 9.1

fecha = input("Introduzca la fecha de su nacimiento en formato dd/mm/aaaa: ")
dia = fecha[0:2]
mes = fecha[3:5]
año = fecha[6:11]
print("Día", dia)
print("Mes", mes)
print("Año", año)


#Ejercicio 9.2

fecha = input("Introduzca la fecha de su nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mes_año = fecha[fecha.find('/')+1:]
mes = mes_año[:mes_año.find('/')]
año = mes_año[mes_año.find('/')+1:]
print("Día", dia)
print("Mes", mes)
print("Año", año)
