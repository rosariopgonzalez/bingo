from src.bingo import carton

def numeros_crecen_hacia_abajo(mi_carton):
    for i in range(0,2):
        for k in range(0,8):
            if mi_carton[i][k] < mi_carton[i+1][k] and mi_carton[i][k] > 0:
                return True
    return False