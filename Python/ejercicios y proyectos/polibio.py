class Mensaje:
    def __init__(self, codificacion, mensaje):
        self.codificacion = codificacion
        self.mensaje = mensaje
        self.tamaño = len(mensaje)
        self.matriz_alfabeto =[
                                ['A', 'B', 'C', 'D', 'E', 'F'],
                                ['G', 'H', 'I', 'J', 'K', 'L'],
                                ['M', 'N', 'O', 'P', 'Q', 'R'],
                                ['S', 'T', 'U', 'V', 'W', 'X'],
                                ['Y', 'Z', '1', '2', '3', '4'],
                                ['5', '6', '7', '8', ' ', ',']
                                ]
        self.posiciones_mensaje = [
                                    ['']*self.tamaño,
                                    ['']*self.tamaño
                                    ]
        self.posiciones_volteadas = [
                                    ['']*self.tamaño,
                                    ['']*self.tamaño
                                    ]

    def identificar_posiciones_letras(self):
        for letra in range(self.tamaño):
            found = False
            for fila in range(6):
                for columna in range(6):
                    if self.mensaje[letra].upper() == self.matriz_alfabeto[fila][columna]:
                        found = True
                        self.posiciones_mensaje[0][letra] = fila 
                        self.posiciones_mensaje[1][letra] = columna
                    if found:
                        break
                if found:
                    break

    def encriptar_mensaje(self):
        pos_vol = 0
        indice = 0
        for pos in range(self.tamaño):
            if mensaje.tamaño % 2 != 0:
                if pos <= mensaje.tamaño//2:
                    try: 
                        self.posiciones_volteadas[0][pos_vol] = self.posiciones_mensaje[0][indice]
                        self.posiciones_volteadas[0][pos_vol+1] = self.posiciones_mensaje[1][indice]
                        indice +=1
                        pos_vol += 2
                    except Exception:
                        self.posiciones_volteadas[1][0] = self.posiciones_mensaje[1][indice]
                        indice +=1
                        pos_vol = 1
                else :
                    self.posiciones_volteadas[1][pos_vol] = self.posiciones_mensaje[0][indice]
                    self.posiciones_volteadas[1][pos_vol+1] = self.posiciones_mensaje[1][indice]
                    indice +=1
                    pos_vol += 2
            else :
                if pos < mensaje.tamaño//2:
                    self.posiciones_volteadas[0][pos_vol] = self.posiciones_mensaje[0][indice]
                    self.posiciones_volteadas[0][pos_vol+1] = self.posiciones_mensaje[1][indice]
                    indice +=1
                    pos_vol += 2
                else :
                    try:
                        self.posiciones_volteadas[1][pos_vol] = self.posiciones_mensaje[0][indice]
                        self.posiciones_volteadas[1][pos_vol+1] = self.posiciones_mensaje[1][indice]
                        indice +=1
                        pos_vol += 2
                    except Exception:
                        pos_vol = 0
                        self.posiciones_volteadas[1][pos_vol] = self.posiciones_mensaje[0][indice]
                        self.posiciones_volteadas[1][pos_vol+1] = self.posiciones_mensaje[1][indice]
                        indice +=1
                        pos_vol += 2

    def desencriptar_mensaje(self):
        pos_ini = 0
        for pos in range(self.tamaño):
            if self.tamaño % 2 != 0:
                if pos <= self.tamaño // 2:
                    try:
                        self.posiciones_volteadas[0][pos] = self.posiciones_mensaje[0][pos_ini]
                        self.posiciones_volteadas[1][pos] = self.posiciones_mensaje[0][pos_ini+1]
                        pos_ini += 2
                    except Exception:
                        pos_ini = 0
                        self.posiciones_volteadas[1][pos] = self.posiciones_mensaje[1][pos_ini]
                        pos_ini += 1
                else:
                    self.posiciones_volteadas[0][pos] = self.posiciones_mensaje[1][pos_ini]
                    self.posiciones_volteadas[1][pos] = self.posiciones_mensaje[1][pos_ini+1]
                    pos_ini += 2
            else :
                if pos < self.tamaño//2:
                    self.posiciones_volteadas[0][pos] = self.posiciones_mensaje[0][pos_ini]
                    self.posiciones_volteadas[1][pos] = self.posiciones_mensaje[0][pos_ini+1]
                    pos_ini += 2
                else:
                    try:
                        self.posiciones_volteadas[0][pos] = self.posiciones_mensaje[1][pos_ini]
                        self.posiciones_volteadas[1][pos] = self.posiciones_mensaje[1][pos_ini+1]
                        pos_ini += 2
                    except Exception:
                        pos_ini = 0
                        self.posiciones_volteadas[0][pos] = self.posiciones_mensaje[1][pos_ini]
                        self.posiciones_volteadas[1][pos] = self.posiciones_mensaje[1][pos_ini+1]
                        pos_ini += 2

    def interpretar_mensaje(self):
        indice = 0 
        mensaje_interpretado = ''
        while indice < self.tamaño:
            mensaje_interpretado += (self.matriz_alfabeto
                                    [self.posiciones_volteadas[0][indice]]
                                    [self.posiciones_volteadas[1][indice]]
                                    )
            indice += 1
            
        return mensaje_interpretado

    def crear_txt_interpretado(self, ruta, mensaje_interpretado):
        if self.codificacion == 'd':
            mensaje_interpretado = 'e.' + mensaje_interpretado
        if self.codificacion == 'e':
            mensaje_interpretado = 'd.' + mensaje_interpretado
        archivo = open(ruta, 'w', encoding='utf-8')
        archivo.write(mensaje_interpretado)
        archivo.close()


def leer_archivo_con_mensaje(ruta):
    archivo = open(ruta, 'r', encoding='utf-8')
    formato_mensaje = archivo.read()
    archivo.close()
    mensaje_split = formato_mensaje.split('.')
    codificacion = mensaje_split[0]
    mensaje = mensaje_split[1]
    return codificacion, mensaje


ruta = r'all\Python\ejercicios y proyectos\mensaje.txt'
codificacion, mensaje = leer_archivo_con_mensaje(ruta)
mensaje = Mensaje(codificacion, mensaje)
mensaje.identificar_posiciones_letras()

if mensaje.codificacion == 'd':
    mensaje.encriptar_mensaje()
if mensaje.codificacion == 'e':
    mensaje.desencriptar_mensaje()
    
print(mensaje.posiciones_mensaje)
print(mensaje.posiciones_volteadas)

interpretacion = mensaje.interpretar_mensaje()
mensaje.crear_txt_interpretado(ruta, interpretacion)




