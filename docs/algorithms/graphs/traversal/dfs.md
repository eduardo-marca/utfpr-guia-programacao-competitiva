# Busca em Profundidade (DFS)

A Busca em Profundidade (Depth First Search - DFS) é um algoritmo de busca/percurso em grafos que explora o máximo possível cada ramo antes de retroceder. É uma técnica fundamental em teoria dos grafos e é amplamente utilizada em várias aplicações, como resolução de labirintos, análise de redes, e muito mais.

## Exemplo

Considere o seguinte grafo:

![](images/dfs-bfs-reference.drawio.svg#center)

Um algoritmo de DFS começaria a partir do vértice 0, visitando um vizinho não visitado (por exemplo, 1), e continuaria a explorar os vizinhos de 1 (como 2 e 3) antes de retroceder para explorar outros vizinhos de 0 (como 4 e 5). O percurso resultante poderia ser algo como: 0 → 1 → 4 → 7 → 2 → 3 → 5 → 8 → 6 → 9.

![](images/dfs-example.drawio.svg#center)

Perceba que a ordem que visitamos os vizinhos de um vértice pode variar dependendo da implementação, mas a característica principal da DFS é que ela explora profundamente cada caminho antes de retroceder.

## Implementação

A forma mais comum de implementar a DFS é utilizando recursão ou uma pilha e marcando os vértices visitados para evitar ciclos. A seguir, apresentamos uma implementação básica da DFS em C++ usando recursão:

```cpp
vector<int> adj[N];
bool visited[N];

void dfs(int v) {
    if (visited[v]) return;
    visited[v] = true;
    // processa o nodo v
    for (auto u: adj[v]) {
        dfs(u);
    }
}
```
!!! note "Nota"
    O algoritmo de DFS também pode ser implementado usando uma pilha diretamente, ao invés de se usar recursão, já que a própria recursão atua como uma espécie de pilha na memória. Porém isso não é muito comum, pois a própria recursão costuma ser boa o suficiente, e em caso de se usar uma estrutura auxiliar a BFS costuma ser mais simples de implementar.

## Complexidade
- **Tempo:** $O(V + E)$, onde $V$ é o número de vértices e $E$ é o número de arestas no grafo.
- **Espaço:** $O(V)$ devido à pilha de chamadas recursivas e ao armazenamento do vetor de visitados.

## Problemas

### Recomendados

- [Atcoder - Count Connected Components](https://atcoder.jp/contests/abc284/tasks/abc284_c)
- [Codeforces - Kefa and Park](https://codeforces.com/problemset/problem/580/C)
- [CSES - Building Roads](https://cses.fi/problemset/task/1666)
- [CSES - Building Teams](https://cses.fi/problemset/task/1668)
- [CSES - Round Trip](https://cses.fi/problemset/task/1669)

### Adicionais

- [Transformation: from A to B](https://codeforces.com/contest/727/problem/A)
- [Codeforces - Generate a String](https://codeforces.com/contest/710/problem/E)
- [Codeforces - Anton and Tree](https://codeforces.com/contest/734/problem/E)
- [CSES - Counting Rooms](https://cses.fi/problemset/task/1192)
- [Atcoder - Count Simple Paths](https://atcoder.jp/contests/abc284/tasks/abc284_e)
- [Codeforces - Centroids](https://codeforces.com/contest/709/problem/E)

## Outros Recursos

- [Geeks for Geeks  ](https://www.geeksforgeeks.org/dsa/depth-first-search-or-dfs-for-a-graph/)
- [CP-Algorithms](https://cp-algorithms.com/graph/depth-first-search.html)
- [Codeforces - Complete Guide to DFS and Graph Algorithms](https://codeforces.com/blog/entry/150274)
