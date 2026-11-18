{% set exercises %}
  recommended:
    - name: Binomial Coefficients
      url: https://cses.fi/problemset/task/1079
      platform: CSES
      difficulty: medium
      topics: [inverso modular, fatoriais, combinações]
      objective: Substitua divisões por multiplicações de inversos sob módulo primo.
    - name: Creating Strings II
      url: https://cses.fi/problemset/task/1715
      platform: CSES
      difficulty: medium
      topics: [inversos, multinomial, strings]
      objective: Conte anagramas distintos com fatoriais inversos.
  additional:
    - name: Distributing Apples
      url: https://cses.fi/problemset/task/1716
      platform: CSES
      difficulty: medium
      topics: [combinações, inverso modular]
      objective: Aplique combinações modulares em uma distribuição de objetos.
{% endset %}

# Inverso modular

O inverso modular de `a` módulo `m` é um inteiro `x` tal que:

$$
ax\equiv1\pmod m
$$

Ele existe se e somente se $\gcd(a,m)=1$. Quando existe, permite interpretar a divisão modular como:

$$
\frac ab\equiv a\cdot b^{-1}\pmod m
$$

## 1. Inverso com Euclides estendido

Pela identidade de Bézout, se `gcd(a,m)=1`, existem `x,y` tais que $ax+my=1$. Reduzindo módulo `m`, sobra $ax\equiv1$, portanto `x` é o inverso desejado.

```cpp
optional<long long> mod_inverse(long long a, long long mod) {
    if (mod <= 1) return nullopt;
    a %= mod;
    if (a < 0) a += mod;

    long long x, y;
    long long g = extended_gcd(a, mod, x, y);
    if (g != 1) return nullopt;
    x %= mod;
    if (x < 0) x += mod;
    return x;
}
```

Esse método custa $O(\log m)$, funciona também para módulo composto e detecta corretamente a inexistência do inverso.

## 2. Inverso com Fermat

Quando `MOD` é primo e `a` não é múltiplo de `MOD`, o Pequeno Teorema de Fermat dá:

$$
a^{-1}\equiv a^{MOD-2}\pmod{MOD}
$$

```cpp
long long inverse_prime_mod(long long a, long long mod) {
    // Pré-condições: mod é primo e a % mod != 0.
    return mod_pow(a, mod - 2, mod);
}
```

Essa versão é especialmente conveniente quando já existe `mod_pow`, mas não deve ser usada com módulo composto. Para uma única inversão, Euclides estendido costuma ser mais rápido; para fórmulas que já usam exponenciação, Fermat é simples.

## 3. Muitos inversos sob módulo primo

Para `1 ≤ i < MOD`, todos os inversos até `N < MOD` podem ser calculados em tempo linear:

```cpp
vector<long long> inverses_up_to(int n, long long mod) {
    vector<long long> inv(n + 1);
    if (n >= 1) inv[1] = 1;
    for (int i = 2; i <= n; i++) {
        inv[i] = mod - (mod / i) * inv[mod % i] % mod;
    }
    return inv;
}
```

A recorrência depende de `mod` primo e de `n < mod`. Outra técnica comum é pré-calcular `fact[i]` e `invfact[i]` para responder combinações em $O(1)$; veja [Coeficientes Binomiais Modulares](../combinatoria/binomial-modular.md).

## 4. Armadilhas frequentes

- `inverse(0)` não existe em nenhum módulo maior que 1.
- Se `gcd(a,m)>1`, não tente "dividir" uma congruência por `a`; primeiro reduza pelo MDC, como em [Equações Inteiras](equacoes-diofantinas.md).
- Sob módulo primo `p`, `fact[n]` não tem inverso quando `n ≥ p`, pois contém um fator `p`.
- Um resultado modular deve ser normalizado após subtrações.

<!-- AUXÍLIO VISUAL 1

Mostrar os resíduos coprimos a 10 (1,3,7,9) e seus pares de inversos: 1·1, 3·7 e 9·9, todos congruentes a 1.

Arquivo sugerido: images/inverso-modular.svg
-->

Sistemas com várias divisões ou condições de restos levam naturalmente ao [Teorema Chinês do Resto](sistemas-de-congruencias.md).

## Problemas

{{ exercise_list(exercises) }}
