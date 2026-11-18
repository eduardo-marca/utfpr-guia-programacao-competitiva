{% set exercises %}
  recommended:
    - name: Exponentiation II
      url: https://cses.fi/problemset/task/1712
      platform: CSES
      difficulty: medium
      topics: [Fermat, Euler, redução de expoentes]
      objective: Reduza expoentes enormes sob um módulo primo com cuidado com as hipóteses.
  additional:
    - name: Prime Multiples
      url: https://cses.fi/problemset/task/2185
      platform: CSES
      difficulty: medium
      topics: [coprimos, primos, inclusão-exclusão]
      objective: Combine propriedades aritméticas e contagem de múltiplos.
{% endset %}

# Função totiente de Euler

O totiente de Euler, $\varphi(n)$, conta os inteiros em `1..n` que são coprimos com `n`. Para `n>1`, é equivalente contar os inteiros em `1..n-1` cujo MDC com `n` é 1.

## 1. Fórmula pela fatoração

Se $n=\prod p_i^{\alpha_i}$, então:

$$
\varphi(n)=n\prod_{p\mid n}\left(1-\frac1p\right)
=\prod_i p_i^{\alpha_i-1}(p_i-1)
$$

A fórmula remove de `1..n` os múltiplos de cada primo que divide `n`. Exemplos:

$$
\varphi(p)=p-1,\qquad \varphi(p^k)=p^k-p^{k-1}
$$

e $\varphi(36)=36(1-1/2)(1-1/3)=12$.

```cpp
long long phi(long long n) {
    long long answer = n;
    for (long long p = 2; p <= n / p; p++) {
        if (n % p != 0) continue;
        while (n % p == 0) n /= p;
        answer -= answer / p;
    }
    if (n > 1) answer -= answer / n;
    return answer;
}
```

O código fatora `n` em $O(\sqrt n)$. Cada primo distinto reduz `answer` uma única vez.

## 2. Propriedades importantes

Se `gcd(a,b)=1`, então:

$$
\varphi(ab)=\varphi(a)\varphi(b)
$$

Além disso:

$$
\sum_{d\mid n}\varphi(d)=n
$$

Uma interpretação da última identidade: agrupe os inteiros de `1` a `n` pelo valor de seu MDC com `n`. Para cada divisor `d`, há $\varphi(n/d)$ inteiros cujo MDC é `d`.

O totiente também mede quantos resíduos possuem inverso módulo `n`: exatamente $\varphi(n)$ dos restos `0..n-1` são coprimos com `n`.

## 3. Crivo de totientes

Para obter todos os valores até `N`, comece com `phi[i]=i`. Quando `p` ainda vale `phi[p]=p`, ele é primo; retire sua fração de todos os múltiplos.

```cpp
vector<int> totients_up_to(int limit) {
    vector<int> phi(limit + 1);
    iota(phi.begin(), phi.end(), 0);
    for (int p = 2; p <= limit; p++) {
        if (phi[p] != p) continue;
        for (int multiple = p; multiple <= limit; multiple += p) {
            phi[multiple] -= phi[multiple] / p;
        }
    }
    return phi;
}
```

O custo é $O(N\log\log N)$. Em uma consulta isolada, a fatoração costuma ser mais simples; em muitas consultas, o crivo compensa.

## 4. Conexão com módulos

O teorema de Euler afirma que, se `gcd(a,m)=1`, então:

$$
a^{\varphi(m)}\equiv1\pmod m
$$

Ele permite reduzir expoentes em problemas modulares, mas a condição de coprimalidade é indispensável. Veja a aplicação detalhada em [Aritmética Modular](modular-arithmetic.md).

<!-- AUXÍLIO VISUAL 1

Exibir os resíduos de 1 a 12, separando os coprimos de 12 e marcando os fatores 2 e 3 que eliminam os demais. Conectar à fórmula 12(1−1/2)(1−1/3).

Arquivo sugerido: images/totiente-euler.svg
-->

## Problemas

{{ exercise_list(exercises) }}
