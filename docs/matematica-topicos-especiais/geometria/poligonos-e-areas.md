{% set exercises %}
  recommended:
    - name: Polygon Area
      url: https://cses.fi/problemset/task/2191
      platform: CSES
      difficulty: medium
      topics: [shoelace, área orientada, polígonos]
      objective: Calcule área e orientação percorrendo as arestas de um polígono.
    - name: Point in Polygon
      url: https://cses.fi/problemset/task/2192
      platform: CSES
      difficulty: hard
      topics: [polígonos, fronteira, orientação]
      objective: Trate simultaneamente interior, exterior e fronteira de um polígono simples.
{% endset %}

# Polígonos, áreas e pontos de grade

Um polígono é uma sequência cíclica de vértices. Em problemas, confirme se ele é simples (arestas não se cruzam), convexo e se a orientação é horário ou anti-horário: essas hipóteses mudam algoritmos e sinais.

## 1. Fórmula do cadarço

Para vértices $P_0,\ldots,P_{n-1}$, com índices módulo `n`:

$$
2A_{orientada}=\sum_{i=0}^{n-1}(x_iy_{i+1}-y_ix_{i+1})
$$

O sinal é positivo para orientação anti-horária e negativo para horária. A área geométrica é o valor absoluto dividido por 2.

```cpp
i128 signed_double_area(const vector<IP>& polygon) {
    i128 twice_area = 0;
    for (int i = 0; i < static_cast<int>(polygon.size()); i++) {
        IP a = polygon[i];
        IP b = polygon[(i + 1) % polygon.size()];
        twice_area += static_cast<i128>(a.x) * b.y - static_cast<i128>(a.y) * b.x;
    }
    return twice_area;
}
```

O perímetro é $\sum_i |P_{i+1}-P_i|$. Para polígonos convexos, a área também é a soma das áreas orientadas dos triângulos formados com qualquer origem.

## 2. Triângulos e centroide

Para lados `a,b,c`, o semiperímetro é $s=(a+b+c)/2$ e a fórmula de Heron dá:

$$
A=\sqrt{s(s-a)(s-b)(s-c)}
$$

Com coordenadas, o produto vetorial costuma ser mais estável. O centroide de um triângulo é simplesmente:

$$
G=\frac{A+B+C}{3}
$$

Para um polígono simples não degenerado, seja $c_i=x_iy_{i+1}-y_ix_{i+1}$ e $S=\sum c_i$, a área orientada dobrada. Seu centroide é:

$$
C_x=\frac{1}{3S}\sum_i(x_i+x_{i+1})c_i,\qquad
C_y=\frac{1}{3S}\sum_i(y_i+y_{i+1})c_i
$$

O sinal de `S` deve ser preservado na fórmula; inverter a orientação do polígono inverte simultaneamente numerador e denominador.

## 3. Pontos de grade e teorema de Pick

Para uma aresta inteira entre `(x₁,y₁)` e `(x₂,y₂)`, o número de passos de grade em sua fronteira é:

$$
\gcd(|x_2-x_1|,|y_2-y_1|)
$$

Somando esse valor sobre as arestas, obtemos `B`, o número de pontos de grade na borda. O teorema de Pick diz:

$$
A=I+\frac B2-1
$$

onde `I` é o número de pontos inteiros estritamente internos. Com área dobrada inteira:

$$
I=\frac{2A-B+2}{2}
$$

Pick vale para polígonos simples com vértices inteiros, não para polígonos auto-intersectantes.

## 4. Recorte de polígonos convexos

Para intersectar um polígono convexo com outro, o algoritmo de Sutherland–Hodgman recorta o polígono atual por cada semi-plano definido pelas arestas do polígono de corte. Para uma borda orientada `A→B`, mantenha os pontos à esquerda; quando uma aresta entra ou sai do semi-plano, insira a interseção de retas.

O algoritmo custa $O(nm)$ para polígonos de `n` e `m` vértices e depende de uma convenção consistente de orientação. Ele é mais simples que algoritmos gerais de interseção de polígonos e suficiente para muitas tarefas competitivas.

!!! warning "Área orientada não é sempre positiva"
    Não aplique valor absoluto cedo demais. O sinal informa a orientação do polígono e é necessário em fórmulas de centroide, clipping e convex hull.

<!-- AUXÍLIO VISUAL 1

Mostrar a soma de trapézios/triângulos da fórmula do cadarço e um polígono de grade com pontos internos I e pontos de borda B para o teorema de Pick.

Arquivo sugerido: images/poligonos-areas.svg
-->

Para decidir se uma consulta está dentro do polígono, siga para [Localização de Pontos](point-in-polygon.md).

## Problemas

{{ exercise_list(exercises) }}
