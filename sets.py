# Definir un conjunto vacío
numeros = set()

numeros.add(1)
numeros.add(2)
numeros.add(3)

print(numeros)

numeros.add(2)  # No se añadirá, ya que 2 ya está en el conjunto
print(numeros)

numeros.remove(1)  # Eliminar un elemento
print(numeros)

print("El conjunto tiene", len(numeros), "elementos.") # Muestra la cantidad de elementos en el conjunto
