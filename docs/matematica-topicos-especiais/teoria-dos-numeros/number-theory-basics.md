{% set exercises %}
  recommended:
    - name: Sum of Divisors
      url: https://cses.fi/problemset/task/1082
      platform: CSES
      difficulty: hard
      topics: [agrupamento por quociente, somatórios, módulo]
      objective: Transforme uma soma aparentemente quadrática em blocos com o mesmo quociente.
  additional:
    - name: Two Knights
      url: https://cses.fi/problemset/task/1072
      platform: CSES
      difficulty: medium
      topics: [soma de progressão, contagem]
      objective: Aplique fórmulas de somatórios em uma contagem geométrica.
{% endset %}

# Fundamentos e identidades aritméticas

Antes de fatorar ou trabalhar com restos, vale reconhecer as somas que aparecem repetidamente. As fórmulas abaixo evitam laços longos e, em muitos problemas, permitem agrupar milhões de termos iguais.

## 1. Progressões e somas de potências

Para uma progressão aritmética com primeiro termo `a`, diferença `d` e `n` termos:

$$
\sum_{i=0}^{n-1}(a+id)=\frac{n(2a+(n-1)d)}{2}
$$

ou

$$
\sum_{i=1}^{n} a_i=\frac{n(a_1 + a_n)}{2}
$$

onde $a_1$ é o primeiro termo e $a_n$ é o último termo.

Casos essenciais:

$$
\sum_{i=1}^{n} i=\frac{n(n+1)}{2},\qquad
\sum_{i=1}^{n} i^2=\frac{n(n+1)(2n+1)}{6}
$$

$$
\sum_{i=1}^{n} i^3=\left(\frac{n(n+1)}{2}\right)^2=\left[ \sum_{i=1}^{n} i \right]^2
$$

Para uma progressão geométrica, quando `r ≠ 1`:

$$
1+r+r^2+\cdots+r^{n-1}=\frac{r^n-1}{r-1}
$$

Em módulo, só use a divisão pela forma multiplicada por um inverso modular quando `r-1` for coprimo ao módulo.

## 2. Pares, ímpares e contagens simples

Há `⌊n/2⌋` pares e `⌈n/2⌉` ímpares em `1..n`. Logo, o número de pares `(i,j)` com `1 ≤ i < j ≤ n` é:

$$
\binom{n}{2}=\frac{n(n-1)}{2}
$$

Essa fórmula também conta arestas de um grafo completo, substrings de comprimento pelo menos 2 e pares de posições em uma string. A identidade

$$
\sum_{d\mid n}\varphi(d)=n
$$

será retomada em [Totiente de Euler](totiente-euler.md): funções aritméticas frequentemente são somadas sobre divisores, não sobre todos os inteiros.

## 3. Agrupamento por quociente

Em somas que contêm `⌊n/i⌋`, o quociente muda apenas $O(\sqrt n)$ vezes. Se `q = n / left`, então todos os índices de `left` até `right = n / q` têm o mesmo valor `q`.

```cpp
long long sum_floor_quotients(long long n) {
    long long answer = 0;
    for (long long left = 1; left <= n; ) {
        long long quotient = n / left;
        long long right = n / quotient;
        answer += quotient * (right - left + 1);
        left = right + 1;
    }
    return answer;
}
```

O laço não percorre todos os `n` índices: para valores grandes de `i`, o quociente é pequeno; para valores pequenos, há poucos índices. Esse padrão é central em somas de divisores e problemas que contam múltiplos.

!!! warning "Overflow antes do módulo"
    Mesmo quando a resposta é modular, produtos como `n * (n + 1)` podem estourar `long long`. Reduza fatores antes de multiplicar, use `__int128` quando necessário ou cancele uma divisão exata antes do produto.

<!-- AUXÍLIO VISUAL 1

Criar uma tabela para n=20 que mostre os intervalos de i com o mesmo valor de floor(20/i), destacando por que há poucos blocos.

Arquivo sugerido: images/agrupamento-por-quociente.svg
-->

## Próximo passo

Siga para [Números Primos e Crivo](primos-e-crivo.md) para transformar propriedades de divisores em algoritmos eficientes.

## Problemas

{{ exercise_list(exercises) }}
