#Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
#- Mostrar una suma de los dos números
#- Mostrar una resta de los dos números (el primero menos el segundo)
#- Mostrar una multiplicación de los dos números
#- En caso de introducir una opción inválida, el programa informará de que no es correcta.
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
print("\nElige una opción:")
print("1 - Suma de los números")
print("2 - Resta del primero menos el segundo")
print("3 - Producto de los dos números")
opcion = int(input("Introduce el número de la opción que necesitas aplicar: "))
if opcion == 1:
    resultado = num1 + num2
    print(f"La suma es: {resultado}")
elif opcion == 2:
    resultado = num1 - num2
    print(f"La resta es: {resultado}")
elif opcion == 3:
    resultado = num1 * num2
    print(f"El producto es: {resultado}")
else:
    print("Opción no válida.")
