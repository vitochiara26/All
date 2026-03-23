import random as ra

def rellenarMatrizArboles(filas, columnas):
    """
    La función `rellenarMatrizArboles` crea una matriz 2D que representa un bosque, donde cada celda
    inicialmente contiene el valor "4", representando un árbol. El número de filas y columnas de la 
    matriz se determina por los parámetros `filas` y `columnas`, respectivamente. La función 
    itera a través de cada filas y columna, llenando cada celda con el valor "4" y luego devuelve
    la matriz completa del bosque. 
    
    :param filas: El parámetro `filas` representa el número de filas que tendrá la matriz 
    del bosque.

    :param columnas: El parámetro `columnas` representa el número de columnas que tendrá 
    la matriz del bosque.

    :return: La función `rellenarMatrizArboles` devuelve una matriz 2D que representa un bosque, 
    donde cada celda contiene el valor "4", indicando que hay un árbol en esa posición.
    """
    bosque = []
    for i in range(0,filas):
        fila_temp = []
        for j in range(0, columnas):
            fila_temp.append("  4")
        bosque.append(fila_temp)
    return bosque


def mostrarMatrizBosque(bosque):
    """
    La función `mostrarMatrizBosque` toma una matriz 2D llamada `bosque` como entrada y construye 
    una cadena de texto que representa visualmente el contenido de la matriz. La función itera a 
    través de cada fila y columna de la matriz, concatenando los valores de cada celda en una 
    cadena llamada `bosque_caracteres`, separando cada fila con un salto de línea. Finalmente, 
    la función devuelve la cadena completa que representa el bosque.

    :param bosque: El parámetro `bosque` es una matriz 2D que representa un bosque, donde cada 
    elemento de la matriz es una cadena que representa el estado de un árbol o una llama en el 
    bosque. La función `mostrarMatrizBosque` toma esta matriz como entrada y construye una cadena 
    de texto que representa visualmente el contenido del bosque, con cada elemento separado por 
    espacios y cada fila separada por saltos de línea.

    :return: La función `mostrarMatrizBosque` devuelve una cadena de texto que representa 
    visualmente el contenido de la matriz `bosque`, donde cada elemento de la matriz se concatena 
    en una cadena con espacios entre ellos y cada fila se separa por un salto de línea. Esta cadena 
    resultante muestra el estado del bosque, incluyendo árboles, llamas y otros elementos 
    representados en la matriz.

    """
    bosque_caracteres = ""  
    for fila in bosque:
        for columna in fila:
            bosque_caracteres += (columna)
        bosque_caracteres += "\n"
    return bosque_caracteres


def mostrarMatrizBosqueEmojis(bosque):
    """ La función `mostrarMatrizBosqueEmojis` toma una matriz 2D llamada `bosque` como entrada y
    construye una cadena de texto que representa visualmente el contenido de la matriz utilizando 
    emojis. La función itera a través de cada fila y columna de la matriz, verificando el valor de 
    cada celda y asignando un emoji correspondiente según el valor encontrado. Por ejemplo, 
    si el valor es " -3", se asigna el emoji de una roca, si es " -2", se asigna el emoji de una 
    gota de agua, y así sucesivamente para diferentes valores. Finalmente, la función devuelve la 
    cadena completa que representa el bosque utilizando emojis.
    
    :param bosque: El parámetro `bosque` es una matriz 2D que representa un bosque, donde cada
    elemento de la matriz es una cadena que representa el estado de un árbol, una llama, una roca, 
    agua u otro elemento en el bosque. La función `mostrarMatrizBosqueEmojis` toma esta matriz como 
    entrada y construye una cadena de texto que representa visualmente el contenido del bosque 
    utilizando emojis. Cada valor en la matriz se mapea a un emoji específico, y la función 
    devuelve una cadena que muestra el estado del bosque con emojis.
    
    :return: La función `mostrarMatrizBosqueEmojis` devuelve una cadena de texto que representa
    visualmente el contenido de la matriz `bosque` utilizando emojis. Cada elemento de la 
    matriz se mapea a un emoji específico según su valor, y la función construye una cadena que
    muestra el estado del bosque con emojis, donde cada fila de la matriz se separa por
    saltos de línea.
    """

    bosque_emojis = ""
    for fila in bosque:
        for columna in fila:
            if columna == " -3":
                bosque_emojis += "\N{ROCK}"
                bosque_emojis += "  "
            elif columna == " -2":
                bosque_emojis += "\N{DROPLET}"
                bosque_emojis += " "
            elif columna == " -1":
                bosque_emojis += "\N{CLOUD WITH TORNADO}" 
                bosque_emojis += "  "
            elif columna == "  0":
                bosque_emojis += "\N{HIGH BRIGHTNESS SYMBOL}"
                bosque_emojis += " "
            elif columna == "  1":
                bosque_emojis += "\N{CANDLE}\N{VARIATION SELECTOR-16}"
                bosque_emojis += "  "
            elif columna == "  2":
                bosque_emojis += "\N{COLLISION SYMBOL}"
                bosque_emojis += " "
            elif columna == "  3":
                bosque_emojis += "\N{FIRE}"
                bosque_emojis += " "
            elif columna == "  4":
                bosque_emojis+= "\N{DECIDUOUS TREE}"
                bosque_emojis += " "
        bosque_emojis += "\n"
    return bosque_emojis


def crearNoQuemables(filas, columnas, bosque):
    """ La función `crearNoQuemables` toma tres parámetros: `filas`, `columnas` y `bosque`. 
    La función tiene como objetivo agregar elementos no quemables al bosque representado por la 
    matriz `bosque`. Para lograr esto, la función calcula un número aleatorio de elementos no 
    quemables basado en el tamaño del bosque (filas*columnas) y luego selecciona aleatoriamente 
    posiciones en la matriz para colocar estos elementos. Los elementos no quemables pueden ser 
    rocas, agua u otros obstáculos que impiden la propagación del fuego. La función utiliza la 
    biblioteca `random` para generar números aleatorios y seleccionar posiciones en la matriz. 
    Finalmente, la función devuelve la matriz `bosque` actualizada con los elementos no quemables. 

    :param filas: El parámetro `filas` representa el número de filas en la matriz `bosque`.
    Es utilizado para determinar el tamaño del bosque y calcular la cantidad de elementos no 
    quemables que se agregarán a la matriz. 

    :param columnas: El parámetro `columnas` representa el número de columnas en la matriz `bosque`.
    Es utilizado para determinar el tamaño del bosque y calcular la cantidad de elementos no 
    quemables que se agregarán a la matriz.
    """
    max_rand = int(((filas*columnas) / 2) + 1)
    porcent_no_quemables = ra.randint(max_rand // 3 , max_rand)
    opciones_por_seleccionar = [" -3", " -2", "  4"]
    
    for _ in range(0, porcent_no_quemables):
        objeto_por_colocar = ra.choice(opciones_por_seleccionar)
        fila = ra.randint(0, filas-1)
        columna = ra.randint(0, columnas-1)
        bosque[fila][columna] = objeto_por_colocar
    
    return bosque 


def crearLlamas(cantidad_llamas, filas, columnas, bosque):
    """ La función `crearLlamas` toma cuatro parámetros: `cantidad_llamas`, `filas`, `columnas` y
    `bosque`. El propósito de esta función es agregar llamas al bosque representado por
    la matriz `bosque`. La función genera posiciones aleatorias dentro de la matriz para colocar las
    llamas, asegurándose de que no se coloquen en celdas que ya contienen elementos no quemables 
    como rocas o agua. Dependiendo del valor de la celda donde se intente colocar una llama, la 
    función actualiza el estado de la llama o del árbol en esa posición. Por ejemplo, si la celda 
    ya tiene un árbol, la llama se hace más grande, mientras que si la celda tiene agua, la llama 
    se extingue. La función utiliza la biblioteca `random` para generar posiciones aleatorias y 
    devuelve la matriz `bosque` actualizada con las llamas colocadas en las posiciones 
    correspondientes. 

    :param cantidad_llamas: El parámetro `cantidad_llamas` representa la cantidad de llamas que se
    desean crear dentro del bosque. Este valor se utiliza para determinar cuántas veces se debe
    iterar para colocar las llamas en la matriz `bosque`. La función generará posiciones aleatorias
    dentro de la matriz para colocar cada llama, asegurándose de que no se coloquen en celdas que ya
    contienen elementos no quemables como rocas o agua.

    :param filas: El parámetro `filas` representa el número de filas en la matriz `bosque`. Es
    utilizado para determinar el tamaño del bosque y calcular la cantidad de elementos no 
    quemables que se agregarán a la matriz. 

    :param columnas: El parámetro `columnas` representa el número de columnas en la matriz `bosque`.
    Es utilizado para determinar el tamaño del bosque y calcular la cantidad de elementos no 
    quemables que se agregarán a la matriz.

    :param bosque: El parámetro `bosque` es una matriz 2D que representa el estado del bosque, 
    donde cada celda puede contener diferentes valores que representan árboles, llamas, rocas, agua 
    u otros elementos. La función `crearLlamas` toma esta matriz como entrada y actualiza su 
    contenido al colocar llamas en posiciones aleatorias dentro del bosque, asegurándose de que no
    se coloquen en celdas que ya contienen elementos no quemables. La función devuelve la matriz 
    `bosque` actualizada con las llamas colocadas en las posiciones correspondientes. 
    
    """
    llama_num = 1
    for _ in range(cantidad_llamas):
        lim_i = ra.randint(0, filas-1)
        lim_j = ra.randint(0, columnas-1)
        if int(bosque[lim_i][lim_j]) >= 4:
            bosque[lim_i][lim_j] = "  0"
        elif int(bosque[lim_i][lim_j]) == -2:
            print(f"La llama #{llama_num} cayó en agua {lim_i, lim_j} y se extinguió.")
        elif int(bosque[lim_i][lim_j]) == 0:
            print(f"La llama #{llama_num} cayó sobre otra {lim_i, lim_j} y se hizo grande.")
            bosque[lim_i][lim_j] = "  1"
        elif int(bosque[lim_i][lim_j]) == 1:
            print(f"La llama #{llama_num} cayó sobre otra {lim_i, lim_j} y se hizo mas grande.")
            bosque[lim_i][lim_j] = "  2"
        elif int(bosque[lim_i][lim_j]) == 2:
            print(f"La llama #{llama_num} cayó en otra {lim_i, lim_j} y se hizo mucho mas grande")
            bosque[lim_i][lim_j] = "  3"
        elif int(bosque[lim_i][lim_j]) == -3:
            print(f"La llama #{llama_num} cayó sobre una roca {lim_i, lim_j} y no hizo combustion.")
        llama_num += 1       
    return bosque


def incrementarLLamas(filas, columnas, bosque):
    """
    La función `incrementarLLamas` toma tres parámetros: `filas`, `columnas` y `bosque`. El 
    propósito de esta función es actualizar el estado de las llamas en el bosque representado por 
    la matriz `bosque`. La función itera a través de cada celda de la matriz y verifica el valor de 
    cada celda. Si el valor de la celda es "  0", se actualiza a "  1", si es "  1", se actualiza 
    a "  2", y así sucesivamente hasta llegar a "  3". Si la celda ya tiene el valor "  3", 
    se actualiza a " -1", lo que podría representar que la llama se ha extinguido o ha alcanzado 
    su máximo nivel. La función devuelve la matriz `bosque` actualizada con el nuevo estado de las
    llamas después de haber sido incrementadas.

    :param filas: El parámetro `filas` representa el número de filas en la matriz `bosque`. Es
    utilizado para iterar a través de cada fila de la matriz y actualizar el estado de las llamas 
    en el bosque. 

    :param columnas: El parámetro `columnas` representa el número de columnas en la matriz `bosque`.
    Es utilizado para iterar a través de cada columna de la matriz y actualizar el estado de las
    llamas en el bosque.

    :param bosque: El parámetro `bosque` es una matriz 2D que representa el estado del bosque,
    donde cada celda puede contener diferentes valores que representan árboles, llamas, rocas,
    agua u otros elementos. La función `incrementarLLamas` toma esta matriz como entrada y actualiza
    su contenido al incrementar el estado de las llamas en el bosque. La función itera a través de 
    cada celda de la matriz y verifica el valor de cada celda para determinar cómo actualizar el 
    estado de las llamas. La función devuelve la matriz `bosque` actualizada con el nuevo estado de 
    las llamas después de haber sido incrementadas.

    :return: La función `incrementarLLamas` devuelve la matriz `bosque` actualizada con el nuevo 
    estado de las llamas después de haber sido incrementadas. Cada celda de la matriz se actualiza
    según su valor actual, incrementando el estado de las llamas o marcándolas como extinguida si 
    ya han alcanzado su máximo nivel. La función devuelve la matriz completa del bosque con las 
    llamas actualizadas.

    """
    for filas in range(0,filas):
        for columna in range(0, columnas):
            if bosque[filas][columna] == "  0":
                bosque[filas][columna] = "  1"

            elif bosque[filas][columna] == "  1":
                bosque[filas][columna] = "  2"

            elif bosque[filas][columna] == "  2":
                bosque[filas][columna] = "  3"

            elif bosque[filas][columna] == "  3":
                bosque[filas][columna] = " -1"
    return bosque


def propagacionLlamas(filas, columnas, bosque):
    """
    La función `propagacionLlamas` toma tres parámetros: `filas`, `columnas` y `bosque`. El
    propósito de esta función es simular la propagación de las llamas en el bosque representado por
    la matriz `bosque`. La función itera a través de cada celda de la matriz y verifica si el valor 
    de la celda es "  3", lo que podría representar una llama en su máximo nivel. Si se encuentra 
    una celda con este valor, la función verifica las celdas adyacentes (arriba, abajo, izquierda, 
    derecha) para determinar si la llama puede propagarse a esas celdas. Si las celdas adyacentes 
    contienen un valor mayor a "  3", se actualizan a "  0", lo que podría representar que la llama 
    ha propagado a esa celda. La función también maneja casos especiales para las celdas en los 
    bordes del bosque para evitar errores de índice. Finalmente, la función devuelve la matriz 
    `bosque` actualizada con el nuevo estado después de la propagación de las llamas.
    
    :param filas: El parámetro `filas` representa el número de filas en la matriz `bosque`. Es
    utilizado para iterar a través de cada fila de la matriz y simular la propagación de las llamas 
    en el bosque.

    :param columnas: El parámetro `columnas` representa el número de columnas en la matriz `bosque`.
    Es utilizado para iterar a través de cada columna de la matriz y simular la propagación de las
    llamas en el bosque.

    :param bosque: El parámetro `bosque` es una matriz 2D que representa el estado del bosque,
    donde cada celda puede contener diferentes valores que representan árboles, llamas, rocas, 
    agua u otros elementos. La función `propagacionLlamas` toma esta matriz como entrada y 
    simula la propagación de las llamas en el bosque. La función itera a través de cada celda de la 
    matriz y verifica si el valor de la celda es "  3", lo que podría representar una llama en su 
    máximo nivel. Si se encuentra una celda con este valor, la función verifica las celdas 
    adyacentes (arriba, abajo, izquierda, derecha) para determinar si la llama puede propagarse a 
    esas celdas. Si las celdas adyacentes contienen un valor mayor a "  3", se actualizan a "  0", 
    lo que podría representar que la llama ha propagado a esa celda. La función también maneja casos
    especiales para las celdas en los bordes del bosque para evitar errores de índice. Finalmente, 
    la función devuelve la matriz `bosque` actualizada con el nuevo estado después de la propagación
    de las llamas.

    """
    
    for fila in range(0,filas):
        for columna in range(0, columnas):
            if bosque[fila][columna] == "  3":
                # Mirar en 4 direcciones
                if 0 < fila < filas-1 and 0 < columna < columnas-1:
                    if int(bosque[fila-1][columna]) > 3:
                        bosque[fila-1][columna] = "  0"
                    if int(bosque[fila][columna+1]) > 3:
                        bosque[fila][columna+1] = "  0"
                    if int(bosque[fila+1][columna]) > 3:
                        bosque[fila+1][columna] = "  0"
                    if int(bosque[fila][columna-1]) > 3:
                        bosque[fila][columna-1] = "  0"
                elif fila == 0 and 0 < columna < columnas-1:
                    # Mirar en 3 direcciones (derecha, abajo, izquierda)
                    if int(bosque[fila][columna+1]) > 3:
                        bosque[fila][columna+1] = "  0"
                    if int(bosque[fila+1][columna]) > 3:
                        bosque[fila+1][columna] = "  0"
                    if int(bosque[fila][columna-1]) > 3:
                        bosque[fila][columna-1] = "  0"
                elif 0 < fila < filas-1 and columna == columnas-1:
                    # Mirar en 3 direcciones (arriba, abajo, izquierda)
                    if int(bosque[fila-1][columna]) > 3:
                        bosque[fila-1][columna] = "  0"
                    if int(bosque[fila+1][columna]) > 3:
                        bosque[fila+1][columna] = "  0"
                    if int(bosque[fila][columna-1]) > 3:
                        bosque[fila][columna-1] = "  0"
                elif fila == filas-1 and 0 < columna < columnas-1:
                    # Mirar en 3 direcciones (derecha, izquierda, arriba)
                    if int(bosque[fila][columna+1]) > 3:
                        bosque[fila][columna+1] = "  0"
                    if int(bosque[fila][columna-1]) > 3:
                        bosque[fila][columna-1] = "  0"
                    if int(bosque[fila-1][columna]) > 3:
                        bosque[fila-1][columna] = "  0"
                elif 0 < fila < filas-1 and columna == 0:
                    # Mirar en 3 direcciones (izquierda, derecha, abajo)
                    if int(bosque[fila-1][columna]) > 3:
                        bosque[fila-1][columna] = "  0"
                    if int(bosque[fila][columna+1]) > 3:
                        bosque[fila][columna+1] = "  0"
                    if int(bosque[fila+1][columna]) > 3:
                        bosque[fila+1][columna] = "  0"
                elif fila == 0 and columna == 0 : 
                    # Mirar en 2 direcciones (derecha, abajo)
                    if int(bosque[fila][columna+1]) > 3:
                        bosque[fila][columna+1] = "  0"
                    if int(bosque[fila+1][columna]) > 3:
                        bosque[fila+1][columna] = "  0"
                elif fila == 0 and columna == columnas-1:
                    # Mirar en 2 direcciones (izquierda, abajo)
                    if int(bosque[fila+1][columna]) > 3:
                        bosque[fila+1][columna] = "  0"
                    if int(bosque[fila][columna-1]) > 3:
                        bosque[fila][columna-1] = "  0"
                elif fila == filas-1 and columna == 0:
                    # Mirar en 2 direcciones (arriba, derecha)
                    if int(bosque[fila-1][columna]) > 3:
                        bosque[fila-1][columna] = "  0"
                    if int(bosque[fila][columna+1]) > 3:
                        bosque[fila][columna+1] = "  0"
                elif fila == filas-1 and columna == columnas-1:
                    # Mirar en 2 direcciones (arriba, izquierda)
                    if int(bosque[fila-1][columna]) > 3:
                        bosque[fila-1][columna] = "  0"
                    if int(bosque[fila][columna-1]) > 3:
                        bosque[fila][columna-1] = "  0"
    return bosque
