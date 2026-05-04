def dibujar_pared(altura):
    if altura > 0:
        dibujar_pared(altura - 1)
        print(' M '*5)


dibujar_pared(7)