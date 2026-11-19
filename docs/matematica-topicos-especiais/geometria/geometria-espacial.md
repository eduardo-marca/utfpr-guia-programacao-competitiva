{% set exercises %}
  recommended:
    - name: Point Location Test
      url: https://cses.fi/problemset/task/2189
      platform: CSES
      difficulty: easy
      topics: [vetores, orientação, predicados]
      objective: Domine os predicados 2D que se generalizam para planos em 3D.
  additional:
    - name: Polygon Area
      url: https://cses.fi/problemset/task/2191
      platform: CSES
      difficulty: medium
      topics: [área, volume, produto vetorial]
      objective: Pratique a relação entre produto vetorial, área e volume.
{% endset %}

# Geometria espacial

Em 3D, pontos possuem coordenada `z`, retas viram relações entre vetores e planos substituem retas como separadores. Produto vetorial e produto misto são as ferramentas centrais.

## 1. Pontos e vetores em 3D

```cpp
struct P3 {
    Real x, y, z;
    P3 operator+(P3 other) const { return {x + other.x, y + other.y, z + other.z}; }
    P3 operator-(P3 other) const { return {x - other.x, y - other.y, z - other.z}; }
    P3 operator*(Real scale) const { return {x * scale, y * scale, z * scale}; }
};

Real dot(P3 a, P3 b) { return a.x * b.x + a.y * b.y + a.z * b.z; }
P3 cross3(P3 a, P3 b) {
    return {a.y * b.z - a.z * b.y,
            a.z * b.x - a.x * b.z,
            a.x * b.y - a.y * b.x};
}
Real norm3(P3 a) { return sqrtl(dot(a, a)); }
Real triple(P3 a, P3 b, P3 c) { return dot(cross3(a, b), c); }
```

Dois vetores são perpendiculares quando o dot product é zero; são paralelos quando seu cross product é o vetor nulo.

## 2. Retas e planos

Uma reta é $p+t\,d$. Um plano por um ponto `A` com normal `n` é:

$$
n\cdot(X-A)=0
$$

Três pontos não colineares `A,B,C` definem a normal $(B-A)\times(C-A)$. Para intersectar a reta `P+t d` com o plano:

$$
t=\frac{n\cdot(A-P)}{n\cdot d}
$$

```cpp
bool line_plane_intersection(P3 p, P3 direction, P3 a, P3 normal, P3& answer) {
    Real denominator = dot(normal, direction);
    if (fabsl(denominator) <= EPS) return false; // paralela ou contida
    Real t = dot(normal, a - p) / denominator;
    answer = p + direction * t;
    return true;
}
```

A distância de um ponto `P` ao plano é:

$$
\frac{|n\cdot(P-A)|}{|n|}
$$

O sinal do numerador decide em qual semiespaço `P` está.

## 3. Áreas e volumes

| Objeto | Medida |
|---|---|
| Paralelogramo com lados `a,b` | $|a\times b|$ |
| Triângulo `ABC` | $|(B-A)\times(C-A)|/2$ |
| Paralelepípedo `a,b,c` | $|(a\times b)\cdot c|$ |
| Tetraedro `ABCD` | $|((B-A)\times(C-A))\cdot(D-A)|/6$ |
| Esfera de raio `r` | volume $4\pi r^3/3$, área $4\pi r^2$ |
| Cilindro de raio `r`, altura `h` | volume $\pi r^2h$ |
| Cone de raio `r`, altura `h` | volume $\pi r^2h/3$ |

O produto misto nulo significa que quatro pontos são coplanares. Para coordenadas inteiras, calcule-o em `__int128` quando os limites permitirem; caso contrário, a escala pode exigir inteiros maiores ou ponto flutuante com tolerância.

## 4. Observações de modelagem

- uma caixa alinhada aos eixos é tratada por intervalos independentes em `x`, `y` e `z`;
- para esferas, compare distância ao quadrado com `r²` antes de calcular raízes;
- a interseção de dois planos é normalmente uma reta; planos paralelos exigem teste de normais e de um ponto;
- em 3D, desenhar ajuda, mas escrever a condição vetorial antes de codificar ajuda mais.

<!-- AUXÍLIO VISUAL 1

Mostrar uma reta atravessando um plano com normal n, o tetraedro formado por quatro pontos e o paralelepípedo associado ao produto misto.

Arquivo sugerido: images/geometria-espacial.svg
-->

## Problemas

{{ exercise_list(exercises) }}
