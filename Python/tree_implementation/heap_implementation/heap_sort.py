from heap_class import MaxHeap


def heapsort(elementos: list) -> list:
    """Ordena una lista de elementos en orden ascendente usando MaxHeap."""
    heap = MaxHeap()

    # 1. Insertar todos los elementos en el Heap
    for x in elementos:
        heap.insert(x)

    # 2. Extraer de mayor a menor
    ordenados = []
    while not heap.is_empty():
        ordenados.append(heap.delete())

    # Se invierte la lista para obtener orden ascendente (menor a mayor)
    return ordenados[::-1]