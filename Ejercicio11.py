#Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
#lista. Su programa debe retornar otra lista sin los duplicados.
#Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
#Lista procesada: [1, 2, 3, 4, 5]
lista_ingreso = input("Introduce los numeros separandolos con comas(,): ")
lista1 = [int(num.strip()) for num in lista_ingreso.split(',')]
lista2 = list(set(lista1))
print("Lista sin duplicados:", lista2)

