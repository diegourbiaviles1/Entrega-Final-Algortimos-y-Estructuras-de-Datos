from radix_sort_modulo import ejecutar_radix_sort
from hashing_modulo import ejecutar_hashing

def menu_principal():
    while True:
        print("\n========= MENÚ PRINCIPAL =========")
        print("1. Ejecutar Radix Sort")
        print("2. Ejecutar Hashing")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_radix_sort()
        elif opcion == "2":
            ejecutar_hashing()
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()

