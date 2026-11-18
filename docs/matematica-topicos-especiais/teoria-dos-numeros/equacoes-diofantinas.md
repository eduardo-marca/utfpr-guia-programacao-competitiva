{% set exercises %}
  recommended:
    - name: Line
      url: https://codeforces.com/problemset/problem/7/C
      platform: Codeforces
      difficulty: medium
      topics: [diofantina linear, Euclides estendido]
      objective: Construa uma solução inteira para ax + by = c.
{% endset %}

# Equações inteiras e congruências lineares

Uma equação diofantina exige soluções inteiras. A pergunta mais importante vem antes de calcular: **a solução existe?** Para expressões lineares, o MDC responde exatamente isso.

## 1. Equação diofantina linear

Considere:

$$
ax+by=c
$$

Se $g=\gcd(a,b)$, existe solução inteira se e somente se $g\mid c$. Isso ocorre porque todo valor de `ax+by` é múltiplo de `g`; Bézout mostra que todo múltiplo de `g` pode ser obtido.

O [Euclides Estendido](euclides-estendido.md) encontra `u,v` com `au+bv=g`. Se `g` divide `c`, então:

$$
x_0=u\frac{c}{g},\qquad y_0=v\frac{c}{g}
$$

é uma solução particular. Todas as soluções são:

$$
x=x_0+t\frac{b}{g},\qquad y=y_0-t\frac{a}{g},\qquad t\in\mathbb Z
$$

```cpp
bool solve_diophantine(long long a, long long b, long long c,
                       long long& x, long long& y, long long& g) {
    g = extended_gcd(a, b, x, y); // a,b não negativos
    if (c % g != 0) return false;
    x *= c / g;
    y *= c / g;
    return true;
}
```

Para exigir limites, como `x,y ≥ 0`, transforme-os em um intervalo válido para `t` e interseccione os intervalos. Essa etapa é onde muitos problemas de moedas e distribuição de recursos ficam mais interessantes.

## 2. Congruência linear

A congruência

$$
ax\equiv b\pmod m
$$

equivale a dizer que `ax - b` é múltiplo de `m`. Seja $g=\gcd(a,m)$. Ela possui solução se e somente se `g` divide `b`.

Depois de dividir tudo por `g`, obtemos:

$$
\frac agx\equiv\frac bg\pmod {m/g}
$$

Agora $a/g$ é coprimo com `m/g`, portanto possui inverso. Uma solução é:

$$
x\equiv\frac bg\left(\frac ag\right)^{-1}\pmod {m/g}
$$

No módulo original, há exatamente `g` soluções distintas, espaçadas por `m/g`.

## 3. Outras equações importantes

Algumas famílias merecem ser reconhecidas, mesmo quando não há uma fórmula universal simples:

- $x^2+y^2=z^2$ possui a parametrização de triplas pitagóricas, apresentada em [Fibonacci e Resultados Clássicos](fibonacci-e-resultados-classicos.md).
- Uma congruência quadrática $x^2\equiv a\pmod m$ é um problema diferente da equação linear: não se pode "dividir por x" sem conhecer `gcd(x,m)`.
- Sistemas com várias congruências lineares são combinados pelo [Teorema Chinês do Resto](sistemas-de-congruencias.md).

!!! warning "Dividir uma congruência não é sempre válido"
    De `ac ≡ bc (mod m)`, só é permitido cancelar `c` quando `gcd(c,m)=1`. Caso contrário, você pode perder ou criar soluções. Reduza pelo MDC, como na seção anterior.

<!-- AUXÍLIO VISUAL 1

Representar as soluções de 6x+9y=30 como pontos de uma linha na malha, destacando o passo (3,−2) entre soluções consecutivas.

Arquivo sugerido: images/diofantina-linear.svg
-->

## Problemas

{{ exercise_list(exercises) }}
