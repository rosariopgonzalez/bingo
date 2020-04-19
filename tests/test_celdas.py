from src.bingo import carton

def test_contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    assert contador == 15
    

def test_no_menos_que_quince():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    assert contador > 14

def test_no_mas_que_quince():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    assert contador < 16

def test_min_una_celda_ocupada():
    mi_carton = carton()
    contador = 0

    for i in range(9):
        if (mi_carton[0][i] + mi_carton[1][i] + mi_carton[2][i]) >= 1:
            contador = contador + 1

    assert contador == 9
    