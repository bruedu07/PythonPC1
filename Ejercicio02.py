#En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
#restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.

#Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
#porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
#dejar como propina.

consumo = float(input("¿Cuál fue el total de tu consumo en el restaurante? "))
porcentaje_propina = float(input("¿Qué porcentaje de propina deseas dejar? "))

propina = consumo * (porcentaje_propina / 100)

print(f"La cantidad de dinero a dejar como propina es: ${propina:.2f}")

