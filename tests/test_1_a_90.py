from src import bingo
mi_carton = bingo.generar_carton()

def test_numeros_1_a_90():
    assert bingo.numeros_1_a_90(mi_carton)