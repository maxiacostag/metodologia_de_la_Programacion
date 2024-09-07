
#empleado: [nombre, legajo, categoría y salario]

empleados = [
    ["Juan Pérez", 1001, "A", 50000],
    ["María López", 1002, "B", 55000],
    ["Carlos García", 1003, "A", 48000],
    ["Ana Fernández", 1004, "C", 60000],
    ["Luis Martínez", 1005, "B", 53000],
    ["Sofía González", 1006, "A", 49000],
    ["Miguel Torres", 1007, "C", 62000],
    ["Lucía Sánchez", 1008, "B", 54000],
    ["José Ramírez", 1009, "A", 51000],
    ["Elena Díaz", 1010, "C", 61000]
]

#aplicar un algoritmo ordenando por salario o categoria o nombre
"""
def insertionSort(lista):
    # Recorremos la lista desde el segundo elemento (índice 1)
    for step in range(1, len(lista)):
        # Guardamos el valor del elemento actual
        key = lista[step]
        
        # Mover los elementos del arreglo que son mayores que la clave, una posición hacia adelante
        j = step - 1

        while j >= 0 and key[2] < lista[j][2]:
            lista[j + 1] = lista[j]
            j = j - 1
        
        # Colocar la clave en su posición correcta
        lista[j + 1] = key
    
    return lista

# Ejemplo
#lista = [12, 11, 13, 5, 6]
#print("Lista desordenada:", lista)
listaOrdenada = insertionSort(empleados)
print("Lista ordenada:", listaOrdenada)

"""

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

lista=[5,2,4,6,1,3]
print(f"Lista desordenada {lista}\n     Orden{selectionSort(lista)}")
