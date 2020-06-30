from src import bingo
mi_carton = bingo.generar_carton()

def test_celdas_ocupadas_consecutivas():
    assert bingo.celdas_ocupadas_consecutivas(mi_carton)