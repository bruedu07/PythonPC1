#Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
#original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a',
#'día', 'buen', 'Di'].
lista1 = input("Introduce las palabras separandolas por comas(,): ")
lista2 = lista1.split(',')
lista2 = [palabra.strip() for palabra in lista2]
lista_invertida = lista2[::-1]
print(lista_invertida)
