from mapa import mapa_romenia, heuristica_bucareste

def busca_a_estrela(inicio, objetivo):
    'Devolve (caminho, custo) do melhor caminho, ou (None, infinito).'
    fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
    explorados = set()

    while fronteira:
        # escolhe o nó de menor f
        fronteira.sort(key=lambda no: no[0])
        # fronteira.sort( key=lambda no: heuristica_bucareste[no[2]])

        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        # teste de objetivo: feito ao RETIRAR o nó, não ao gerar
        # if cidade_atual == objetivo:
            # return caminho, g_atual

        # cidade já explorada por um caminho melhor: descarta
        if cidade_atual in explorados:
            continue
        explorados.add(cidade_atual)

        # gera os filhos e coloca na fronteira
        for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
            if vizinho not in explorados:
                novo_g = g_atual + custo_estrada
                if vizinho == objetivo:
                    return caminho + [vizinho], novo_g
                novo_f = novo_g + heuristica_bucareste[vizinho]
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))
    return None, float('inf')


caminho, custo = busca_a_estrela('Arad', 'Bucharest')
print('Caminho:', ' -> '.join(caminho))
print('Custo :', custo, 'km')
print('Passos :', len(caminho) - 1, 'estradas')


# ----------------------------- Desafios -----------------------------------
# 1 Mude a ordenação para key=lambda no: heuristica_bucareste[no[2]] (só h). Você acabou de escrever a busca gulosa: o resultado vira 450 km. Depois desfaça.

# 2 Mova o teste de objetivo para dentro do for, logo depois de calcular novo_g: if vizinho == objetivo: return caminho + [vizinho], novo_g. O resultado vira 450 km. Explique por quê com a árvore da Fase 6.

# No caso colocando logo após novo_g o resultado vira 450km porque é o instante que Bucharest é gerado a partir de Fagaras, ou seja, não da uma chance de posteriormente encontrar um caminho melhor no nosso caso o de 418 Por isso ao mover o teste para dentro do for, você perde a garantia de eficacia do A*.
