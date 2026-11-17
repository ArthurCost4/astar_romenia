# Arthur Linhares 
## Como rodar

    python a_estrela.py

## Resultado
Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
(418 km em 4 passos, igual à Figura 3.24 do livro)

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

# Documentação do Código - FASE 4 

Este código apresenta uma evolução da implementação do algoritmo **A\***, introduzindo o conceito de **estados explorados** para evitar ciclos durante a busca. Além disso, simula várias rodadas de expansão dos nós e permite visualizar a evolução da fronteira ao longo da execução.

## Passo 2 - Função `mostrar_fronteira`

```python
def mostrar_fronteira(fronteira):
    partes = []
    for f, g, cidade, caminho in fronteira:
        partes.append(f'{cidade}(f={f})')
    print('     fronteira:', ', '.join(partes))
```

Recebe a fronteira atual e exibe seus elementos de forma resumida.

### Exemplo de saída

```text
fronteira: Sibiu(f=393), Timisoara(f=447), Zerind(f=449)
```

### Informações exibidas

- Cidade armazenada no nó;
- Valor de `f(n)`.

**Objetivo:** facilitar a visualização dos candidatos à expansão.

---

## Passo 3 - Função `expandir`

```python
def expandir(no, explorados):
```

Responsável por gerar os sucessores de um nó.

O nó recebido possui a estrutura:

```python
(f, g, cidade, caminho)
```

---

### Extraindo informações do nó

```python
f_atual, g_atual, cidade_atual, caminho = no
```

Obtém os dados do nó atualmente expandido.

---

### Percorrendo os vizinhos

```python
for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
```

Percorre todas as cidades conectadas à cidade atual.

---

### Ignorando cidades já exploradas

```python
if vizinho in explorados:
    continue
```

Impede que cidades já expandidas sejam processadas novamente.

**Objetivo:** evitar ciclos desnecessários no grafo.

---

### Calculando os novos valores

#### Novo custo acumulado

```python
novo_g = g_atual + custo_estrada
```

Representa o custo real percorrido até o vizinho.

---

#### Novo valor de avaliação

```python
novo_f = novo_g + heuristica_bucareste[vizinho]
```

Aplica a fórmula:

```text
f(n) = g(n) + h(n)
```

---

#### Novo caminho

```python
caminho + [vizinho]
```

Adiciona o novo nó ao caminho percorrido.

---

### Criando o nó filho

```python
filhos.append(
    (novo_f, novo_g, vizinho, caminho + [vizinho])
)
```

Armazena o sucessor gerado.

---

### Retorno da função

```python
return filhos
```

Retorna todos os filhos válidos gerados a partir do nó expandido.

**Objetivo:** produzir os próximos nós candidatos à busca.

---

## Passo 4 - Inicialização da Busca

```python
inicio = 'Arad'
```

Define a cidade inicial.

---

### Criação da fronteira

```python
fronteira = [
    (
        heuristica_bucareste[inicio],
        0,
        inicio,
        [inicio]
    )
]
```

Resultado:

```python
[(366, 0, 'Arad', ['Arad'])]
```

Formato:

```python
(f, g, cidade, caminho)
```

onde:

| Campo | Significado |
|---------|-------------|
| f | g + h |
| g | custo real acumulado |
| cidade | cidade atual |
| caminho | percurso realizado |

---

### Conjunto de explorados

```python
explorados = set()
```

Inicialmente vazio.

**Objetivo:** armazenar cidades que já foram expandidas.

---

## Passo 5 - Laço Principal de Busca

```python
for rodada in range(1, 7):
```

Executa seis rodadas de expansão.

Cada rodada representa uma etapa do algoritmo A*.

---

### Ordenando a Fronteira

```python
fronteira.sort(key=lambda no: no[0])
```

Ordena pelo valor de:

```python
no[0]
```

que corresponde a:

```text
f(n)
```

Assim, o melhor candidato fica na primeira posição.

---

### Removendo o Melhor Nó

```python
no = fronteira.pop(0)
```

Seleciona o nó com menor valor de `f`.

---

### Obtendo a Cidade Atual

```python
cidade = no[2]
```

Extrai o nome da cidade armazenada.

---

### Marcando como Explorada

```python
explorados.add(cidade)
```

Adiciona a cidade ao conjunto de explorados.

**Objetivo:** impedir futuras expansões da mesma cidade.

---

### Exibindo Informações da Rodada

```python
print(
    f'Rodada {rodada}: expandido {cidade} (f={no[0]}, g={no[1]})'
)
```

Mostra:

- cidade expandida;
- valor de `f`;
- valor de `g`.

---

### Gerando os Filhos

```python
fronteira = fronteira + expandir(no, explorados)
```

Adiciona à fronteira todos os sucessores válidos.

---

### Exibindo a Fronteira

```python
mostrar_fronteira(fronteira)
```

Mostra os nós disponíveis para expansão futura.

---

### Exibindo os Explorados

```python
print('explorados:', sorted(explorados))
```

Permite acompanhar quais cidades já foram processadas.

---

## Passo 6 - Evolução da Busca

Durante as rodadas, o algoritmo realizará expansões semelhantes a:

```text
Rodada 1 → Arad
Rodada 2 → Sibiu
Rodada 3 → Rimnicu Vilcea
Rodada 4 → Fagaras
Rodada 5 → Pitesti
Rodada 6 → Bucharest
```

A cada iteração:

1. Escolhe o menor `f`;
2. Expande seus vizinhos;
3. Evita cidades já exploradas;
4. Atualiza a fronteira.

---

# Desafio - O que está faltando?

Ao alterar:

```python
range(1, 3)
```

para

```python
range(1, 7)
```

observa-se que na sexta rodada:

```text
Bucharest é expandida com f = 418
```

Mesmo tendo chegado ao objetivo, o algoritmo continua executando.

---

## Problema

O código ainda não possui uma condição de parada.

Depois de encontrar Bucareste, o laço continua executando:

```python
for rodada in range(...)
```

gerando novas expansões desnecessárias.

---

## O que deveria existir?

Uma verificação como:

```python
if cidade == 'Bucharest':
    break
```

Assim que o objetivo for encontrado.

---

## Por que isso é importante?

O algoritmo A* deve encerrar a busca quando remove da fronteira o nó objetivo com o menor valor de `f`.

Nesse momento:

- a melhor solução já foi encontrada;
- novas expansões não são necessárias.

---

## Resposta do Desafio

> O que está faltando?

Está faltando uma **condição de parada ao alcançar Bucharest**.

Atualmente o programa consegue chegar ao destino, mas não sabe que deve encerrar a busca, continuando a expandir nós desnecessariamente.

---

# Resumo

Este código adiciona um elemento fundamental ao algoritmo A*:

✅ Controle de estados explora*os.

Além disso demonstra:

1. Cri*ção da fronteira inicial.
2. Expan*ão de nós.
3. Evitação de ciclos a*ravés do conjunto `explorados`.
4.*Ordenação da fronteira pelo menor *f`.
5. Escolha do melhor nó para e*pansão.
6. Evolução passo a passo da busca.
7. Identificação da necessidade de uma condição de parada ao atingir o objetivo.

Esses conceitos aproximam a implementação do comportamento real do algoritmo **A\***, preparando o código para encontrar a rota ótima de forma eficiente.

# Documentação do Código - Fase 5

Este código apresenta uma implementação completa do algoritmo **A\*** (*A-Star*), responsável por encontrar o melhor caminho entre duas cidades utilizando tanto o custo já percorrido quanto uma estimativa da distância restante até o objetivo.

A estratégia utilizada é baseada na função:

```text
f(n) = g(n) + h(n)
```

onde:

- `g(n)` = custo real do caminho percorrido;
- `h(n)` = estimativa da distância restante;
- `f(n)` = custo total estimado.

---

## Passo 1 - Definição da Função `busca_a_estrela`

```python
def busca_a_estrela(inicio, objetivo):
```

A função recebe:

- `inicio`: cidade de partida;
- `objetivo`: cidade desejada.

### Retorno

```python
(caminho, custo)
```

ou

```python
(None, float('inf'))
```

caso não exista caminho.

**Objetivo:** executar a busca A* e encontrar a melhor rota entre duas cidades.

---

## Passo 2 - Inicialização da Fronteira

```python
fronteira = [
    (
        heuristica_bucareste[inicio],
        0,
        inicio,
        [inicio]
    )
]
```

Cria o nó inicial.

Formato de cada nó:

```python
(f, g, cidade, caminho)
```

Para Arad:

```python
(366, 0, 'Arad', ['Arad'])
```

onde:

| Campo | Significado |
|---------|-------------|
| f | custo estimado total |
| g | custo acumulado |
| cidade | cidade atual |
| caminho | rota percorrida |

**Objetivo:** inserir o primeiro nó na fronteira.

---

## Passo 3 - Conjunto de Explorados

```python
explorados = set()
```

Armazena as cidades já processadas.

**Objetivo:** evitar expansões repetidas e ciclos no grafo.

---

## Passo 4 - Laço Principal da Busca

```python
while fronteira:
```

O algoritmo continua executando enquanto houver nós para explorar.

**Objetivo:** permitir que a busca avance até encontrar o destino ou esgotar todas as possibilidades.

---

## Passo 5 - Escolha do Melhor Nó

```python
fronteira.sort(key=lambda no: no[0])
```

Ordena a fronteira pelo valor de:

```python
no[0]
```

que corresponde a:

```text
f(n)
```

Ou seja:

```text
f(n) = g(n) + h(n)
```

---

### Remoção do Melhor Candidato

```python
f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)
```

Remove o nó com menor valor de `f`.

**Objetivo:** seguir a estratégia do algoritmo A*, sempre expandindo o nó mais promissor.

---

## Passo 6 - Teste de Objetivo

```python
if cidade_atual == objetivo:
    return caminho, g_atual
```

Verifica se a cidade retirada da fronteira é o destino.

Se for:

- retorna o caminho encontrado;
- retorna o custo total da rota.

**Importante**

O teste é realizado quando o nó é retirado da fronteira e não quando é gerado.

Isso garante que a melhor solução foi encontrada.

---

## Passo 7 - Verificação de Cidade Explorada

```python
if cidade_atual in explorados:
    continue
```

Ignora cidades que já foram processadas anteriormente.

---

### Adicionando aos Explorados

```python
explorados.add(cidade_atual)
```

Marca a cidade atual como visitada.

**Objetivo:** evitar retrabalho e laços infinitos.

---

## Passo 8 - Expansão dos Vizinhos

```python
for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
```

Percorre todas as cidades conectadas à cidade atual.

---

### Ignorando Explorados

```python
if vizinho not in explorados:
```

Somente cidades ainda não exploradas são consideradas.

---

### Calculando o Novo Custo

```python
novo_g = g_atual + custo_estrada
```

Representa o custo acumulado da rota até o vizinho.

---

### Calculando o Novo Valor de Avaliação

```python
novo_f = novo_g + heuristica_bucareste[vizinho]
```

Aplica:

```text
f(n) = g(n) + h(n)
```

---

### Inserindo na Fronteira

```python
fronteira.append(
    (
        novo_f,
        novo_g,
        vizinho,
        caminho + [vizinho]
    )
)
```

Cria o novo nó e o adiciona à fronteira.

**Objetivo:** disponibilizar os próximos candidatos à expansão.

---

## Passo 9 - Falha na Busca

```python
return None, float('inf')
```

Executado apenas quando a fronteira fica vazia.

Significa que nenhum caminho foi encontrado.

---

## Passo 10 - Executando o Algoritmo

```python
caminho, custo = busca_a_estrela(
    'Arad',
    'Bucharest'
)
```

Busca a melhor rota entre:

```text
Arad → Bucharest
```

---

### Exibindo o Resultado

```python
print('Caminho:', ' -> '.join(caminho))
print('Custo :', custo, 'km')
print('Passos :', len(caminho) - 1, 'estradas')
```

Saída esperada:

```text
Caminho:
Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest

Custo:
418 km

Passos:
4 estradas
```

**Objetivo:** apresentar a rota ótima encontrada pelo A*.

---

# Desafio 1 - Transformando em Busca Gulosa

Troque:

```python
fronteira.sort(key=lambda no: no[0])
```

por:

```python
fronteira.sort(
    key=lambda no: heuristica_bucareste[no[2]]
)
```

ou seja:

```text
ordenar apenas pelo h(n)
```

---

## O que muda?

Antes:

```text
f(n) = g(n) + h(n)
```

Depois:

```text
f(n) = h(n)
```

O algoritmo passa a considerar apenas a estimativa de proximidade ao objetivo.

---

## Resultado

O caminho encontrado passa a ser:

```text
Arad
→ Sibiu
→ Fagaras
→ Bucharest
```

com custo:

```text
450 km
```

---

## Por quê?

Porque a Busca Gulosa escolhe sempre a cidade que parece mais próxima do objetivo, ignorando o custo já percorrido.

Ela é mais rápida, mas não garante a melhor solução.

---

# Desafio 2 - Movendo o Teste de Objetivo

Alterar para:

```python
novo_g = g_atual + custo_estrada

if vizinho == objetivo:
    return caminho + [vizinho], novo_g
```

dentro do `for`.

---

## O que acontece?

O resultado também passa a ser:

```text
450 km
```

---

## Por que isso acontece?

Ao expandir **Fagaras**, Bucareste é gerada como vizinha:

```text
Arad
→ Sibiu
→ Fagaras
→ Bucharest
```

com custo:

```text
450 km
```

Nesse momento o algoritmo encerra imediatamente.

---

## Qual o problema?

Ele não permite que a busca continue explorando alternativas.

Pouco depois seria encontrado o caminho:

```text
Arad
→ Sibiu
→ Rimnicu Vilcea
→ Pitesti
→ Bucharest
```

com custo:

```text
418 km
```

que é melhor.

---

## Por que o A* testa o objetivo ao retirar da fronteira?

Porque quando um nó sai da fronteira com o menor valor de `f`, o algoritmo possui garantia de que aquele é o melhor caminho encontrado até então.

Se o teste for feito durante a geração dos filhos:

```python
if vizinho == objetivo
```

essa garantia é perdida.

---

## Resposta do Desafio

> Por que o resultado vira 450 km?

Porque Bucareste é encontrada pela primeira vez através de **Fagaras**, e o algoritmo encerra imediatamente.

Dessa forma ele não tem oportunidade de descobrir posteriormente a rota ótima passando por **Rimnicu Vilcea** e **Pitesti**, que possui custo total de **418 km**.

---

# Resumo

Esta implementação representa uma versão funcional do algoritmo **A\*** e demonstra:

1. Criação e gerenciamento da fronteira.
2. Uso da função de avaliação `f(n) = g(n) + h(n)`.
3. Controle de cidades exploradas.
4. Expansão dos nós sucessores.
5. Teste correto do objetivo.
6. Retorno da rota ótima.
7. Diferença entre A* e Busca Gulosa.
8. Importância de testar o objetivo ao remover um nó da fronteira.

Com essas etapas, o algoritmo encontra corretamente o melhor caminho:

```text
Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest
```

com custo mínimo de:

```text
418 km
```

# Documentação do Código - Fase 6

Este código apresenta uma versão mais completa e organizada do algoritmo **A\***, permitindo:

- acompanhar a evolução da busca passo a passo;
- reutilizar o algoritmo para qualquer origem e destino;
- ativar ou desativar a exibição do processo de busca;
- comparar o comportamento do A\* com a Busca de Custo Uniforme;
- validar automaticamente o resultado esperado.

A função continua utilizando a fórmula clássica:

```text
f(n) = g(n) + h(n)
```

onde:

- `g(n)` = custo real acumulado;
- `h(n)` = estimativa restante até o objetivo;
- `f(n)` = custo total estimado.

---

# Passo 1 - Função `resumo_fronteira`

```python
def resumo_fronteira(fronteira):
```

Gera uma representação resumida da fronteira.

```python
return ', '.join(
    f'{cidade}({f})'
    for f, g, cidade, caminho in fronteira
)
```

### Exemplo

Se a fronteira contiver:

```python
[
    (393, 140, 'Sibiu', ...),
    (447, 118, 'Timisoara', ...),
    (449, 75, 'Zerind', ...)
]
```

a saída será:

```text
Sibiu(393), Timisoara(447), Zerind(449)
```

**Objetivo:** facilitar a visualização dos nós que ainda podem ser expandidos.

---

# Passo 2 - Definição da Função `busca_a_estrela`

```python
def busca_a_estrela(
    inicio,
    objetivo,
    grafo,
    heuristica,
    mostrar=True
):
```

Implementa o algoritmo A* de forma genérica.

### Parâmetros

| Parâmetro | Descrição |
|------------|------------|
| inicio | cidade inicial |
| objetivo | cidade destino |
| grafo | mapa utilizado na busca |
| heuristica | tabela de valores h(n) |
| mostrar | exibe ou não o passo a passo |

### Retorno

```python
(caminho, custo)
```

ou

```python
(None, infinito)
```

quando não existir solução.

---

# Passo 3 - Inicialização da Busca

```python
fronteira = [
    (
        heuristica[inicio],
        0,
        inicio,
        [inicio]
    )
]
```

Cria o nó inicial.

Formato de cada nó:

```python
(f, g, cidade, caminho)
```

Exemplo para Arad:

```python
(366, 0, 'Arad', ['Arad'])
```

---

### Conjunto de Explorados

```python
explorados = set()
```

Armazena as cidades já processadas.

---

### Contador de Iterações

```python
iteracao = 0
```

Permite acompanhar quantos nós foram expandidos até a solução.

---

# Passo 4 - Exibindo Informações Iniciais

```python
if mostrar:
    print(
        f'--- Busca A* de {inicio} para {objetivo} ---'
    )
```

Mostra qual busca será executada.

### Exemplo

```text
--- Busca A* de Arad para Bucharest ---
```

**Objetivo:** identificar claramente a execução atual.

---

# Passo 5 - Laço Principal

```python
while fronteira:
```

A busca continua enquanto houver nós disponíveis.

---

## Incrementando o Número da Iteração

```python
iteracao = iteracao + 1
```

Conta quantas expansões foram realizadas.

---

## Ordenando a Fronteira

```python
fronteira.sort(
    key=lambda no: no[0]
)
```

Ordena pelo valor de:

```python
no[0]
```

que representa:

```text
f(n)
```

---

## Selecionando o Melhor Nó

```python
f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)
```

Retira o nó com menor valor de `f`.

**Objetivo:** seguir a estratégia do A*, sempre expandindo o candidato mais promissor.

---

# Passo 6 - Exibindo o Nó Expandido

```python
print(
    f'{iteracao}. Expandido: {cidade_atual} | '
    f'g(n)={g_atual}, '
    f'h(n)={heuristica[cidade_atual]} '
    f'-> f(n)={f_atual}'
)
```

### Exemplo

```text
1. Expandido: Arad | g(n)=0, h(n)=366 -> f(n)=366
```

**Objetivo:** mostrar exatamente como o algoritmo está avaliando cada cidade.

---

# Passo 7 - Teste de Objetivo

```python
if cidade_atual == objetivo:
```

Verifica se o nó removido da fronteira é o destino.

---

### Encontrando a Solução

```python
return caminho, g_atual
```

Retorna:

- caminho encontrado;
- custo total da rota.

Antes disso:

```python
print(
    f'Objetivo encontrado em {iteracao} iterações'
)
```

### Exemplo

```text
Objetivo encontrado em 6 iterações
```

**Objetivo:** encerrar a busca quando a solução ótima for retirada da fronteira.

---

# Passo 8 - Controle de Explorados

```python
if cidade_atual in explorados:
    continue
```

Ignora cidades já processadas.

---

### Registrando a Cidade

```python
explorados.add(cidade_atual)
```

Marca a cidade atual como explorada.

**Objetivo:** evitar ciclos e expansões redundantes.

---

# Passo 9 - Geração dos Filhos

```python
for vizinho, custo_estrada in grafo.get(cidade_atual, [])
```

Percorre os vizinhos da cidade atual.

---

## Ignorando Nós Já Explorados

```python
if vizinho not in explorados:
```

Impede que cidades processadas voltem para a fronteira.

---

## Calculando o Novo Custo

```python
novo_g = g_atual + custo_estrada
```

Representa o custo real até o vizinho.

---

## Calculando o Novo `f`

```python
novo_f = novo_g + heuristica[vizinho]
```

Aplica:

```text
f(n) = g(n) + h(n)
```

---

## Adicionando à Fronteira

```python
fronteira.append(
    (
        novo_f,
        novo_g,
        vizinho,
        caminho + [vizinho]
    )
)
```

Adiciona o novo candidato à busca.

---

# Passo 10 - Exibindo a Fronteira

```python
fronteira.sort(key=lambda no: no[0])
```

Ordena novamente a fronteira.

---

### Exibição

```python
print(
    '     fronteira:',
    resumo_fronteira(fronteira)
)
```

### Exemplo

```text
fronteira:
Sibiu(393), Timisoara(447), Zerind(449)
```

**Objetivo:** acompanhar visualmente os próximos candidatos.

---

# Passo 11 - Falha da Busca

```python
return None, float('inf')
```

Executado apenas quando não existe caminho possível.

---

# Passo 12 - Função `main`

```python
def main():
```

Responsável pelos testes do programa.

---

## Criando uma Heurística Zerada

```python
h_zero = {c: 0 for c in mapa_romenia}
```

Produz:

```python
{
    'Arad': 0,
    'Sibiu': 0,
    ...
}
```

### O que isso significa?

Como:

```text
f(n) = g(n) + h(n)
```

e:

```text
h(n) = 0
```

temos:

```text
f(n) = g(n)
```

Ou seja:

```text
Busca de Custo Uniforme
```

---

## Executando a Busca

```python
caminho, custo = busca_a_estrela(
    'Arad',
    'Bucharest',
    mapa_romenia,
    h_zero
)
```

Busca o caminho ótimo a partir de Arad.

---

# Passo 13 - Exibindo o Resultado

```python
print(
    'Caminho encontrado:',
    ' -> '.join(caminho)
)
```

### Exemplo

```text
Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
```

---

### Custo Total

```python
print(
    f'Custo real total: {custo} km'
)
```

Resultado:

```text
418 km
```

---

### Número de Passos

```python
len(caminho) - 1
```

Resultado:

```text
4 estradas
```

---

# Passo 14 - Teste de Regressão

```python
if custo == 418 and len(caminho) - 1 == 4:
```

Verifica se o resultado encontrado está igual ao exemplo clássico apresentado no livro.

---

### Resultado Esperado

```text
418 km
4 passos
```

---

### Mensagem de Sucesso

```python
Conferido: igual ao livro
(418 km, 4 passos)
```

**Objetivo:** validar automaticamente o algoritmo.

---

# Passo 15 - Testando Outras Origens

```python
for origem in [
    'Lugoj',
    'Mehadia',
    'Eforie',
    'Iasi'
]:
```

Executa novas buscas para Bucareste utilizando cidades diferentes.

---

### Exemplo

```python
busca_a_estrela(
    origem,
    'Bucharest',
    mapa_romenia,
    heuristica_bucareste,
    mostrar=True
)
```

Para cada cidade o algoritmo:

1. Executa a busca;
2. Mostra as expansões;
3. Exibe o caminho encontrado;
4. Mostra o custo total.

---

# Passo 16 - Ponto de Entrada do Programa

```python
if __name__ == '__main__':
    main()
```

Executa a função principal somente quando o arquivo é rodado diretamente.

**Objetivo:** permitir que o módulo seja reutilizado sem executar automaticamente os testes.

---

# Resumo

Esta versão representa uma implementação completa e reutilizável do algoritmo **A\***.

Ela adiciona:

✅ Exibição detalhada das iterações.  
✅ Visualização da fronteira.  
✅ Controle de cidades exploradas.  
✅ Encerramento correto ao encontrar o objetivo.  
✅ Teste automático de validação.  
✅ Comparação entre A* e Busca de Custo Uniforme.  
✅ Execução para múltiplas cidades de origem.

O resultado esperado para o problema clássico continua sendo:

```text
Arad
→ Sibiu
→ Rimnicu Vilcea
→ Pitesti
→ Bucharest
```

com:

```text
Custo total = 418 km
Passos = 4 estradas
```

que corresponde à solução ótima encontrada pelo algoritmo A*.
