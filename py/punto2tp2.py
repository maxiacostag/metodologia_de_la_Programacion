"""
1.numero positivos
2.5 numeros
3.separados por espacios
"""
import os


# Complete la función 'miniMaxSum' siguiente.
def miniMaxSum(arr):
    sumas = []
    for num in arr:
        sumas.append(sum(arr)- num)
    return f"{min(sumas)} {max(sumas)}"

# Pedir al usuario que ingrese los números separados por espacios
os.system("cls")
arr = list(map(int, input("Ingrese 5 números separados por espacios: ").split()))
def numerosPositivos(arr):
    # Verifica que todos los números en la lista sean positivos
    for num in arr:
        if num <= 0:
            return False
    return True

# Bucle que continúa hasta que se ingresen 5 números enteros y positivos
while True:
    try:
        arr = list(map(int, input("Ingresa 5 números enteros positivos: ").split()))
        
        # Verificar que la longitud sea 5 y que todos los números sean positivos
        if len(arr) == 5 and numerosPositivos(arr):
            break  # Salir del bucle si la condición se cumple
        else:
            print("Por favor, ingresa exactamente 5 números enteros positivos.")
    
    except ValueError:
        # Manejar el caso donde la conversión a entero falla
        print("Entrada no válida. Asegúrate de ingresar números enteros.")
print(miniMaxSum(arr))

