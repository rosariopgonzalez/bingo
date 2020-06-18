from src.bingo import carton

def no_hay_numeros_repetidos(mi_carton):
    for fila in mi_carton:
        for celda in fila:
            if celda != 0: 
                for filaSiguiente in mi_carton:
                    for celda2 in filaSiguiente:
                        if celda == celda2:
                            return False
    return True
