{% set exercises %}
  recommended:
    - name: Minimum Euclidean Distance
      url: https://cses.fi/problemset/task/2194
      platform: CSES
      difficulty: hard
      topics: [distância, pares de pontos, sweep line]
      objective: Encontre um par mais próximo sem enumerar todos os pares.
  additional:
    - name: Point Location Test
      url: https://cses.fi/problemset/task/2189
      platform: CSES
      difficulty: easy
      topics: [distância, produto vetorial]
      objective: Relacione área orientada e distância à reta.
{% endset %}

# Distâncias, projeções e reflexões

Comparar distâncias é recorrente em geometria. Sempre que possível, compare valores ao quadrado: isso elimina raízes e preserva a ordem para quantidades não negativas.

## 1. Métricas comuns

Para `A=(x₁,y₁)` e `B=(x₂,y₂)`:

| Métrica | Fórmula | Uso típico |
|---|---|---|
| Euclidiana ao quadrado | $(x_1-x_2)^2+(y_1-y_2)^2$ | distância geométrica, par mais próximo |
| Manhattan | $|x_1-x_2|+|y_1-y_2|$ | movimentos em grade ortogonal |
| Chebyshev | $\max(|x_1-x_2|,|y_1-y_2|)$ | movimentos em oito direções |

Uma rotação de 45 graus relaciona Manhattan e Chebyshev: com `u=x+y` e `v=x-y`, várias consultas de Manhattan se tornam comparações de máximos e mínimos em novas coordenadas.

```cpp
Real dist2(P a, P b) { return norm2(a - b); }
Real distance(P a, P b) { return sqrtl(dist2(a, b)); }
```

## 2. Ponto para reta e segmento

Projete `P` na reta por `A` e `B`. Se $v=B-A$, o parâmetro da projeção é:

$$
t=\frac{(P-A)\cdot v}{v\cdot v}
$$

Na reta, `t` pode ser qualquer real; no segmento, limite `t` ao intervalo `[0,1]`.

```cpp
P projection_on_line(P p, P a, P b) {
    P direction = b - a;
    return a + direction * (dot(p - a, direction) / norm2(direction));
}

Real point_segment_distance(P p, P a, P b) {
    P direction = b - a;
    Real length2 = norm2(direction);
    if (length2 <= EPS) return distance(p, a);

    Real t = dot(p - a, direction) / length2;
    t = max(static_cast<Real>(0), min(static_cast<Real>(1), t));
    P closest = a + direction * t;
    return distance(p, closest);
}
```

A reflexão de `P` na reta é $2\cdot\operatorname{proj}(P)-P$. Ela aparece em problemas que usam o princípio de reflexão para transformar caminhos com ricochetes em segmentos retos.

## 3. Distância entre objetos

- entre dois segmentos: é 0 se eles se intersectam; caso contrário, é o mínimo das quatro distâncias de cada extremo ao outro segmento;
- entre ponto e círculo: $||P-C|-r|$;
- entre duas circunferências: compare a distância entre centros com `r₁+r₂` e `|r₁-r₂|`.

Para a distância de `P` à reta `AB`, a fórmula equivalente é:

$$
\frac{|(B-A)\times(P-A)|}{|B-A|}
$$

O numerador é duas vezes a área do triângulo, e a fórmula é simplesmente $\text{área}=\text{base}\times\text{altura}/2$.

## 4. Par mais próximo

O algoritmo ingênuo para `n` pontos testa $O(n^2)$ pares. O problema clássico do par euclidiano mais próximo é resolvido em $O(n\log n)$ por divide and conquer ou sweep line: ordene por `x`, mantenha candidatos por `y` numa faixa de largura determinada pela melhor distância atual e compare apenas pontos próximos.

O capítulo [Sweep Line e Pares Próximos](sweep-line.md) detalha a estrutura de eventos. Antes de usar qualquer algoritmo, confirme se o problema pede distância euclidiana, Manhattan ou ao quadrado.

<!-- AUXÍLIO VISUAL 1

Mostrar um ponto P, sua projeção em uma reta AB e os três casos do segmento: projeção interna, extremo A e extremo B. Incluir o paralelogramo que conecta cross product à altura.

Arquivo sugerido: images/distancia-projecao.svg
-->

## Problemas

{{ exercise_list(exercises) }}
