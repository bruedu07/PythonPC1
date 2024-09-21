#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
#pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
#puede ser calculada de la siguiente forma:
N = int(input("Introduce un número entero positivo: "))
if N > 0:
    suma = N * (N + 1) // 2
    print(f"La suma de los enteros desde 1 hasta {N} es: {suma}")
else:
    print("El número ingresado no es entero positivo.")