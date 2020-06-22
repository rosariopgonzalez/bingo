from src import bingo
mi_carton = bingo.generar_carton()

def test_sin_columnas_completas():
    assert bingo.sin_columnas_completas(mi_carton)