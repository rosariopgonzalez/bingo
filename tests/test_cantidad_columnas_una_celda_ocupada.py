from src import bingo
mi_carton = bingo.generar_carton()

def test_cantidad_columnas_una_celda_ocupada():
    assert bingo.cantidad_columnas_una_celda_ocupada(mi_carton)