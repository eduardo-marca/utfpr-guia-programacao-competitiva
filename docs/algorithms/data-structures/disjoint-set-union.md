
{% set exercises %}
  recommended:
    - name: Road Construction
      url: https://cses.fi/problemset/task/1676/
      platform: CSES
      difficulty: easy
      topics: [DSU, componentes conexas]
      objective: Acompanhar a quantidade e o tamanho das componentes.
    - name: Road Reparation
      url: https://cses.fi/problemset/task/1675/
      platform: CSES
      difficulty: medium
      topics: [Kruskal, DSU]
      objective: Construir uma árvore geradora mínima.
    - name: Decayed Bridges
      url: "https://atcoder.jp/contests/abc120/tasks/abc120_d?lang=en"
      platform: AtCoder
      difficulty: medium
      topics: [DSU, processamento reverso]
      objective: Adicionar arestas na ordem inversa das remoções.
{% endset %}

# Disjoint Set Union (DSU)

**Dificuldade:** Intermediário  
**Pré-requisitos:** Vetores, árvores e conceitos básicos de grafos  
**Também conhecido como:** Union-Find

## Introdução

Imagine um conjunto de cidades inicialmente desconectadas. Novas estradas são construídas entre pares de cidades, e precisamos responder perguntas como:

- Duas cidades estão conectadas?
- Quantos grupos de cidades conectadas existem?
- Qual é o tamanho do maior grupo?

Uma possibilidade seria executar uma DFS ou BFS sempre que precisássemos verificar a conectividade entre duas cidades. Entretanto, se tivermos muitas operações, essa abordagem pode se tornar lenta.

A estrutura **Disjoint Set Union (DSU)**, também chamada de **Union-Find**, permite manter uma coleção de conjuntos disjuntos, realizando operações de consulta e união de maneira muito eficiente.

Ela é especialmente útil em problemas nos quais os conjuntos são gradualmente unidos.

## Operações fundamentais

A DSU oferece duas operações principais:

- `find(x)`: retorna o representante do conjunto que contém `x`.
- `unite(a, b)`: une os conjuntos que contêm `a` e `b`, caso sejam diferentes.

Podemos determinar se dois elementos pertencem ao mesmo conjunto verificando:

```cpp
find(a) == find(b)
```

A estrutura também pode armazenar informações adicionais, como o tamanho de cada conjunto.

## Como funciona?

Cada conjunto é representado por uma árvore enraizada.

A DSU utiliza um vetor `parent`, no qual `parent[x]` indica o pai do elemento `x`.

O representante de um conjunto é sua raiz, caracterizada por:

```cpp
parent[x] == x
```

Inicialmente, cada elemento forma seu próprio conjunto:

```text
Elementos:  1  2  3  4  5  6
Parent:     1  2  3  4  5  6

Conjuntos:
{1} {2} {3} {4} {5} {6}
```

### Operação find

A operação `find(x)` percorre os pais do elemento `x` até encontrar a raiz.

```cpp
int find(int x) {
    if (parent[x] == x)
        return x;

    return find(parent[x]);
}
```

Por exemplo, considere:

```text
1
└── 2
    └── 3
        └── 4
```

Se executarmos `find(4)`, visitaremos os elementos `4`, `3`, `2` e `1`, retornando `1`.

O problema é que, se as árvores ficarem muito altas, essa operação pode ser lenta.

### Otimização 1: Path Compression

**Path Compression**, ou compressão de caminho, faz com que os elementos visitados durante um `find` passem a apontar diretamente para a raiz.

```cpp
int find(int x) {
    if (parent[x] == x)
        return x;

    return parent[x] = find(parent[x]);
}
```

No exemplo anterior, após executar `find(4)`, a estrutura passa a ser:

```text
    1
  / | \
 2  3  4
```

Isso reduz a profundidade dos elementos visitados, acelerando consultas futuras.

### Otimização 2: Union by Size

Quando unimos dois conjuntos, podemos escolher qual raiz será anexada à outra.

Uma união ingênua pode gerar árvores desnecessariamente altas.

A técnica **Union by Size** sempre conecta a raiz do conjunto menor à raiz do conjunto maior.

Para isso, mantemos um vetor `sz`, armazenando o tamanho de cada conjunto em sua raiz.

```cpp
bool unite(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b)
        return false;

    if (sz[a] < sz[b])
        swap(a, b);

    parent[b] = a;
    sz[a] += sz[b];

    return true;
}
```

A função retorna `true` quando dois conjuntos diferentes foram unidos, e `false` quando os elementos já pertenciam ao mesmo conjunto.

!!! note "Union by Rank"
    Outra otimização comum é **Union by Rank**, que utiliza uma estimativa da altura das árvores em vez do tamanho dos conjuntos.

    Ambas podem ser combinadas com Path Compression e oferecem a mesma complexidade amortizada.

## Exemplo passo a passo

Considere seis cidades, inicialmente sem estradas.

Adicionaremos as seguintes conexões, nessa ordem:

```text
(1, 2)
(2, 3)
(4, 5)
(3, 5)
(2, 5)
(5, 6)
```

Vamos acompanhar os conjuntos existentes após cada operação.

| Operação | Conjuntos | Componentes | Maior tamanho |
|---|---|---:|---:|
| Inicial | {1}, {2}, {3}, {4}, {5}, {6} | 6 | 1 |
| unite(1, 2) | {1,2}, {3}, {4}, {5}, {6} | 5 | 2 |
| unite(2, 3) | {1,2,3}, {4}, {5}, {6} | 4 | 3 |
| unite(4, 5) | {1,2,3}, {4,5}, {6} | 3 | 3 |
| unite(3, 5) | {1,2,3,4,5}, {6} | 2 | 5 |
| unite(2, 5) | {1,2,3,4,5}, {6} | 2 | 5 |
| unite(5, 6) | {1,2,3,4,5,6} | 1 | 6 |

Observe dois detalhes importantes:

1. Ao executar `unite(3, 5)`, unimos conjuntos inteiros, e não apenas os elementos `3` e `5`.
2. A operação `unite(2, 5)` não altera os conjuntos, pois esses elementos já estão conectados.

Esse comportamento torna a DSU ideal para manter a conectividade de um grafo enquanto novas arestas são adicionadas.

## Implementação em C++17

Abaixo temos uma implementação reutilizável de DSU, utilizando as duas otimizações apresentadas.

```cpp
#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> parent, sz;
    int components;

    DSU(int n) : parent(n + 1), sz(n + 1, 1),
                 components(n) {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if (parent[x] == x)
            return x;

        return parent[x] = find(parent[x]);
    }

    bool unite(int a, int b) {
        a = find(a);
        b = find(b);

        if (a == b)
            return false;

        if (sz[a] < sz[b])
            swap(a, b);

        parent[b] = a;
        sz[a] += sz[b];
        components--;

        return true;
    }

    bool same(int a, int b) {
        return find(a) == find(b);
    }

    int size(int x) {
        return sz[find(x)];
    }
};
```

!!! tip "Indexação"
    Esta implementação considera elementos numerados de `1` até `n`. Para problemas com índices de `0` até `n-1`, basta ajustar o tamanho dos vetores.

### Exemplo de aplicação: Construção de estradas

Considere o seguinte problema:

> Existem `N` cidades inicialmente desconectadas. Serão construídas `M` estradas, uma de cada vez. Após cada construção, determine o número de componentes conexas e o tamanho da maior componente.

Podemos resolver o problema utilizando a DSU.

```cpp
#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> parent, sz;
    int components;
    int largest;

    DSU(int n) : parent(n + 1), sz(n + 1, 1),
                 components(n), largest(1) {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if (parent[x] == x)
            return x;

        return parent[x] = find(parent[x]);
    }

    bool unite(int a, int b) {
        a = find(a);
        b = find(b);

        if (a == b)
            return false;

        if (sz[a] < sz[b])
            swap(a, b);

        parent[b] = a;
        sz[a] += sz[b];

        components--;
        largest = max(largest, sz[a]);

        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    DSU dsu(n);

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;

        dsu.unite(a, b);

        cout << dsu.components << " "
             << dsu.largest << "\n";
    }

    return 0;
}
```

**Entrada:**

```text
6 6
1 2
2 3
4 5
3 5
2 5
5 6
```

**Saída:**

```text
5 2
4 3
3 3
2 5
2 5
1 6
```

A atualização do número de componentes ocorre apenas quando dois conjuntos diferentes são unidos.

Já o tamanho da maior componente pode ser atualizado diretamente após cada união bem-sucedida, sem precisar percorrer todos os elementos.

## Análise de complexidade

Considere `N` elementos e `M` operações.

### Inicialização

A inicialização dos vetores exige:

$$
O(N)
$$

### Find e Unite

Com **Path Compression** e **Union by Size**, uma sequência de operações apresenta complexidade amortizada de:

$$
O(\alpha(N))
$$

por operação, onde $\alpha(N)$ é a função inversa de Ackermann.

Essa função cresce extremamente devagar. Para todos os tamanhos de entrada encontrados normalmente em programação competitiva, seu valor é muito pequeno.

Portanto, na prática, as operações podem ser consideradas quase constantes.

!!! warning "Complexidade amortizada"
    Isso não significa que uma operação individual de `find` sempre tenha custo constante.

    A garantia se refere ao custo médio amortizado ao longo de uma sequência de operações.

### Complexidade total

Para o problema de construção de estradas, temos:

$$
\boxed{O(N + M\alpha(N))}
$$

A memória utilizada é:

$$
\boxed{O(N)}
$$

## Aplicações importantes

### 1. Componentes conexas

A DSU permite manter componentes conexas de um grafo não direcionado enquanto novas arestas são adicionadas.

### 2. Detecção de ciclos

Ao adicionar uma aresta `(u, v)` a um grafo não direcionado, se `find(u) == find(v)`, já existe um caminho entre os dois vértices.

Portanto, a nova aresta cria um ciclo.

### 3. Algoritmo de Kruskal

O algoritmo de Kruskal encontra uma árvore geradora mínima de um grafo ponderado e não direcionado.

Ele ordena as arestas por peso e adiciona cada uma apenas se conectar componentes diferentes.

A DSU permite verificar isso eficientemente.

### 4. Processamento de operações em ordem reversa

A DSU é especialmente eficiente para unir conjuntos, mas não oferece suporte direto à separação de conjuntos.

Em alguns problemas envolvendo remoção de arestas, podemos processar as operações em ordem inversa.

Assim, as remoções se tornam adições, permitindo utilizar a DSU normalmente.

Essa técnica é importante em problemas de conectividade offline.

## Exercícios sugeridos

Resolva os problemas na seguinte ordem:

{{ exercise_list(exercises) }}

### Desafio adicional

Modifique a estrutura DSU para responder quantos pares não ordenados de elementos pertencem à mesma componente.

**Dica:** quando duas componentes de tamanhos `a` e `b` são unidas, o número de novos pares conectados é:

$$
a \cdot b
$$

Utilize `long long` para armazenar a resposta.

## Quando não utilizar DSU?

Apesar de eficiente, a DSU não resolve todos os problemas de conectividade.

A estrutura tradicional não é adequada quando precisamos:

- Remover arestas arbitrariamente e atualizar a conectividade online.
- Encontrar o menor caminho entre dois vértices.
- Recuperar o caminho entre dois elementos.
- Trabalhar diretamente com conectividade forte em grafos direcionados.

Nesses casos, outras estruturas e algoritmos podem ser necessários, como DFS, BFS, Dijkstra ou técnicas mais avançadas de conectividade dinâmica.

## Resumo

A Disjoint Set Union é uma estrutura fundamental em programação competitiva, permitindo manter conjuntos disjuntos com operações eficientes de união e consulta.

As principais ideias são:

- Cada conjunto possui um representante.
- `find(x)` encontra o representante de `x`.
- `unite(a, b)` une conjuntos diferentes.
- Path Compression reduz a profundidade dos caminhos.
- Union by Size evita árvores desnecessariamente altas.
- A complexidade amortizada por operação é $O(\alpha(N))$.

Dominar DSU é um passo importante para resolver problemas de conectividade, detecção de ciclos, árvores geradoras mínimas e processamento offline de consultas.
