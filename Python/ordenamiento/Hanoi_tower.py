def hanoi_solver(disks):
    varillas = [list(range(disks, 0, -1)), [], []]
    historial = []

    def registar_movimiento():
        historial.append(f'{varillas[0]} {varillas[1]} {varillas[2]}')
    
    def mover_discos(k: int, origen: int, destino: int, varilla_aux: int):
        if k > 0:
            mover_discos(k - 1, origen, varilla_aux, destino)
            
            disco = varillas[origen].pop()
            varillas[destino].append(disco)
            registar_movimiento()
            
            mover_discos(k - 1, varilla_aux, destino, origen)

    registar_movimiento()
    
    mover_discos(disks, 0, 2, 1)
    
    return '\n'.join(historial)

if __name__ == "__main__":
    resultado = hanoi_solver(3)
    print(resultado)

