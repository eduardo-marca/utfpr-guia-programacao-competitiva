# Básico de Grafos

Muitos problemas de programação competitiva podem ser modelados como um grafo e usando algoritmos de grafos. Grafos podem ser usados para representar conexões entre objetos, como redes de estradas, amizades em redes sociais, ou até mesmo rotas de voo entre aeroportos. Compreender os conceitos básicos de grafos é essencial para resolver uma ampla variedade de problemas.

## Definição de Grafo

Um grafo é uma estrutura de dados composta por um conjunto de vértices (ou nós) e um conjunto de arestas que conectam pares de vértices.

![](images/graph-example.drawio.svg#center)

### Terminologia Básica

- **Vértices (ou nós)**: Os elementos individuais do grafo.
- **Arestas**: As conexões entre os vértices. Uma aresta pode ser direcionada (indicando uma direção) ou não direcionada (sem direção específica).
- **Grau de um vértice**: O número de arestas conectadas a um vértice. Em grafos direcionados, distinguimos entre grau de entrada (número de arestas que chegam ao vértice) e grau de saída (número de arestas que saem do vértice).
- **Caminho**: Uma sequência de vértices conectados por arestas. Um caminho pode ser simples (sem vértices repetidos) ou pode ter vértices repetidos.
- **Ciclo**: Um caminho que começa e termina no mesmo vértice, sem repetir arestas. Um ciclo simples não repete vértices, exceto o vértice inicial/final.
- **Subgrafo**: Um subconjunto de vértices e arestas de um grafo maior. Todo grafo é subgrafo de si mesmo.

### Conectividade

Um grafo é considerado conectado (ou conexo) se houver um caminho entre qualquer par de vértices. Caso contrário, ele é chamado de desconectado (ou desconexo).

As partes conectadas de um grafo desconectado são chamadas de componentes conectados, componentes conexos ou simplesmente componentes.

![](images/connected-graph.drawio.svg#center)

### Árvores

Uma árvore é um tipo especial de grafo que é conectado e não possui ciclos. Em outras palavras, uma árvore é um grafo acíclico e conectado. As árvores têm várias propriedades importantes, como:

- Uma árvore com $n$ vértices tem exatamente $n-1$ arestas.
- Um caminho entre dois vértices em uma árvore é sempre único.

Essas propriedades das árvores fazem com que existam muitos algoritmos próprios para árvores e que só funcionam com árvores.

Também é comum definir uma hierarquia entre os vértices de uma árvore, onde um vértice é dito ser a raiz da árvore, e à todo vértice (com exceção da raiz) pode ser atribuído um único outro vértice conectado a ele, dito ser o pai do vértice. Dois vértices não podem ser pais um do outro. Essa terminologia é utilizada em alguns algoritmos envolvendo árvores.

![](images/tree.drawio.svg#center)


!!! note "Nota"
    Na prática, qualquer vértice de uma árvore pode ser definido como a raiz da árvore.

### Grafos Direcionados e Não Direcionados

Em um grafo direcionado (ou dígrafo), as arestas têm uma direção associada, indicando a relação de um vértice para outro. As arestas são representadas como pares ordenados (u, v), onde u é o vértice de origem e v é o vértice de destino. Grafos direcionados são úteis para modelar relações assimétricas, como fluxos de tráfego ou dependências entre tarefas.

Grafos que não possuem arestas com uma direção associada são chamados de não direcionados. Grafos não direcionados podem ser modelados como grafos direcionados onde cada aresta $(A, B)$ se torna duas arestas $(A, B)$ e $(B, A)$.

![](images/undirected.drawio.svg#center)

### Grafos Ponderados e Não Ponderados

Em alguns casos, as arestas de um grafo podem ter pesos associados a elas, representando custos, distâncias ou capacidades. Esses grafos são chamados de grafos ponderados. Alguns algoritmos, como o algoritmo de Dijkstra, são projetados para encontrar o caminho mais curto em grafos ponderados.

![](images/weighted.drawio.svg#center)

### Coloração de Grafos

A coloração de grafos é um problema em que se deseja atribuir cores aos vértices de um grafo de forma que vértices adjacentes não compartilhem a mesma cor. A coloração de grafos tem aplicações em problemas de alocação de recursos, como agendamento de tarefas e design de circuitos.

Um grafo é chamado de bipartido se é possível colorir seus vértices com apenas duas cores, de forma que vértices adjacentes tenham cores diferentes. Grafos bipartidos têm propriedades especiais e são frequentemente usados em problemas de correspondência e fluxo.

![](images/color.drawio.svg#center)

### Simplicidade

Um grafo é considerado simples se não possui laços (arestas que conectam um vértice a si mesmo) e não possui múltiplas arestas entre o mesmo par de vértices. Grafos simples são frequentemente usados em teoria dos grafos devido à sua simplicidade e clareza.

![](images/simple.drawio.svg#center)

## Representação de Grafos

Existem várias maneiras de representar grafos em um computador, sendo as mais comuns a matriz de adjacência, lista de adjacência e a lista de arestas.

Como exemplo usaremos o seguinte grafo para as representações.

![](images/graph-reference.drawio.svg#center)

### Lista de Adjacência

O grafo é representado por uma lista de vértices, onde cada vértice contém uma lista de seus vizinhos.

É a forma mais popular de representar grafos, especialmente quando o grafo é esparso (ou seja, possui poucas arestas em relação ao número de vértices).

Pode ser implementada usando um array de `vector` ou um `vector` de `vector`:

```cpp
vector<int> adj[N];
vector<vector<int>> adj(N);
```

Se o grafo for direcionado, cada aresta (u, v) é adicionada apenas à lista de adjacência do vértice u. Se o grafo for não direcionado, a aresta (u, v) é adicionada à lista de adjacência de ambos os vértices u e v.

Se o grafo for ponderado, cada aresta (u, v) pode ser armazenada como um par (v, peso) na lista de adjacência do vértice u.
```cpp
vector<pair<int, int>> adj[N]; // (v, peso)
```

Com a lista de adjacência, é fácil percorrer os vizinhos de um vértice e realizar operações como busca em profundidade (DFS) ou busca em largura (BFS).

```cpp
for(auto u : adj[v]) {
    // processa o vizinho u
}
```

![](images/adj-list.drawio.svg#center)

### Matriz de Adjacência

A matriz de adjacência é uma representação de grafos usando uma matriz bidimensional. Cada célula da matriz indica se existe uma aresta entre dois vértices. Se o grafo for ponderado, a célula pode armazenar o peso da aresta.

A matriz de adjacência é útil para grafos densos (ou seja, grafos com muitas arestas em relação ao número de vértices), mas pode ser ineficiente em termos de espaço para grafos esparsos, pois requer O(V^2) espaço, onde V é o número de vértices.

![](images/adj-matrix.drawio.svg#center)

### Lista de Arestas

A lista de arestas é uma representação de grafos onde todas as arestas do grafo são armazenadas como uma lista de pares de vértices (u, v) em alguma ordem. Esta representação é útil para algoritmos que precisam processar todas as arestas do grafo.

A lista de arestas pode ser implementada com um `vector`:

```cpp
vector<pair<int, int>> edges;
```

Em um grafo ponderado, cada aresta (u, v) pode ser armazenada como um triplo (u, v, peso):

```cpp
vector<tuple<int, int, int>> edges; // (u, v, peso)
```

![](images/edge-list.drawio.svg#center)
