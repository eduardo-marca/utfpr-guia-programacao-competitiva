{% set exercises %}
  recommended:
    - name: Point Location Test
      url: https://cses.fi/problemset/task/2189
      platform: CSES
      difficulty: easy
      topics: [produto vetorial, orientação]
      objective: Use o sinal do cross product para classificar três pontos.
    - name: Line Segment Intersection
      url: https://cses.fi/problemset/task/2190
      platform: CSES
      difficulty: medium
      topics: [orientação, segmentos]
      objective: Combine orientações para detectar interseções de segmentos.
{% endset %}

# Produtos escalar e vetorial

Os produtos escalar e vetorial são as duas operações mais importantes da geometria 2D. Eles substituem grande parte do raciocínio visual por expressões algébricas curtas.

## 1. Produto escalar

Para vetores `a` e `b`:

$$
a\cdot b=a_xb_x+a_yb_y=|a||b|\cos\theta
$$

O sinal decide o tipo de ângulo: positivo para agudo, zero para perpendicular e negativo para obtuso. Ele também permite projetar `a` na direção de `b`:

$$
\operatorname{proj}_b(a)=b\frac{a\cdot b}{|b|^2}
$$

```cpp
Real dot(P a, P b) { return a.x * b.x + a.y * b.y; }

P projection(P a, P direction) {
    return direction * (dot(a, direction) / norm2(direction));
}
```

## 2. Produto vetorial em 2D

Em 2D, o produto vetorial é o escalar:

$$
a\times b=a_xb_y-a_yb_x=|a||b|\sin\theta
$$

Seu módulo é a área do paralelogramo formado pelos vetores. Para três pontos, calcule:

$$
\operatorname{cross}(A,B,C)=(B-A)\times(C-A)
$$

O sinal é positivo quando `C` está à esquerda da reta orientada `A→B`, negativo quando está à direita e zero quando os três são colineares.

```cpp
Real cross(P a, P b) { return a.x * b.y - a.y * b.x; }
Real cross(P a, P b, P c) { return cross(b - a, c - a); }

Real angle_between(P a, P b) {
    return atan2l(fabsl(cross(a, b)), dot(a, b)); // resultado em [0, π]
}
```

`atan2(|cross|, dot)` é mais estável do que usar apenas `acos`, especialmente perto de 0 e π.

## 3. Área e orientação

O triângulo `ABC` possui área:

$$
\frac{|\operatorname{cross}(A,B,C)|}{2}
$$

Assim, a mesma função decide lado, colinearidade, área e convexidade local de um polígono. Essa reutilização é a razão pela qual o produto vetorial aparece em convex hull, interseções e localização de pontos.

## 4. Extensão para 3D

Em 3D, `a×b` é um vetor perpendicular aos dois, e o produto misto mede volume:

$$
(a\times b)\cdot c
$$

O sinal indica de que lado de um plano um ponto está; o módulo dividido por 6 é o volume de um tetraedro. A implementação e as aplicações aparecem em [Geometria Espacial](geometria-espacial.md).

!!! warning "Escala do cross"
    Se as coordenadas inteiras podem chegar a $10^9$, um cross product pode chegar à ordem de $10^{18}$ ou mais. Use `__int128` para o cálculo antes de comparar seu sinal.

<!-- AUXÍLIO VISUAL 1

Mostrar dois vetores com projeção de a sobre b, o ângulo θ e o paralelogramo cuja área é |a×b|. Incluir três pontos A→B→C para os casos esquerda, direita e colinear.

Arquivo sugerido: images/dot-cross.svg
-->

## Problemas

{{ exercise_list(exercises) }}
