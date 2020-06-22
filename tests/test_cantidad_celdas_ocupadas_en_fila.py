from src import bingo
mi_carton = bingo.generar_carton()

def test_cantidad_celdas_ocupadas_en_fila():
    assert bingo.cantidad_celdas_ocupadas_en_fila(mi_carton)