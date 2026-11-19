{% set exercises %}
  recommended:
    - name: Point Location Test
      url: https://cses.fi/problemset/task/2189
      platform: CSES
      difficulty: easy
      topics: [orientação, produto vetorial, inteiros]
      objective: Classifique pontos à esquerda, à direita ou sobre uma reta orientada.
  additional:
    - name: Polygon Area
      url: https://cses.fi/problemset/task/2191
      platform: CSES
      difficulty: medium
      topics: [polígonos, área, coordenadas]
      objective: Trabalhe com coordenadas inteiras sem introduzir erros de ponto flutuante.
{% endset %}

# Fundamentos, representação e precisão

Geometria computacional começa pela escolha do tipo numérico. Em problemas de orientação, área dobrada e interseção de segmentos com entrada inteira, use inteiros. Em distâncias, ângulos e interseções que produzem coordenadas fracionárias, use `long double`.

## 1. Um tipo de ponto reutilizável

Pontos e vetores em 2D podem compartilhar a mesma estrutura: a diferença de dois pontos é um vetor, e somar um vetor a um ponto produz outro ponto.

```cpp
using Real = long double;
constexpr Real EPS = 1e-12L;

template <class T>
struct Point {
    T x, y;

    Point operator+(const Point& other) const { return {x + other.x, y + other.y}; }
    Point operator-(const Point& other) const { return {x - other.x, y - other.y}; }
    Point operator*(T scale) const { return {x * scale, y * scale}; }
    Point operator/(T scale) const { return {x / scale, y / scale}; }
};

using P = Point<Real>;
using IP = Point<long long>;

int sgn(Real value) {
    if (value > EPS) return 1;
    if (value < -EPS) return -1;
    return 0;
}
```

Use `IP` quando a lógica depende apenas de comparação e sinal; para produtos de coordenadas grandes, promova a conta para `__int128`. Use `P` quando precisar de raiz, divisão, seno ou cosseno.

## 2. Precisão e EPS

Valores de ponto flutuante quase nunca devem ser comparados com `==`. Em vez disso:

$$
a\approx b\iff |a-b|\le EPS
$$

O `EPS` deve ser pequeno comparado à escala da entrada, mas não existe uma constante universal. `1e-12` é um ponto de partida para `long double` com coordenadas moderadas; um problema com coordenadas da ordem de $10^{12}$ pode exigir uma tolerância relativa ou uma abordagem exata.

!!! warning "EPS não corrige uma fórmula errada"
    Não adicione EPS arbitrariamente a todas as comparações. Primeiro escolha a expressão geometricamente estável; depois use EPS apenas ao decidir se um valor teoricamente nulo é positivo, negativo ou zero.

## 3. Convenções que evitam bugs

- use radianos em `sin`, `cos` e `atan2`;
- defina se fronteira conta como dentro antes de implementar localização de pontos;
- documente se um polígono vem em sentido horário ou anti-horário;
- compare distância ao quadrado quando a raiz não for necessária;
- normalize vetores somente depois de verificar que a norma não é zero.

## 4. Geometria analítica em uma linha

Uma reta pode ser escrita de duas formas equivalentes:

$$
p(t)=a+t(b-a)
$$

e

$$
Ax+By+C=0
$$

A forma paramétrica é natural para interseções e segmentos; a implícita é natural para testar lados e distâncias. Os capítulos seguintes alternam entre elas conforme a operação.

<!-- AUXÍLIO VISUAL 1

Mostrar dois pontos A e B, o vetor B−A, a reta paramétrica e a mesma reta com um vetor normal para conectar as formas paramétrica e implícita.

Arquivo sugerido: images/representacao-geometrica.svg
-->

Continue em [Pontos e Vetores](pontos-vetores.md) para construir as operações básicas sobre essa representação.

## Problemas

{{ exercise_list(exercises) }}
