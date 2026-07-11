# Básico de Grafos

Muitos problemas de programação competitiva podem ser modelados como um grafo e usando algoritmos de grafos. Grafos podem ser usados para representar conexões entre objetos, como redes de estradas, amizades em redes sociais, ou até mesmo rotas de voo entre aeroportos. Compreender os conceitos básicos de grafos é essencial para resolver uma ampla variedade de problemas.

## Definição de Grafo
Um grafo é uma estrutura de dados composta por um conjunto de vértices (ou nós) e um conjunto de arestas que conectam pares de vértices. A terminologia básica de grafos inclui:

### Terminologia Básica
- **Vértices (ou nós)**: Os elementos individuais do grafo.
- **Arestas**: As conexões entre os vértices. Uma aresta pode ser direcionada (indicando uma direção) ou não direcionada (sem direção específica).
- **Grau de um vértice**: O número de arestas conectadas a um vértice. Em grafos direcionados, distinguimos entre grau de entrada (número de arestas que chegam ao vértice) e grau de saída (número de arestas que saem do vértice).
- **Caminho**: Uma sequência de vértices conectados por arestas. Um caminho pode ser simples (sem vértices repetidos) ou pode ter vértices repetidos.
- **Ciclo**: Um caminho que começa e termina no mesmo vértice, sem repetir arestas. Um ciclo simples não repete vértices, exceto o vértice inicial/final.

### Conectividade
Um grafo é considerado conectado (ou conexo) se houver um caminho entre qualquer par de vértices. Caso contrário, ele é chamado de desconectado (ou desconexo).

As partes conectadas de um grafo desconectado são chamadas de componentes conectados, componentes conexos ou simplesmente componentes.

### Árvores
Uma árvore é um tipo especial de grafo que é conectado e não possui ciclos. Em outras palavras, uma árvore é um grafo acíclico e conectado. As árvores têm várias propriedades importantes, como:
- Uma árvore com n vértices tem exatamente n-1 arestas.
- Cada vértice de uma árvore tem exatamente um pai (exceto o vértice raiz).
- Um caminho entre dois vértices em uma árvore é sempre único.

### Grafos Direcionados
Em um grafo direcionado (ou dígrafo), as arestas têm uma direção associada, indicando a relação de um vértice para outro. As arestas são representadas como pares ordenados (u, v), onde u é o vértice de origem e v é o vértice de destino. Grafos direcionados são úteis para modelar relações assimétricas, como fluxos de tráfego ou dependências entre tarefas.

### Grafos Ponderados
Em alguns casos, as arestas de um grafo podem ter pesos associados a elas, representando custos, distâncias ou capacidades. Esses grafos são chamados de grafos ponderados. Alguns algoritmos, como o algoritmo de Dijkstra, são projetados para encontrar o caminho mais curto em grafos ponderados.

### Coloração de Grafos
A coloração de grafos é um problema em que se deseja atribuir cores aos vértices de um grafo de forma que vértices adjacentes não compartilhem a mesma cor. A coloração de grafos tem aplicações em problemas de alocação de recursos, como agendamento de tarefas e design de circuitos.

Um grafo é chamado de bipartido se é possível colorir seus vértices com apenas duas cores, de forma que vértices adjacentes tenham cores diferentes. Grafos bipartidos têm propriedades especiais e são frequentemente usados em problemas de correspondência e fluxo.

### Simplicidade
Um grafo é considerado simples se não possui laços (arestas que conectam um vértice a si mesmo) e não possui múltiplas arestas entre o mesmo par de vértices. Grafos simples são frequentemente usados em teoria dos grafos devido à sua simplicidade e clareza.

## Representação de Grafos
Existem várias maneiras de representar grafos em um computador, sendo as mais comuns a matriz de adjacência, lista de adjacência e a lista de arestas.

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

### Matriz de Adjacência
A matriz de adjacência é uma representação de grafos usando uma matriz bidimensional. Cada célula da matriz indica se existe uma aresta entre dois vértices. Se o grafo for ponderado, a célula pode armazenar o peso da aresta.

A matriz de adjacência é útil para grafos densos (ou seja, grafos com muitas arestas em relação ao número de vértices), mas pode ser ineficiente em termos de espaço para grafos esparsos, pois requer O(V^2) espaço, onde V é o número de vértices.

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
