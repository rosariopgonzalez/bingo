from src import bingo
mi_carton = bingo.generar_carton()

def test_numeros_1_a_90():
    assert bingo.numeros_1_a_90(mi_carton)

def test_cantidad_celdas_ocupadas():
    assert bingo.cantidad_celdas_ocupadas(mi_carton)

def test_cantidad_celdas_ocupadas_en_fila():
    assert bingo.cantidad_celdas_ocupadas_en_fila(mi_carton)

def test_cantidad_columnas_una_celda_ocupada():
    assert bingo.cantidad_columnas_una_celda_ocupada(mi_carton)

def test_celdas_ocupadas_consecutivas():
    assert bingo.celdas_ocupadas_consecutivas(mi_carton)

def test_celdas_vacias_consecutivas():
    assert bingo.celdas_vacias_consecutivas(mi_carton)

def test_crecen_hacia_abajo():
    assert bingo.crecen_hacia_abajo(mi_carton)

def test_crecen_hacia_derecha():
    assert bingo.crecen_hacia_derecha(mi_carton)

def test_rangos_columnas():
    assert bingo.rangos_columnas(mi_carton)

def test_sin_columnas_completas():
    assert bingo.sin_columnas_completas(mi_carton)

def test_sin_columnas_vacias():
    assert bingo.sin_columnas_vacias(mi_carton)

def test_sin_filas_vacias():
    assert bingo.sin_filas_vacias(mi_carton)

def test_sin_repetidos():
    assert bingo.sin_repetidos(mi_carton)
