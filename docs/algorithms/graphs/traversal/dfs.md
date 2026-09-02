# Busca em Profundidade (DFS)

A Busca em Profundidade (Depth First Search - DFS) é um algoritmo de busca/percurso em grafos que explora o máximo possível cada ramo antes de retroceder. É uma técnica fundamental em teoria dos grafos e é amplamente utilizada em várias aplicações, como resolução de labirintos, análise de redes, e muito mais.

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
