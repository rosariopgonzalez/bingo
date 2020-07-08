import random
import math

def cantidad_celdas_ocupadas(mi_carton):
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda > 0:
                contador += 1
    return contador

def cantidad_celdas_ocupadas_en_fila(mi_fila):
    contador = 0
    for celda in mi_fila:
        if celda != 0:
            contador += 1
    return contador

def cantidad_columnas_una_celda_ocupada(mi_carton):
    contador = 0
    for columna in range(9):
        contador2 = 0
        for fila in range(3):
            if mi_carton[fila][columna] != 0:
                contador2 += 1
        if contador2 == 1:
            contador += 1
    return contador

# Si hay alguna columna vacia, retorna False. Caso contrario, retorna True.
def sin_columnas_vacias(mi_carton):
    for columna in range(9):
        if not(mi_carton[0][columna] or mi_carton[1][columna] or mi_carton[2][columna]):
            return False
    return True

# Si hay alguna fila vacia retorna False, si no True.
def sin_filas_vacias(mi_carton):
    for fila in mi_carton:
        sum = 0
        for celda in fila:
            sum += celda
        if sum == 0:
            return False
    return True

# Si hay numeros repetidos retorna False. Caso contrario, True.
def sin_repetidos(mi_carton):
    aux = mi_carton[0] + mi_carton[1] + mi_carton[2]
    if len(set(aux)) != 16:
        return False
    return True

# Si algun numero esta fuera del rango 1-90 retorna False, si no, True.
def numeros_1_a_90(mi_carton):
    for fila in mi_carton:
        for celda in fila:
            if not(celda >= 0 and celda <= 90):
                return False
    return True

# Si los numeros se encuentran en orden creciente hacia abajo en una columna, retorna True; si no, False.
def crecen_hacia_abajo(mi_carton):
    for columna in range(9):
        if mi_carton[0][columna] != 0:
            if mi_carton[1][columna] != 0:
                if mi_carton[0][columna] > mi_carton[1][columna]:
                    return False
            if mi_carton[2][columna] != 0:
                if mi_carton[0][columna] > mi_carton[2][columna]:
                    return False

        if mi_carton[1][columna] != 0:
            if mi_carton[2][columna] != 0:
                if mi_carton[1][columna] > mi_carton[2][columna]:
                    return False
    return True

# Si los numeros se encuentran en orden creciente hacia la derecha en una fila, retorna True, Si no, false.
def crecen_hacia_derecha(mi_carton):
    x = 0
    y = 9
    for columna in range(9):
        for fila in range(3):
            if mi_carton[fila][columna] != 0:
                if not(x <= mi_carton[fila][columna] <= y):
                    return False
        x += 10
        y += 10
        if y == 89:
            y = 90
    return True

# Si una columna tiene sus tres celdas ocupadas, retorna False. Si no, True.
def sin_columnas_completas(mi_carton):
    for columna in range(9):
        if mi_carton[0][columna] and mi_carton[1][columna] and mi_carton[2][columna]:
            return False
    return True

# Si ninguna fila tiene mas de dos celdas consecutivas vacias, retorna True. Si no, False.
def celdas_vacias_consecutivas(mi_carton):
    for fila in mi_carton:
        contador = 0
        for celda in fila:
            if celda != 0:
                contador = 0
            else:
                contador += 1
            if contador == 3:
                return False
    return True


# Si ninguna fila tiene mas de dos celdas consecutivas ocupadas, retorna True. Si no, False.
def celdas_ocupadas_consecutivas(mi_carton):
    for fila in mi_carton:
        contador = 0
        for celda in fila:
            if celda == 0:
                contador = 0
            else:
                contador += 1
            if contador == 3:
                return False
    return True

def rangos_columnas(mi_carton):
    min_rango = 1
    max_rango = 9
    for c in range (9):
        for f in range (3):
            if mi_carton[f][c] != 0:
                if mi_carton[f][c] >= min_rango and mi_carton[f][c] <= max_rango:
                    return True
        min_rango = max_rango + 1
        max_rango = max_rango + 10
    return False

def carton_de_prueba():
    contador = 0

    carton = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    numeros_carton = 0

    while numeros_carton < 15:
        contador += 1
        if contador == 50 :
            return carton_de_prueba()
        numero = random.randint(1, 90)

        columna = math.floor(numero / 10)
        if columna == 9:
            columna = 8
        celdas_vacias = 0
        for i in range(3):
            if carton[i][columna] == 0:
                celdas_vacias += 1
            if carton[i][columna] == numero:
                celdas_vacias = 0
                break
        if(celdas_vacias < 2):
            continue

        fila = 0
        for j in range(3):
            celdas_vacias = 0
            for i in range(9):
                if carton[fila][i] == 0:
                    celdas_vacias += 1
            if celdas_vacias < 5 or carton[fila][columna] != 0:
                fila += 1
            else:
                break
        if fila == 3:
            continue

        carton[fila][columna] = numero
        numeros_carton += 1
        contador = 0

    for x in range(9):
        celdas_vacias = 0
        for y in range(3):
            if carton[y][x] == 0:
                celdas_vacias += 1
        if celdas_vacias == 3:
            return carton_de_prueba()
    return carton

def generar_carton():
    while True:
        carton = carton_de_prueba()
        if(cantidad_celdas_ocupadas(carton) == 15
        and cantidad_celdas_ocupadas_en_fila(carton[0]) == 5
        and cantidad_celdas_ocupadas_en_fila(carton[1]) == 5
        and cantidad_celdas_ocupadas_en_fila(carton[2]) == 5
        and sin_columnas_vacias(carton)
        and sin_filas_vacias(carton)
        and numeros_1_a_90(carton)
        and crecen_hacia_derecha(carton)
        and crecen_hacia_abajo(carton)
        and sin_repetidos(carton)
        and rangos_columnas(carton)
        and sin_columnas_completas(carton)
        and celdas_ocupadas_consecutivas(carton)
        and celdas_vacias_consecutivas(carton)
        and cantidad_columnas_una_celda_ocupada(carton) == 3):
            break
    return carton

carton = generar_carton()
for fila in carton:
    print(fila)

def carton_false1():
    carton = (
        (0,3,0,5,5,5,0,4,91),
        (1,2,0,0,6,8,7,0,0),
        (3,1,0,14,0,16,0,17,0),
        (0,0,0,0,0,0,0,0,0)
    )
    return carton

def carton_false2(): 
    carton = (
        (0,3,0,5,5,5,0,4,91),
        (1,2,0,0,0,0,0,0,0,0),
        (0,0,0,0,0,0,0,0,0)
    )
    return carton