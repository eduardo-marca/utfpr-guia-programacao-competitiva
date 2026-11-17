{% set exercises %}
  recommended:
    - name: Range Updates and Sums
      url: https://cses.fi/problemset/task/1735
      platform: CSES
      difficulty: hard
      topics: [lazy propagation, soma em intervalo, atribuição em intervalo]
      objective: Combine atualizações de adição e atribuição com consultas de soma.
    - name: Horrible Queries
      url: https://www.spoj.com/problems/HORRIBLE/
      platform: SPOJ
      difficulty: hard
      topics: [lazy propagation, range add, range sum]
      objective: Pratique a versão clássica de adicionar em um intervalo e consultar sua soma.
    - name: Polynomial Queries
      url: https://cses.fi/problemset/task/1736
      platform: CSES
      difficulty: hard
      topics: [lazy propagation, atualizações não uniformes]
      objective: Adapte a marca pendente para uma atualização que depende da posição.
  additional:
    - name: Multiples of 3
      url: https://www.spoj.com/problems/MULTQ3/
      platform: SPOJ
      difficulty: hard
      topics: [lazy propagation, estados, rotação]
      objective: Armazene contagens por resto e atualize os estados de um intervalo inteiro.
    - name: Range Affine Range Sum
      url: https://atcoder.jp/contests/practice2/tasks/practice2_k
      platform: AtCoder
      difficulty: hard
      topics: [lazy propagation, transformações afins, composição de tags]
      objective: Exercite a composição ordenada de atualizações do tipo ax + b.
{% endset %}

# Lazy Propagation em Árvores de Segmentos

Lazy propagation é uma extensão da [Árvore de Segmentos](segtree.md) para problemas que atualizam **intervalos inteiros**. Ela permite adições, atribuições e outras transformações em um intervalo, mantendo consultas e atualizações em $O(\log N)$.

## 1. Por que a segtree comum não basta?

Uma segtree comum atualiza uma posição seguindo um único caminho da raiz até uma folha. Porém, considere a operação:

> Some `x` a todos os valores do intervalo `[L, R]`.

Atualizar folha por folha visita até $R-L+1$ posições. Mesmo usando uma segtree para recalcular os pais, a operação pode custar $O(N)$.

Por exemplo, no vetor abaixo, adicionar `5` a `[2, 6]` alteraria cinco folhas:

```text
Índice:  0  1  2  3  4  5  6  7
Valor:  [2, 1, 3, 4, 5, 2, 6, 1]
```

Mas a árvore já possui nós que representam segmentos completos como `[2, 3]` e `[4, 5]`. Se conseguirmos atualizar esses nós sem descer até cada folha, economizamos trabalho.

## 2. A ideia de adiar trabalho

Em uma lazy segtree, cada nó armazena duas coisas:

- `tree[p]`: o resumo correto do segmento do nó, **já considerando todas as atualizações** que o atingiram;
- `lazy[p]`: uma atualização que seus filhos ainda não receberam.

Para uma árvore de soma com atualização “adicionar `delta`”, se o nó `p` representa `[l, r]`, aplicar a atualização nele significa:

$$
tree[p] \mathrel{+}= delta \cdot (r-l+1)
$$

e registrar que seus filhos também devem receber essa adição algum dia:

```cpp
tree[p] += delta * (r - l + 1);
lazy[p] += delta;
```

Não é necessário visitar os filhos agora. Essa é a parte “lazy”: o trabalho só será propagado se uma operação posterior realmente precisar entrar nos filhos.

!!! important "Invariante principal"
    `tree[p]` deve estar sempre correto para o intervalo inteiro de `p`.

    A marca `lazy[p]` não significa que o valor de `tree[p]` está desatualizado. Ela significa apenas que os filhos ainda não foram informados da atualização.

<!-- AUXÍLIO VISUAL 1 — PRIORITÁRIO

Criar um SVG de uma árvore de segmentos para soma, destacando um nó que representa `[2, 3]`.

- Antes da atualização, exibir folhas `3` e `4` e nó com soma `7`.
- Depois de adicionar `5` ao intervalo completo `[2, 3]`, exibir o nó com soma `17` e uma etiqueta `lazy = +5`.
- Manter as folhas visualmente inalteradas, com uma observação de que receberão a atualização apenas se for necessário descer até elas.

Arquivo sugerido:
../../assets/images/estruturas-de-dados/lazy-segtree/marca-pendente.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Marca pendente em uma lazy segtree](../../assets/images/estruturas-de-dados/lazy-segtree/marca-pendente.svg)
-->

## 3. As operações `apply` e `push`

Para evitar repetir lógica, separamos duas operações.

### 3.1. `apply`: atualiza um nó inteiro

`apply` recebe um nó e uma atualização que cobre exatamente seu segmento. Ela atualiza o resumo do nó e acumula a marca pendente.

```cpp
void apply(int p, int l, int r, long long delta) {
    tree[p] += delta * (r - l + 1);
    lazy[p] += delta;
}
```

### 3.2. `push`: transmite uma marca para os filhos

Antes de fazer uma operação que precisa descer de um nó para seus filhos, devemos garantir que eles recebam a marca pendente do pai.

```cpp
void push(int p, int l, int r) {
    if (l == r || lazy[p] == 0) {
        return;
    }

    int mid = l + (r - l) / 2;
    apply(2 * p, l, mid, lazy[p]);
    apply(2 * p + 1, mid + 1, r, lazy[p]);
    lazy[p] = 0;
}
```

Depois de `push`, o pai continua correto, os filhos passam a estar corretos e a marca do pai é limpa. As marcas podem continuar acumuladas mais abaixo — isso é esperado.

!!! warning "A ordem importa"
    Chame `push` antes de descer para os filhos em uma atualização ou consulta parcial. Sem isso, o algoritmo pode usar resumos de filhos que não receberam atualizações já aplicadas ao pai.

## 4. Exemplo passo a passo

Use novamente o vetor:

```text
A = [2, 1, 3, 4, 5, 2, 6, 1]
```

Vamos adicionar `5` ao intervalo `[2, 6]`.

```text
[0, 7] cruza a atualização                  → dividir
├─ [0, 3] cruza a atualização               → dividir
│  ├─ [0, 1] está fora                      → ignorar
│  └─ [2, 3] está totalmente dentro         → apply(+5)
│      soma: 7 → 17, lazy: +5
└─ [4, 7] cruza a atualização               → dividir
   ├─ [4, 5] está totalmente dentro         → apply(+5)
   │   soma: 7 → 17, lazy: +5
   └─ [6, 7] cruza a atualização            → dividir
      ├─ [6, 6] está totalmente dentro      → apply(+5)
      └─ [7, 7] está fora                   → ignorar
```

Foram alterados poucos nós, independentemente de `[2, 6]` possuir cinco elementos. A raiz é recalculada com as somas atualizadas e passa de `24` para `49`.

Se depois consultarmos `[2, 5]`, os nós `[2, 3]` e `[4, 5]` já estão totalmente cobertos e retornam `17` cada um. Nem precisamos propagar suas marcas para as folhas:

$$
17 + 17 = 34
$$

<!-- AUXÍLIO VISUAL 2 — PRIORITÁRIO

Criar um SVG da atualização `add(2, 6, +5)` no vetor `[2, 1, 3, 4, 5, 2, 6, 1]`.

- Marcar em verde os nós completamente cobertos que recebem `apply`.
- Marcar em amarelo os nós atravessados apenas para alcançar filhos.
- Mostrar `lazy = +5` nos nós `[2,3]` e `[4,5]`.
- Mostrar a nova soma da raiz, `49`.

Arquivo sugerido:
../../assets/images/estruturas-de-dados/lazy-segtree/atualizacao-de-intervalo.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Atualização de intervalo com lazy propagation](../../assets/images/estruturas-de-dados/lazy-segtree/atualizacao-de-intervalo.svg)
-->

## 5. Implementação completa: range add e range sum

Esta implementação aceita as operações:

- `add(left, right, delta)`: soma `delta` a todos os valores de `[left, right]`;
- `sum(left, right)`: devolve a soma de `[left, right]`.

Os intervalos são inclusivos e os índices vão de `0` a `n - 1`.

```cpp
#include <bits/stdc++.h>
using namespace std;

struct LazySegmentTree {
    int n;
    vector<long long> tree, lazy;

    LazySegmentTree(const vector<long long>& values) {
        n = static_cast<int>(values.size());
        tree.assign(4 * n, 0);
        lazy.assign(4 * n, 0);
        build(1, 0, n - 1, values);
    }

    void build(int p, int l, int r, const vector<long long>& values) {
        if (l == r) {
            tree[p] = values[l];
            return;
        }

        int mid = l + (r - l) / 2;
        build(2 * p, l, mid, values);
        build(2 * p + 1, mid + 1, r, values);
        tree[p] = tree[2 * p] + tree[2 * p + 1];
    }

    void apply(int p, int l, int r, long long delta) {
        tree[p] += delta * (r - l + 1);
        lazy[p] += delta;
    }

    void push(int p, int l, int r) {
        if (l == r || lazy[p] == 0) {
            return;
        }

        int mid = l + (r - l) / 2;
        apply(2 * p, l, mid, lazy[p]);
        apply(2 * p + 1, mid + 1, r, lazy[p]);
        lazy[p] = 0;
    }

    void add(int left, int right, long long delta) {
        add(1, 0, n - 1, left, right, delta);
    }

    void add(int p, int l, int r, int ql, int qr, long long delta) {
        if (qr < l || r < ql) {
            return;
        }

        if (ql <= l && r <= qr) {
            apply(p, l, r, delta);
            return;
        }

        push(p, l, r);
        int mid = l + (r - l) / 2;
        add(2 * p, l, mid, ql, qr, delta);
        add(2 * p + 1, mid + 1, r, ql, qr, delta);
        tree[p] = tree[2 * p] + tree[2 * p + 1];
    }

    long long sum(int left, int right) {
        return sum(1, 0, n - 1, left, right);
    }

    long long sum(int p, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) {
            return 0;
        }

        if (ql <= l && r <= qr) {
            return tree[p];
        }

        push(p, l, r);
        int mid = l + (r - l) / 2;
        return sum(2 * p, l, mid, ql, qr) +
               sum(2 * p + 1, mid + 1, r, ql, qr);
    }
};
```

### Exemplo de uso

```cpp
vector<long long> values = {2, 1, 3, 4, 5, 2, 6, 1};
LazySegmentTree seg(values);

seg.add(2, 6, 5);
cout << seg.sum(2, 5) << '\n';  // 34
cout << seg.sum(0, 7) << '\n';  // 49

seg.add(0, 3, -2);
cout << seg.sum(0, 3) << '\n';  // 12
```

## 6. Adaptando a marca pendente

A estrutura da recursão é a mesma em quase todos os problemas. O que muda é a atualização guardada em `lazy` e a forma de aplicá-la a `tree[p]`.

### 6.1. Adição em intervalo e mínimo ou máximo

Se cada valor de um intervalo recebe `+delta`, o mínimo e o máximo do intervalo também recebem `+delta`. Portanto:

```cpp
tree[p] += delta;
lazy[p] += delta;
```

Não multiplicamos pelo tamanho do segmento porque `tree[p]` não é uma soma.

### 6.2. Atribuição em intervalo

Para definir todos os valores de `[L, R]` como `value`, em uma árvore de soma:

```cpp
tree[p] = value * (r - l + 1);
```

Porém, `lazy[p] += value` está errado: uma atribuição nova substitui, e não se soma à marca anterior. Uma implementação costuma precisar de dois vetores:

```cpp
vector<long long> lazy_set;
vector<bool> has_set;
```

Ao aplicar uma atribuição, guardamos `lazy_set[p] = value` e `has_set[p] = true`. Ao fazer `push`, uma atribuição pendente deve ser enviada antes de qualquer adição pendente, pois ela descarta os valores antigos.

### 6.3. Compor atualizações na ordem correta

O ponto mais delicado de uma lazy segtree é que duas marcas podem atingir o mesmo nó antes de serem propagadas.

Para adições, a composição é simples:

```text
+3 seguido de +5  =  +8
```

Para transformações afins, em que cada atualização é `x ← a*x + b`, a ordem importa. Se uma marca antiga é `(a1, b1)` e depois chega `(a2, b2)`, a marca combinada deve representar:

$$
x \leftarrow a_2(a_1x+b_1)+b_2
$$

Logo:

$$
a = a_2a_1, \qquad b = a_2b_1+b_2
$$

!!! tip "Modelo mental"
    Leia uma tag lazy como uma função que ainda será aplicada aos descendentes. Quando uma nova tag chega, componha as funções na mesma ordem em que as atualizações ocorreram.

### 6.4. Checklist para uma nova lazy segtree

Antes de codificar, complete estas frases:

1. `tree[p]` guarda __________ no segmento `[l, r]`.
2. Uma atualização completa altera `tree[p]` por __________.
3. `lazy[p]` representa a função __________ ainda pendente nos filhos.
4. Duas marcas consecutivas são compostas como __________.
5. Em `push`, a marca é aplicada aos filhos e depois __________.

Se alguma resposta estiver vaga, experimente a operação em um segmento de dois elementos e acompanhe os valores manualmente.

<!-- AUXÍLIO VISUAL 3 — PRIORITÁRIO

Criar um diagrama em três quadros para explicar `push`.

1. Pai `[2,3]` com `sum = 17` e `lazy = +5`; filhos com valores antigos `3` e `4`.
2. O algoritmo precisa consultar apenas `[2,2]`, então executa `push`.
3. Filhos recebem a marca, ficam `8` e `9`; pai mantém `sum = 17` e sua marca torna-se `0`.

Arquivo sugerido:
../../assets/images/estruturas-de-dados/lazy-segtree/push.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Propagando uma marca pendente para os filhos](../../assets/images/estruturas-de-dados/lazy-segtree/push.svg)
-->

## 7. Complexidade

Para `N` elementos:

| Operação | Complexidade |
|---|---:|
| Construção | $O(N)$ |
| Atualização em intervalo | $O(\log N)$ |
| Consulta em intervalo | $O(\log N)$ |
| Memória | $O(N)$ |

Embora `push` possa executar `apply` em dois filhos, cada nível relevante da árvore é visitado apenas um número constante de vezes por operação. Por isso, a complexidade continua logarítmica.

## 8. Erros comuns

### 1. Atualizar `lazy` sem atualizar `tree`

Uma consulta que cobre totalmente o nó retorna `tree[p]` sem descer. Portanto, `tree[p]` precisa refletir a atualização imediatamente.

### 2. Esquecer de chamar `push` antes de uma operação parcial

Se o pai tem uma marca pendente e a operação desce a apenas um filho, os dois filhos precisam receber a marca antes de a árvore ser dividida novamente.

### 3. Limpar a marca antes de aplicá-la aos dois filhos

Guarde o valor de `lazy[p]` até chamar `apply` nos dois filhos; só depois faça `lazy[p] = 0`.

### 4. Usar a fórmula de soma em uma árvore de máximo

Para soma, adicionar `delta` em um segmento de tamanho `len` muda o nó em `delta * len`. Para mínimo ou máximo, a mudança é apenas `delta`.

### 5. Compor atribuição e adição como se fossem iguais

`set(4)` seguido de `add(3)` é diferente de `add(3)` seguido de `set(4)`. Em operações não comutativas, a ordem das tags é parte da solução.

## Problemas

{{ exercise_list(exercises) }}

## Recursos

- [Lazy Propagation - cp-algorithms](https://cp-algorithms.com/data_structures/segment_tree.html#range-updates-lazy-propagation)
- [Range Updates and Sums - CSES](https://cses.fi/problemset/task/1735)
- [Segment Tree - AtCoder Library](https://atcoder.github.io/ac-library/production/document_en/lazysegtree.html)
