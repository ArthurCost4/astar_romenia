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