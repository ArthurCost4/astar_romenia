from mapa import mapa_romenia, heuristica_bucareste


def mostrar_fronteira(fronteira):
    partes = []
    for f, g, cidade, caminho in fronteira:
        partes.append(f'{cidade}(f={{f}})')
    print('     fronteira:', ', '.join(partes))

