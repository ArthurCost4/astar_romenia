from mapa import mapa_romenia, heuristica_bucareste


def mostrar_fronteira(fronteira):
    partes = []
    for f, g, cidade, caminho in fronteira:
        partes.append(f'{cidade}(f={{f}})')
    print('     fronteira:', ', '.join(partes))


def expandir(no, explorados):
    "Devolve a lista de nós filhos, pulando cidades já exploradas."
    f_atual, g_atual, cidade_atual, caminho = no
    filhos = []
    for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
        if vizinho in explorados:
            continue
        novo_g = g_atual + custo_estrada
        novo_f = novo_g + heuristica_bucareste[vizinho]
        filhos.append((novo_f, novo_g, vizinho, caminho + [vizinho]))
    return filhos

inicio = 'Arad'
fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
explorados = set()

for rodada in [1,2,3]:
    fronteira.sort(key=lambda no: no[0])
    no = fronteira.pop(0)
    cidade = no[2]
    explorados.add(cidade)
    print(f'Rodada {rodada}: expandido {cidade} (f={no[0]}, g={no[1]})')
    fronteira = fronteira + expandir(no, explorados)
    mostrar_fronteira(fronteira)
    print('     explorados:', sorted(explorados))
    print()