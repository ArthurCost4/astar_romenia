from mapa import mapa_romenia, heuristica_bucareste

# Passo 2
print(f'Quantidade de cidades no mapa: {len(mapa_romenia)}')
print(f'Quantidade de valores de h(n): {len(heuristica_bucareste)}')

# Passo 3 
vizinhos_arad = mapa_romenia['Arad']
print()
print(f'Vizinhos de Arad: {vizinhos_arad}')
print(f'Tipo do valor: {type(vizinhos_arad)}')