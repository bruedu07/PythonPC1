#Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
#último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
#verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.
cantidad_musicales = int(input("¿Cuántos shows musicales has visto en el último año? "))
variable = cantidad_musicales > 3
print(f"¿Has visto más de 3 shows? {variable}")
