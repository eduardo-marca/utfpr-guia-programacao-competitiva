# Percurso de Grafos

Alguns problemas podem exigir que você percorra um grafo, passando por todos os seus vértices/arestas e processando esses elementos. Veremos duas formas muito importantes de se percorrer grafos, cada uma com sua forma de percorrer e com suas vantagens e desvantagens.

## Busca em Profundidade (DFS)

A Busca em Profundidade (Depth First Search - DFS) é um algoritmo de busca em grafos que explora o máximo possível cada ramo antes de retroceder. É uma técnica fundamental em teoria dos grafos e é amplamente utilizada em várias aplicações, como resolução de labirintos, análise de redes, e muito mais.

### Implementação

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

### Complexidade
- **Tempo:** $O(V + E)$, onde $V$ é o número de vértices e $E$ é o número de arestas no grafo.
- **Espaço:** $O(V)$ devido à pilha de chamadas recursivas e ao armazenamento do vetor de visitados.

## Busca em Largura (BFS)

A Busca em Largura (Breadth First Search - BFS) é um algoritmo de busca em grafos que explora todos os vértices vizinhos antes de avançar para os próximos níveis. É uma técnica fundamental em teoria dos grafos e é amplamente utilizada em várias aplicações, como encontrar o caminho mais curto em grafos não ponderados, análise de redes sociais, e muito mais.

### Implementação
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

### Complexidade
- **Tempo:** $O(V + E)$, onde $V$ é o número de vértices e $E$ é o número de arestas no grafo.
- **Espaço:** $O(V)$ devido à fila e ao armazenamento do vetor de visitados.
