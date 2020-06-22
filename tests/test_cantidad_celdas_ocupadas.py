from src import bingo
mi_carton = bingo.generar_carton()

def test_cantidad_celdas_ocupadas():
    assert bingo.cantidad_celdas_ocupadas(mi_carton)