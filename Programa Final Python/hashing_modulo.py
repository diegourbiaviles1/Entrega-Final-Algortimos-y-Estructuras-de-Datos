
from modulo_utils import generar_lista_enteros, medir_tiempo, pedir_datos_usuario

def hash_division(k, m):
    return k % m

def crear_tabla_hash(lista, m):
    tabla = [[] for _ in range(m)]
    for k in lista:
        indice = hash_division(k, m)
        tabla[indice].append(k)
    return tabla

def ejecutar_hashing():
    print("\n--- HASHING (método de división) ---")
    opcion = input("1. Usar datos predefinidos\n2. Ingresar mis propios datos\nSeleccione: ")

    if opcion == "1":
        lista = generar_lista_enteros(20, 500)
    else:
        lista = pedir_datos_usuario()

    m = int(input("Ingrese tamaño de la tabla hash (ej. 10): "))
    print("Lista de claves:", lista)
    tabla_hash, tiempo = medir_tiempo(crear_tabla_hash, lista, m)
    for i, bucket in enumerate(tabla_hash):
        print(f"Índice {i}: {bucket}")
    print(f"Tiempo de ejecución: {tiempo:.6f} segundos")
