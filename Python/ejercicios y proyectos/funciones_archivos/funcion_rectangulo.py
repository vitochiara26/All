def comprobar_punto_dentro_fuera(pos_x_uno, pos_x_dos, pos_y_uno, pos_y_dos, punto_x, punto_y):
    dentro_x = pos_x_uno <= punto_x <= pos_x_dos
    dentro_y = pos_y_uno <= punto_y <= pos_y_dos
    if dentro_x and dentro_y:
        return True
    return False