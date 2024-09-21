#Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
#encuentran en la posición 0, 4 y 5.
#lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
#Resultado esperado: ['Verde', 'Blanco', 'Negro']
lista_ingresada = input("Introduce las palabras separandolas por comas(,): ")
lista1 = lista_ingresada.split(',')
lista1 = [elemento.strip() for elemento in lista1]
lista_editada = [elemento for i, elemento in enumerate(lista1) if i not in [0, 4, 5]]
print("La lista tras eliminar los elementos es:", lista_editada)

