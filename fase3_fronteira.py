from mapa import mapa_romenia, heuristica_bucareste

inicio = 'Arad'
g = 0 
h = heuristica_bucareste[inicio]
no_inicial = (g +h, g, inicio, [inicio])

fronteira = [no_inicial]
print(f'Fronteira no começo: {fronteira}')