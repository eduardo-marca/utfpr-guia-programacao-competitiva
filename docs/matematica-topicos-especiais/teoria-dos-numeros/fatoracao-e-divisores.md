{% set exercises %}
  recommended:
    - name: Counting Divisors
      url: https://cses.fi/problemset/task/1713
      platform: CSES
      difficulty: medium
      topics: [fatoração, número de divisores]
      objective: Calcule τ(n) a partir dos expoentes da fatoração prima.
    - name: Sum of Divisors
      url: https://cses.fi/problemset/task/1082
      platform: CSES
      difficulty: hard
      topics: [divisores, somatórios, módulo]
      objective: Relacione pares divisor-quociente e agrupamento por quociente.
  additional:
    - name: Common Divisors
      url: https://cses.fi/problemset/task/1081
      platform: CSES
      difficulty: medium
      topics: [divisores, frequências]
      objective: Encontre o maior divisor que aparece em pelo menos dois números.
{% endset %}

# Fatoração e divisores

Escreva $n=\prod p_i^{\alpha_i}$. Todo divisor positivo de `n` escolhe, independentemente, um expoente entre `0` e $\alpha_i$ para cada primo `p_i`. Essa observação explica quase todas as fórmulas desta página.

## 1. Fatoração por divisão de tentativa

Para uma consulta, basta testar possíveis fatores até a raiz do valor restante. Quando removemos todas as cópias de um primo, a raiz diminui.

```cpp
vector<pair<long long, int>> factorize(long long n) {
    vector<pair<long long, int>> factors;
    for (long long p = 2; p <= n / p; p += (p == 2 ? 1 : 2)) {
        if (n % p != 0) continue;
        int exponent = 0;
        while (n % p == 0) n /= p, exponent++;
        factors.push_back({p, exponent});
    }
    if (n > 1) factors.push_back({n, 1});
    return factors;
}
```

O salto após `2` evita pares. Para muitas consultas limitadas por `N`, substitua a tentativa pelo vetor `spf` de [Primos e Crivo](primos-e-crivo.md).

## 2. Número, soma e produto dos divisores

Para $n=p_1^{\alpha_1}\cdots p_k^{\alpha_k}$:

$$
\tau(n)=\prod_{i=1}^{k}(\alpha_i+1)
$$

pois há $\alpha_i+1$ escolhas para o expoente de cada `p_i`. A soma dos divisores é o produto de séries geométricas:

$$
\sigma(n)=\prod_{i=1}^{k}(1+p_i+\cdots+p_i^{\alpha_i})
=\prod_{i=1}^{k}\frac{p_i^{\alpha_i+1}-1}{p_i-1}
$$

O produto de todos os divisores é:

$$
\prod_{d\mid n}d=n^{\tau(n)/2}
$$

A fórmula vem do emparelhamento `d` com `n/d`. Quando `n` é quadrado perfeito, o divisor $\sqrt n$ fica sozinho; a expressão ainda é inteira, mas não interprete o expoente fracionário como uma divisão modular automática.

Exemplo: $360=2^3\cdot3^2\cdot5$. Logo,

$$
\tau(360)=4\cdot3\cdot2=24,\qquad
\sigma(360)=(1+2+4+8)(1+3+9)(1+5)=1170
$$

Evite a divisão da forma fechada ao implementar a soma: construa cada série geometricamente com inteiros.

```cpp
pair<long long, long long> divisor_count_and_sum(
    const vector<pair<long long, int>>& factors
) {
    long long count = 1, sum = 1;
    for (auto [p, exponent] : factors) {
        count *= exponent + 1;
        long long power = 1, geometric_sum = 1;
        for (int i = 0; i < exponent; i++) {
            power *= p;
            geometric_sum += power;
        }
        sum *= geometric_sum;
    }
    return {count, sum};
}
```

O produto dos divisores pode ser deduzido pela fórmula acima; em código, verifique cuidadosamente overflow ou trabalhe sob um módulo apropriado antes de tentar exponenciá-lo.

## 3. Enumerando divisores

Divisores vêm em pares `d` e `n/d`; por isso é suficiente testar até a raiz.

```cpp
vector<long long> divisors(long long n) {
    vector<long long> answer;
    for (long long d = 1; d <= n / d; d++) {
        if (n % d != 0) continue;
        answer.push_back(d);
        if (d != n / d) answer.push_back(n / d);
    }
    sort(answer.begin(), answer.end());
    return answer;
}
```

Um número é **perfeito** quando a soma de seus divisores próprios é ele mesmo; equivalentemente, $\sigma(n)=2n$. Esse é um bom exemplo de como uma definição sobre todos os divisores se reduz à fatoração.

!!! warning "Fórmula racional sob módulo"
    A forma $(p^{\alpha+1}-1)/(p-1)$ não permite divisão comum quando a resposta é módulo `MOD`. Use um inverso modular somente se `gcd(p-1, MOD)=1`; caso contrário, some a progressão geometricamente ou use uma técnica específica.

<!-- AUXÍLIO VISUAL 1

Mostrar a árvore de escolhas dos expoentes para 2³·3², conectando cada folha a um divisor. Destacar como o produto das quantidades de escolhas produz τ(n).

Arquivo sugerido: images/divisores-da-fatoracao.svg
-->

O próximo capítulo mostra como MDC e MMC capturam a interseção e a união dos expoentes primos de dois números.

## Problemas

{{ exercise_list(exercises) }}
