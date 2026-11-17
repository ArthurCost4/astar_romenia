from mapa import mapa_romenia, heuristica_bucareste

def resumo_fronteira(fronteira):
    'Texto curto com a fronteira: Cidade(f) separados por vírgula.'
    return ', '.join(f'{cidade}({f})' for f, g, cidade, caminho in fronteira)

def busca_a_estrela(inicio, objetivo, grafo, heuristica, mostrar=True):
    """Busca A* em grafo. Devolve (caminho, custo) ou (None, infinito).

    Cada nó da fronteira é a tupla (f, g, cidade, caminho); o f fica na
    posição 0 porque é por ele que a fronteira é ordenada.
    """
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]
    explorados = set()
    iteracao = 0

    if mostrar:
        print(f'--- Busca A* de {inicio} para {objetivo} ---')

    while fronteira:
        iteracao = iteracao + 1
        fronteira.sort(key=lambda no: no[0])
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        if mostrar:
            print(f'{iteracao}. Expandido: {cidade_atual} | '
                  f'g(n) ={g_atual}, h(n)={heuristica[cidade_atual]} '
                  f'-> f(n)={f_atual}')

        if cidade_atual == objetivo:
            return caminho, g_atual

        if cidade_atual in explorados:
            continue
        explorados.add(cidade_atual)

        for vizinho, custo_estrada in grafo.get(cidade_atual, []):
            if vizinho not in explorados:
                novo_g = g_atual + custo_estrada
                novo_f = novo_g + heuristica[vizinho]
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

        if mostrar:
            fronteira.sort(key=lambda no: no[0])
            print('     fronteira:', resumo_fronteira(fronteira))

    return None, float('inf')