{% set exercises %}
  recommended:
    - name: Game of Stones
      url: https://codeforces.com/problemset/problem/768/E
      platform: Codeforces
      difficulty: hard
      topics: [Grundy, mex, jogo de retirada]
      objective: Calcule Grundy numbers para regras de remoção que dependem do estado.
    - name: Arpa and a game with Mojtaba
      url: https://codeforces.com/contest/850/problem/C
      platform: Codeforces
      difficulty: hard
      topics: [Sprague-Grundy, fatoração]
      objective: Transforme números fatorados em subgames independentes.
  additional:
    - name: Interval Game 2
      url: https://atcoder.jp/contests/abc206/tasks/abc206_f
      platform: AtCoder
      difficulty: hard
      topics: [Grundy, intervalos, mex]
      objective: Modele movimentos que dividem intervalos em componentes independentes.
{% endset %}

# Números de Grundy

O **Grundy number** de uma posição é um inteiro não negativo que representa seu comportamento estratégico em jogos imparciais normais. Uma posição com Grundy `g` é equivalente, para fins de jogo, a uma pilha de Nim de tamanho `g`.

## 1. Mex e definição recursiva

`mex` (*minimum excluded*) de um conjunto é o menor inteiro não negativo ausente:

$$
\operatorname{mex}(\{0,1,3\})=2,\qquad \operatorname{mex}(\varnothing)=0
$$

Para uma posição `v`:

$$
g(v)=\operatorname{mex}\{g(u)\mid v\to u\}
$$

Em particular, posições terminais têm Grundy 0. A definição é uma DP sobre o grafo acíclico de estados.

```cpp
vector<int> grundy_subtraction(int max_stones, const vector<int>& moves) {
    vector<int> grundy(max_stones + 1, 0);
    for (int stones = 1; stones <= max_stones; stones++) {
        vector<char> seen(moves.size() + 1, false);
        for (int take : moves) {
            if (take <= stones && grundy[stones - take] <= static_cast<int>(moves.size())) {
                seen[grundy[stones - take]] = true;
            }
        }
        while (seen[grundy[stones]]) grundy[stones]++;
    }
    return grundy;
}
```

Para `moves={1,3,4}`, os valores iniciais são `0, 1, 0, 1, 2, 3, 2, 0, ...`. Observe que Grundy não é, em geral, o tamanho da pilha nem apenas `P/N`.

## 2. Relação com posições vencedoras

Uma posição é perdedora se e somente se seu Grundy number é 0.

**Demonstração.** Se `g(v)=0`, o valor 0 não aparece em nenhum sucessor; portanto, todos eles têm Grundy não nulo e são vencedores. Se `g(v)>0`, como `g(v)` é o `mex`, o valor 0 aparece entre os sucessores; há uma jogada para uma posição perdedora. Isso é exatamente a recorrência `P/N`.

O valor adicional guarda mais informação: ele permitirá combinar posições independentes por XOR.

## 3. Memoização em um grafo de estados

Quando os estados não são inteiros em ordem crescente, use DFS com memoização. O grafo precisa ser acíclico ou ter uma medida que sempre diminui.

```cpp
int grundy_dag(int v, const vector<vector<int>>& graph, vector<int>& memo) {
    if (memo[v] != -1) return memo[v];

    vector<char> seen(graph[v].size() + 1, false);
    for (int next : graph[v]) {
        int value = grundy_dag(next, graph, memo);
        if (value <= static_cast<int>(graph[v].size())) seen[value] = true;
    }

    int value = 0;
    while (seen[value]) value++;
    return memo[v] = value;
}
```

Inicialize `memo` com `-1`; vértices sem saída recebem `mex(∅)=0`. Se o estado possuir ciclos, não use essa DFS sem antes resolver a possibilidade de empates.

## 4. Movimentos que dividem o jogo

Às vezes uma jogada quebra uma componente em duas partes independentes, como ao remover pinos de uma fileira ou escolher um ponto de um intervalo. O valor da posição resultante é o XOR dos valores das partes:

$$
g(\text{parte esquerda})\oplus g(\text{parte direita})
$$

Portanto, ao calcular `mex`, insira esse XOR para cada corte possível. A justificativa formal é o [Teorema de Sprague–Grundy](sprague-grundy-theorem.md).

!!! tip "Tamanho do mex"
    Se uma posição tem `d` movimentos distintos, seu Grundy é no máximo `d`: um conjunto com no máximo `d` valores não consegue conter todos os inteiros de `0` até `d`. Por isso, um vetor `seen` de tamanho `d+1` basta.

<!-- AUXÍLIO VISUAL 1

Mostrar uma posição com três sucessores de Grundy 0, 1 e 3, destacando que seu mex e Grundy valem 2. Incluir uma jogada de intervalo que se divide em duas partes e combina por XOR.

Arquivo sugerido: images/mex-e-grundy.svg
-->

## Problemas

{{ exercise_list(exercises) }}
