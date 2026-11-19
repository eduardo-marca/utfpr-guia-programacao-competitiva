{% set exercises %}
  recommended:
    - name: Fifa and Fafa
      url: https://codeforces.com/problemset/problem/935/C
      platform: Codeforces
      difficulty: medium
      topics: [círculos, tangência, construção geométrica]
      objective: Construa um círculo sujeito a uma condição de tangência interna.
  additional:
    - name: Ancient Berland Circus
      url: https://codeforces.com/problemset/problem/1/C
      platform: Codeforces
      difficulty: hard
      topics: [círculos, triângulos, trigonometria]
      objective: Relacione pontos de um triângulo ao círculo circunscrito.
{% endset %}

# Círculos e relações métricas

Um círculo é definido pelo centro `C` e raio `r`. Em problemas, quase todas as decisões vêm de comparar a distância entre centros com a soma ou a diferença dos raios.

## 1. Fórmulas essenciais

$$
\text{circunferência}=2\pi r,\qquad \text{área}=\pi r^2
$$

Para um triângulo de área `A`, lados `a,b,c` e semiperímetro `s`:

$$
R=\frac{abc}{4A},\qquad r_{inscrito}=\frac{A}{s}
$$

onde `R` é o raio do círculo circunscrito. Essas fórmulas conectam comprimentos de lados a círculos sem construir explicitamente os centros.

## 2. Relação entre dois círculos

Se `d` é a distância entre centros:

| Condição | Relação |
|---|---|
| $d>r_1+r_2$ | separados externamente |
| $d=r_1+r_2$ | tangentes externamente |
| $|r_1-r_2|<d<r_1+r_2$ | duas interseções |
| $d=|r_1-r_2|$ | tangentes internamente |
| $d<|r_1-r_2|$ | um dentro do outro, sem interseção |

Centros iguais exigem um caso separado: raios diferentes não intersectam; raios iguais representam o mesmo círculo e possuem infinitos pontos em comum.

## 3. Interseção de reta e círculo

Projete o centro na reta. Se a distância da projeção ao centro é maior que o raio, não há pontos; se é igual, há tangência; se é menor, avance e recue pela direção unitária da reta.

```cpp
vector<P> line_circle_intersections(P a, P b, P center, Real radius) {
    P direction = b - a;
    Real length2 = norm2(direction);
    if (length2 <= EPS) return {};

    Real t = dot(center - a, direction) / length2;
    P foot = a + direction * t;
    Real height2 = radius * radius - dist2(foot, center);
    if (height2 < -EPS) return {};

    Real offset = sqrtl(max(static_cast<Real>(0), height2) / length2);
    vector<P> answer = {foot + direction * offset};
    if (offset > EPS) answer.push_back(foot - direction * offset);
    return answer;
}
```

O código encontra interseções com a **reta**. Para restringir ao segmento `AB`, conserve apenas pontos cujo parâmetro `t` esteja em `[0,1]` com tolerância EPS.

## 4. Interseção de dois círculos

O ponto de referência sobre a linha dos centros fica a distância:

$$
a=\frac{r_1^2-r_2^2+d^2}{2d}
$$

do primeiro centro. A distância perpendicular até cada interseção é $h=\sqrt{r_1^2-a^2}$.

```cpp
vector<P> circle_intersections(P c1, Real r1, P c2, Real r2) {
    Real d = distance(c1, c2);
    if (d <= EPS) return {}; // nenhum ou infinitos; trate conforme a consulta
    if (d > r1 + r2 + EPS || d < fabsl(r1 - r2) - EPS) return {};

    Real a = (r1 * r1 - r2 * r2 + d * d) / (2 * d);
    Real h2 = max(static_cast<Real>(0), r1 * r1 - a * a);
    P direction = (c2 - c1) / d;
    P base = c1 + direction * a;
    P perpendicular = rotate90(direction) * sqrtl(h2);

    vector<P> answer = {base + perpendicular};
    if (norm2(perpendicular) > EPS * EPS) answer.push_back(base - perpendicular);
    return answer;
}
```

## 5. Tangentes e potência de um ponto

De um ponto externo `P` a um círculo de centro `C`, o comprimento da tangente satisfaz:

$$
T^2=|P-C|^2-r^2
$$

Essa expressão é a **potência do ponto** em relação ao círculo. Ela também aparece em problemas de cordas e secantes e permite comparar tangências sem calcular ângulos.

!!! warning "Classifique antes de dividir"
    Fórmulas de interseção dividem por `d`. Sempre trate primeiro centros coincidentes e casos sem interseção; caso contrário, tangências e círculos iguais podem produzir divisão por zero ou raízes negativas pequenas.

<!-- AUXÍLIO VISUAL 1

Mostrar a linha dos centros de dois círculos, o ponto base a e o deslocamento perpendicular h. Incluir reta secante, tangente e externa em relação a um círculo.

Arquivo sugerido: images/circulos-intersecoes.svg
-->

## Problemas

{{ exercise_list(exercises) }}
