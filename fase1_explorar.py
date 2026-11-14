from mapa import mapa_romenia, heuristica_bucareste

# Passo 2
print(f'Quantidade de cidades no mapa: {len(mapa_romenia)}')
print(f'Quantidade de valores de h(n): {len(heuristica_bucareste)}')

# Passo 3 
vizinhos_arad = mapa_romenia['Arad']
print()
print(f'Vizinhos de Arad: {vizinhos_arad}')
print(f'Tipo do valor: {type(vizinhos_arad)}')

# Passo 4
primeira = vizinhos_arad[0]
print()
print(f'Primeira estrada que sai de Arad: {primeira}')
print(f'    posição [0] -> cidade vizinha: {primeira[0]}')
print(f'    posição [1] -> custo em km   : {primeira[1]}')

# Passo 5 
print()
print("Estradas que saem de Arad:")
for vizinho, custo in mapa_romenia['Arad']:
    print(f" Arad -> {vizinho} = {custo}km")

# Passo 6 
print()
print('Numero de estradas de cada cidade:')
for cidade in mapa_romenia:
    quantidade = len(mapa_romenia[cidade])
    print(f' {cidade:<15} {quantidade} estrada(s)')

# Passo 7
print()
print(f'h(Arad) = {heuristica_bucareste['Arad']} km em linha reta até Bucareste')
print('Para cada vizinho de Arad: custo da estrada e h(vizinho)')
for vizinho, custo in mapa_romenia['Arad']:
    h = heuristica_bucareste[vizinho]
    print(f' {vizinho:<10} estrada = {custo:>3} km  h = {h:>3} km')

## ----------------------------------------------------------------------------
# Desafios
# 1 Cidades com uma estrada apenas
print()
print('Cidades com apenas 1 estrada')
for cidade in mapa_romenia:
    quantidade = len(mapa_romenia[cidade])
    if(quantidade == 1):
        print(f'Cidade: {cidade}')

# 2 Cidades com o h(n) menor do que 200km
print()
print('Cidades com o h(n) menor do que 200')
for cidade in heuristica_bucareste:
    if heuristica_bucareste[cidade] < 200:
        print(cidade)
