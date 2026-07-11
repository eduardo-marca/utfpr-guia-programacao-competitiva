# Teoria dos Números

## Identidades Aritméticas

Existem fórmulas conhecidas para se calcular a soma de potências $k$ de números de $1$ à $n^k$. As principais são

$$ \sum_{i=1}^{n}i = \frac{n(n+1)}{2} $$

$$ \sum_{i=1}^{n}i^{2} = \frac{n(n+1)(2n+1)}{6} $$

$$ \sum_{i=1}^{n}i^{3} = \left[ \frac{n(n+1)}{2} \right]^{2} = \left[ \sum_{i=1}^{n}i \right]^{2} $$

## Números Primos e Fatoração

### Definições e Propriedades

Um número inteiro maior que 1 é chamado de **número primo** se ele não pode ser formado pela multiplicação de dois números inteiros menores que ele mesmo. Caso contrário, ele é chamado de **número composto**.

Para todo número $n > 1$, existe uma única **fatoração prima**

$$ n=p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_k^{\alpha_k} $$

onde $p_1,p_2,\ldots,p_k$ são números primos.

O **número de fatores** de um número $n$ é

$$ \tau(n)=\prod_{i=1}^k (\alpha_i+1) $$

A **soma dos fatores** de $n$ é

$$ \sigma(n)=\prod_{i=1}^k (1+p_i+\cdots+p_i^{\alpha_i})=\prod_{i=1}^k \frac{p_i^{\alpha_i+1}-1}{p_i-1} $$

O **produto dos fatores** de $n$ é
$$ \mu(n)=n^{\tau(n)/2} $$

As vezes, um número é chamado de um **número perfeito** se $n = \sigma(n)-n$.

Existem infinitos números primos, e a quantidade de números primos menores que $n$ é aproximadamente

$$ \pi(n)=\frac{n}{\ln n} $$

Essa aproximação se torna melhor conforme $n$ cresce.

### Algoritmos Básicos

Testa se um número $n$ é primo em $O(\sqrt{n})$:

```cpp
bool prime(int n) {
    if(n < 2) return false;
    for(int x = 2; x*x <= n; x++) {
        if(n % x == 0) return false;
    }
    return true;
}
```

Constrói os fatores primos de $n$ em $O(\sqrt{n})$:

```cpp
vector<int> factors(int n) {
    vector<int> f;
    for(int x = 2; x*x <= n; x++) {
        while(n % x == 0) {
            f.push_back(x);
            n /= x;
        }
    }
    if(n > 1) f.push_back(n);
    return f;
}
```

O **Crivo de Eratóstenes** constrói uma lista de números primos até $n$ em $O(n \log \log n)$:

```cpp
for(int x = 2; x <= n; x++) {
    if(sieve[x]) continue;
    for(int u = 2*x; u <= n; u += x) {
        sieve[u] = x;
    }
}
```

Onde $sieve[n]$ indica o primeiro fator primo de $n$ e deve ser inicializado com $0$. Se $sieve[n] = n$, então $n$ é primo.

Acha todos os divisores de $n$ em $O(\sqrt{n})$:

```cpp
vector<int> findAllDivisors(int n) {
    vector<int> divisors;
    for (int i = 1; i * i <= n; ++i) {
        if (n % i == 0) {
            divisors.push_back(i);
            if (i * i != n) divisors.push_back(n / i);
        }
    }
    sort(divisors.begin(), divisors.end()); // sort if necessary
    return divisors;
}
```

## Máximo Divisor Comum e Mínimo Múltiplo Comum

### Definições e Algoritmo de Euclides

O **Máximo Divisor Comum** (MDC ou GCD) de dois números $a$ e $b$ é o maior número que divide ambos. Pode ser calculado recursivamente com o **Algoritmo de Euclides** em $O(\log \min(a, b))$:

```cpp
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a%b);
}
```

O **Mínimo Múltiplo Comum** (MMC ou LCM) de dois números $a$ e $b$ é o menor número que é múltiplo de ambos. Pode ser calculado em termos do MDC:

$$ \text{MMC}(a, b) = \frac{a \times b}{\text{MDC}(a, b)} $$

### Algoritmo de Euclides Estendido

O **Algoritmo de Euclides Estendido** calcula o MDC de dois números $a$ e $b$, além de encontrar inteiros $x$ e $y$ tais que

$$ ax + by = \text{MDC}(a, b) $$

Pode ser implementado em $O(\log \min(a, b))$:

```cpp
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a%b);
}
```

O algoritmo é baseado no teorema de Bezout, que diz que se existem inteiros $x$ e $y$ tais que $ax + by = d$, então $d$ é múltiplo do MDC de $a$ e $b$.

### Função Totiente de Euler

Dois números inteiros $a$ e $b$ são **coprimos** se o MDC deles é 1. A **Função Totiente de Euler** $\phi(n)$ conta a quantidade de inteiros menores que $n$ e coprimos com ele. A função pode ser calculada a partir da fatoração prima de $n$:

$$ \phi(n) = \prod_{i=1}^k p_i^{\alpha_i-1}(p_i-1) $$

$\phi(n)=n-1$ se $n$ é primo.

A função pode ser implementada em $O(\sqrt{n})$:

```cpp
int phi(int n) {
    int result = n;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0)
                n /= i;
            result -= result / i;
        }
    }
    if (n > 1)
        result -= result / n;
    return result;
}
```

## Aritmética Modular

### Definições e Propriedades

Dado um número inteiro $n > 1$, dois inteiros $a$ e $ b$ são **congruentes módulo** $n$ se $n$ divide a diferença $a - b$. Isso é denotado como

$$ a \equiv b \mod n $$

As principais propriedades da aritmética modular são:

- Se $a \equiv b \mod n$ e $c \equiv d \mod n$, então
    - $a + c \equiv b + d \mod n$
    - $a - c \equiv b - d \mod n$
    - $a \times c \equiv b \times d \mod n$
- Se $a \equiv b \mod n$, então para qualquer inteiro $k$, $a^k \equiv b^k \mod n$.
- Se $ac \equiv bc \mod n$ e MDC$(c, n) = 1$, então $a \equiv b \mod n$.

### Cálculo Modular

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

### Exponenciação Modular

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

### Pequeno Teorema de Fermat e Teorema de Euler

O **Pequeno Teorema de Fermat** diz que, se $m$ é primo e $x$ e $m$ são coprimos (MDC$(x, m) = 1$), então

$$ x^{m-1} \equiv 1 \mod m $$

$$ x^{k} \equiv x^{k \mod (m-1)} \mod m $$

Mais geralmente, o **Teorema de Euler** diz que, se $x$ e $m$ são coprimos, então

$$ x^{\phi(m)} \equiv 1 \mod m $$

### Inverso Modular

O **Inverso Modular** de um número $a$ módulo $m$ é um número $x$ tal que

$$ ax \equiv 1 \mod m $$

O inverso modular existe se e somente se MDC$(a, m) = 1$. Pode ser calculado usando o Algoritmo de Euclides Estendido em $O(\log m)$:

```cpp
// pode ser otimizado com dp
int inv(int a) {
  return a <= 1 ? a : m - (long long)(m/a) * inv(m % a) % m;
}
```

### Teorema Chinês do Resto (CRT) e Sistemas de Congruências

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

## Resolução de Equações

### Equações Diofantinas Lineares

Uma **Equação Diofantina Linear** é uma equação da forma

$$ ax + by = c $$

onde $a$, $b$, $c$ são inteiros conhecidos e $x$, $y$ são inteiros desconhecidos. A equação tem solução se e somente se GCD$(a, b)$ divide $c$.

Podemos encontrar uma solução particular usando o Algoritmo de Euclides Estendido.

A solução geral é obtida adicionando múltiplos de $\frac{b}{\text{MDC}(a, b)}$ a $x$ e subtraindo múltiplos de $\frac{a}{\text{MDC}(a, b)}$ de $y$. Ou seja,

$$ \left( x+ \frac{kb}{\text{gcd}(a, b)}, y- \frac{ka}{\text{gcd}(a, b)} \right) $$

onde $k$ é um número inteiro qualquer.

## Outros Resultados

### Números de Fibonacci
Os **Números de Fibonacci** são uma sequência de números inteiros definidos recursivamente da seguinte forma:

$$ F_0 = 0, \quad F_1 = 1 $$

$$ F_n = F_{n-1} + F_{n-2} \quad \text{para } n \geq 2 $$

A sequência começa como $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, \ldots$.

Eles podem ser calculados eficientemente usando a fórmula de Binet:

$$ F_n = \frac{\phi^n - (1 - \phi)^n}{\sqrt{5}} $$

onde $\phi = \frac{1 + \sqrt{5}}{2}$ é a razão áurea.

### Teorema de Wilson

O **Teorema de Wilson** afirma que um número inteiro $n > 1$ é primo se e somente se

$$ (n-1)! \equiv -1 \mod n $$

Apesar de ser um critério para primalidade, o Teorema de Wilson não é usado em prática para testar se um número é primo devido à ineficiência do cálculo de fatoriais para números grandes.

### Último Teorema de Fermat

O **Último Teorema de Fermat** afirma que não existem inteiros positivos $a$, $b$ e $c$ que satisfaçam a equação

$$ a^n + b^n = c^n $$

para qualquer valor inteiro de $n$ maior que 2.

### Critério de Divisibilidade

Um número é divisível por:

- 2: se o último dígito é par.
- 3: se a soma dos dígitos é divisível por 3.
- 4: se os dois últimos dígitos formam um número divisível por 4.
- 5: se o último dígito é 0 ou 5.
- 6: se é divisível por 2 e 3.
- 7: se a diferença entre o dobro do último dígito e o restante é divisível por 7.
- 8: se os três últimos dígitos formam um número divisível por 8.
- 9: se a soma dos dígitos é divisível por 9.
- 10: se o último dígito é 0.

### Teorema de Lagrange sobre Números Quadrados

O **Teorema de Lagrange sobre Números Quadrados** afirma que qualquer número inteiro positivo pode ser escrito como a soma de, no máximo, quatro quadrados de inteiros. Ou seja, para qualquer inteiro positivo $n$, existem inteiros $a$, $b$, $c$ e $d$ tais que 

$$ n = a^2 + b^2 + c^2 + d^2 $$

### Teorema de Zeckendorf

O **Teorema de Zeckendorf** afirma que qualquer número inteiro positivo pode ser escrito como a soma de números de Fibonacci diferentes e não consecutivos. Ou seja, para qualquer inteiro positivo $n$, existem índices $k_1, k_2, \ldots, k_m$ tais que

$$ n = F_{k_1} + F_{k_2} + \cdots + F_{k_m} $$

onde $F_k$ é o $k$-ésimo número de Fibonacci.

### Triplas Pitagóricas

Uma **Tripla Pitagórica** é uma tripla de inteiros positivos $(a, b, c)$ tal que

$$ a^2 + b^2 = c^2 $$

Se $(a, b, c)$ é uma tripla pitagórica, então $(ka, kb, kc)$ também é uma tripla pitagórica para qualquer inteiro positivo $k$.

Se $a$, $b$ e $c$ são coprimos dois a dois, então $(a, b, c)$ é chamada de **tripla pitagórica primitiva**.

Todas as triplas pitagóricas podem ser geradas a partir de triplas primitivas multiplicando por um inteiro positivo.

As triplas pitagóricas primitivas podem ser geradas usando os seguintes parâmetros inteiros positivos $m$ e $n$:

$$ a = m^2 - n^2 $$

$$ b = 2mn $$

$$ c = m^2 + n^2 $$

Onde $0<n<m$ $m$ e $n$ são coprimos e não são ambos ímpares.