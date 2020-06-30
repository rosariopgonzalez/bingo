from src import bingo
mi_carton = bingo.generar_carton()

def test_celdas_vacias_consecutivas():
    assert bingo.celdas_vacias_consecutivas(mi_carton)