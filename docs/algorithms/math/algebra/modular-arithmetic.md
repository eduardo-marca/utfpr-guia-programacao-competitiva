# Aritmética Modular

## Definições e Propriedades

Dado um número inteiro $n > 1$, dois inteiros $a$ e $ b$ são **congruentes módulo** $n$ se $n$ divide a diferença $a - b$. Isso é denotado como

$$ a \equiv b \mod n $$

As principais propriedades da aritmética modular são:

- Se $a \equiv b \mod n$ e $c \equiv d \mod n$, então
    - $a + c \equiv b + d \mod n$
    - $a - c \equiv b - d \mod n$
    - $a \times c \equiv b \times d \mod n$
- Se $a \equiv b \mod n$, então para qualquer inteiro $k$, $a^k \equiv b^k \mod n$.
- Se $ac \equiv bc \mod n$ e MDC$(c, n) = 1$, então $a \equiv b \mod n$.

## Cálculo Modular

O **Cálculo Modular** é uma técnica usada para evitar overflow em operações aritméticas com números grandes. Ele consiste em aplicar a operação de módulo em cada passo da operação.

Aqui estão algumas operações básicas em aritmética modular:

$$ (a + b) \mod m = ((a \mod m) + (b \mod m)) \mod m $$

$$ (a - b) \mod m = ((a \mod m) - (b \mod m)) \mod m $$

$$ (a \times b) \mod m = ((a \mod m) \times (b \mod m)) \mod m $$

$$ a^{n} \mod m = {(a \mod m)}^{n} \mod m $$

$$ (a / b) \mod m = (a \mod m) \times (b^{-1} \mod m) \mod m $$

Onde $b^{-1}$ é o inverso multiplicativo de $b$ módulo $m$ (ver Inverso Modular).

Se o resultado for negativo, adicione $m$ para obter um resultado positivo.

$$ (x \mod m + m) \mod m $$

## Exponenciação Modular

A **Exponenciação Modular** calcula $a^b \mod m$ em $O(\log b)$:

```cpp
int modpow(int x, int n, int m) {
    if (n == 0) return 1%m;
    long long u = modpow(x,n/2,m);
    u = (u*u)%m;
    if (n%2 == 1) u = (u*x)%m;
    return u;
}
```

## Pequeno Teorema de Fermat e Teorema de Euler

O **Pequeno Teorema de Fermat** diz que, se $m$ é primo e $x$ e $m$ são coprimos (MDC$(x, m) = 1$), então

$$ x^{m-1} \equiv 1 \mod m $$

$$ x^{k} \equiv x^{k \mod (m-1)} \mod m $$

Mais geralmente, o **Teorema de Euler** diz que, se $x$ e $m$ são coprimos, então

$$ x^{\phi(m)} \equiv 1 \mod m $$

## Inverso Modular

O **Inverso Modular** de um número $a$ módulo $m$ é um número $x$ tal que

$$ ax \equiv 1 \mod m $$

O inverso modular existe se e somente se MDC$(a, m) = 1$. Pode ser calculado usando o Algoritmo de Euclides Estendido em $O(\log m)$:

```cpp
// pode ser otimizado com dp
int inv(int a) {
  return a <= 1 ? a : m - (long long)(m/a) * inv(m % a) % m;
}
```

## Teorema Chinês do Resto (CRT) e Sistemas de Congruências

O **Teorema Chinês do Resto** (CRT) fornece uma maneira de resolver sistemas de congruências da forma

$$ x \equiv a_1 \mod m_1 $$

$$ x \equiv a_2 \mod m_2 $$

$$\vdots$$

$$ x \equiv a_k \mod m_k $$

onde os módulos $m_1, m_2, \ldots, m_k$ são coprimos dois a dois.

Seja $x_m^{-1}$ o inverso de $x$ módulo $m$, e

$$ X_k=\frac{m_1 m_2 \cdots m_n}{m_k} $$

Então uma solução para o sistema é dada por

$$ x=a_1X_1X_{1_{m_1}}^{-1}+a_2X_2X_{2_{m_2}}^{-1}+\cdots+a_n X_n X_{n_{m_n}}^{-1} $$

A solução pode ser encontrada em $O(k \log M)$, onde $M = m_1 m_2 \cdots m_k$:

```cpp
struct Congruence {
    long long a, m;
};

long long chinese_remainder_theorem(vector<Congruence> const& congruences) {
    long long M = 1;
    for (auto const& congruence : congruences) {
        M *= congruence.m;
    }

    long long solution = 0;
    for (auto const& congruence : congruences) {
        long long a_i = congruence.a;
        long long M_i = M / congruence.m;
        long long N_i = mod_inv(M_i, congruence.m);
        solution = (solution + a_i * M_i % M * N_i) % M;
    }
    return solution;
}
```
