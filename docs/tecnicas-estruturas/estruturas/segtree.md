{% set exercises %}
  recommended:
    - name: Dynamic Range Sum Queries
      url: https://cses.fi/problemset/task/1648
      platform: CSES
      difficulty: medium
      topics: [segment tree, soma em intervalo, atualização pontual]
      objective: Implemente a versão básica com consultas de soma e atualizações de atribuição.
    - name: Dynamic Range Minimum Queries
      url: https://cses.fi/problemset/task/1649
      platform: CSES
      difficulty: medium
      topics: [segment tree, mínimo em intervalo]
      objective: Troque a operação de soma por mínimo e escolha o elemento neutro correto.
    - name: Hotel Queries
      url: https://cses.fi/problemset/task/1143
      platform: CSES
      difficulty: medium
      topics: [segment tree, máximo, busca na árvore]
      objective: Desça pela árvore para encontrar a primeira posição com capacidade suficiente.
    - name: Prefix Sum Queries
      url: https://cses.fi/problemset/task/2166
      platform: CSES
      difficulty: hard
      topics: [segment tree, nó customizado, prefix sum]
      objective: Modele cada nó com mais de uma informação para responder consultas de prefixo máximo.
  additional:
    - name: List Removals
      url: https://cses.fi/problemset/task/1749
      platform: CSES
      difficulty: medium
      topics: [segment tree, k-ésimo elemento, busca na árvore]
      objective: Localize e remova repetidamente o k-ésimo elemento ainda ativo.
    - name: Xenia and Bit Operations
      url: https://codeforces.com/problemset/problem/339/D
      platform: Codeforces
      difficulty: medium
      topics: [segment tree, operações alternadas]
      objective: Adapte o merge de acordo com a altura do nó.
    - name: GSS1 - Can you answer these queries I
      url: https://www.spoj.com/problems/GSS1/
      platform: SPOJ
      difficulty: hard
      topics: [segment tree, máximo subarray, nó customizado]
      objective: Combine soma total, melhor prefixo, melhor sufixo e melhor subarray.
{% endset %}

# Árvore de Segmentos

Uma **árvore de segmentos** (*segment tree* ou *segtree*) mantém informações sobre intervalos de um vetor enquanto ele recebe atualizações. Ela é uma das estruturas mais versáteis da programação competitiva para problemas de consultas em intervalo.

## 1. O problema que a estrutura resolve

Considere um vetor `A` com `N` elementos e muitas operações dos tipos:

- consultar a soma, o mínimo ou o máximo no intervalo `[L, R]`;
- alterar o valor de uma posição.

Se calcularmos cada consulta percorrendo o intervalo, uma operação pode custar $O(N)$. Com `Q` operações, o pior caso é $O(NQ)$.

Prefix sums resolvem consultas de soma em $O(1)$, mas deixam de ser eficientes quando os valores mudam: alterar `A[i]` pode exigir corrigir muitos prefixos.

A árvore de segmentos equilibra essas duas necessidades:

| Operação | Vetor simples | Prefix sums | Árvore de segmentos |
|---|---:|---:|---:|
| Consulta em intervalo | $O(N)$ | $O(1)$ | $O(\log N)$ |
| Atualização pontual | $O(1)$ | $O(N)$ | $O(\log N)$ |

!!! note "Quando usar"
    Ela é especialmente indicada quando há muitas **consultas de intervalo** e muitas **atualizações**. Para um vetor estático e apenas consultas de soma, prefix sums continuam sendo mais simples e mais rápidas.

## 2. A ideia: guardar respostas para intervalos

Cada nó da árvore representa um segmento contínuo do vetor. A raiz representa o vetor inteiro; seus filhos representam as duas metades desse intervalo; as folhas representam posições individuais.

Vamos usar:

```text
Índice:  0  1  2  3  4  5  6  7
Valor:  [2, 1, 3, 4, 5, 2, 6, 1]
```

Em uma árvore que armazena somas, cada nó guarda a soma de seu intervalo:

```text
                                [0, 7] = 24
                     ┌────────────┴────────────┐
                [0, 3] = 10                [4, 7] = 14
               ┌──────┴──────┐              ┌──────┴──────┐
          [0, 1] = 3     [2, 3] = 7    [4, 5] = 7     [6, 7] = 7
           ┌───┴───┐       ┌───┴───┐      ┌───┴───┐       ┌───┴───┐
        [0]=2   [1]=1   [2]=3   [3]=4  [4]=5   [5]=2   [6]=6   [7]=1
```

Para montar a árvore, combinamos os valores dos dois filhos. No exemplo:

$$
tree[p] = tree[2p] + tree[2p+1]
$$

O índice `p` identifica um nó no vetor interno da estrutura. Convencionalmente, os filhos de `p` ficam em `2p` e `2p+1`.

<!-- AUXÍLIO VISUAL 1 — PRIORITÁRIO

Criar um SVG de uma árvore de segmentos para o vetor `[2, 1, 3, 4, 5, 2, 6, 1]`.

- Cada nó deve exibir seu intervalo e a soma correspondente.
- As folhas devem exibir também o índice e o valor original.
- Usar uma cor para os nós internos e outra para as folhas.
- Tornar legíveis as relações pai-filho e preservar a ordem dos índices da esquerda para a direita.

Arquivo sugerido:
../assets/images/estruturas-de-dados/segment-tree/arvore-de-intervalos.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Árvore de segmentos que armazena somas](../assets/images/estruturas-de-dados/segment-tree/arvore-de-intervalos.svg)
-->

## 3. Consulta de intervalo passo a passo

Vamos calcular a soma no intervalo `[2, 6]`. Não precisamos visitar todas as folhas; basta decompor a consulta em nós cujos segmentos já estão completamente dentro do intervalo.

```text
Consulta: [2, 6]

[0, 7]  cruza a consulta                 → dividir
├─ [0, 3] cruza a consulta                → dividir
│  ├─ [0, 1] está fora                    → ignorar
│  └─ [2, 3] está totalmente dentro       → usar 7
└─ [4, 7] cruza a consulta                → dividir
   ├─ [4, 5] está totalmente dentro       → usar 7
   └─ [6, 7] cruza a consulta             → dividir
      ├─ [6, 6] está totalmente dentro    → usar 6
      └─ [7, 7] está fora                 → ignorar

Resposta: 7 + 7 + 6 = 20
```

Em cada nó, há três casos:

| Relação entre o nó `[l, r]` e a consulta `[ql, qr]` | Ação |
|---|---|
| Sem interseção | Retornar o elemento neutro. |
| Intervalo do nó inteiramente contido | Usar o valor já armazenado no nó. |
| Interseção parcial | Consultar os dois filhos e combinar as respostas. |

Para soma, o elemento neutro é `0`, pois `x + 0 = x`. Essa escolha é essencial: segmentos fora da consulta não podem alterar a resposta.

<!-- AUXÍLIO VISUAL 2 — PRIORITÁRIO

Criar uma versão da árvore anterior para a consulta `[2, 6]`.

- Pintar de verde os nós usados diretamente: `[2,3]`, `[4,5]` e `[6,6]`.
- Pintar de cinza os nós totalmente fora da consulta.
- Pintar de amarelo os nós que são apenas abertos para alcançar filhos.
- Exibir a expressão final `7 + 7 + 6 = 20` abaixo da árvore.

Arquivo sugerido:
../assets/images/estruturas-de-dados/segment-tree/consulta-de-intervalo.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Decomposição de uma consulta em uma árvore de segmentos](../assets/images/estruturas-de-dados/segment-tree/consulta-de-intervalo.svg)
-->

## 4. Atualização pontual

Suponha que `A[3]` mude de `4` para `10`. Apenas os nós cujos intervalos contêm o índice `3` precisam ser recalculados:

```text
[3, 3]:  4  → 10
[2, 3]:  7  → 13
[0, 3]: 10  → 16
[0, 7]: 24  → 30
```

Os demais segmentos permanecem corretos. Como o caminho da raiz até uma folha tem altura $O(\log N)$, a atualização também é logarítmica.

Depois dessa modificação, a consulta `[2, 6]` passa a valer:

$$
3 + 10 + 5 + 2 + 6 = 26
$$

<!-- AUXÍLIO VISUAL 3

Criar uma animação curta ou dois painéis SVG comparando o estado antes e depois de atualizar `A[3]` de `4` para `10`.

- Destacar em laranja o caminho `[3,3] → [2,3] → [0,3] → [0,7]`.
- Exibir os valores antigos e novos desses nós.
- Manter os nós não afetados visualmente apagados para enfatizar que não são recalculados.

Arquivo sugerido:
../assets/images/estruturas-de-dados/segment-tree/atualizacao-pontual.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Propagação de uma atualização pontual](../assets/images/estruturas-de-dados/segment-tree/atualizacao-pontual.svg)
-->

## 5. Implementação base: soma no intervalo

Esta implementação usa índices de `0` a `n - 1`, consultas inclusivas `[left, right]` e atualizações de atribuição: `set(index, value)`.

```cpp
#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    int n;
    vector<long long> tree;

    SegmentTree(const vector<long long>& values) {
        n = static_cast<int>(values.size());
        tree.assign(4 * n, 0);
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

    void set(int index, long long value) {
        set(1, 0, n - 1, index, value);
    }

    void set(int p, int l, int r, int index, long long value) {
        if (l == r) {
            tree[p] = value;
            return;
        }

        int mid = l + (r - l) / 2;
        if (index <= mid) {
            set(2 * p, l, mid, index, value);
        } else {
            set(2 * p + 1, mid + 1, r, index, value);
        }

        tree[p] = tree[2 * p] + tree[2 * p + 1];
    }

    long long query(int left, int right) {
        return query(1, 0, n - 1, left, right);
    }

    long long query(int p, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) {
            return 0;
        }

        if (ql <= l && r <= qr) {
            return tree[p];
        }

        int mid = l + (r - l) / 2;
        return query(2 * p, l, mid, ql, qr) +
               query(2 * p + 1, mid + 1, r, ql, qr);
    }
};
```

### Exemplo de uso

```cpp
vector<long long> values = {2, 1, 3, 4, 5, 2, 6, 1};
SegmentTree seg(values);

cout << seg.query(2, 6) << '\n';  // 20

seg.set(3, 10);
cout << seg.query(2, 6) << '\n';  // 26
```

!!! tip "Por que 4 * n?"
    A árvore não precisa ser completa quando `n` não é potência de dois. Reservar `4 * n` posições é uma forma simples e segura de ter espaço suficiente para a versão recursiva.

## 6. Como adaptar uma segtree para um problema

Esta é a parte que exige mais raciocínio. A recursão, a divisão dos intervalos e a complexidade quase nunca mudam; o que muda é **o significado de cada nó** e a regra para combinar dois filhos.

Antes de escrever código, responda a estas perguntas:

1. Qual é exatamente a consulta sobre um intervalo?
2. Que informação um nó deve guardar para responder a consulta quando dois segmentos são unidos?
3. Como combinar a informação do filho esquerdo com a do direito?
4. Qual é o elemento neutro para uma consulta sem interseção?
5. A atualização muda um ponto ou um intervalo inteiro?

O princípio que guia todas as adaptações é:

> `tree[p]` deve resumir corretamente o segmento `[l, r]` que o nó `p` representa.

### 6.1. Operações simples: troque merge e neutro

Para soma, usamos `merge(a, b) = a + b` e neutro `0`. Para outras operações associativas, a estrutura é idêntica.

| Consulta | Valor do nó | `merge(left, right)` | Neutro fora da consulta |
|---|---|---|---|
| Soma | soma do segmento | `left + right` | `0` |
| Mínimo | menor valor | `min(left, right)` | `+INF` |
| Máximo | maior valor | `max(left, right)` | `-INF` |
| MDC | MDC do segmento | `gcd(left, right)` | `0` |
| XOR | XOR do segmento | `left ^ right` | `0` |

Por exemplo, para uma árvore de mínimos, as únicas mudanças na implementação base são:

```cpp
const long long INF = (1LL << 60);

// Ao construir e recalcular um nó:
tree[p] = min(tree[2 * p], tree[2 * p + 1]);

// Sem interseção na consulta:
return INF;
```

!!! warning "O neutro faz parte da solução"
    Retornar `0` para uma consulta de mínimo pode produzir respostas incorretas quando todos os valores são positivos. Escolha sempre um valor `e` tal que `merge(x, e) = x`.

### 6.2. Atualização: atribuição ou incremento?

Uma atualização pontual pode ter semânticas diferentes:

```cpp
set(index, value);          // A[index] = value
add(index, delta);          // A[index] += delta
```

Para uma árvore de soma, `add` pode ser escrito alterando apenas a folha e somando novamente no caminho de volta:

```cpp
void add(int p, int l, int r, int index, long long delta) {
    if (l == r) {
        tree[p] += delta;
        return;
    }

    int mid = l + (r - l) / 2;
    if (index <= mid) {
        add(2 * p, l, mid, index, delta);
    } else {
        add(2 * p + 1, mid + 1, r, index, delta);
    }

    tree[p] = tree[2 * p] + tree[2 * p + 1];
}
```

Não confunda essas operações: substituir um valor por `x` e adicionar `x` ao valor anterior são atualizações diferentes.

### 6.3. Procurar uma posição usando informações dos nós

Uma segtree também pode encontrar uma posição, não apenas devolver um agregado. Para isso, descemos pela árvore escolhendo o primeiro filho que ainda pode conter a resposta.

Exemplo: cada hotel tem certa capacidade livre e cada grupo deve ocupar o **primeiro** hotel com capacidade pelo menos `x`. Armazene o máximo de cada segmento.

```cpp
int first_at_least(int p, int l, int r, long long x) {
    if (tree[p] < x) {
        return -1;
    }

    if (l == r) {
        return l;
    }

    int mid = l + (r - l) / 2;
    if (tree[2 * p] >= x) {
        return first_at_least(2 * p, l, mid, x);
    }

    return first_at_least(2 * p + 1, mid + 1, r, x);
}
```

Se o índice retornado for `i`, a capacidade daquele hotel diminui e fazemos uma atualização pontual em `i`.

O detalhe decisivo é a condição `tree[p] < x`: se até o máximo do segmento é insuficiente, nenhum descendente pode servir. Essa é a justificativa para descartar toda uma metade.

O mesmo padrão aparece em:

- encontrar o primeiro índice cujo valor atinge um limite;
- encontrar o k-ésimo elemento ativo, guardando contagens;
- localizar o primeiro prefixo cuja soma alcança `x`, quando os valores são não negativos.

### 6.4. Nós com várias informações: máximo subarray

Algumas consultas não podem ser respondidas guardando apenas uma soma, um mínimo ou um máximo. Para encontrar a maior soma de subarray em um intervalo, um nó precisa guardar quatro valores:

| Campo | Significado no segmento |
|---|---|
| `sum` | soma de todos os valores |
| `pref` | maior soma de um prefixo não vazio |
| `suff` | maior soma de um sufixo não vazio |
| `best` | maior soma de um subarray não vazio |

Se `left` e `right` representam segmentos adjacentes, o melhor subarray pode estar inteiramente em um filho ou atravessar a fronteira. A combinação é:

```cpp
struct Node {
    long long sum, pref, suff, best;
};

Node merge(const Node& left, const Node& right) {
    Node result;
    result.sum = left.sum + right.sum;
    result.pref = max(left.pref, left.sum + right.pref);
    result.suff = max(right.suff, right.sum + left.suff);
    result.best = max({left.best, right.best, left.suff + right.pref});
    return result;
}

Node make_leaf(long long value) {
    return {value, value, value, value};
}
```

Observe o termo `left.suff + right.pref`: ele representa exatamente os subarrays que atravessam a divisão entre os dois filhos. Identificar essas respostas que cruzam a fronteira é a chave para criar nós customizados.

!!! tip "Estratégia para criar um Node"
    Desenhe dois segmentos adjacentes. Liste as formas possíveis de uma resposta ficar inteiramente à esquerda, inteiramente à direita ou cruzar a fronteira. As informações necessárias para avaliar esses três casos são candidatas a campos do nó.

### 6.5. Quando uma atualização abrange um intervalo

A implementação deste capítulo atualiza uma única posição. Se a operação for “somar `x` a todos os valores de `[L, R]`”, modificar cada folha separadamente pode custar $O(N)$.

**Lazy propagation** resolve esse caso ao adiar a descida da atualização até ela ser necessária. Como essa técnica adiciona um segundo invariante — uma marca pendente em cada nó — ela possui um capítulo próprio: [Lazy Propagation em Árvores de Segmentos](lazy.md).

!!! note "Progressão sugerida"
    Antes de avançar, domine a segtree comum: a divisão dos intervalos, a regra de `merge`, o elemento neutro e a atualização pontual. Lazy propagation preserva esses fundamentos e acrescenta as operações `apply` e `push`.

<!-- AUXÍLIO VISUAL 4 — PRIORITÁRIO

Criar um fluxograma de adaptação de uma árvore de segmentos.

Perguntas em sequência:
1. A consulta é estática? Se sim, sugerir prefix sums ou sparse table quando apropriado.
2. Há atualização pontual? Se sim, usar segtree base.
3. A operação é soma, mínimo, máximo, MDC ou XOR? Exibir merge e neutro.
4. A resposta precisa de várias informações? Sugerir `struct Node` e análise da fronteira.
5. A atualização cobre intervalos? Sugerir lazy propagation e apontar para o capítulo específico.
6. É preciso achar uma posição? Sugerir descida guiada pela informação do nó.

Arquivo sugerido:
../assets/images/estruturas-de-dados/segment-tree/guia-de-adaptacao.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Fluxograma para adaptar uma árvore de segmentos](../assets/images/estruturas-de-dados/segment-tree/guia-de-adaptacao.svg)
-->

## 7. Roteiro de implementação e depuração

Antes de submeter, confira este roteiro:

1. Defina claramente se os intervalos do enunciado são inclusivos ou semiabertos.
2. Escreva a função `merge` e o elemento neutro antes da recursão.
3. Verifique se cada folha recebe a informação correta.
4. Após uma atualização, recalcule todos os ancestrais no caminho até a raiz.
5. Teste consultas de um único elemento, do vetor inteiro e fora do intervalo relevante.
6. Teste `n = 1`, valores repetidos e valores negativos quando o problema permitir.

Para depurar, um vetor pequeno é melhor que uma entrada aleatória grande. Por exemplo, após cada atualização, compare algumas consultas com a resposta calculada por um laço simples.

## 8. Complexidade

Para um vetor com `N` elementos:

| Operação | Complexidade |
|---|---:|
| Construção | $O(N)$ |
| Consulta de intervalo | $O(\log N)$ |
| Atualização pontual | $O(\log N)$ |
| Busca guiada pela árvore | $O(\log N)$ |
| Memória | $O(N)$ |

A construção visita cada nó uma vez. Embora o vetor interno tenha tamanho `4 * N`, a quantidade de nós da árvore é linear em `N`.

## 9. Erros comuns

### 1. Escolher o neutro errado

O caso de “sem interseção” participa da combinação. Para mínimo, use `+INF`; para máximo, `-INF`; para soma e XOR, `0`.

### 2. Misturar intervalos inclusivos e semiabertos

Este capítulo usa `[left, right]`. Se você preferir `[left, right)`, ajuste consistentemente a construção, as consultas e os testes de sobreposição.

### 3. Esquecer de recalcular o pai

Depois de mudar uma folha, todo ancestral precisa receber novamente o resultado de `merge(filho_esquerdo, filho_direito)`.

### 4. Usar segtree quando uma solução simples basta

Se não há atualizações, prefix sums, sparse table ou uma solução offline podem ser mais simples. A árvore de segmentos é poderosa, mas não deve ser automática.

### 5. Não provar o que o nó guarda

Em uma adaptação, escreva uma frase como: “`tree[p]` guarda o máximo subarray do segmento `[l, r]`”. Se não for possível explicar como dois filhos produzem essa informação, o `merge` provavelmente está incompleto.

## Problemas

{{ exercise_list(exercises) }}

## Recursos

- [Segment Tree - cp-algorithms](https://cp-algorithms.com/data_structures/segment_tree.html)
- [Segment Tree - CSES Range Queries](https://cses.fi/problemset/list/)
- [Segment Tree - AtCoder Library](https://atcoder.github.io/ac-library/production/document_en/segtree.html)
