{% set exercises %}
  recommended:
    - name: Message Route
      url: https://cses.fi/problemset/task/1667
      platform: CSES
      difficulty: easy
      topics: [BFS, reconstrução de caminho]
    - name: Labyrinth
      url: https://cses.fi/problemset/task/1193
      platform: CSES
      difficulty: easy
      topics: [BFS, grid]
    - name: Monsters
      url: https://cses.fi/problemset/task/1194
      platform: CSES
      difficulty: medium
      topics: [BFS multi-source, grid]
    - name: Escape Route
      url: https://atcoder.jp/contests/abc405/tasks/abc405_d
      platform: AtCoder
      difficulty: medium
      topics: [BFS, grid]
  additional:
    - name: Shortest Path
      url: https://codeforces.com/contest/59/problem/E
      platform: Codeforces
      difficulty: hard
      topics: [BFS, estados]
    - name: Police Stations
      url: https://codeforces.com/contest/796/problem/D
      platform: Codeforces
      difficulty: medium
      topics: [BFS multi-source, árvores]
{% endset %}

# Busca em Largura (BFS)

A Busca em Largura (Breadth First Search - BFS) é um algoritmo de busca/percurso em grafos que explora todos os vértices vizinhos antes de avançar para os próximos níveis. É uma técnica fundamental em teoria dos grafos e é amplamente utilizada em várias aplicações, como encontrar o caminho mais curto em grafos não ponderados, análise de redes sociais, e muito mais.

## Exemplo

Considere o seguinte grafo:

![](images/dfs-bfs-reference.drawio.svg#center)

Um algoritmo de BFS começaria a partir do vértice 0, visitando todos os vizinhos de 0 (como 1, 2 e 3) antes de avançar para os próximos níveis. O percurso resultante poderia ser algo como: 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9. Ou seja, o algoritmo visita todos os vértices de um nível (a uma mesma distância) antes de passar para o próximo nível.

![](images/bfs-example.drawio.svg#center)

Perceba que a ordem que visitamos os vizinhos de um vértice pode variar dependendo da implementação, mas a característica principal da BFS é que ela explora todos os caminhos de um nível antes de avançar para o próximo nível. Portanto, outra ordem de visitação poderia ser: 0 → 3 → 2 → 1 → 5 → 4 → 6 → 9 → 8 → 7.

## Implementação
A forma mais comum de implementar a BFS é utilizando uma fila e marcando os vértices visitados para evitar ciclos. A seguir, apresentamos uma implementação básica da BFS em C++ usando uma fila:

```cpp
vector<int> adj[N];
bool visited[N];

void bfs(int s) {
    queue<int> q;
    visited[s] = true;
    q.push(s);
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        // processa o nodo v
        for (auto u: adj[v]) {
            if (!visited[u]) {
                visited[u] = true;
                q.push(u);
            }
        }
    }
}
```

## Complexidade
- **Tempo:** $O(V + E)$, onde $V$ é o número de vértices e $E$ é o número de arestas no grafo.
- **Espaço:** $O(V)$ devido à fila e ao armazenamento do vetor de visitados.

## Problemas

{{ exercise_list(exercises) }}

## Outros Recursos

- [CP-Algorithms](https://cp-algorithms.com/graph/breadth-first-search.html)
- [Geeks for Geeks](https://www.geeksforgeeks.org/dsa/bfs-using-stl-competitive-coding/)
