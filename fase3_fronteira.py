from mapa import mapa_romenia, heuristica_bucareste

inicio = 'Arad'
g = 0 
h = heuristica_bucareste[inicio]
no_inicial = (g +h, g, inicio, [inicio])

fronteira = [no_inicial]
print(f'Fronteira no começo: {fronteira}')

no = fronteira.pop(0)
f_atual, g_atual, cidade_atual, caminho = no
print()
print(f'Nó retirado: {no}')
print(f'    f = {f_atual} | g = {g_atual} | cidade = {cidade_atual} | caminho = {caminho}')
print(f'Fronteira agora: {fronteira}')