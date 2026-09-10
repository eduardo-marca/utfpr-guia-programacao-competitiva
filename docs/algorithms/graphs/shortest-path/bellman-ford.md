# Bellman Ford

O algoritmo de Bellman-Ford é um algoritmo para encontrar o caminho mais curto de um único vértice para todos os outros vértices em um grafo ponderado, mesmo que o grafo contenha arestas com pesos negativos. Ele é especialmente útil em situações onde o algoritmo de Dijkstra não pode ser aplicado devido à presença de pesos negativos.

Além disso, o algoritmo de Bellman-Ford pode detectar ciclos de peso negativo no grafo, que são ciclos cujo peso total é negativo. Isso significa que não há um caminho mais curto definido, pois é possível continuar a percorrer o ciclo indefinidamente, reduzindo o peso total do caminho.

## Idea

O algoritmo funciona matendo a distância de cada vértice a partir do vértice inicial. Inicialmente, a distância para o vértice inicial é definida como 0 e para todos os outros vértices como infinito.

Em seguida, o algoritmo busca arestas que diminuam a distância de um vértice para outro. Ele faz isso repetidamente, relaxando todas as arestas do grafo, até não ser mais possível encontrar uma aresta que possa reduzir a distância de algum vértice.

O processo é repetido $V-1$ vezes, onde $V$ é o número de vértices no grafo. Isso garente que o caminho mais curto de um vértice para outro será encontrado, mesmo que haja arestas com pesos negativos.

O algoritmo também verifica se há ciclos de peso negativo no grafo. Se, após $V-1$ iterações, ainda for possível relaxar uma aresta, isso indica a presença de um ciclo de peso negativo.

!!! note
    Na teória, nem sempre é necessário percorrer todas as arestas $V-1$ vezes, pois o algoritmo pode parar antes se não houver mais arestas que possam reduzir a distância de algum vértice. No entanto, para garantir a correção do algoritmo, e por conta do pior caso, é comum percorrer todas as arestas $V-1$ vezes.

## Complexidade

- Tempo: $O(VE)$
- Memória $O(V)$

Onde $V$ é o número de vértices e $E$ é o número de arestas no grafo.

## Implementação

O jeito mais simples de implementar o algoritmo de Bellman-Ford é utilizando uma lista de arestas. A cada iteração, percorremos todas as arestas do grafo e relaxamos cada uma delas.

```cpp
vector<int> distance(n+1);
for (int i = 1; i <= n; i++) distance[i] = INF;
distance[x] = 0;

for (int i = 1; i <= n-1; i++) {
    for (auto e : edges) {
        int v, u, w;
        tie(v, u, w) = e;
        distance[u] = min(distance[u], distance[v]+w);
    }
}
```

## Exemplos

## Problemas

### Recomendados

### Adicionais

## Outros Recursos
