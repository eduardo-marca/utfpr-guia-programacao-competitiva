# Combinatória

## Fatorial

$$ n!=n\times (n-1)\times (n-2)\times \cdots \times 1 $$

Pode ser computado eficientemente com recursão + DP

```cpp
constexpr int maxN = 20; // O maior N cujo fatorial precisa ser calculado

int fact[maxN+1]; // Deve ser inicializado com -1 (ou utilizar map)

int factorial(int n) {
    if(n <= 1) return 1;
    if(fact[n] == -1) {
        fact[n] = n * factorial(n-1);
    }

    return fact[n];
}
```

## Coeficiente Binomial

$$ \binom{n}{k}=\frac{n!}{k!(n-k)!} $$

Pode ser interpretado como o número de maneiras de escolher $k$ elementos de $n$.
Também escrito como $C(n, k)$ ou $nCk$.

### Propriedades

#### Simetria

$$ \binom{n}{k}=\binom{n}{n-k} $$

#### Identidade de Pascal

$$ \binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k} $$

#### Soma de Combinações

$$ \sum_{k=0}^{n} \binom{n}{k}=2^n $$

#### Fórmula Multiplicativa

$$ \binom{n}{k}=\frac{n(n-1)(n-k+1)}{k!} $$

### Computação Eficiente

Pode ser computado eficientemente com recursão (identidade de Pascal) + DP

```cpp
constexpr int maxN = 20; // O maior N cujo binomial precisa ser calculado

int dp[maxN+1][maxN+1]; // Deve ser inicializado com -1 (ou utilizar map)

int binom(int n, int k) {
    if(k == 0 || n == k) return 1;

    if(dp[n][k] == -1) {
        dp[n][k] = binom(n-1, k-1) + binom(n-1, k);
    }

    return dp[n][k];
}
```

### Computação Eficiente (Modular)

Pode ser computado eficientemente com módulo.

```cpp
constexpr int MOD = 1e9 + 7; // Modulo precisa ser primo
constexpr int maxN = 1e6;

// Pre computar fatoriais e inverso modular do fatorial
fact[i] = (fact[i-1] * i) % MOD;
invfact[i] = modinv(fact[i], MOD);

int binom(int n, int k) = {
    fact[n] * invfact[k] % MOD * invfact[n-k] % MOD;
}
```

## Principais Fórmulas

### Arranjo

### Permutação

Número de arranjos ordenados de $k$ elementos entre $n$ elementos.

$$ P(n, k)=\frac{n!}{(n-k)!} $$

### Permutação com repetição

$n$ elementos com repetições $n_1, n_2, \dots$

$$ \frac{n!}{n_1!n_2!\dots n_3!} $$

### Combinação

Número de formas de escolher $k$ elementos distintos de $n$ tipos.

$$ _{n}C_k=\binom{n}{k}=\frac{n!}{k!(n-k)!} $$

### Combinação com repetição

Número de formas de escolher $k$ elementos de $n$ tipos.

$$ _{n}C_k=\binom{n+k-1}{k}=\frac{(n+k-1)!}{k!(n-1)!} $$

### Teorema Binomial

$$ {(a+b)}^{n}=\sum_{k=0}^n\binom{n}{k}a^{n-k}b^k $$

## Coeficientes Multinomiais

Generalização dos coeficientes binomiais.

$$ \binom{n}{k_1,k_2,\dots ,k_m}=\frac{n!}{k_1!k_2!\dots k_m!} $$

com $k_1+k_2+\cdots +k_m=n$.

Usado para dividir $n$ elementos nomeados em grupos de tamanhos dados.

## Números de Catalan

Podem ser calculados com coeficientes binomiais

$$ C_{n}=\frac{1}{n+1}\binom{2n}{n}=\binom{2n}{n}-\binom{2n}{n+1} $$

Ou de forma recursiva

$$ C_{n}=\sum_{i=0}^{n}C_{i}C{n-1} $$

$$ C_{0}=1 $$

Algumas aplicações:

- $C_n$: número de formas de construir expressões válidas de parênteses com $n$ parênteses de abertura e $n$ de fechamento.
- $C_n$: número de árvores binárias com $n$ nodos.
- $C_{n-1}$: número de árvores binárias com raiz e $n$ nodos.
- $C_n$: maneiras de triangular um polígono.
