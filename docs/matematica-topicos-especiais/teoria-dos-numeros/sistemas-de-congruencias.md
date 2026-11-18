{% set exercises %}
  recommended:
    - name: Exponentiation II
      url: https://cses.fi/problemset/task/1712
      platform: CSES
      difficulty: medium
      topics: [congruências, Fermat, redução de expoentes]
      objective: Combine congruências de expoentes com uma exponenciação modular rápida.
{% endset %}

# Sistemas de congruências e teorema chinês do resto

Um sistema de congruências impõe várias condições sobre o mesmo inteiro:

$$
x\equiv a_i\pmod {m_i}
$$

O **Teorema Chinês do Resto** (CRT) explica quando essas condições podem ser combinadas em uma só.

## 1. Módulos coprimos dois a dois

Se os módulos são coprimos dois a dois, existe uma única solução módulo:

$$
M=m_1m_2\cdots m_k
$$

Para cada condição, tome $M_i=M/m_i$ e calcule o inverso $y_i=M_i^{-1}\pmod {m_i}$. Então:

$$
x\equiv\sum_{i=1}^{k}a_iM_iy_i\pmod M
$$

Cada termo é 0 nos módulos dos outros termos e vale $a_i$ no módulo `m_i`.

Exemplo: $x\equiv2\pmod3$ e $x\equiv3\pmod5$. Entre os números `2,5,8,11,14,...`, o primeiro que deixa resto 3 por 5 é 8. A solução é $x\equiv8\pmod{15}$.

## 2. Módulos não coprimos

Para combinar:

$$
x\equiv a\pmod m,\qquad x\equiv b\pmod n
$$

seja $g=\gcd(m,n)$. Existe solução se e somente se:

$$
a\equiv b\pmod g
$$

Quando existe, a solução é única módulo $\operatorname{lcm}(m,n)=mn/g$. Isso inclui o caso coprimo, em que `g=1` e sempre há compatibilidade.

Podemos escrever $x=a+mt$ e resolver:

$$
mt\equiv b-a\pmod n
$$

Depois de dividir por `g`, `m/g` possui inverso módulo `n/g`.

```cpp
struct Congruence {
    long long remainder;
    long long modulus; // positivo
};

long long normalize(long long value, long long mod) {
    value %= mod;
    if (value < 0) value += mod;
    return value;
}

optional<Congruence> merge_congruences(Congruence lhs, Congruence rhs) {
    long long a = normalize(lhs.remainder, lhs.modulus);
    long long b = normalize(rhs.remainder, rhs.modulus);
    long long x, y;
    long long g = extended_gcd(lhs.modulus, rhs.modulus, x, y);
    long long difference = b - a;
    if (difference % g != 0) return nullopt;

    long long reduced_modulus = rhs.modulus / g;
    long long step = static_cast<long long>(
        static_cast<__int128>(difference / g) * x % reduced_modulus
    );
    step = normalize(step, reduced_modulus);

    __int128 lcm128 = static_cast<__int128>(lhs.modulus / g) * rhs.modulus;
    if (lcm128 > LLONG_MAX) return nullopt;
    long long lcm = static_cast<long long>(lcm128);
    long long remainder = static_cast<long long>(
        (static_cast<__int128>(a) + static_cast<__int128>(lhs.modulus) * step) % lcm
    );
    return Congruence{normalize(remainder, lcm), lcm};
}
```

Para um sistema inteiro, comece com $x\equiv0\pmod1$ e incorpore cada congruência com `merge_congruences`. Se alguma fusão falhar, não há solução.

!!! warning "O produto pode estourar"
    Mesmo que cada módulo caiba em `long long`, o MMC acumulado pode não caber. Verifique os limites do enunciado ou use inteiros grandes quando a resposta precisa ser exata.

## 3. Onde CRT aparece

- reconstruir um número a partir de restos;
- sincronizar eventos periódicos com fases diferentes;
- separar cálculos módulo potências de primos e recombinar resultados;
- acelerar certas potências e contagens em módulos compostos.

<!-- AUXÍLIO VISUAL 1

Desenhar duas linhas de resíduos para módulos 3 e 5, destacando que os números 2 mod 3 e 3 mod 5 se cruzam em 8 e depois a cada 15 unidades.

Arquivo sugerido: images/teorema-chines-resto.svg
-->

## Problemas

{{ exercise_list(exercises) }}
