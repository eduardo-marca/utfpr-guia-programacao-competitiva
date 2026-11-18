{% set exercises %}
  recommended:
    - name: Game on Tree
      url: https://atcoder.jp/contests/agc017/tasks/agc017_d
      platform: AtCoder
      difficulty: hard
      topics: [Sprague-Grundy, árvores, XOR]
      objective: Calcule valores de Grundy em subárvores e combine-os corretamente.
    - name: Interval Game 2
      url: https://atcoder.jp/contests/abc206/tasks/abc206_f
      platform: AtCoder
      difficulty: hard
      topics: [Sprague-Grundy, intervalos]
      objective: Combine subintervalos criados por cada movimento usando nim-sum.
  additional:
    - name: Arpa and a game with Mojtaba
      url: https://codeforces.com/contest/850/problem/C
      platform: Codeforces
      difficulty: hard
      topics: [Grundy, fatoração, componentes]
      objective: Identifique componentes independentes escondidas em fatores primos.
    - name: Sagheer and Apple Tree
      url: https://codeforces.com/contest/812/problem/E
      platform: Codeforces
      difficulty: hard
      topics: [Nim, árvores, XOR]
      objective: Encontre a estrutura de Nim escondida em uma árvore enraizada.
{% endset %}

# Teorema de Sprague–Grundy

O teorema de Sprague–Grundy afirma que todo jogo imparcial, finito e normal é equivalente a uma pilha de Nim cujo tamanho é o Grundy number da posição. Sua consequência prática é ainda mais importante: uma soma de subgames independentes é resolvida pelo XOR de seus Grundy numbers.

## 1. Soma disjunta de jogos

Em uma **soma disjunta**, o estado é formado por componentes independentes. Em cada turno, o jogador escolhe exatamente uma componente e faz uma jogada nela; todas as demais ficam inalteradas.

Se as componentes possuem valores `g₁, g₂, ..., gₙ`, defina:

$$
G=g_1\oplus g_2\oplus\cdots\oplus g_n
$$

Então:

$$
\text{posição é P}\iff G=0
$$

Isso generaliza Nim: em Nim, o Grundy da pilha de tamanho `x` é o próprio `x`.

```cpp
bool first_player_wins(const vector<int>& component_grundies) {
    int nim_sum = 0;
    for (int value : component_grundies) nim_sum ^= value;
    return nim_sum != 0;
}
```

## 2. Demonstração da regra do XOR

Se `G=0`, qualquer jogada altera apenas uma componente de Grundy `g` para algum sucessor de Grundy `h`. Pela definição de `mex`, `h` nunca é igual a `g`; caso contrário, `g` não seria o menor valor ausente. Assim, o XOR muda de $G$ para $g\oplus h\neq0$.

Se `G≠0`, escolha uma componente `i` para a qual:

$$
g_i\oplus G<g_i
$$

exatamente como em Nim. Chame o alvo de `t=g_i xor G`. Como `t<g_i` e `g_i` é um `mex`, existe uma jogada naquela componente para um sucessor com Grundy `t`: todos os valores menores que o `mex` aparecem entre os sucessores. Após a jogada:

$$
G\oplus g_i\oplus t=0
$$

Logo, zero só leva a não zero e não zero sempre possui um movimento para zero. Essa é a caracterização de posições perdedoras e vencedoras.

## 3. Exemplo: duas pilhas com retiradas restritas

Considere em cada pilha as retiradas `{1,3,4}`. Os Grundy values iniciais são:

| Tamanho | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Grundy | 0 | 1 | 0 | 1 | 2 | 3 | 2 | 0 |

Para pilhas de tamanhos 4 e 5, o XOR é $2\oplus3=1$, então a posição é vencedora. O alvo para a segunda pilha é $3\oplus1=2$; ela pode ir de 5 para 4 removendo uma pedra. O novo XOR é $2\oplus2=0$.

Não faça XOR dos tamanhos (`4 xor 5`) — isso seria Nim comum. Faça XOR dos Grundy numbers, que codificam as regras reais de retirada.

## 4. Receita para problemas

1. Verifique que é um jogo imparcial, normal e sem ciclos.
2. Identifique as componentes independentes e confirme que uma jogada mexe em apenas uma delas.
3. Defina o Grundy de uma componente por `mex` dos sucessores.
4. Se uma jogada a divide em partes, use XOR dos Grundy das partes como valor do sucessor.
5. Faça XOR dos valores iniciais. Zero significa derrota com jogo perfeito.

!!! warning "Hipóteses do teorema"
    Sprague–Grundy não vale diretamente para jogos misère, jogos com pontuação, jogos com informação incompleta ou jogos em que uma jogada altera duas componentes. Nesses casos, use a análise específica do problema.

<!-- AUXÍLIO VISUAL 1

Mostrar três componentes com Grundy 2, 5 e 7, cujo XOR é 0. Em seguida, alterar somente a componente de Grundy 5 para 1 e destacar que o XOR deixa de ser zero.

Arquivo sugerido: images/sprague-grundy-xor.svg
-->

Para calcular os valores de cada componente, consulte [Números de Grundy](grundy-numbers.md). Para a exceção da última jogada perdedora, siga para [Jogos Misère](misere-games.md).

## Problemas

{{ exercise_list(exercises) }}
