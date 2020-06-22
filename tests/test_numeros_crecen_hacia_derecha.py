from src import bingo
mi_carton = bingo.generar_carton()

def test_crecen_hacia_derecha():
    assert bingo.crecen_hacia_derecha(mi_carton)