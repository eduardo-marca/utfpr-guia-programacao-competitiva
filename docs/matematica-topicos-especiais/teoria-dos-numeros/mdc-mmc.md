{% set exercises %}
  recommended:
    - name: Common Divisors
      url: https://cses.fi/problemset/task/1081
      platform: CSES
      difficulty: medium
      topics: [MDC, divisores, frequência]
      objective: Reconheça MDC como o maior divisor compartilhado por dois valores.
{% endset %}

# MDC e MMC

O **máximo divisor comum** (MDC) mede o que dois inteiros compartilham em sua fatoração; o **mínimo múltiplo comum** (MMC) mede o necessário para conter ambas as fatorações.

## 1. Definições pela fatoração

Se $a=\prod p^{\alpha_p}$ e $b=\prod p^{\beta_p}$, então:

$$
\gcd(a,b)=\prod p^{\min(\alpha_p,\beta_p)},\qquad
\operatorname{lcm}(a,b)=\prod p^{\max(\alpha_p,\beta_p)}
$$

Para `a,b > 0`, segue a identidade:

$$
\gcd(a,b)\cdot\operatorname{lcm}(a,b)=a\cdot b
$$

Exemplo: $84=2^2\cdot3\cdot7$ e $60=2^2\cdot3\cdot5$. Portanto, `gcd=12` e `lcm=420`.

## 2. Algoritmo de Euclides

O algoritmo usa o fato de que os divisores comuns de `a` e `b` são exatamente os de `b` e `a mod b`:

$$
\gcd(a,b)=\gcd(b, a\bmod b)
$$

```cpp
long long gcd(long long a, long long b) {
    a = abs(a);
    b = abs(b);
    while (b != 0) {
        long long remainder = a % b;
        a = b;
        b = remainder;
    }
    return a;
}

long long lcm(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return abs(a / gcd(a, b) * b);
}
```

O custo é $O(\log\min(|a|,|b|))$. Dividir antes de multiplicar em `lcm` reduz o risco de overflow; ainda assim, o resultado final precisa caber em `long long`. Em C++17, `std::gcd` e `std::lcm` existem em `<numeric>`.

## 3. Propriedades úteis

$$
\gcd(a,b)=\gcd(a,b+ka)
$$

para qualquer inteiro `k`. É a forma algébrica da redução de Euclides e permite simplificar expressões.

- `gcd(a,b)=1` significa que `a` e `b` são coprimos.
- Se `gcd(a,b)=1` e `a | bc`, então `a | c`.
- `gcd(a_1,\ldots,a_n)` pode ser acumulado da esquerda para a direita; o mesmo vale para MMC.
- A diferença de dois múltiplos de `g` também é múltipla de `g`. Essa observação aparece em problemas de distâncias e operações que somam ou subtraem valores.

!!! tip "MDC como invariante"
    Se uma operação permite substituir dois valores por sua diferença, o MDC do conjunto não muda. Muitos problemas de operações repetidas se resolvem identificando esse invariante, em vez de simular as operações.

<!-- AUXÍLIO VISUAL 1

Criar a sequência de restos do algoritmo de Euclides para gcd(84,60): 84 = 1·60 + 24, 60 = 2·24 + 12, 24 = 2·12. Relacionar os expoentes mínimos e máximos ao MDC e MMC.

Arquivo sugerido: images/euclides-mdc-mmc.svg
-->

Para obter coeficientes `x` e `y` tais que `ax + by = gcd(a,b)`, continue em [Euclides Estendido](euclides-estendido.md).

## Problemas

{{ exercise_list(exercises) }}
