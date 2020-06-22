from src import bingo
mi_carton = bingo.generar_carton()

def test_sin_filas_vacias():
    assert bingo.sin_filas_vacias(mi_carton)