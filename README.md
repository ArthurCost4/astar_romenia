# Documentação FASE 1

Este código realiza uma exploração da estrutura de dados de um **mapa da Romênia** (`mapa_romenia`) e de uma tabela de **heurísticas para Bucareste** (`heuristica_bucareste`). O objetivo é compreender como os dados do grafo estão organizados e como acessar informações relevantes para algoritmos de busca heurística, como o **A\***.

---

## Passo 2 - Verificação dos Dados

```python
print(f'Quantidade de cidades no mapa: {len(mapa_romenia)}')
print(f'Quantidade de valores de h(n): {len(heuristica_bucareste)}')
```

Exibe:

- O número total de cidades presentes no mapa.
- O número de valores heurísticos disponíveis.

**Objetivo:** verificar se as estruturas de dados foram carregadas corretamente.

---

## Passo 3 - Obtendo os Vizinhos de Arad

```python
vizinhos_arad = mapa_romenia['Arad']

print()
print(f'Vizinhos de Arad: {vizinhos_arad}')
print(f'Tipo do valor: {type(vizinhos_arad)}')
```

Recupera todas as estradas que partem da cidade de **Arad** e exibe:

- A lista de cidades vizinhas;
- O tipo da estrutura armazenada.

**Objetivo:** entender como as conexões do grafo são representadas.

---

## Passo 4 - Acessando uma Estrada Específica

```python
primeira = vizinhos_arad[0]

print()
print(f'Primeira estrada que sai de Arad: {primeira}')
print(f'    posição [0] -> cidade vizinha: {primeira[0]}')
print(f'    posição [1] -> custo em km   : {primeira[1]}')
```

Seleciona a primeira estrada cadastrada para Arad.

Cada estrada é armazenada como uma tupla:

| Posição | Significado |
|----------|-------------|
| `[0]` | Cidade vizinha |
| `[1]` | Distância (custo) em quilômetros |

**Objetivo:** demonstrar como acessar elementos individuais da estrutura.

---

## Passo 5 - Listando Todas as Estradas de Arad

```python
print()
print("Estradas que saem de Arad:")
for vizinho, custo in mapa_romenia['Arad']:
    print(f" Arad -> {vizinho} = {custo}km")
```

Percorre todas as conexões da cidade de Arad e exibe:

- Cidade de destino;
- Distância da estrada.

Exemplo de saída:

```text
Arad -> Zerind = 75km
Arad -> Sibiu = 140km
Arad -> Timisoara = 118km
```

**Objetivo:** mostrar como iterar sobre os vizinhos de um nó do grafo.

---

## Passo 6 - Contagem de Estradas por Cidade

```python
print()
print('Numero de estradas de cada cidade:')
for cidade in mapa_romenia:
    quantidade = len(mapa_romenia[cidade])
    print(f' {cidade:<15} {quantidade} estrada(s)')
```

Percorre todas as cidades do mapa e conta quantas estradas saem de cada uma.

**Objetivo:** identificar o grau de conectividade de cada cidade.

---

## Passo 7 - Consultando Valores Heurísticos

```python
print()
print(f'h(Arad) = {heuristica_bucareste["Arad"]} km em linha reta até Bucareste')
```

Exibe a heurística da cidade de Arad, representando a distância estimada em linha reta até Bucareste.

Em seguida:

```python
print('Para cada vizinho de Arad: custo da estrada e h(vizinho)')
for vizinho, custo in mapa_romenia['Arad']:
    h = heuristica_bucareste[vizinho]
    print(f' {vizinho:<10} estrada = {custo:>3} km  h = {h:>3} km')
```

Mostra para cada cidade vizinha:

- O custo real da estrada;
- O valor heurístico da cidade até Bucareste.

**Objetivo:** comparar custos reais e estimativas heurísticas, conceito fundamental em algoritmos de busca informada.

---

# Documentação da Fase 2
---

## Função `custo_da_estrada`

```python
def custo_da_estrada(origem, destino):
    'devolve os km da estrada de origem -> destino, ou None se ela não existe.'
    for vizinho, custo in mapa_romenia[origem]:
        if vizinho == destino:
            return custo
    return None
```

Procura uma estrada direta entre duas cidades.

### Parâmetros

- `origem`: cidade de partida;
- `destino`: cidade de destino.

### Retorno

- Distância da estrada em quilômetros;
- `None` caso não exista conexão direta.

### Exemplo

```python
custo_da_estrada('Arad', 'Sibiu')
```

Retorna:

```text
140
```

**Objetivo:** consultar rapidamente o custo de uma estrada específica.

---

## Função `custo_do_caminho`

```python
def custo_do_caminho(caminho):
    'Recebe uma lista de cidades e devolve a soma das estradas, em km.'
    total = 0
    for i in range(len(caminho) - 1):
        total = total + custo_da_estrada(caminho[i], caminho[i + 1])
    return total
```

Calcula o custo total de um percurso.

### Parâmetro

- `caminho`: lista contendo as cidades na ordem em que serão percorridas.

### Retorno

- Soma das distâncias entre todas as cidades consecutivas.

### Exemplo

```python
['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
```

Resultado:

```text
450 km
```

**Objetivo:** calcular o custo acumulado de uma rota completa.

---

## Testando a Função `custo_da_estrada`

```python
print(f'Arad -> Sibiu custa {custo_da_estrada("Arad", "Sibiu")} km')
print(f'Arad -> Bucharest custa {custo_da_estrada("Arad", "Bucharest")} (Não existe estrada diretamente)')
```

Realiza duas consultas:

1. Uma estrada que existe (`Arad → Sibiu`);
2. Uma estrada inexistente (`Arad → Bucharest`).

**Objetivo:** validar o funcionamento da busca de estradas.

---

## Comparação Entre Dois Caminhos

### Caminho por Făgăraș

```python
por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
```

### Caminho por Pitești

```python
por_pitesti = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
```

Os custos são calculados utilizando:

```python
custo_do_caminho(...)
```

e exibidos na tela.

### Exemplo de saída

```text
Caminho por Fagaras:
Arad -> Sibiu -> Fagaras -> Bucharest
custo = 450 km

Caminho por Pitesti:
Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
custo = 418 km
```

**Objetivo:** comparar rotas alternativas para chegar ao mesmo destino.

---

## Função `mostrar_g_h_f`

```python
def mostrar_g_h_f(caminho):
```

Esta função calcula os três valores fundamentais do algoritmo **A\***:

| Valor | Significado |
|---------|-------------|
| `g(n)` | custo real percorrido até a cidade atual |
| `h(n)` | estimativa até Bucareste (heurística) |
| `f(n)` | soma de `g(n) + h(n)` |

---

### Cálculo do custo percorrido

```python
g = custo_do_caminho(caminho[:i + 1])
```

Representa a distância já percorrida desde a cidade inicial.

---

### Consulta da heurística

```python
h = heuristica_bucareste[cidade]
```

Obtém a estimativa da distância restante até Bucareste.

---

### Cálculo da função de avaliação

```python
f = g + h
```

Combina custo real e estimativa.

Essa é exatamente a fórmula utilizada pelo algoritmo A*:

```text
f(n) = g(n) + h(n)
```

---

## Análise das Rotas

### Caminho por Făgăraș

```python
mostrar_g_h_f(por_fagaras)
```

Exibe a evolução dos valores `g`, `h` e `f` ao longo do percurso.

---

### Caminho por Pitești

```python
mostrar_g_h_f(por_pitesti)
```

Permite comparar o comportamento da função de avaliação em outra rota.

**Objetivo:** visualizar como o algoritmo A* avalia cada cidade durante a busca.

---

# Desafio 1 - Novo Caminho por Pitești

```python
por_pitesti = [
    'Arad',
    'Timisoara',
    'Lugoj',
    'Mehadia',
    'Drobeta',
    'Craiova',
    'Pitesti',
    'Bucharest'
]
```

Calcula o custo total da rota:

```python
print('custo =', custo_do_caminho(por_pitesti), 'km')
```

**Objetivo:** praticar o uso da função `custo_do_caminho` em trajetos maiores.

---

# Desafio 2 - Análise de g(n), h(n) e f(n)

```python
mostrar_g_h_f(por_pitesti)
```

Analisa os valores de cada cidade ao longo do percurso.

### Pergunta

> Em qual cidade o valor de `f(n)` ultrapassa 418?

### Resposta

```text
Timisoara
```

Isso ocorre porque a soma entre o custo acumulado (`g`) e a estimativa restante (`h`) torna-se maior que o custo da melhor rota conhecida até Bucareste (418 km).

**Objetivo:** compreender como a função de avaliação pode indicar que um caminho está se tornando menos promissor.

---
# Documentação passo 3 
# Documentação do Código

Este código apresenta uma **simulação manual das primeiras etapas do algoritmo A\***, mostrando como a fronteira é criada, como os nós são expandidos e como a escolha do próximo nó ocorre com base na função de avaliação:

```text
f(n) = g(n) + h(n)
```

onde:

- `g(n)` = custo real acumulado até o nó;
- `h(n)` = estimativa restante até Bucareste;
- `f(n)` = custo total estimado.

---

## Passo 1 - Criação do Nó Inicial

```python
inicio = 'Arad'

g = 0
h = heuristica_bucareste[inicio]

no_inicial = (g + h, g, inicio, [inicio])
```

Inicializa a busca pela cidade de **Arad**.

### Componentes do nó

A tupla segue o formato:

```python
(f, g, cidade, caminho)
```

Para Arad:

```python
(366, 0, 'Arad', ['Arad'])
```

onde:

| Valor | Significado |
|---------|-------------|
| `f=366` | custo estimado total |
| `g=0` | nenhum custo percorrido |
| `cidade='Arad'` | cidade atual |
| `['Arad']` | caminho percorrido |

**Objetivo:** criar o primeiro nó que será inserido na fronteira.

---

## Passo 2 - Inicialização da Fronteira

```python
fronteira = [no_inicial]

print(f'Fronteira no começo: {fronteira}')
```

A fronteira representa os nós candidatos à expansão.

Inicialmente contém apenas:

```text
[(366, 0, 'Arad', ['Arad'])]
```

**Objetivo:** armazenar os nós que podem ser explorados.

---

## Passo 3 - Removendo o Primeiro Nó da Fronteira

```python
no = fronteira.pop(0)

f_atual, g_atual, cidade_atual, caminho = no
```

Remove o primeiro elemento da fronteira para expansão.

Resultado:

```python
f_atual = 366
g_atual = 0
cidade_atual = 'Arad'
caminho = ['Arad']
```

Em seguida, os dados do nó são exibidos.

**Objetivo:** selecionar o próximo nó a ser expandido.

---

## Passo 4 - Expansão de Arad

```python
for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
```

Percorre todos os vizinhos de Arad:

- Zerind
- Sibiu
- Timisoara

Para cada vizinho são calculados:

### Novo custo acumulado

```python
novo_g = g_atual + custo_estrada
```

Representa a distância já percorrida.

---

### Nova heurística

```python
novo_h = heuristica_bucareste[vizinho]
```

Representa a distância estimada até Bucareste.

---

### Nova função de avaliação

```python
novo_f = novo_g + novo_h
```

Aplica a fórmula do algoritmo A*.

---

### Novo caminho

```python
novo_caminho = caminho + [vizinho]
```

Adiciona o vizinho ao caminho percorrido.

---

### Inserção na fronteira

```python
fronteira.append(
    (novo_f, novo_g, vizinho, novo_caminho)
)
```

Adiciona o novo nó à fronteira.

**Objetivo:** gerar todos os sucessores do nó atual.

---

## Passo 5 - Exibindo a Fronteira Após a Expansão

```python
print('Fronteira depois de expandir Arad:')
```

Após expandir Arad, a fronteira contém:

```text
(449, 75, Zerind, ...)
(393, 140, Sibiu, ...)
(447, 118, Timisoara, ...)
```

Os nós aparecem na ordem em que foram inseridos.

**Objetivo:** visualizar os nós gerados antes da ordenação.

---

## Passo 6 - Ordenando a Fronteira

```python
fronteira.sort(key=lambda no: no[0])
```

Ordena a fronteira pelo valor de `f`.

Lembrando que:

```python
no[0] = f
```

Após a ordenação:

```text
Sibiu      (393)
Timisoara  (447)
Zerind     (449)
```

**Objetivo:** garantir que o próximo nó expandido seja aquele com menor valor de `f`.

---

## Passo 7 - Escolhendo o Próximo Nó

```python
proximo = fronteira.pop(0)
```

Remove o primeiro elemento da fronteira ordenada.

Resultado:

```text
Sibiu
```

pois possui o menor valor de `f`.

```text
f = 393
```

**Objetivo:** reproduzir o comportamento do algoritmo A* ao escolher o melhor candidato disponível.

---

# Desafio 1 - Expandindo Sibiu Manualmente

O exercício solicita expandir **Sibiu** manualmente.

Os vizinhos de Sibiu são:

```text
Arad
Oradea
Fagaras
Rimnicu Vilcea
```

---

## Iteração 1 - Arad

```python
novo_g = 140 + 140
novo_h = 366
novo_f = 280 + 366
```

Resultado:

```text
f = 646
```

Caminho:

```python
['Arad', 'Sibiu', 'Arad']
```

---

## Iteração 2 - Oradea

```python
novo_g = 140 + 151
novo_h = 380
novo_f = 291 + 380
```

Resultado:

```text
f = 671
```

Caminho:

```python
['Arad', 'Sibiu', 'Oradea']
```

---

## Iteração 3 - Fagaras

```python
novo_g = 140 + 99
novo_h = 176
novo_f = 239 + 176
```

Resultado:

```text
f = 415
```

Caminho:

```python
['Arad', 'Sibiu', 'Fagaras']
```

---

## Iteração 4 - Rimnicu Vilcea

```python
novo_g = 140 + 80
novo_h = 193
novo_f = 220 + 193
```

Resultado:

```text
f = 413
```

Caminho:

```python
['Arad', 'Sibiu', 'Rimnicu Vilcea']
```

---

## Fronteira Ordenada

Após expandir Sibiu:

```text
Rimnicu Vilcea (413)
Fagaras        (415)
Timisoara      (447)
Zerind         (449)
Arad           (646)
Oradea         (671)
```

### Por que Arad apareceu novamente?

Porque o algoritmo implementado até este ponto:

```python
ainda não controla nós visitados
```

Assim, ao expandir Sibiu, a cidade Arad é considerada novamente um vizinho válido e volta para a fronteira.

Isso gera ciclos como:

```text
Arad -> Sibiu -> Arad
```

A correção desse problema ocorre em etapas posteriores, quando são adicionadas estruturas para evitar revisitar estados já explorados.

---

# Desafio 2 - Busca de Custo Uniforme

O A* ordena a fronteira por:

```python
no[0]
```

que corresponde a:

```python
f = g + h
```

O desafio propõe ordenar por:

```python
no[1]
```

ou seja:

```python
g
```

---

## Novo Critério

```python
fronteira.sort(key=lambda no: no[1])
```

Agora o algoritmo escolhe sempre o nó com menor custo acumulado.

---

## Nó Escolhido

O primeiro nó removido será aquele que possuir o menor valor de:

```text
g(n)
```

independentemente da heurística.

---

## Por que isso é Busca de Custo Uniforme?

Porque a decisão de expansão passa a considerar apenas:

```text
g(n)
```

ou seja, o custo real já percorrido.

A heurística deixa de influenciar a escolha.

Matematicamente:

```text
f(n) = g(n)
```

Esse é exatamente o comportamento da **Busca de Custo Uniforme (Uniform Cost Search - UCS)**, que sempre expande o caminho mais barato encontrado até o momento.

---

# Resumo

Este código demonstra as etapas iniciais do algoritmo A*:

1. Criação do nó inicial.
2. Inserção do nó na fronteira.
3. Remoção do próximo nó a ser expandido.
4. Geração dos sucessores.
5. Cálculo dos valores `g`, `h` e `f`.
6. Ordenação da fronteira pelo menor `f`.
7. Escolha do próximo nó para expansão.
8. Identificação do problema de revisitação de estados.
9. Comparação entre A* e Busca de Custo Uniforme.

Esses conceitos são fundamentais para compreender o funcionamento interno de algoritmos de busca inform