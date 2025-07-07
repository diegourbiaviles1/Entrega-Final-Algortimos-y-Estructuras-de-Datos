
import random
import time

def generar_lista_enteros(tamano, max_valor=10000):
    return [random.randint(0, max_valor) for _ in range(tamano)]

def medir_tiempo(funcion, *args, **kwargs):
    inicio = time.time()
    resultado = funcion(*args, **kwargs)
    fin = time.time()
    return resultado, fin - inicio

def pedir_datos_usuario():
    entrada = input("Ingrese números separados por coma (ej: 4,12,55): ")
    return [int(x.strip()) for x in entrada.split(",")]
