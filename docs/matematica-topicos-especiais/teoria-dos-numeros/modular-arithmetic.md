{% set exercises %}
  recommended:
    - name: Exponentiation
      url: https://cses.fi/problemset/task/1095
      platform: CSES
      difficulty: medium
      topics: [exponenciação binária, módulo]
      objective: Calcule potências enormes em tempo logarítmico.
    - name: Exponentiation II
      url: https://cses.fi/problemset/task/1712
      platform: CSES
      difficulty: medium
      topics: [pequeno teorema de Fermat, expoentes]
      objective: Reduza um expoente que já é uma potência muito grande.
  additional:
    - name: Binomial Coefficients
      url: https://cses.fi/problemset/task/1079
      platform: CSES
      difficulty: medium
      topics: [inverso modular, fatoriais]
      objective: Use divisão modular para responder muitas combinações.
{% endset %}

# Aritmética modular

Trabalhar módulo `m` significa guardar apenas o resto na divisão por `m`. Escrevemos:

$$
a\equiv b\pmod m
$$

quando `m` divide `a-b`. Em programação competitiva, isso permite representar resultados enormes por um valor entre `0` e `m-1`.

## 1. Operações e normalização

Se $a\equiv b\pmod m$ e $c\equiv d\pmod m$, então:

$$
a+c\equiv b+d,\quad a-c\equiv b-d,\quad ac\equiv bd\pmod m
$$

Também podemos elevar ambos os lados a uma potência inteira não negativa. Portanto, reduza valores após cada soma, subtração e multiplicação.

$$
(a+b)\bmod m=((a\bmod m)+(b\bmod m))\bmod m
$$

$$
(ab)\bmod m=((a\bmod m)(b\bmod m))\bmod m
$$

O cancelamento exige coprimalidade: de $ac\equiv bc\pmod m$, só concluímos $a\equiv b\pmod m$ quando $\gcd(c,m)=1$.

```cpp
long long normalize(long long value, long long mod) {
    value %= mod;
    if (value < 0) value += mod;
    return value;
}

long long add_mod(long long a, long long b, long long mod) {
    return (normalize(a, mod) + normalize(b, mod)) % mod;
}
```

Subtrações exigem normalização: em C++, `(-1) % mod` continua negativo. Para `mod` próximo de $10^{18}$, o produto de dois resíduos pode estourar `long long`; use `(__int128)a*b % mod` quando o compilador permitir.

!!! warning "Divisão é diferente"
    Em geral, $(a/b)\bmod m$ não significa divisão inteira nem divisão comum seguida de módulo. Ela só é definida como $a\cdot b^{-1}\pmod m$ quando `b` possui inverso modular. Veja [Inverso Modular](inverso-modular.md).

## 2. Exponenciação binária modular

Elevar `a` a `e` por multiplicações repetidas custa `O(e)`. Ao quadrar a base e examinar os bits de `e`, o custo cai para $O(\log e)$:

```cpp
long long mod_pow(long long base, long long exponent, long long mod) {
    long long answer = 1 % mod;
    base = normalize(base, mod);
    while (exponent > 0) {
        if (exponent & 1) answer = static_cast<__int128>(answer) * base % mod;
        base = static_cast<__int128>(base) * base % mod;
        exponent >>= 1;
    }
    return answer;
}
```

O invariante é: `answer × base^exponent` representa a potência original. A cada passo, removemos um bit do expoente; quando ele é 1, multiplicamos a resposta pela base corrente.

## 3. Pequeno Teorema de Fermat e Teorema de Euler

Se `p` é primo e `p` não divide `a`, o **Pequeno Teorema de Fermat** afirma:

$$
a^{p-1}\equiv1\pmod p
$$

Logo, para expoente positivo, podemos reduzir o expoente módulo `p-1` sob essas hipóteses. Se `a` é múltiplo de `p`, trate esse caso separadamente: $a^e\equiv0\pmod p$ para `e>0`.

O **Teorema de Euler** generaliza a afirmação. Se `gcd(a,m)=1`:

$$
a^{\varphi(m)}\equiv1\pmod m
$$

Aqui, $\varphi(m)$ é o [Totiente de Euler](totiente-euler.md). Euler permite reduzir expoentes com módulo composto, mas somente para bases coprimas a `m`.

## 4. Quando os expoentes também são grandes

Para calcular $a^{b^c}\pmod p$ com `p` primo e `p∤a`, calcule primeiro $b^c\pmod {p-1}$ e use o resultado como expoente de `a`. Isso é a ideia de *Exponentiation II*.

Não aplique essa redução cegamente em módulo composto. Por exemplo, a base pode compartilhar fatores com o módulo, e o comportamento dos expoentes pequenos antes da estabilização importa. Quando o problema exige isso, fatorar o módulo ou usar CRT pode ser necessário.

<!-- AUXÍLIO VISUAL 1

Criar um diagrama de exponenciação binária para 3¹³ mod 17, com os bits 1101 e as bases 3, 9, 13, 16. Destacar as multiplicações selecionadas pelos bits 1.

Arquivo sugerido: images/exponenciacao-modular.svg
-->

Continue em [Inverso Modular](inverso-modular.md) e [Sistemas de Congruências e CRT](sistemas-de-congruencias.md) para resolver divisões e múltiplas condições de restos.

## Problemas

{{ exercise_list(exercises) }}
