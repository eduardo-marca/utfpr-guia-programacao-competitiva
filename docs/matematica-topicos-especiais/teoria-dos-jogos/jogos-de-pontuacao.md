{% set exercises %}
  recommended:
    - name: Removal Game
      url: https://cses.fi/problemset/task/1097
      platform: CSES
      difficulty: medium
      topics: [minimax, programação dinâmica, intervalos]
      objective: Maximize a diferença de pontos ao remover valores das extremidades.
    - name: Deque
      url: https://atcoder.jp/contests/dp/tasks/dp_l
      platform: AtCoder
      difficulty: medium
      topics: [minimax, DP de intervalos]
      objective: Modele o melhor saldo que o jogador da vez ainda pode garantir.
{% endset %}

# Jogos de pontuação e minimax

Nem todo jogo competitivo é um jogo imparcial de "quem faz a última jogada". Quando cada movimento rende pontos, ou quando jogadores têm ações diferentes, Grundy e nim-sum não bastam. O estado precisa guardar o **valor ótimo** que o jogador da vez consegue garantir.

## 1. Valor como diferença de pontuação

Em jogos de soma zero, defina `dp(s)` como a maior diferença:

$$
\text{pontos do jogador da vez}-\text{pontos do adversário}
$$

que o jogador da vez pode garantir a partir de `s`. Se uma jogada ganha `w` pontos e leva a `t`, o adversário passa a ter vantagem `dp(t)` naquele subgame. Portanto, a vantagem atual é:

$$
w-dp(t)
$$

e a recorrência é:

$$
dp(s)=\max_{s\to t}\bigl(w(s,t)-dp(t)\bigr)
$$

Essa troca de sinal já embute a alternância de turnos; é a forma **negamax** de minimax.

## 2. Exemplo: remover das extremidades

No *Removal Game*, há um vetor `a[l..r]` e cada jogador escolhe a ponta esquerda ou direita, somando o valor removido. Seja `dp[l][r]` a melhor diferença que o jogador da vez consegue no intervalo:

$$
dp[l][r]=\max\bigl(a_l-dp[l+1][r],\;a_r-dp[l][r-1]\bigr)
$$

```cpp
long long optimal_difference(const vector<long long>& values) {
    int n = static_cast<int>(values.size());
    vector dp(n, vector<long long>(n));

    for (int i = 0; i < n; i++) dp[i][i] = values[i];
    for (int length = 2; length <= n; length++) {
        for (int left = 0; left + length <= n; left++) {
            int right = left + length - 1;
            dp[left][right] = max(values[left] - dp[left + 1][right],
                                  values[right] - dp[left][right - 1]);
        }
    }
    return dp[0][n - 1];
}
```

Se a soma total é `S` e a diferença final é `D`, a pontuação do primeiro jogador é $(S+D)/2$. A formulação por diferença elimina a necessidade de guardar dois placares em cada estado.

## 3. Minimax com memoização

Quando o jogo não é uma simples DP de intervalos, enumere movimentos e memorize o estado. Para um jogo simétrico de soma zero, a recorrência continua sendo `ganho - valor_do_adversário`.

```cpp
long long negamax(const State& state) {
    if (terminal(state)) return terminal_score_for_player_to_move(state);
    auto it = memo.find(state);
    if (it != memo.end()) return it->second;

    long long best = LLONG_MIN;
    for (const Move& move : legal_moves(state)) {
        State next = apply(state, move);
        best = max(best, immediate_score(state, move) - negamax(next));
    }
    memo[state] = best;
    return best;
}
```

Em um jogo geral com papéis assimétricos, use `max` nos turnos do primeiro jogador e `min` nos do segundo. A poda alfa-beta pode acelerar uma árvore de busca, mas em programação competitiva a memoização e uma boa compressão de estado costumam ser mais importantes.

## 4. Escolhendo entre minimax e Grundy

| Objetivo e regra | Técnica principal |
|---|---|
| Última jogada vence, movimentos idênticos | `P/N`, Grundy ou Sprague–Grundy |
| Última jogada perde | Análise misère específica |
| Pontos acumulados | Diferença de pontuação / minimax |
| Jogadores têm movimentos diferentes | Minimax ou DP por turno |
| Há sorte ou informação oculta | Probabilidade, expectativa ou outra modelagem |

!!! tip "Mude a perspectiva no turno"
    Definir o estado como "vantagem do jogador que vai jogar" torna a transição simétrica: cada escolha soma o ganho imediato e subtrai a vantagem que o adversário obterá depois.

<!-- AUXÍLIO VISUAL 1

Mostrar um intervalo [4, -2, 7, 3], com as duas escolhas nas extremidades e setas invertendo o sinal da vantagem ao passar o turno.

Arquivo sugerido: images/minimax-diferenca.svg
-->

## Problemas

{{ exercise_list(exercises) }}
