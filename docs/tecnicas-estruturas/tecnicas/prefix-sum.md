{% set exercises %}
  recommended:
    - name: Static Range Sum Queries
      url: https://cses.fi/problemset/task/1646
      platform: CSES
      difficulty: easy
      topics: [prefix sum, consultas em intervalo]
      objective: Responda somas de subarrays com dois valores de prefixo.
    - name: Forest Queries
      url: https://cses.fi/problemset/task/1652
      platform: CSES
      difficulty: medium
      topics: [prefix sum 2D, consultas em retângulo]
      objective: Construa uma matriz de prefixos para contar células em retângulos.
    - name: Subarray Divisibility
      url: https://cses.fi/problemset/task/1662
      platform: CSES
      difficulty: medium
      topics: [prefix sum, restos, contagem]
      objective: Conte subarrays cuja soma é divisível por N usando frequências de restos.
  additional:
    - name: Good Subarrays
      url: https://codeforces.com/problemset/problem/1398/C
      platform: Codeforces
      difficulty: medium
      topics: [prefix sum, transformação de valores, contagem]
      objective: Transforme a condição do enunciado em igualdade entre prefixos.
    - name: Subarray Sums II
      url: https://cses.fi/problemset/task/1661
      platform: CSES
      difficulty: medium
      topics: [prefix sum, map, contagem]
      objective: Conte somas-alvo mesmo quando o vetor contém valores negativos.
{% endset %}

# Prefix Sum

**Prefix sum** pré-processa um vetor para responder somas de intervalos em tempo constante. A técnica é simples, mas aparece em problemas de consultas, contagem de subarrays, matrizes e em várias transformações de estado.

## 1. A ideia central

Para um vetor `A`, definimos `prefix[i]` como a soma dos primeiros `i` elementos. Usar um prefixo com uma posição extra elimina casos especiais:

```text
prefix[0] = 0
prefix[i + 1] = prefix[i] + A[i]
```

Considere:

```text
Índice:       0   1   2   3   4   5
A:           [3, -2,  4,  1, -5,  2]

prefix:   [0,  3,  1,  5,  6,  1,  3]
índice:     0   1   2   3   4   5   6
```

A soma do intervalo inclusivo `[L, R]` é:

$$
sum(L,R) = prefix[R+1] - prefix[L]
$$

Por exemplo, a soma de `[2, 4]` é `4 + 1 - 5 = 0`:

```text
prefix[5] - prefix[2] = 1 - 1 = 0
```

Subtrair `prefix[L]` remove exatamente todos os elementos que estão antes do intervalo.

<!-- AUXÍLIO VISUAL 1 — PRIORITÁRIO

Criar um SVG para o vetor `[3, -2, 4, 1, -5, 2]` e seus prefixos.

- Mostrar o intervalo de consulta `[2,4]` destacado no vetor.
- Mostrar `prefix[5]` e `prefix[2]` destacados na linha de prefixos.
- Exibir a subtração `1 - 1 = 0` e indicar quais elementos são cancelados.

Arquivo sugerido:
images/prefixos-e-intervalos.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Consulta de intervalo por prefix sums](images/prefixos-e-intervalos.svg)
-->

## 2. Implementação 1D

```cpp
vector<long long> build_prefix_sum(const vector<int>& values) {
    int n = static_cast<int>(values.size());
    vector<long long> prefix(n + 1, 0);

    for (int i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + values[i];
    }
    return prefix;
}

long long range_sum(const vector<long long>& prefix, int left, int right) {
    return prefix[right + 1] - prefix[left];
}
```

Use `long long`: mesmo que cada elemento caiba em `int`, a soma de muitos elementos pode não caber.

| Etapa | Complexidade |
|---|---:|
| Construir os prefixos | $O(N)$ |
| Cada consulta de soma | $O(1)$ |
| Memória | $O(N)$ |

!!! warning "Vetor estático"
    Prefix sums são ideais quando o vetor não muda. Se houver atualizações entre consultas, use uma [Fenwick Tree](../estruturas/fenwick.md) ou uma [Árvore de Segmentos](../estruturas/segtree.md).

## 3. Contando subarrays por soma

Prefixos também transformam condições sobre subarrays em relações entre dois prefixos.

Queremos contar subarrays com soma igual a `target`. Se a soma de `[i, j]` é `target`, então:

$$
prefix[j+1] - prefix[i] = target
$$

Logo, para o prefixo atual `current`, precisamos saber quantas vezes já apareceu `current - target`.

```cpp
long long count_subarrays_with_sum(const vector<int>& values, long long target) {
    map<long long, long long> frequency;
    frequency[0] = 1;

    long long answer = 0;
    long long current = 0;
    for (int value : values) {
        current += value;
        answer += frequency[current - target];
        frequency[current]++;
    }
    return answer;
}
```

`frequency[0] = 1` representa o prefixo vazio e permite contar subarrays que começam na posição zero.

### Restos e divisibilidade

Para contar subarrays cuja soma é divisível por `K`, dois prefixos precisam ter o mesmo resto ao dividir por `K`:

$$
prefix[j] \bmod K = prefix[i] \bmod K
$$

Guarde a frequência de cada resto. Em C++, normalize restos negativos com:

```cpp
remainder = (remainder % K + K) % K;
```

## 4. Prefix sum 2D

Para uma matriz, `prefix[i][j]` guarda a soma do retângulo que vai do canto superior esquerdo até antes de `(i, j)`. A linha e coluna extras mantêm a fórmula uniforme:

```cpp
prefix[i + 1][j + 1] = grid[i][j]
                      + prefix[i][j + 1]
                      + prefix[i + 1][j]
                      - prefix[i][j];
```

A soma do retângulo inclusivo com cantos `(r1, c1)` e `(r2, c2)` é:

```cpp
prefix[r2 + 1][c2 + 1]
- prefix[r1][c2 + 1]
- prefix[r2 + 1][c1]
+ prefix[r1][c1]
```

O último termo é somado porque foi removido duas vezes.

<!-- AUXÍLIO VISUAL 2 — PRIORITÁRIO

Criar um diagrama de prefix sum 2D para uma matriz 4×4.

- Destacar um retângulo de consulta e os quatro prefixos usados.
- Usar sinais `+`, `-`, `-`, `+` para mostrar inclusão-exclusão.
- Indicar visualmente por que o canto superior esquerdo é adicionado de volta.

Arquivo sugerido:
images/prefix-sum-2d.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Consulta de retângulo com prefix sums 2D](images/prefix-sum-2d.svg)
-->

## 5. Erros comuns

1. Usar `prefix[R] - prefix[L]` com a convenção de prefixo deslocado; o correto para `[L,R]` é `prefix[R+1] - prefix[L]`.
2. Esquecer o prefixo vazio, que representa subarrays iniciados na primeira posição.
3. Usar `int` para somas grandes.
4. Aplicar prefix sums em consultas com atualizações sem reconstruir os valores.
5. Errar o sinal do quarto termo na consulta 2D.

## Problemas

{{ exercise_list(exercises) }}

## Recursos

- [Prefix Sum Array - USACO Guide](https://usaco.guide/silver/prefix-sums)
- [Prefix sums - cp-algorithms](https://cp-algorithms.com/others/maximum_average_segment.html)
