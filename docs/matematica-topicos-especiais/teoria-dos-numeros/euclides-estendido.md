{% set exercises %}
  recommended:
    - name: Line
      url: https://codeforces.com/problemset/problem/7/C
      platform: Codeforces
      difficulty: medium
      topics: [Euclides estendido, diofantina linear]
      objective: Encontre uma solução inteira para uma equação linear ou determine que ela não existe.
  additional:
    - name: Exponentiation
      url: https://cses.fi/problemset/task/1095
      platform: CSES
      difficulty: medium
      topics: [MDC, inverso modular, módulo]
      objective: Pratique o raciocínio que reaparece na construção de inversos.
{% endset %}

# Algoritmo de Euclides estendido

O algoritmo de Euclides calcula `gcd(a,b)`. A versão estendida faz mais: encontra coeficientes inteiros `x` e `y` tais que

$$
ax+by=\gcd(a,b)
$$

Essa é a **identidade de Bézout**. Ela é a ponte entre MDC, equações diofantinas e inversos modulares.

## 1. Atualizando os coeficientes

Se $a=qb+r$, então $r=a-qb$. Suponha que a chamada recursiva encontrou:

$$
bx_1+ry_1=g
$$

Substituindo `r`, temos:

$$
g=bx_1+(a-qb)y_1=ay_1+b(x_1-qy_1)
$$

Portanto, os novos coeficientes são `x=y₁` e `y=x₁-qy₁`.

```cpp
long long extended_gcd(long long a, long long b, long long& x, long long& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long g = extended_gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}
```

Para `a,b ≥ 0` e não ambos nulos, o retorno é positivo e o custo é $O(\log\min(a,b))$. Para entradas negativas, aplique o algoritmo aos valores absolutos e ajuste o sinal do coeficiente correspondente.

## 2. Exemplo completo

Para `a=30` e `b=18`, o MDC é 6. Uma execução devolve `x=-1` e `y=2`:

$$
30(-1)+18(2)=6
$$

Os coeficientes não são únicos. Se `(x,y)` resolve a identidade e `g=gcd(a,b)`, então:

$$
\left(x+t\frac{b}{g},\;y-t\frac{a}{g}\right)
$$

também resolve para todo inteiro `t`. Essa é exatamente a forma das soluções de uma equação diofantina linear.

## 3. Aplicações diretas

- Para resolver `ax + by = c`, existe solução se e somente se `gcd(a,b)` divide `c`.
- Se `gcd(a,m)=1`, a identidade $ax+my=1$ mostra que `x` é o inverso de `a` módulo `m`.
- Ao combinar congruências, o algoritmo fornece o inverso necessário pelo [Teorema Chinês do Resto](sistemas-de-congruencias.md).

!!! warning "Coeficientes podem crescer"
    Mesmo que `a` e `b` caibam em `int`, as multiplicações intermediárias dos coeficientes podem exigir `long long`. Ao multiplicar a solução por `c/g`, verifique também o limite de resposta exigido pelo problema.

<!-- AUXÍLIO VISUAL 1

Mostrar a volta da recursão para 30 e 18: 30=1·18+12, 18=1·12+6, depois reconstruir 6=2·18−30.

Arquivo sugerido: images/euclides-estendido.svg
-->

Continue em [Equações Inteiras e Congruências Lineares](equacoes-diofantinas.md) para usar esses coeficientes em problemas concretos.

## Problemas

{{ exercise_list(exercises) }}
