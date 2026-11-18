{% set exercises %}
  recommended:
    - name: Fibonacci Numbers
      url: https://cses.fi/problemset/task/1722
      platform: CSES
      difficulty: medium
      topics: [Fibonacci, fast doubling, exponenciação]
      objective: Calcule F(n) para n enorme sem iterar até n.
  additional:
    - name: Throwing Dice
      url: https://cses.fi/problemset/task/1096
      platform: CSES
      difficulty: medium
      topics: [recorrência linear, matriz, módulo]
      objective: Generalize a ideia de acelerar uma recorrência para além de Fibonacci.
{% endset %}

# Fibonacci e resultados clássicos

Alguns teoremas são mais úteis como lentes para reconhecer estruturas do que como algoritmos prontos. Fibonacci, quadrados e triplas pitagóricas aparecem em recorrências, decomposições e construções de inteiros.

## 1. Números de Fibonacci

Definimos:

$$
F_0=0,\qquad F_1=1,\qquad F_n=F_{n-1}+F_{n-2}
$$

A fórmula de Binet descreve a sequência:

$$
F_n=\frac{\phi^n-(1-\phi)^n}{\sqrt5},\qquad \phi=\frac{1+\sqrt5}{2}
$$

Ela é útil para análise, mas aritmética de ponto flutuante perde precisão rapidamente. Em código, use **fast doubling**, baseado nas identidades:

$$
F_{2n}=F_n(2F_{n+1}-F_n),\qquad
F_{2n+1}=F_n^2+F_{n+1}^2
$$

```cpp
pair<long long, long long> fibonacci_pair(long long n, long long mod) {
    if (n == 0) return {0, 1}; // F(0), F(1)
    auto [a, b] = fibonacci_pair(n / 2, mod);
    long long c = a * ((2 * b % mod - a + mod) % mod) % mod; // F(2k)
    long long d = (a * a % mod + b * b % mod) % mod;         // F(2k+1)
    if (n % 2 == 0) return {c, d};
    return {d, (c + d) % mod};
}
```

O custo é $O(\log n)$. Para módulos próximos de $10^{18}$, substitua as multiplicações por `__int128` ou multiplicação modular segura.

Identidades úteis:

$$
F_{m+n}=F_mF_{n+1}+F_{m-1}F_n
$$

$$
\gcd(F_m,F_n)=F_{\gcd(m,n)},\qquad
\sum_{i=0}^{n}F_i=F_{n+2}-1
$$

e a identidade de Cassini:

$$
F_{n+1}F_{n-1}-F_n^2=(-1)^n
$$

## 2. Teorema de Zeckendorf

Todo inteiro positivo possui uma representação única como soma de números de Fibonacci **distintos e não consecutivos**, usando `1, 2, 3, 5, 8, ...`.

Por exemplo, $100=89+8+3$. A construção é gulosa: escolha o maior Fibonacci que não excede o restante, subtraia e repita. Como números consecutivos nunca são escolhidos, a representação obtida é a de Zeckendorf.

```cpp
vector<long long> zeckendorf(long long n) {
    vector<long long> fib = {1, 2};
    while (fib.back() <= n - fib[fib.size() - 2]) {
        fib.push_back(fib[fib.size() - 1] + fib[fib.size() - 2]);
    }

    vector<long long> answer;
    for (int i = static_cast<int>(fib.size()) - 1; i >= 0; i--) {
        if (fib[i] <= n) answer.push_back(fib[i]), n -= fib[i];
    }
    return answer;
}
```

## 3. Teoremas sobre potências e quadrados

O **Teorema de Wilson** diz que, para `n>1`:

$$
n\text{ é primo}\iff(n-1)!\equiv-1\pmod n
$$

É uma caracterização elegante, mas calcular o fatorial o torna impraticável como teste de primalidade.

O **Último Teorema de Fermat** afirma que não existem inteiros positivos `a`, `b`, `c` com:

$$
a^n+b^n=c^n\qquad(n>2)
$$

Não o confunda com o **Pequeno Teorema de Fermat**, que é uma ferramenta algorítmica de aritmética modular.

O teorema dos quatro quadrados de **Lagrange** garante que todo inteiro positivo pode ser escrito como:

$$
n=a^2+b^2+c^2+d^2
$$

com inteiros `a,b,c,d`. Um refinamento útil: `n` é soma de três quadrados se e somente se não tem a forma $4^u(8v+7)$.

## 4. Triplas pitagóricas

Uma tripla pitagórica satisfaz $a^2+b^2=c^2$. Todas as primitivas são geradas por:

$$
a=m^2-n^2,\qquad b=2mn,\qquad c=m^2+n^2
$$

onde `m>n>0`, `gcd(m,n)=1` e `m,n` têm paridades diferentes. Multiplicar uma tripla por qualquer `k>0` gera todas as não primitivas.

Exemplo: `m=2`, `n=1` produz `(3,4,5)`; `m=3`, `n=2` produz `(5,12,13)`. Essas fórmulas são úteis para construir lados inteiros, mas exigem cuidado para não gerar a mesma tripla por parâmetros inválidos.

<!-- AUXÍLIO VISUAL 1

Conectar o triângulo 3-4-5 à escolha m=2,n=1 e mostrar a decomposição de 100=89+8+3 em Fibonacci não consecutivos.

Arquivo sugerido: images/fibonacci-e-triplas.svg
-->

## Problemas

{{ exercise_list(exercises) }}
