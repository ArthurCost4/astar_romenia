from mapa import mapa_romenia, heuristica_bucareste

def resumo_fronteira(fronteira):
    'Texto curto com a fronteira: Cidade(f) separados por vírgula.'
    return ', '.join(f'{cidade}({f})' for f, g, cidade, caminho in fronteira)