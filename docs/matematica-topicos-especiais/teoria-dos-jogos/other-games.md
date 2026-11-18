{% set exercises %}
  recommended:
    - name: Interval Game 2
      url: https://atcoder.jp/contests/abc206/tasks/abc206_f
      platform: AtCoder
      difficulty: hard
      topics: [intervalos, Grundy, divisão de componentes]
      objective: Reconheça uma jogada que divide um jogo em dois subintervalos independentes.
  additional:
    - name: Game of Pairs
      url: https://codeforces.com/contest/1404/problem/D
      platform: Codeforces
      difficulty: hard
      topics: [jogos, grafos, estratégia]
      objective: Modele as escolhas do adversário sem confundir vitória/derrota com pontuação.
{% endset %}

# Jogos clássicos e padrões de modelagem

Os jogos abaixo não devem ser decorados como fórmulas isoladas. Cada um ilustra um padrão recorrente: divisão de uma fileira, estado comprimido, pares especiais de posições ou valor de uma árvore.

## 1. Kayles: remover pinos e dividir intervalos

Em **Kayles**, há uma fileira de pinos. Em uma jogada, remove-se um pino ou dois pinos adjacentes. A remoção pode separar a fileira em dois intervalos independentes, o que torna o jogo um exemplo direto de Sprague–Grundy.

Se `g[n]` é o Grundy de uma fileira com `n` pinos, os sucessores são:

$$
g[i]\oplus g[n-1-i]\quad(0\le i<n)
$$

ao remover um pino `i`, e:

$$
g[i]\oplus g[n-2-i]\quad(0\le i<n-1)
$$

ao remover um par adjacente. Portanto, `g[n]` é o `mex` de todos esses XORs.

```cpp
vector<int> kayles_grundy(int max_pins) {
    vector<int> grundy(max_pins + 1, 0);
    for (int n = 1; n <= max_pins; n++) {
        vector<char> seen(2 * n, false);
        for (int left = 0; left < n; left++) {
            int value = grundy[left] ^ grundy[n - 1 - left];
            if (value < static_cast<int>(seen.size())) seen[value] = true;
        }
        for (int left = 0; left + 1 < n; left++) {
            int value = grundy[left] ^ grundy[n - 2 - left];
            if (value < static_cast<int>(seen.size())) seen[value] = true;
        }
        while (seen[grundy[n]]) grundy[n]++;
    }
    return grundy;
}
```

Se houver várias fileiras, faça XOR dos valores de cada uma. O detalhe importante não é Kayles em si: sempre que uma jogada em um intervalo cria intervalos independentes, o sucessor costuma ser o XOR dos Grundy das partes.

## 2. Chomp: quando a estratégia existe, mas não é construtiva

Em **Chomp**, uma barra retangular possui uma casa envenenada, geralmente no canto inferior esquerdo. Escolher uma casa remove ela e todas as casas acima e à direita; escolher a casa envenenada perde.

Uma posição pode ser codificada pelas alturas não crescentes das colunas. Para tabuleiros pequenos, use memoização sobre esse vetor e a regra `P/N` misère. O jogo não se separa naturalmente em componentes, portanto não aplique XOR de Grundy sem justificar uma decomposição.

O teorema de *strategy stealing* mostra que qualquer posição inicial não trivial é vencedora para o primeiro jogador: se o segundo tivesse uma estratégia vencedora, o primeiro poderia remover inicialmente uma casa segura e depois imitar essa estratégia. Ter uma casa extra já removida nunca prejudica as opções do primeiro. A demonstração prova existência, mas não produz a jogada vencedora — uma distinção importante em problemas algorítmicos.

## 3. Jogo de Wythoff

Em Wythoff há duas pilhas `(a,b)`. Uma jogada pode reduzir uma pilha, ou reduzir ambas pela mesma quantidade. Ordene `a≤b`. As posições perdedoras são precisamente:

$$
(\lfloor k\varphi\rfloor,\lfloor k\varphi^2\rfloor),\qquad k\ge0
$$

onde $\varphi=(1+\sqrt5)/2$. Os primeiros pares são `(0,0)`, `(1,2)`, `(3,5)`, `(4,7)`, `(6,10)`.

Como $\varphi^2=\varphi+1$, a diferença entre as coordenadas do par de índice `k` é `k`. Assim, para testar uma posição, basta verificar se:

$$
a=\lfloor(b-a)\varphi\rfloor
$$

```cpp
bool is_wythoff_losing(long long a, long long b) {
    if (a > b) swap(a, b);
    long long k = b - a;
    long double phi = (1.0L + sqrtl(5.0L)) / 2.0L;
    return a == static_cast<long long>(floorl(k * phi));
}
```

O teorema de Beatty garante que as duas sequências $\lfloor k\varphi\rfloor$ e $\lfloor k\varphi^2\rfloor$ particionam os inteiros positivos. Isso prova que nenhuma posição perdedora alcança outra e que qualquer posição fora da lista alcança uma delas. Para limites extremos, trate cuidadosamente arredondamentos de ponto flutuante.

## 4. Green Hackenbush em árvores

No **Green Hackenbush**, todas as arestas são verdes e conectadas ao chão. Remover uma aresta remove também qualquer parte que fique desconectada do chão. É um jogo imparcial normal.

Para uma árvore enraizada no chão, o Grundy de um vértice é:

$$
g(v)=\bigoplus_{(v,u)}(g(u)+1)
$$

Cada ramo começa por uma aresta cuja remoção apaga o ramo inteiro; uma haste acima dela acrescenta 1 ao valor do subgame. Ramos distintos são uma soma disjunta, logo combinam por XOR.

```cpp
int green_hackenbush(int v, int parent, const vector<vector<int>>& tree) {
    int value = 0;
    for (int to : tree[v]) {
        if (to == parent) continue;
        value ^= green_hackenbush(to, v, tree) + 1;
    }
    return value;
}
```

Uma cadeia de `L` arestas tem valor `L`, isto é, uma pilha de Nim. A fórmula acima generaliza essa observação para ramificações.

## 5. Como escolher a abordagem

| Estrutura | Ferramenta |
|---|---|
| Jogo de retirada em uma pilha | DP `P/N` ou Grundy |
| Jogada que separa uma linha/intervalo | `mex` dos XORs das partes |
| Pares com movimentos geométricos especiais | Caracterização matemática, como Wythoff |
| Tabuleiro pequeno sem decomposição | Memoização do estado canônico |
| Árvore de componentes removíveis | DFS de Grundy |

!!! tip "Estratégia antes da implementação"
    Primeiro prove quais propriedades uma jogada preserva ou destrói. Só depois escolha a estrutura de DP. O estado correto pode ser uma quantidade, um intervalo, um vetor ordenado de alturas ou uma subárvore.

<!-- AUXÍLIO VISUAL 1

Criar quatro painéis: uma fileira de Kayles partida em dois intervalos, uma posição escalonada de Chomp, os pares perdedores de Wythoff numa grade e uma árvore de Green Hackenbush ligada ao chão.

Arquivo sugerido: images/jogos-classicos.svg
-->

## Problemas

{{ exercise_list(exercises) }}
