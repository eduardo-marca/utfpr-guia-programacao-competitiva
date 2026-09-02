# Algoritmo de Dijkstra

Dijkstra é um algoritmo que permite encontrar o caminho mais curto entre um vértice de origem e todos os outros vértices de um grafo ponderado. Esse algoritmo funciona apenas em grafos que não possuem arestas com pesos negativos.

## Idea
A idea do algoritmo é manter um conjunto de vértices cujas distâncias a partir da origem já foram calculadas e, a cada iteração, escolher o vértice com a menor distância conhecida para expandir suas arestas e atualizar as distâncias dos vértices adjacentes. O processo continua até que todos os vértices tenham sido processados.

O algoritmo começa inicializando a distância de todos os vértices como infinita, exceto o vértice de origem, que tem distância zero. Em seguida, ele atualiza as distâncias dos vértices adjacentes ao vértice de origem. Então o algoritmo seleciona o vértice com a menor distância conhecida, marca-o como processado e repete o processo de atualização das distâncias dos vértices adjacentes. Esse processo continua até que todos os vértices tenham sido processados.

Isso funciona porque o algoritmo sempre escolhe o vértice com a menor distância conhecida atualmente, garantindo que a distância calculada para cada vértice seja a menor possível.

!!! danger "Arestas Negativas"
    O algoritmo de Dijkstra não funciona corretamente em grafos com arestas de peso negativo. Se o grafo contiver arestas negativas, o algoritmo pode produzir resultados incorretos.

## Complexidade

- Tempo: $O((V + E)\log V)$
- Memória: $O(V+E)$

Onde $V$ é o número de vértices e $E$ é o número de arestas do grafo. A complexidade de tempo é dominada pelo uso da fila de prioridade, que permite selecionar o vértice com a menor distância conhecida em tempo logarítmico.

## Implementação

Esse algoritmo pode ser implementado utilizando uma fila de prioridade (min-heap) para selecionar o vértice com a menor distância conhecida a cada iteração. Abaixo está uma implementação em C++:

```cpp
using pii = pair<int, int>;
vector<vector<pii>>& adj;

// p é opcional, mas útil para recuperar o caminho mais curto
vector<int> dijkstra(int src, vector<int> & p) {
    
    int V = adj.size();
    vector<bool> vis(V, false);
    vector<int> dist(V, INT_MAX);
    priority_queue<pii, vector<pii>, greater<pii>> pq;

    dist[src] = 0;
    pq.emplace(0, src);

    while (!pq.empty()) {
        auto [d, v] = pq.top();
        pq.pop();

        if (vis[v]) continue;

        for (auto &[u, w] : adj[v]) {

            if (dist[v] + w < dist[u]) {
                dist[u] = dist[v] + w;   
                pq.emplace(dist[u], u);
                p[u] = v;
            }
        }
    }

    return dist;
}
```

!!! tip "Dica"
    Também é possível implementar o algoritmo de Dijkstra utilizando uma fila de prioridade padrão do C++ (max-heap) e armazenando as distâncias como valores negativos. No entanto, isso pode tornar o código menos intuitivo e mais difícil de entender, por tanto use isso com cuidado.

    ```cpp
    priority_queue<pii> pq; // max-heap
    pq.emplace(-dist[u], u); // armazenando distâncias como valores negativos
    ```

## Recuperar o Caminho mais Curto

É possível recuperar o caminho mais curto de um vértice de origem para um vértice de destino utilizando um vetor de predecessores $p$. A cada vez que uma distância é atualizada, o vértice predecessor é registrado. Após a execução do algoritmo, o caminho pode ser reconstruído percorrendo os predecessores a partir do vértice de destino até o vértice de origem.

```cpp
vector<int> restore_path(int s, int t, vector<int> const& p) {
    vector<int> path;

    for (int v = t; v != s; v = p[v])
        path.push_back(v);
    path.push_back(s);

    reverse(path.begin(), path.end());
    return path;
}
```

## Problemas

### Recomendados
- [CSES - Shortest Routes I](https://cses.fi/problemset/task/1671)
- [Codeforces - Dijkstra?](https://codeforces.com/problemset/problem/20/C)
- [CSES - Shortest Routes II](https://cses.fi/problemset/task/1672)
- [Codeforces - Jzzhu and Cities](https://codeforces.com/problemset/problem/449/B)
- [Atcoder -Foreign Friends](https://atcoder.jp/contests/abc245/tasks/abc245_g)
- [SPOJ - CCHESS - COSTLY CHESS](https://www.spoj.com/problems/CCHESS/)
- [Codeforces - Complete The Graph](https://codeforces.com/contest/715/problem/B)

### Adicionais
- [CSES - Flight Discount](https://cses.fi/problemset/task/1195)
- [Codeforces - Jzzhu and Cities](https://codeforces.com/problemset/problem/449/B)
- [SPOJ - ADATRIP - Ada and Trip](https://www.spoj.com/problems/ADATRIP/)
- [Codeforces - Shortest Path](https://codeforces.com/contest/59/problem/E)
- [Codeforces - The Classic Problem](https://codeforces.com/problemset/problem/464/E)
- [Codeforces - President and Roads](https://codeforces.com/problemset/problem/567/E)
- [Codeforces - Complete The Graph](https://codeforces.com/problemset/problem/715/B)

## Outros Recursos
- [Geeks for Geeks](https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/)
- [CP-Algorithms](https://cp-algorithms.com/graph/dijkstra.html)
- [Geeks for Geeks - Competitive Programming](https://www.geeksforgeeks.org/dsa/dijkstras-algorithm-for-competitive-programming/)
