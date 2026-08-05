# Algoritmo de Dijkstra

Dijkstra é um algoritmo que permite encontrar o caminho mais curto entre um vértice de origem e todos os outros vértices de um grafo ponderado. Esse algoritmo funciona apenas em grafos que não possuem arestas com pesos negativos.

## Idea
A idea do algoritmo é manter um conjunto de vértices cujas distâncias a partir da origem já foram calculadas e, a cada iteração, escolher o vértice com a menor distância conhecida para expandir suas arestas e atualizar as distâncias dos vértices adjacentes. O processo continua até que todos os vértices tenham sido processados.

O algoritmo começa inicializando a distância de todos os vértices como infinita, exceto o vértice de origem, que tem distância zero. Em seguida, ele atualiza as distâncias dos vértices adjacentes ao vértice de origem. Então o algoritmo seleciona o vértice com a menor distância conhecida, marca-o como processado e repete o processo de atualização das distâncias dos vértices adjacentes. Esse processo continua até que todos os vértices tenham sido processados.

Isso funciona porque o algoritmo sempre escolhe o vértice com a menor distância conhecida atualmente, garantindo que a distância calculada para cada vértice seja a menor possível.

## Complexidade

- Tempo: $O((V + E)\log V)$
- Memória: $O(V+E)$

Onde $V$ é o número de vértices e $E$ é o número de arestas do grafo. A complexidade de tempo é dominada pelo uso da fila de prioridade, que permite selecionar o vértice com a menor distância conhecida em tempo logarítmico.

## Implementação

Esse algoritmo pode ser implementado utilizando uma fila de prioridade (min-heap) para selecionar o vértice com a menor distância conhecida a cada iteração. Abaixo está uma implementação em C++:

```cpp
vector<int> dijkstra(vector<vector<pair<int,int>>>& adj, int src) {

    int V = adj.size();

    // Fila de prioridade (min-heap) armazenando pares de (distância, nó)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    vector<int> dist(V, INT_MAX);

    // Distância do vértice de origem para ele mesmo é 0
    dist[src] = 0;
    pq.emplace(0, src);

    // Processa a fila até que todos os vértices alcançáveis sejam finalizados
    while (!pq.empty()) {
        auto top = pq.top();
        pq.pop();

        int d = top.first;  
        int u = top.second; 

        // Se a distância não for a mais recente menor distância, ignore
        if (d > dist[u])
            continue;

        // Explora todos os vizinhos do vértice atual
        for (auto &p : adj[u]) {
            int v = p.first; 
            int w = p.second; 

            // Se achar um caminho mais curto para v através de u, atualize-o
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;   
                pq.emplace(dist[v], v);
            }
        }
    }

    // Retorna a distância final mais curta a partir da origem
    return dist;
}
```

## Problemas

### Recomendados
- [Shortest Routes I](https://cses.fi/problemset/task/1671)
- [Dijkstra?](https://codeforces.com/problemset/problem/20/C)
- [Shortest Routes II](https://cses.fi/problemset/task/1672)
- [Foreign Friends](https://atcoder.jp/contests/abc245/tasks/abc245_g)
- [CCHESS - COSTLY CHESS](https://www.spoj.com/problems/CCHESS/)
- [Complete The Graph](https://codeforces.com/contest/715/problem/B)

### Adicionais
- [Flight Discount](https://cses.fi/problemset/task/1195)
- [Jzzhu and Cities](https://codeforces.com/problemset/problem/449/B)
- [ADATRIP - Ada and Trip](https://www.spoj.com/problems/ADATRIP/)
- [Shortest Path](https://codeforces.com/contest/59/problem/E)

## Outros Recursos
- [Geeks for Geeks](https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/)
- [CP-Algorithms](https://cp-algorithms.com/graph/dijkstra.html)
- [Geeks for Geeks - Competitive Programming](https://www.geeksforgeeks.org/dsa/dijkstras-algorithm-for-competitive-programming/)
