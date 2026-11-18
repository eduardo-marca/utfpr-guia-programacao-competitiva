{% set exercises %}
  recommended:
    - name: Binomial Coefficients
      url: https://cses.fi/problemset/task/1079
      platform: CSES
      difficulty: medium
      topics: [binomial, inverso modular, pré-cálculo]
      objective: Responda muitas consultas de C(n,k) módulo 1e9+7.
    - name: Creating Strings II
      url: https://cses.fi/problemset/task/1715
      platform: CSES
      difficulty: medium
      topics: [multinomial, fatorial modular]
      objective: Conte anagramas distintos usando fatoriais e inversos.
  additional:
    - name: Distributing Apples
      url: https://cses.fi/problemset/task/1716
      platform: CSES
      difficulty: medium
      topics: [stars and bars, binomial modular]
      objective: Combine distribuição de objetos com combinações modulares.
{% endset %}

# Coeficientes Binomiais Modulares

Quando há muitas consultas de $\binom{n}{k}$, recalcular fatoriais é caro e dividir diretamente não funciona sob módulo. Para módulo primo, pré-calculamos fatoriais e fatoriais inversos.

## 1. A fórmula modular

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

Sob módulo `MOD`, divisão por `x` significa multiplicar por seu inverso modular `x^{-1}`:

$$
\binom{n}{k} \equiv fact[n] \cdot invfact[k] \cdot invfact[n-k] \pmod{MOD}
$$

Se `MOD` é primo e `x` não é múltiplo de `MOD`, o pequeno teorema de Fermat dá:

$$
x^{-1} \equiv x^{MOD-2} \pmod{MOD}
$$

## 2. Pré-cálculo em O(N)

```cpp
const long long MOD = 1'000'000'007;

long long mod_pow(long long base, long long exponent) {
    long long answer = 1;
    while (exponent > 0) {
        if (exponent & 1) answer = answer * base % MOD;
        base = base * base % MOD;
        exponent >>= 1;
    }
    return answer;
}

struct Binomial {
    vector<long long> fact, invfact;

    Binomial(int max_n) : fact(max_n + 1), invfact(max_n + 1) {
        fact[0] = 1;
        for (int i = 1; i <= max_n; i++) fact[i] = fact[i - 1] * i % MOD;
        invfact[max_n] = mod_pow(fact[max_n], MOD - 2);
        for (int i = max_n; i >= 1; i--) invfact[i - 1] = invfact[i] * i % MOD;
    }

    long long choose(int n, int k) const {
        if (k < 0 || k > n) return 0;
        return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD;
    }
};
```

O pré-cálculo custa $O(N + \log MOD)$; cada consulta posterior custa $O(1)$.

!!! warning "Hipótese do módulo"
    Esse código usa Fermat e exige módulo primo. Para módulo composto, ou quando `n ≥ MOD`, são necessárias técnicas adicionais, como o Teorema do Resto Chinês.

## 3. Próximos usos

Use `choose` diretamente em combinações, stars and bars e fórmulas multinomiais. A teoria e as identidades estão em [Coeficientes Binomiais](coeficientes-binomial.md); depois aplique a estrutura em [Números de Catalan](catalan.md) e [Inclusão-Exclusão](inclusao-exclusao.md).

## Problemas

{{ exercise_list(exercises) }}
