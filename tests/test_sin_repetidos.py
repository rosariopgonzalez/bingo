from src import bingo
mi_carton = bingo.generar_carton()

def test_sin_repetidos():
    assert bingo.sin_repetidos(mi_carton)