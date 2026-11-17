{% set exercises %}
  recommended:
    - name: Dynamic Range Sum Queries
      url: https://cses.fi/problemset/task/1648
      platform: CSES
      difficulty: medium
      topics: [Fenwick Tree, soma em intervalo, atualização pontual]
      objective: Use uma BIT para atualizar valores e consultar somas em intervalos.
    - name: List Removals
      url: https://cses.fi/problemset/task/1749
      platform: CSES
      difficulty: medium
      topics: [Fenwick Tree, k-ésimo elemento, frequências]
      objective: Encontre repetidamente a posição do k-ésimo elemento ainda ativo.
    - name: Forest Queries II
      url: https://cses.fi/problemset/task/1739
      platform: CSES
      difficulty: medium
      topics: [Fenwick Tree 2D, soma em retângulo]
      objective: Estenda a estrutura para duas dimensões.
  additional:
    - name: Salary Queries
      url: https://cses.fi/problemset/task/1144
      platform: CSES
      difficulty: hard
      topics: [Fenwick Tree, compressão de coordenadas, contagem]
      objective: Conte valores em faixas depois de comprimir salários e atualizações.
    - name: Enemy is weak
      url: https://codeforces.com/problemset/problem/61/E
      platform: Codeforces
      difficulty: hard
      topics: [Fenwick Tree, inversões, compressão de coordenadas]
      objective: Conte triplas decrescentes combinando varreduras e frequências.
{% endset %}

# Fenwick Tree

A **Fenwick Tree**, também chamada de **Binary Indexed Tree** ou **BIT**, mantém somas de prefixos com atualizações pontuais eficientes. É uma alternativa mais curta à [Árvore de Segmentos](segtree.md) quando o problema envolve soma, contagem ou XOR.

## 1. Prefixos que mudam

Considere muitas operações para alterar `A[i]` e consultar a soma de `[L, R]`.

| Operação | Vetor simples | Prefix sums | Fenwick Tree |
|---|---:|---:|---:|
| Consulta em intervalo | $O(N)$ | $O(1)$ | $O(\log N)$ |
| Atualização pontual | $O(1)$ | $O(N)$ | $O(\log N)$ |

Prefix sums deixam de ser práticos porque uma alteração exige corrigir todos os prefixos posteriores. A BIT armazena blocos de tamanhos diferentes para evitar esse custo.

!!! note "Quando preferir Fenwick"
    Para soma, contagem ou XOR com atualização pontual, uma BIT costuma ser mais simples que uma [Árvore de Segmentos](segtree.md). Para mínimo, máximo, nós customizados ou operações mais gerais, prefira segtree.

## 2. A ideia por trás de `i & -i`

A estrutura interna usa índices de `1` até `N`. Cada `bit[i]` guarda a soma de um bloco que termina em `i`; o tamanho desse bloco é o último bit ligado de `i`:

```cpp
int lowbit = i & -i;
```

| `i` | Binário | `i & -i` | Intervalo guardado em `bit[i]` |
|---:|---|---:|---|
| 1 | `0001` | 1 | `[1, 1]` |
| 2 | `0010` | 2 | `[1, 2]` |
| 3 | `0011` | 1 | `[3, 3]` |
| 4 | `0100` | 4 | `[1, 4]` |
| 6 | `0110` | 2 | `[5, 6]` |
| 8 | `1000` | 8 | `[1, 8]` |

Para o vetor abaixo, os nós da BIT representam estes blocos:

```text
Índice:  1  2  3  4  5  6  7  8
Valor:  [2, 1, 3, 4, 5, 2, 6, 1]

bit[1]=2, bit[2]=3, bit[3]=3, bit[4]=10,
bit[5]=5, bit[6]=7, bit[7]=6, bit[8]=24
```

<!-- AUXÍLIO VISUAL 1 — PRIORITÁRIO

Criar um SVG para a Fenwick Tree do vetor `[2, 1, 3, 4, 5, 2, 6, 1]`.

- Exibir o vetor original e, abaixo, os nós `bit[1]` até `bit[8]`.
- Cada nó deve mostrar o intervalo que resume e sua soma.
- Usar uma cor diferente para blocos de tamanhos 1, 2, 4 e 8.
- Destacar que `lowbit(i)` determina o tamanho do bloco.

Arquivo sugerido:
../assets/images/estruturas-de-dados/fenwick-tree/blocos-da-bit.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Blocos armazenados por uma Fenwick Tree](../assets/images/estruturas-de-dados/fenwick-tree/blocos-da-bit.svg)
-->

## 3. Consultando e atualizando

Para obter a soma de `[1, i]`, acumulamos blocos e removemos o último bit ligado:

```cpp
for (; i > 0; i -= i & -i) {
    answer += bit[i];
}
```

No prefixo `[1, 6]`, usamos `bit[6]` para `[5, 6]` e depois `bit[4]` para `[1, 4]`: `7 + 10 = 17`.

Para somar `delta` na posição `i`, visitamos todos os blocos que contêm essa posição:

```cpp
for (; i <= n; i += i & -i) {
    bit[i] += delta;
}
```

Por exemplo, adicionar `6` à posição `4` modifica apenas `bit[4]` e `bit[8]`:

```text
4 → 8 → fim

bit[4]: 10 → 16
bit[8]: 24 → 30
```

Uma soma de intervalo vem de dois prefixos:

$$
sum(L,R) = prefix(R) - prefix(L-1)
$$

<!-- AUXÍLIO VISUAL 2 — PRIORITÁRIO

Criar um SVG ou animação curta para `add(4, +6)` na BIT do exemplo.

- Destacar a posição 4 do vetor e o caminho `4 → 8`.
- Exibir os valores antes e depois de `bit[4]` e `bit[8]`.
- Indicar que os demais nós não mudam.

Arquivo sugerido:
../assets/images/estruturas-de-dados/fenwick-tree/atualizacao-pontual.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Caminho de atualização em uma Fenwick Tree](../assets/images/estruturas-de-dados/fenwick-tree/atualizacao-pontual.svg)
-->

## 4. Implementação base

A API abaixo usa índices de `0` a `n - 1`; a conversão para a numeração interna de `1` a `n` fica isolada na estrutura.

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<long long> bit;

    Fenwick(int n) : n(n), bit(n + 1, 0) {}

    void add(int index, long long delta) {
        for (int i = index + 1; i <= n; i += i & -i) {
            bit[i] += delta;
        }
    }

    // Soma dos índices [0, end).
    long long prefix_sum(int end) const {
        long long answer = 0;
        for (int i = end; i > 0; i -= i & -i) {
            answer += bit[i];
        }
        return answer;
    }

    // Soma do intervalo inclusivo [left, right].
    long long sum(int left, int right) const {
        return prefix_sum(right + 1) - prefix_sum(left);
    }

    // Menor índice 0-based com prefix_sum(index + 1) >= k.
    // Requer frequências não negativas e 1 <= k <= soma total.
    int kth(long long k) const {
        int index = 0;
        int jump = 1;
        while ((jump << 1) <= n) {
            jump <<= 1;
        }

        for (; jump > 0; jump >>= 1) {
            int next = index + jump;
            if (next <= n && bit[next] < k) {
                index = next;
                k -= bit[next];
            }
        }
        return index;
    }
};
```

### Exemplo de uso

```cpp
vector<long long> values = {2, 1, 3, 4, 5, 2, 6, 1};
Fenwick fenwick(static_cast<int>(values.size()));

for (int i = 0; i < static_cast<int>(values.size()); i++) {
    fenwick.add(i, values[i]);
}

cout << fenwick.sum(2, 5) << '\n';  // 14
fenwick.add(3, 6);                  // values[3] passa de 4 para 10
cout << fenwick.sum(2, 5) << '\n';  // 20
```

!!! warning "Adicionar não é atribuir"
    `add(index, delta)` soma `delta` ao valor atual. Para definir `A[index] = value`, guarde o vetor original e use `add(index, value - A[index])`.

## 5. Adaptações importantes

### 5.1. Frequências e o k-ésimo elemento

Se a BIT guarda frequências, a soma de prefixo informa quantos elementos existem até uma posição. O método `kth` desce diretamente pelos blocos e localiza o k-ésimo elemento ativo em $O(\log N)$. Ele é útil em remoções por ordem, rankings e multiconjuntos.

### 5.2. Atualização de intervalo e consulta pontual

Para adicionar `delta` a todos os valores de `[L, R]`, mantenha um vetor de diferenças:

```text
diff[L]     += delta
diff[R + 1] -= delta
```

Uma BIT sobre `diff` mantém essas alterações; o valor atual de `A[i]` é a soma de prefixo até `i`.

### 5.3. Atualização e soma de intervalo

Também é possível suportar atualização e soma de intervalos com **duas** BITs. A ideia usa diferenças para representar o efeito das atualizações sobre prefixos. É útil para somas, mas uma [lazy segtree](lazy.md) costuma ser mais fácil quando há operações diferentes.

### 5.4. Fenwick Tree 2D

Para uma grade, use dois laços com `i & -i`: um na linha e outro na coluna. Atualizações e somas de retângulos custam $O(\log^2 N)$.

## 6. Limitações

Uma BIT precisa de uma operação que permita desfazer prefixos. Para soma, usamos subtração; para XOR, usamos XOR novamente.

| Operação | BIT para intervalo? | Observação |
|---|---|---|
| Soma, XOR e contagem | Sim | Há forma de combinar e desfazer prefixos. |
| Mínimo ou máximo com mudanças arbitrárias | Não diretamente | Não há inversa simples. |

Para mínimos, máximos e combinações de várias informações, prefira uma [Árvore de Segmentos](segtree.md).

## 7. Erros comuns

1. Usar o índice `0` nos laços internos: ele nunca avança.
2. Confundir soma de `delta` com atribuição de um novo valor.
3. Misturar prefixos inclusivos com a API `[0, end)`.
4. Usar `kth` quando as frequências podem ser negativas, pois os prefixos deixam de ser monotônicos.

## 8. Complexidade

| Operação | Complexidade |
|---|---:|
| `add` | $O(\log N)$ |
| Prefixo ou soma em intervalo | $O(\log N)$ |
| `kth` | $O(\log N)$ |
| Memória | $O(N)$ |

## Problemas

{{ exercise_list(exercises) }}

## Recursos

- [Fenwick Tree - cp-algorithms](https://cp-algorithms.com/data_structures/fenwick.html)
- [Binary Indexed Tree - USACO Guide](https://usaco.guide/gold/PURS)
