from mapa import mapa_romenia, heuristica_bucareste

inicio = 'Arad'
g = 0 
h = heuristica_bucareste[inicio]
no_inicial = (g + h, g, inicio, [inicio])

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
    #print(novo_g)
    novo_h = heuristica_bucareste[vizinho]
    #print(novo_h)
    novo_f = novo_g + novo_h
    #print(novo_f)
    novo_caminho = caminho + [vizinho]
    #print(novo_caminho)
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

proximo = fronteira.pop(0)
print()
print('Próximo nó a expandir:', proximo[2], 'com f =', proximo[0])


#--------------------------- DESAFIO ------------------------------------
# Copie o Passo 4 e expanda Sibiu à mão. A fronteira ordenada deve ser: Rimnicu Vilcea(413), Fagaras(415), Timisoara(447), Zerind(449), Arad(646) e Oradea(671). Por que Arad apareceu? (A Fase 4 resolve.)

# Iteração 1: Arad (140)
novo_g = 140 + 140
novo_h = 366
novo_f = 280 + 366
novo_caminho = ['Arad','Sibiu','Arad']

#Iteração 2: Oradea (151)
novo_g = 140 + 151
novo_h = 380
novo_f = 291 + 380
novo_caminho = ['Arad','Sibiu','Oradea']

# Iteração 3: Fagaras (99)
novo_g = 140 + 99
novo_h = 366
novo_f = 239 + 176
novo_caminho = ['Arad','Sibiu','Fagaras']

# Iteração 4: Rimnicu Vilcea (80)
novo_g = 140 + 80 
novo_h = 193
novo_f = 220 + 193 
novo_caminho = ['Arad', 'Sibiu', 'Rimnicu Vilcea']

# Arad volta porque o codigo em si ainda não filtra já visitadas, então Arad entra de novo com f = 646.