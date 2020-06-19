from src.bingo import carton

def numeros_crecen_hacia_derecha(mi_carton):
    for i in range(0,8):
        for k in range(0,2):
            if mi_carton[k][i] < mi_carton[k+1][i] and mi_carton[k][i] > 0:
                return True
    return False