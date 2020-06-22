from src import bingo
mi_carton = bingo.generar_carton()

def test_crecen_hacia_abajo():
    assert bingo.crecen_hacia_abajo(mi_carton)