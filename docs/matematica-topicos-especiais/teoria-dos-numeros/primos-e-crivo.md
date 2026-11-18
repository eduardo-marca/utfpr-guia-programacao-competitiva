{% set exercises %}
  recommended:
    - name: Prime Multiples
      url: https://cses.fi/problemset/task/2185
      platform: CSES
      difficulty: medium
      topics: [primos, múltiplos, inclusão-exclusão]
      objective: Use fatores primos como conjuntos de múltiplos.
    - name: Counting Divisors
      url: https://cses.fi/problemset/task/1713
      platform: CSES
      difficulty: medium
      topics: [fatoração, primos]
      objective: Fatore muitos inteiros e derive propriedades a partir dos expoentes.
  additional:
    - name: Common Divisors
      url: https://cses.fi/problemset/task/1081
      platform: CSES
      difficulty: medium
      topics: [crivo, frequências, divisores]
      objective: Inverta a perspectiva, percorra possíveis divisores em vez de pares de valores.
{% endset %}

# Números primos e crivo

Primos são os blocos de construção dos inteiros. A fatoração prima é única; por isso, muitas propriedades de um número podem ser calculadas apenas olhando para os expoentes de seus primos.

## 1. Propriedades fundamentais

Um inteiro maior que 1 é **primo** quando possui exatamente dois divisores positivos: `1` e ele próprio. Todo inteiro `n > 1` possui uma fatoração única:

$$
n=p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_k^{\alpha_k}
$$

onde os `p_i` são primos distintos e os $\alpha_i$ são positivos. Duas consequências muito usadas são:

- se um primo `p` divide `ab`, então `p` divide `a` ou `p` divide `b`;
- se `n` é composto, ele possui algum fator primo `p ≤ \sqrt n`.

Existem infinitos primos. A quantidade $\pi(n)$ de primos até `n` é aproximadamente $n/\ln n$ para `n` grande; essa estimativa ajuda a prever a quantidade de trabalho e memória de um crivo, mas não substitui uma contagem exata.

A segunda propriedade justifica o teste por tentativa até a raiz. Não é necessário testar além dela: se ambos os fatores fossem maiores que $\sqrt n$, o produto seria maior que `n`.

```cpp
bool is_prime(long long n) {
    if (n < 2) return false;
    for (long long p = 2; p <= n / p; p++) {
        if (n % p == 0) return false;
    }
    return true;
}
```

Para uma única consulta moderada, o custo $O(\sqrt n)$ é adequado. Para muitas consultas até um limite comum, use um crivo.

## 2. Crivo de Eratóstenes

O crivo marca os múltiplos de cada primo. Ao chegar em `p`, se ele ainda não foi marcado, é primo. Podemos iniciar em `p²`, porque múltiplos menores já receberam um fator menor.

```cpp
vector<bool> eratosthenes(int limit) {
    vector<bool> is_prime(limit + 1, true);
    if (limit >= 0) is_prime[0] = false;
    if (limit >= 1) is_prime[1] = false;

    for (long long p = 2; p * p <= limit; p++) {
        if (!is_prime[p]) continue;
        for (long long multiple = p * p; multiple <= limit; multiple += p) {
            is_prime[multiple] = false;
        }
    }
    return is_prime;
}
```

O custo é $O(N\log\log N)$ e a memória é $O(N)$. Para listar os primos, percorra o vetor resultante. Para intervalos muito grandes `[L,R]`, um **crivo segmentado** marca nesse intervalo usando primos até $\sqrt R$, sem armazenar tudo até `R`.

## 3. Menor fator primo

Guardar o menor fator primo (`spf`) permite fatorar cada número até `N` em $O(\log N)$ após o pré-processamento.

```cpp
vector<int> smallest_prime_factor(int limit) {
    vector<int> spf(limit + 1, 0);
    for (int p = 2; p <= limit; p++) {
        if (spf[p] != 0) continue;
        spf[p] = p;
        if (1LL * p * p > limit) continue;
        for (long long multiple = 1LL * p * p; multiple <= limit; multiple += p) {
            if (spf[multiple] == 0) spf[multiple] = p;
        }
    }
    return spf;
}

vector<pair<int, int>> factorize_with_spf(int n, const vector<int>& spf) {
    vector<pair<int, int>> factors;
    while (n > 1) {
        int p = spf[n], exponent = 0;
        while (n % p == 0) n /= p, exponent++;
        factors.push_back({p, exponent});
    }
    return factors;
}
```

!!! tip "Escolha do algoritmo"
    Uma consulta com `n` até cerca de $10^{12}$ pode aceitar divisão por tentativa até $\sqrt n$. Muitas consultas com valores até `N` normalmente pedem crivo e `spf`. Os limites do problema decidem mais do que o nome da técnica.

<!-- AUXÍLIO VISUAL 1

Criar uma grade de 1 a 50 com os múltiplos de 2, 3, 5 e 7 riscados em etapas, deixando os primos destacados. Incluir uma seta mostrando que o crivo começa em p².

Arquivo sugerido: images/crivo-eratostenes.svg
-->

Continue em [Fatoração e Divisores](fatoracao-e-divisores.md), onde os expoentes da fatoração viram fórmulas.

## Problemas

{{ exercise_list(exercises) }}
