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

Essas operações servem como base para a implementação de algoritmos de busca como **Busca Gulosa (Greedy Search)** e **A\***.