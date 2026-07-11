# BFS

A Busca em Largura (Breadth First Search - BFS) é um algoritmo de busca em grafos que explora todos os vértices vizinhos antes de avançar para os próximos níveis. É uma técnica fundamental em teoria dos grafos e é amplamente utilizada em várias aplicações, como encontrar o caminho mais curto em grafos não ponderados, análise de redes sociais, e muito mais.

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
