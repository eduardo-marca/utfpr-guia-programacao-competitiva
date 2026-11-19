{% set exercises %}
  recommended:
    - name: Point Location Test
      url: https://cses.fi/problemset/task/2189
      platform: CSES
      difficulty: easy
      topics: [pontos, vetores, orientação]
      objective: Converta relações geométricas em operações entre vetores.
  additional:
    - name: Convex Hull
      url: https://cses.fi/problemset/task/2195
      platform: CSES
      difficulty: hard
      topics: [ordenação, vetores, polígono convexo]
      objective: Ordene pontos e mantenha uma fronteira orientada.
{% endset %}

# Pontos e vetores

Um ponto representa uma posição; um vetor representa deslocamento, direção ou velocidade. Em coordenadas cartesianas, ambos podem usar o mesmo par `(x,y)`, mas interpretar corretamente a operação evita erros conceituais.

## 1. Operações elementares

Para pontos `A`, `B` e um vetor `v`:

$$
\overrightarrow{AB}=B-A,\qquad A+v=\text{ponto transladado}
$$

O comprimento ao quadrado de `v=(x,y)` é $x^2+y^2$. Prefira-o à distância quando só é preciso comparar comprimentos.

```cpp
Real norm2(P v) { return v.x * v.x + v.y * v.y; }
Real norm(P v) { return sqrtl(norm2(v)); }
Real distance(P a, P b) { return norm(a - b); }

P unit(P v) {
    Real length = norm(v);
    return v / length; // pré-condição: length > EPS
}
```

O ponto médio é $(A+B)/2$. Uma divisão interna na razão `u:v` é:

$$
\frac{vA+uB}{u+v}
$$

onde o coeficiente de cada extremo é a distância até o outro extremo.

## 2. Rotações e vetores perpendiculares

Uma rotação de 90 graus anti-horária transforma `(x,y)` em `(-y,x)`. Ela é muito útil para construir normais sem trigonometria.

```cpp
P rotate90(P v) { return {-v.y, v.x}; }

P rotate(P v, Real angle) {
    Real c = cosl(angle), s = sinl(angle);
    return {v.x * c - v.y * s, v.x * s + v.y * c};
}
```

A rotação geral usa radianos. Para rotacionar um ponto `p` em torno de `center`, aplique `center + rotate(p-center, angle)`.

## 3. Ordenação angular

Ordenar direções por `atan2` é simples, mas pode introduzir imprecisão. Para coordenadas inteiras, separe o plano em dois semiplanos e use produto vetorial como comparador.

```cpp
int half(IP v) {
    return (v.y > 0 || (v.y == 0 && v.x >= 0)) ? 0 : 1;
}

bool polar_less(IP a, IP b) {
    if (half(a) != half(b)) return half(a) < half(b);
    __int128 cross = static_cast<__int128>(a.x) * b.y
                   - static_cast<__int128>(a.y) * b.x;
    if (cross != 0) return cross > 0;
    return static_cast<__int128>(a.x) * a.x + static_cast<__int128>(a.y) * a.y
         < static_cast<__int128>(b.x) * b.x + static_cast<__int128>(b.y) * b.y;
}
```

Essa ordenação aparece ao varrer raios em torno de um ponto, encontrar ângulos mínimos e processar polígonos estrelados.

!!! tip "Translade antes de analisar"
    Muitas fórmulas ficam mais claras se um ponto relevante vira a origem. Para analisar direções a partir de `O`, trabalhe com os vetores `P-O`.

<!-- AUXÍLIO VISUAL 1

Criar um painel com vetor AB, sua rotação de 90 graus e uma rotação por um ângulo θ em torno de um centro. Mostrar também os dois semiplanos usados na ordenação polar.

Arquivo sugerido: images/pontos-vetores.svg
-->

Os [produtos escalar e vetorial](produto-escalar-vetorial.md) transformam essas operações em testes de ângulo, lado e área.

## Problemas

{{ exercise_list(exercises) }}
