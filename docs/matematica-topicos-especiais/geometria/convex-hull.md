{% set exercises %}
  recommended:
    - name: Convex Hull
      url: https://cses.fi/problemset/task/2195
      platform: CSES
      difficulty: hard
      topics: [convex hull, orientação, ordenação]
      objective: Implemente monotonic chain com a política correta para pontos colineares.
    - name: Minimum Euclidean Distance
      url: https://cses.fi/problemset/task/2194
      platform: CSES
      difficulty: hard
      topics: [convexidade, distância, pares de pontos]
      objective: Diferencie estruturas convexas de algoritmos para pares próximos.
{% endset %}

# Convex hull e aplicações

O **convex hull** é o menor polígono convexo que contém todos os pontos. Imagine uma faixa elástica envolvendo o conjunto: os pontos tocados pela faixa formam o hull.

## 1. Monotonic chain

O algoritmo de Andrew ordena os pontos lexicograficamente e constrói as cadeias inferior e superior. Ao adicionar um ponto, remove o último vértice enquanto ele forma uma curva que não pertence à fronteira convexa.

```cpp
vector<IP> convex_hull(vector<IP> points) {
    sort(points.begin(), points.end(), [](IP a, IP b) {
        return a.x != b.x ? a.x < b.x : a.y < b.y;
    });
    points.erase(unique(points.begin(), points.end(), [](IP a, IP b) {
        return a.x == b.x && a.y == b.y;
    }), points.end());
    if (points.size() <= 1) return points;

    vector<IP> lower, upper;
    for (IP p : points) {
        while (lower.size() >= 2
            && cross(lower[lower.size() - 2], lower.back(), p) <= 0) {
            lower.pop_back();
        }
        lower.push_back(p);
    }
    for (int i = static_cast<int>(points.size()) - 1; i >= 0; i--) {
        IP p = points[i];
        while (upper.size() >= 2
            && cross(upper[upper.size() - 2], upper.back(), p) <= 0) {
            upper.pop_back();
        }
        upper.push_back(p);
    }

    lower.pop_back();
    upper.pop_back();
    lower.insert(lower.end(), upper.begin(), upper.end());
    return lower; // anti-horário, sem repetir o primeiro ponto
}
```

O custo é $O(n\log n)$ pela ordenação; cada ponto entra e sai da pilha no máximo uma vez. O teste `cross <= 0` descarta pontos colineares intermediários. Troque por `cross < 0` quando o problema exigir todos os pontos da borda no hull.

## 2. Por que a pilha funciona

Na cadeia inferior, uma curva à direita ou colinear não extrema faria a fronteira "entrar" no conjunto ou manteria um ponto que está no segmento entre dois outros. Removê-la preserva a propriedade de que cada nova aresta é borda da envoltória parcial. A ordenação garante que um ponto removido não precisa voltar.

Esse argumento por invariante é mais importante que memorizar o sinal: desenhe a cadeia que deseja construir e escolha se pontos colineares devem permanecer.

## 3. Depois do hull

Com `h` vértices no hull, várias tarefas ficam menores:

- área e perímetro: percorra as `h` arestas;
- ponto em polígono convexo: consultas em $O(\log h)$;
- diâmetro (par mais distante): *rotating calipers* em $O(h)$;
- largura mínima e pares antipodais: também por calipers;
- soma de Minkowski de dois polígonos convexos: mescle as sequências de direções das arestas.

Para o diâmetro, avance um segundo ponteiro enquanto a área do paralelogramo aumenta. Cada ponteiro faz no máximo uma volta, por isso o algoritmo é linear após o hull.

## 4. Casos de borda

- nenhum ponto: trate conforme a interface do problema;
- um ponto: o hull tem um vértice;
- todos colineares: com `<=0`, o resultado contém apenas os dois extremos;
- pontos repetidos: remova antes de construir;
- coordenadas grandes: calcule `cross` em `__int128`.

!!! tip "Hull não resolve par mais próximo"
    O par mais distante pertence ao hull, mas o par mais próximo pode estar completamente no interior. Não aplique convex hull a problemas de menor distância sem uma justificativa adicional.

<!-- AUXÍLIO VISUAL 1

Mostrar pontos ordenados, a pilha da cadeia inferior removendo uma curva à direita e a união das cadeias inferior e superior. Incluir pares antipodais percorridos por rotating calipers.

Arquivo sugerido: images/convex-hull.svg
-->

## Problemas

{{ exercise_list(exercises) }}
