{% set exercises %}
  recommended:
    - name: Binomial Coefficients
      url: https://cses.fi/problemset/task/1079
      platform: CSES
      difficulty: medium
      topics: [coeficiente binomial, fatorial, módulo]
      objective: Responda muitas consultas de C(n,k) sob módulo primo.
    - name: Bracket Sequences I
      url: https://cses.fi/problemset/task/2064
      platform: CSES
      difficulty: medium
      topics: [binomial, Catalan, parênteses]
      objective: Conecte escolhas de posições a sequências de parênteses válidas.
  additional:
    - name: Binomial Coefficients
      url: https://cses.fi/problemset/task/1079
      platform: CSES
      difficulty: medium
      topics: [triângulo de Pascal, combinação]
      objective: Compare o cálculo por recorrência com o pré-cálculo modular.
{% endset %}

# Coeficientes binomiais

O coeficiente binomial $\binom{n}{k}$ conta escolhas de `k` elementos entre `n`. Além da fórmula, suas identidades dão soluções para strings, subconjuntos, caminhos e somas combinatórias.

## 1. Propriedades essenciais

### Simetria

$$
\binom{n}{k} = \binom{n}{n-k}
$$

A simetria troca “escolher os que entram” por “escolher os que ficam fora”.

### Identidade de Pascal

$$
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
$$

A identidade de Pascal separa as escolhas que contêm um elemento fixo das que não o contêm.

### Soma dos coeficientes binomiais

$$
\sum_{k=0}^{n}\binom{n}{k} = 2^n
$$

Ela conta todos os subconjuntos de um conjunto de `n` elementos, agrupados pelo tamanho. Também é a soma da linha `n` no triângulo de Pascal.

### Identidade do hockey-stick

Uma identidade útil em contagens acumuladas é o *hockey-stick*:

$$
\sum_{i=k}^{n}\binom{i}{k}=\binom{n+1}{k+1}
$$

### Convolution de Vandermonde

Outra identidade particularmente útil ao dividir um conjunto em dois grupos é a convolução de Vandermonde:

$$
\sum_i \binom{r}{i}\binom{s}{k-i}=\binom{r+s}{k}
$$

O lado esquerdo escolhe `i` elementos do primeiro grupo e `k-i` do segundo; o lado direito simplesmente escolhe `k` entre todos. Por exemplo, ela conta strings binárias com `k` uns quando parte das posições tem regras diferentes.

## 2. Triângulo de Pascal

As bordas do triângulo valem 1 e cada posição interna é a soma das duas acima:

```text
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1
```

Essa construção calcula todos os binomiais até `N` em $O(N^2)$ e não exige divisão modular:

```cpp
vector binom(n + 1, vector<long long>(n + 1, 0));
for (int i = 0; i <= n; i++) {
    binom[i][0] = binom[i][i] = 1;
    for (int k = 1; k < i; k++) {
        binom[i][k] = binom[i - 1][k - 1] + binom[i - 1][k];
    }
}
```

## 3. Fórmula multiplicativa

Quando `k` é pequeno, calcule sem fatoriais completos:

$$
\binom{n}{k} = \prod_{i=1}^{k}\frac{n-k+i}{i}
$$

```cpp
long long choose_small(long long n, long long k) {
    k = min(k, n - k);
    long long answer = 1;
    for (long long i = 1; i <= k; i++) {
        answer = answer * (n - k + i) / i;
    }
    return answer;
}
```

Essa versão exige que o resultado caiba no tipo. Para muitas consultas sob módulo, use [Coeficientes Binomiais Modulares](binomial-modular.md).

## 4. Teorema binomial e multinomiais

O teorema binomial é:

$$
(a+b)^n = \sum_{k=0}^{n}\binom{n}{k}a^{n-k}b^k
$$

O coeficiente escolhe quais `k` dos `n` fatores contribuem com `b`. É também a razão para $\binom{n}{k}$ contar strings binárias de tamanho `n` com exatamente `k` uns.

Para mais de dois tipos, usamos o coeficiente multinomial:

$$
\binom{n}{c_1,c_2,\ldots,c_m}=\frac{n!}{c_1!c_2!\cdots c_m!}
$$

Ele conta strings com quantidades fixas de cada símbolo. Por exemplo, é a fórmula dos anagramas de `MISSISSIPPI` estudada no capítulo anterior.

<!-- AUXÍLIO VISUAL 1

Criar um triângulo de Pascal com cores para uma diagonal e para a soma de uma linha, conectando-as a escolhas de subconjuntos e ao teorema binomial.

Arquivo sugerido: images/triangulo-de-pascal.svg
-->

Para sequências de parênteses, triangulações e outras estruturas recursivas, prossiga para [Números de Catalan](catalan.md).

## Problemas

{{ exercise_list(exercises) }}
