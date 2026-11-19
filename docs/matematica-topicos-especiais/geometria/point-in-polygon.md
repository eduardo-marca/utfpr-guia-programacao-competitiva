{% set exercises %}
  recommended:
    - name: Point in Polygon
      url: https://cses.fi/problemset/task/2192
      platform: CSES
      difficulty: hard
      topics: [ray casting, polígonos, fronteira]
      objective: Classifique consultas como interior, exterior ou fronteira.
  additional:
    - name: Point Location Test
      url: https://cses.fi/problemset/task/2189
      platform: CSES
      difficulty: easy
      topics: [orientação, segmentos]
      objective: Domine o predicado usado nas verificações de fronteira.
{% endset %}

# Localização de pontos

Antes de decidir se um ponto está dentro de uma figura, defina a convenção: o enunciado considera a fronteira como dentro? Nesta página, distinguimos explicitamente `Outside`, `Boundary` e `Inside`.

## 1. Ponto em triângulo

Para um triângulo orientado, calcule as orientações em relação às três arestas. O ponto está no interior ou borda quando os três sinais são não negativos, ou todos não positivos, dependendo da orientação do triângulo.

Essa é uma aplicação direta da ideia de que um polígono convexo é a interseção de semi-planos. Pontos sobre arestas precisam ser tratados com `on_segment` antes ou junto das comparações de sinal.

## 2. Ray casting em polígonos simples

Trace um raio horizontal de `P` para a direita. Se ele cruza a borda um número ímpar de vezes, `P` está dentro; se cruza um número par, está fora. O teste de borda deve vir primeiro.

```cpp
enum class Location { Outside, Boundary, Inside };

bool on_segment(P a, P b, P p) {
    return sgn(cross(a, b, p)) == 0
        && min(a.x, b.x) - EPS <= p.x && p.x <= max(a.x, b.x) + EPS
        && min(a.y, b.y) - EPS <= p.y && p.y <= max(a.y, b.y) + EPS;
}

Location point_in_polygon(P p, const vector<P>& polygon) {
    bool inside = false;
    for (int i = 0; i < static_cast<int>(polygon.size()); i++) {
        P a = polygon[i];
        P b = polygon[(i + 1) % polygon.size()];
        if (on_segment(a, b, p)) return Location::Boundary;

        bool crosses_height = (a.y > p.y) != (b.y > p.y);
        if (crosses_height) {
            Real x_at_height = a.x + (b.x - a.x) * (p.y - a.y) / (b.y - a.y);
            if (x_at_height > p.x) inside = !inside;
        }
    }
    return inside ? Location::Inside : Location::Outside;
}
```

Usar o intervalo semiaberto implícito em `(a.y > p.y) != (b.y > p.y)` impede contar duas vezes quando o raio passa por um vértice. Para entrada inteiramente inteira e resposta exata, compare sem dividir usando o sinal do produto vetorial.

## 3. Número de enrolamento

Outra formulação soma `+1` quando uma aresta cruza o raio para cima à esquerda do ponto e `-1` quando cruza para baixo. O número de enrolamento é zero fora e não zero dentro. Ele é especialmente útil quando a orientação das bordas importa ou quando se trabalha com curvas orientadas.

Para um polígono simples, paridade e número de enrolamento concordam sobre estar dentro; ray casting costuma ser mais simples de implementar.

## 4. Polígono convexo em O(log n)

Para muitas consultas no mesmo polígono convexo, `O(n)` por ponto pode ser caro. Com vértices em ordem anti-horária e um vértice fixo `P₀`:

1. rejeite pontos fora do leque entre as arestas `P₀P₁` e `P₀P_{n-1}`;
2. faça busca binária para achar o setor triangular `P₀P_iP_{i+1}` que contém a direção da consulta;
3. teste se o ponto está nesse triângulo.

O pré-processamento é só garantir a orientação e escolher um vértice; cada consulta custa $O(\log n)$. A fronteira continua exigindo testes de segmento.

!!! warning "Ray casting supõe polígono simples"
    Em polígonos auto-intersectantes, "dentro" pode depender da regra de preenchimento escolhida (paridade ou winding number). Leia a definição do problema antes de aplicar este código.

<!-- AUXÍLIO VISUAL 1

Mostrar um raio horizontal saindo de P com cruzamentos ímpares e pares, incluindo um caso que passa por vértice. Ao lado, mostrar o leque de triângulos para busca binária em polígono convexo.

Arquivo sugerido: images/point-in-polygon.svg
-->

## Problemas

{{ exercise_list(exercises) }}
