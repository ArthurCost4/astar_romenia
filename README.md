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