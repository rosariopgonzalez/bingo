from src import bingo
mi_carton = bingo.generar_carton()

def test_sin_columnas_vacias():
    assert bingo.sin_columnas_vacias(mi_carton)