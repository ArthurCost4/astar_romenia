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


# ________________________________________ DESAFIO ____________________________
# Troque [1, 2, 3] por range(1, 7). Na rodada 6 sai Bucharest com f = 418 e mesmo assim o programa continua expandindo. O que está faltando? (É exatamente o que a Fase 5 acrescenta.)

for rodada in range(1,7):
    fronteira.sort(key=lambda no: no[0])
    no = fronteira.pop(0)
    cidade = no[2]
    explorados.add(cidade)
    print(f'Rodada {rodada}: expandido {cidade} (f={no[0]}, g={no[1]})')
    fronteira = fronteira + expandir(no, explorados)
    mostrar_fronteira(fronteira)
    print('     explorados:', sorted(explorados))
    print()

# Está faltando uma ordem de parada quando chegar em Bucharest, o codigo em si ainda não entende isso e concluindo ele continua expandindo 'infinitamente'

