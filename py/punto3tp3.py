import random

def selectionSort(lista):
    #Se recorre la lista
    for i in range(len(lista)):
        # Encuentra el índice del valor mínimo en la sublista no ordenada
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
                print(lista)
        # Intercambia el valor mínimo encontrado con el primer valor de la sublista no ordenada
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return (lista)







def generar_lista_aleatoria(tamaño, rango_minimo, rango_maximo):
    lista_aleatoria = [random.randint(rango_minimo, rango_maximo) for _ in range(tamaño)]
    return lista_aleatoria

tamaño = 5  # Tamaño de la lista
rango_minimo = 1  # Valor mínimo del rango
rango_maximo = 100  # Valor máximo del rango

lista1 = selectionSort(generar_lista_aleatoria(tamaño, rango_minimo, rango_maximo))
lista2 = selectionSort(generar_lista_aleatoria(tamaño, rango_minimo, rango_maximo))

print("Lista de números aleatorios:", lista1)
print("Lista de números aleatorios:", lista2)

lista3 = selectionSort(lista1+lista2)

print(lista3)

