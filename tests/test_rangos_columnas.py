from src import bingo
mi_carton = bingo.generar_carton()

def test_rangos_columnas():
    assert bingo.rangos_columnas(mi_carton)