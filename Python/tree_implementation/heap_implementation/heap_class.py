class MaxHeap:
    def __init__(self):
        # Se inicia con un elemento placeholder en el índice 0
        # para mantener la indexación basada en 1:
        # Hijo izquierdo: 2 * i
        # Hijo derecho:   2 * i + 1
        # Padre:          i // 2
        self.aHeap = [None]
        self.iSize = 0

    def is_empty(self) -> bool:
        """Comprueba si el Heap está vacío."""
        return self.iSize == 0

    def get_root(self):
        """Obtiene el mayor elemento (raíz) sin eliminarlo."""
        if self.is_empty():
            raise IndexError("El Heap está vacío")
        return self.aHeap[1]

    def insert(self, x) -> None:
        """Inserta un elemento y restaura la propiedad con UpHeap (flotar)."""
        self.iSize += 1
        self.aHeap.append(x)
        self._up_heap(self.iSize)

    def _up_heap(self, iPos: int) -> None:
        """Reorganiza hacia arriba (UpHeap / Sift-Up / Flotar)."""
        iParent = iPos // 2
        while iParent >= 1 and self.aHeap[iPos] > self.aHeap[iParent]:
            # Intercambio
            self.aHeap[iPos], self.aHeap[iParent] = (
                self.aHeap[iParent],
                self.aHeap[iPos],
            )
            iPos = iParent
            iParent = iPos // 2

    def delete(self):
        """Elimina y retorna el elemento máximo (raíz), reorganizando con DownHeap."""
        if self.is_empty():
            raise IndexError("El Heap está vacío")

        max_val = self.aHeap[1]

        # Colocar el último elemento en la raíz y decrementar el tamaño
        self.aHeap[1] = self.aHeap[self.iSize]
        self.aHeap.pop()
        self.iSize -= 1

        # Reorganizar el árbol si aún quedan elementos
        if not self.is_empty():
            self._down_heap(1)

        return max_val

    def _down_heap(self, iPos: int) -> None:
        """Reorganiza hacia abajo (DownHeap / Sift-Down / Hundir)."""
        iC = 2 * iPos
        bFlag = False

        while iC <= self.iSize and not bFlag:
            # Si tiene hijo derecho y es mayor que el izquierdo, elegimos el derecho
            if iC < self.iSize and self.aHeap[iC] < self.aHeap[iC + 1]:
                iC += 1

            # Si el hijo elegido es mayor que el padre actual, intercambiamos
            if self.aHeap[iPos] < self.aHeap[iC]:
                self.aHeap[iPos], self.aHeap[iC] = self.aHeap[iC], self.aHeap[iPos]
                iPos = iC
                iC = 2 * iPos
            else:
                bFlag = True

    def __str__(self) -> str:
        """Representación en texto del arreglo subyacente (ignorando el índice 0)."""
        return str(self.aHeap[1:])
