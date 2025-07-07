
from modulo_utils import generar_lista_enteros, medir_tiempo, pedir_datos_usuario

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    return output

def radix_sort_lsd(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10
    return arr

def ejecutar_radix_sort():
    print("\n--- RADIX SORT ---")
    opcion = input("1. Usar datos predefinidos\n2. Ingresar mis propios datos\nSeleccione: ")

    if opcion == "1":
        lista = generar_lista_enteros(20)
    else:
        lista = pedir_datos_usuario()

    print("Lista original:", lista)
    ordenada, tiempo = medir_tiempo(radix_sort_lsd, lista)
    print("Lista ordenada:", ordenada)
    print(f"Tiempo de ejecución: {tiempo:.6f} segundos")
