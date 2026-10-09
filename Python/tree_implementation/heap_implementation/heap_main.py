from heap_sort import heapsort
from heap_class import MaxHeap

if __name__ == "__main__":
    # Datos de ejemplo
    datos = [77, 60, 41, 15, 55, 35]

    # Pruebas de operaciones con el MaxHeap
    mi_heap = MaxHeap()
    for item in datos:
        mi_heap.insert(item)

    print("Heap formado:", mi_heap)  # Output: [77, 60, 41, 15, 55, 35]
    print("Elemento raíz (máximo):", mi_heap.get_root())  # Output: 77

    # Eliminación de la raíz
    eliminado = mi_heap.delete()
    print("Elemento eliminado:", eliminado)  # Output: 77
    print("Heap tras DownHeap:", mi_heap)  # Output: [60, 55, 41, 15, 35]

    # Prueba de Heapsort
    lista_desordenada = [15, 77, 35, 60, 41, 55]
    lista_ordenada = heapsort(lista_desordenada)
    print("Lista ordenada con Heapsort:", lista_ordenada)  # Output: [15, 35, 41, 55, 60, 77]
