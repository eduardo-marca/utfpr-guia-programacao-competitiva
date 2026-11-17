{% set exercises %}
  recommended:
    - name: Salary Queries
      url: https://cses.fi/problemset/task/1144
      platform: CSES
      difficulty: hard
      topics: [compressão de coordenadas, Fenwick Tree, consultas de faixa]
      objective: Comprima salários de atualizações e consultas antes de contar frequências.
    - name: Enemy is weak
      url: https://codeforces.com/problemset/problem/61/E
      platform: Codeforces
      difficulty: hard
      topics: [compressão de coordenadas, Fenwick Tree, inversões]
      objective: Converta valores grandes em ranks para contar triplas decrescentes.
    - name: Nested Ranges Count
      url: https://cses.fi/problemset/task/2169
      platform: CSES
      difficulty: hard
      topics: [compressão de coordenadas, ordenação, Fenwick Tree]
      objective: Ordene intervalos e conte relações de contenção por ranks.
  additional:
    - name: K-th Number
      url: https://www.spoj.com/problems/MKTHNUM/
      platform: SPOJ
      difficulty: hard
      topics: [compressão de coordenadas, persistent segment tree]
      objective: Use ranks para representar valores em uma estrutura persistente.
{% endset %}

# Compressão de Coordenadas

Compressão de coordenadas substitui valores grandes ou esparsos por seus **ranks** na ordem crescente, preservando comparações e empates. Ela permite usar vetores, [Fenwick Trees](../estruturas/fenwick.md) e árvores de segmentos quando os valores originais não cabem em um intervalo pequeno de índices.

## 1. Quando usar?

Imagine valores como salários, coordenadas ou tempos que chegam a $10^9$, mas existem apenas `N` valores relevantes. Criar um vetor de tamanho $10^9$ é inviável; criar um vetor de tamanho `N` é suficiente se preservarmos a ordem.

Exemplo:

```text
Valores:       [100, -7, 1000000000, 42, -7]
Valores únicos: [-7, 42, 100, 1000000000]
Rank 0-based:   [ 2,  0,          3,  1,  0]
```

Depois da compressão:

```text
x < y  ⇔  rank(x) < rank(y)
x = y  ⇔  rank(x) = rank(y)
```

Os valores repetidos recebem o mesmo rank.

## 2. Construindo os ranks

O procedimento possui três passos:

1. Copiar todos os valores relevantes.
2. Ordenar e remover duplicatas.
3. Localizar cada valor com `lower_bound`.

```cpp
vector<long long> coordinates = values;
sort(coordinates.begin(), coordinates.end());
coordinates.erase(unique(coordinates.begin(), coordinates.end()), coordinates.end());

auto rank_of = [&](long long value) {
    return static_cast<int>(lower_bound(
        coordinates.begin(), coordinates.end(), value
    ) - coordinates.begin());
};
```

`coordinates[rank]` preserva o valor original, então a transformação também pode ser revertida.

<!-- AUXÍLIO VISUAL 1 — PRIORITÁRIO

Criar um SVG que transforme os valores `[100, -7, 1000000000, 42, -7]` em ranks.

- Mostrar a ordenação e remoção de duplicatas.
- Conectar cada valor original ao rank correspondente.
- Destacar que os dois valores `-7` recebem o mesmo rank.

Arquivo sugerido:
images/ranks.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Compressão de valores em ranks](images/ranks.svg)
-->

## 3. Exemplo: consultas de faixa com Fenwick Tree

Suponha consultas que perguntam quantos valores estão entre `L` e `R`. Depois de comprimir os valores de todas as atualizações e limites de consulta, uma Fenwick Tree pode armazenar frequências por rank.

Para um limite qualquer `x`:

```cpp
int count_less_than_or_equal(long long x) {
    int end = upper_bound(coordinates.begin(), coordinates.end(), x)
            - coordinates.begin();
    return fenwick.prefix_sum(end);
}
```

Então a quantidade em `[L, R]` é:

```cpp
count_less_than_or_equal(R) - count_less_than_or_equal(L - 1)
```

O uso de `upper_bound` é importante: ele retorna o primeiro valor estritamente maior que `x`, incluindo todos os valores iguais a `x` no prefixo.

## 4. Compressão offline

Se uma operação futura pode introduzir um valor novo, esse valor também precisa estar em `coordinates`. Em problemas **offline**, leia primeiro todas as operações, guarde seus valores e só então comprima.

```text
1. Ler vetor inicial e todas as consultas.
2. Inserir em coordinates cada valor que pode aparecer.
3. Ordenar, remover duplicatas e construir a estrutura.
4. Processar as operações usando os ranks.
```

Se as operações chegam online e valores inéditos não podem ser conhecidos antes, considere uma árvore balanceada, uma policy-based data structure ou outra estrutura dinâmica.

## 5. Adaptações frequentes

| Objetivo | Busca em `coordinates` |
|---|---|
| Rank exato de um valor existente | `lower_bound(x)` |
| Quantidade de valores `< x` | `lower_bound(x)` |
| Quantidade de valores `<= x` | `upper_bound(x)` |
| Valores no intervalo `[L, R]` | prefixo em `upper_bound(R)` menos prefixo em `lower_bound(L)` |

### Compressão em duas dimensões

Para pontos `(x, y)`, muitas soluções comprimem apenas uma dimensão e ordenam a outra. Isso é comum em sweep line: ordene por `x`, comprima `y` e use uma Fenwick Tree sobre os ranks de `y`.

<!-- AUXÍLIO VISUAL 2

Criar um diagrama de pontos 2D com coordenadas Y esparsas.

- Mostrar os valores Y originais e seus ranks em uma segunda escala compacta.
- Desenhar uma Fenwick Tree conectada aos ranks de Y.
- Indicar que a ordem vertical é preservada, embora as distâncias não sejam.

Arquivo sugerido:
images/sweep-line-ranks.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Compressão de coordenadas em uma sweep line](images/sweep-line-ranks.svg)
-->

## 6. Erros comuns

1. Esquecer valores que aparecem apenas em atualizações futuras.
2. Usar `lower_bound` quando a consulta exige incluir valores iguais ao limite superior.
3. Esperar que a compressão preserve distâncias; ela preserva ordem e igualdade, não diferenças numéricas.
4. Atribuir ranks diferentes para valores repetidos.
5. Misturar ranks 0-based com estruturas internas 1-based, como Fenwick Tree.

## 7. Complexidade

Para `M` valores relevantes:

| Etapa | Complexidade |
|---|---:|
| Ordenar e remover duplicatas | $O(M \log M)$ |
| Encontrar um rank com busca binária | $O(\log M)$ |
| Armazenar coordenadas | $O(M)$ |

## Problemas

{{ exercise_list(exercises) }}

## Recursos

- [Coordinate Compression - USACO Guide](https://usaco.guide/silver/sorting-custom)
- [Coordinate Compression - cp-algorithms](https://cp-algorithms.com/data_structures/segment_tree.html)
