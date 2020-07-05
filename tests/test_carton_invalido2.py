from src import bingo
carton_false = bingo.carton_false2()


def test_cantidad_celdas_ocupadas():
    assert bingo.cantidad_celdas_ocupadas(carton_false) != 15

def test_cantidad_celdas_ocupadas_en_fila():
    assert bingo.cantidad_celdas_ocupadas_en_fila(carton_false) != 5

def test_cantidad_columnas_una_celda_ocupada():
    assert bingo.cantidad_columnas_una_celda_ocupada(carton_false) != 3

def test_celdas_ocupadas_consecutivas():
    assert  bingo.celdas_ocupadas_consecutivas(carton_false) 

def test_celdas_vacias_consecutivas():
    assert  bingo.celdas_vacias_consecutivas(carton_false)

def test_rangos_columnas():
    assert  bingo.rangos_columnas(carton_false)