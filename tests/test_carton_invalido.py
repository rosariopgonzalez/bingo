from src import bingo
carton_false = bingo.carton_false1()

def test_numeros_1_a_90():
    assert not bingo.numeros_1_a_90(carton_false)

def test_crecen_hacia_abajo():
    assert not bingo.crecen_hacia_abajo(carton_false)
    
def test_crecen_hacia_derecha():
    assert not bingo.crecen_hacia_derecha(carton_false)

def test_sin_columnas_completas():
    assert not bingo.sin_columnas_completas(carton_false)

def test_sin_columnas_vacias():
    assert not bingo.sin_columnas_vacias(carton_false)

def test_sin_filas_vacias():
    assert not bingo.sin_filas_vacias(carton_false)


