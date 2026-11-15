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

for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]
    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

print()
print('Fronteira depois de expandir Arad (ordem de inserção):')
for item in fronteira:
    print(' ', item)

fronteira.sort(key=lambda no: no[0])
print()
print(f'Fronteira ordenada pelo f (posição 0 da tupla):')
for item in fronteira:
    print(' ', item)