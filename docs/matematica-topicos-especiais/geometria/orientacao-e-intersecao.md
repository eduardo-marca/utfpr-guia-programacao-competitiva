{% set exercises %}
  recommended:
    - name: Line Segment Intersection
      url: https://cses.fi/problemset/task/2190
      platform: CSES
      difficulty: medium
      topics: [orientação, interseção de segmentos]
      objective: Cubra corretamente cruzamentos, toques nas extremidades e colinearidade.
    - name: Point Location Test
      url: https://cses.fi/problemset/task/2189
      platform: CSES
      difficulty: easy
      topics: [orientação, produto vetorial]
      objective: Use o sinal da área orientada como predicado geométrico.
{% endset %}

# Retas, orientação e interseções

Orientação é o predicado central da geometria 2D. Para pontos inteiros, seu sinal pode e deve ser calculado exatamente.

## 1. Orientação de três pontos

$$
\operatorname{orient}(A,B,C)=\operatorname{sgn}((B-A)\times(C-A))
$$

O resultado é `+1` quando `C` está à esquerda de `A→B`, `-1` quando está à direita e 0 quando os pontos são colineares.

```cpp
using i128 = __int128_t;

i128 cross(IP a, IP b, IP c) {
    return static_cast<i128>(b.x - a.x) * (c.y - a.y)
         - static_cast<i128>(b.y - a.y) * (c.x - a.x);
}

int orientation(IP a, IP b, IP c) {
    i128 value = cross(a, b, c);
    return (value > 0) - (value < 0);
}
```

Use `__int128` mesmo quando as coordenadas cabem em `long long`: diferenças e produtos podem ultrapassar esse tipo.

## 2. Ponto em segmento

Após confirmar colinearidade, basta testar a caixa delimitadora:

```cpp
bool on_segment(IP a, IP b, IP p) {
    return orientation(a, b, p) == 0
        && min(a.x, b.x) <= p.x && p.x <= max(a.x, b.x)
        && min(a.y, b.y) <= p.y && p.y <= max(a.y, b.y);
}
```

Separar esses dois testes é importante: estar no mesmo retângulo não implica estar na reta; estar na reta não implica estar entre as extremidades.

## 3. Interseção de segmentos

Dois segmentos próprios se cruzam quando os extremos de cada um ficam em lados opostos da reta do outro. Além disso, é preciso cobrir casos colineares que tocam a fronteira.

```cpp
bool segments_intersect(IP a, IP b, IP c, IP d) {
    int ab_c = orientation(a, b, c);
    int ab_d = orientation(a, b, d);
    int cd_a = orientation(c, d, a);
    int cd_b = orientation(c, d, b);

    if (ab_c == 0 && on_segment(a, b, c)) return true;
    if (ab_d == 0 && on_segment(a, b, d)) return true;
    if (cd_a == 0 && on_segment(c, d, a)) return true;
    if (cd_b == 0 && on_segment(c, d, b)) return true;
    return ab_c != ab_d && cd_a != cd_b;
}
```

Essa implementação considera tocar em uma ponta ou sobrepor parcialmente segmentos colineares como interseção. Se o enunciado exige cruzamento estrito, remova os quatro casos de fronteira e use apenas lados estritamente opostos.

## 4. Interseção de retas e segmentos em ponto flutuante

Para retas `A+t r` e `C+u s`, com `r=B-A` e `s=D-C`:

$$
t=\frac{(C-A)\times s}{r\times s}
$$

```cpp
bool line_intersection(P a, P b, P c, P d, P& answer) {
    P r = b - a, s = d - c;
    Real denominator = cross(r, s);
    if (sgn(denominator) == 0) return false; // paralelas ou coincidentes

    Real t = cross(c - a, s) / denominator;
    answer = a + r * t;
    return true;
}
```

Para segmentos, após obter `t` e `u`, a interseção pertence a ambos exatamente quando eles estão em `[0,1]`, com tolerância EPS. Quando a entrada é inteira e a resposta pede apenas sim/não, prefira a versão exata da seção anterior.

<!-- AUXÍLIO VISUAL 1

Mostrar os quatro sinais de orientação para segmentos que cruzam, além de exemplos de toque em ponta, sobreposição colinear e segmentos paralelos separados.

Arquivo sugerido: images/intersecao-segmentos.svg
-->

## Problemas

{{ exercise_list(exercises) }}
