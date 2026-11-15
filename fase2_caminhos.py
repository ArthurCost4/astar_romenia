from mapa import mapa_romenia, heuristica_bucareste

def custo_da_estrada(origem, destino):
    'devolve os km da estrada de origem -> destino, ou None se ela não existe.'
    for vizinho, custo in mapa_romenia[origem]:
        if vizinho == destino:
            return custo
    return None

def custo_do_caminho(caminho):
    'Recene uma lista de cidades e devolve a soma das estradas, em km.'
    total = 0
    for i in range(len(caminho) - 1):
        total = total + custo_da_estrada(caminho[i], caminho[i + 1])
    return total

print(f'Arad -> Sibiu custa {custo_da_estrada('Arad', 'Sibiu')} km')
print(f'Arad -> Bucharest custa {custo_da_estrada('Arad', 'Bucharest')} (Não existe estrada diretamente)')

por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
por_pitesti = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
print()
print('Caminho por Fagaras:', ' -> '.join(por_fagaras))
print('     custo =', custo_do_caminho(por_fagaras), 'Km')
print('Caminho por Pitesti:', ' -> '.join(por_pitesti))
print(' custo =', custo_do_caminho(por_pitesti), 'km')