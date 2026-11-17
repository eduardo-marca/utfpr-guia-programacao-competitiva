{% set exercises %}
  recommended:
    - name: Dice Combinations
      url: https://cses.fi/problemset/task/1633
      platform: CSES
      difficulty: easy
      topics: [programação dinâmica, contagem, estados unidimensionais]
      objective: Conte maneiras de alcançar uma soma usando uma transição direta.
    - name: Minimizing Coins
      url: https://cses.fi/problemset/task/1634
      platform: CSES
      difficulty: easy
      topics: [programação dinâmica, minimização, moedas]
      objective: Modele a menor quantidade de moedas para cada soma possível.
    - name: Grid Paths
      url: https://cses.fi/problemset/task/1638
      platform: CSES
      difficulty: medium
      topics: [programação dinâmica, grid, contagem de caminhos]
      objective: Defina o estado por célula e combine caminhos de cima e da esquerda.
    - name: Book Shop
      url: https://cses.fi/problemset/task/1158
      platform: CSES
      difficulty: medium
      topics: [programação dinâmica, knapsack 0/1]
      objective: Escolha a ordem correta de iteração para não reutilizar um livro.
  additional:
    - name: Removal Game
      url: https://cses.fi/problemset/task/1097
      platform: CSES
      difficulty: medium
      topics: [programação dinâmica, intervalos, jogos]
      objective: Modele a vantagem ótima em cada intervalo restante.
    - name: Frog 1
      url: https://atcoder.jp/contests/dp/tasks/dp_a
      platform: AtCoder
      difficulty: easy
      topics: [programação dinâmica, transição, minimização]
      objective: Pratique a passagem de uma recorrência simples para tabulação.
    - name: Longest Flight Route
      url: https://cses.fi/problemset/task/1680
      platform: CSES
      difficulty: medium
      topics: [DP em grafos, DAG, reconstrução]
      objective: Combine ordem topológica, estados em vértices e ponteiros de reconstrução.
{% endset %}

# Programação Dinâmica

**Programação dinâmica** (PD ou *dynamic programming*) resolve problemas por subproblemas e armazena suas respostas, para que cada estado seja calculado uma única vez.

O ponto principal não é criar uma tabela: é escolher um estado que contenha exatamente a informação necessária para continuar a solução.

## 1. Quando programação dinâmica se aplica?

Uma DP normalmente possui duas propriedades:

- **subproblemas sobrepostos**: o mesmo estado aparece em diferentes caminhos de solução;
- **estrutura ótima**: uma solução ótima pode ser construída a partir de soluções ótimas de estados menores.

Fibonacci ilustra a sobreposição. Para calcular `fib(5)`, `fib(3)` aparece tanto dentro de `fib(4)` quanto diretamente:

```text
fib(5)
├─ fib(4)
│  ├─ fib(3)  ← calculado aqui
│  └─ fib(2)
└─ fib(3)     ← e seria calculado outra vez aqui
```

!!! important "A pergunta certa"
    Em vez de perguntar “como resolvo o problema inteiro?”, pergunte: “qual é a menor informação que define um subproblema cuja resposta eu posso reutilizar?”

## 2. O roteiro para criar uma DP

### 2.1. Defina o estado

Escreva uma frase completa para `dp[...]`.

- `dp[x]` = menor número de moedas para formar a soma `x`;
- `dp[i][j]` = quantidade de caminhos até a célula `(i, j)`;
- `dp[i][b]` = maior valor usando os primeiros `i` itens com orçamento `b`;
- `dp[mask][last]` = menor custo para visitar `mask` e terminar em `last`.

### 2.2. Encontre a transição

Pergunte quais estados menores podem produzir o atual. Para cada possibilidade, combine a resposta anterior com a escolha feita agora.

### 2.3. Escolha os casos base

Estados sem predecessores precisam de valores iniciais corretos. Eles podem representar uma solução vazia, a origem de um grid ou uma situação impossível.

### 2.4. Determine a ordem de cálculo

Todo estado precisa ser calculado depois dos estados dos quais depende. Isso exige atenção em grids, intervalos, grafos e máscaras.

### 2.5. Extraia a resposta

A resposta pode estar em `dp[target]` ou ser o máximo/mínimo entre estados finais.

<!-- AUXÍLIO VISUAL 1 — PRIORITÁRIO

Criar um fluxograma para modelar programação dinâmica:
estado → decisões e predecessores → transição → bases e impossíveis → ordem de cálculo → resposta/reconstrução.

Usar uma seta de retorno de transição para estado, indicando que uma fórmula confusa exige revisar a definição do estado.

Arquivo sugerido:
../../assets/images/paradigmas/programacao-dinamica/roteiro-de-modelagem.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Roteiro para modelar programação dinâmica](../../assets/images/paradigmas/programacao-dinamica/roteiro-de-modelagem.svg)
-->

## 3. Memoização e tabulação

| Abordagem | Como funciona | Vantagem | Atenção |
|---|---|---|---|
| Memoização | Recursão que salva respostas já calculadas. | Calcula apenas estados alcançáveis. | Profundidade de recursão e sentinelas. |
| Tabulação | Preenche estados em ordem iterativa. | Evita pilha recursiva e expõe dependências. | Pode preencher estados desnecessários. |

### Exemplo: Fibonacci

```cpp
vector<long long> memo;

long long fib(int n) {
    if (n <= 1) {
        return n;
    }
    if (memo[n] != -1) {
        return memo[n];
    }
    return memo[n] = fib(n - 1) + fib(n - 2);
}
```

```cpp
long long fib_bottom_up(int n) {
    if (n <= 1) {
        return n;
    }
    vector<long long> dp(n + 1);
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}
```

As duas versões custam $O(N)$, enquanto a recursão ingênua repete estados e custa tempo exponencial.

!!! tip "Escolha prática"
    Comece com memoização quando a recorrência ainda está sendo descoberta. Converta para tabulação quando a ordem ficar clara ou a recursão ficar profunda.

## 4. Problema exemplo: mínimo de moedas

Com moedas `[1, 3, 4]`, queremos formar a soma `6` usando o menor número possível de moedas.

Definimos:

$$
dp[x] = \text{menor quantidade de moedas para formar } x
$$

Se a última moeda tem valor `c`, antes dela precisávamos formar `x-c`:

$$
dp[x] = \min_{c \le x}(dp[x-c] + 1)
$$

O caso base é `dp[0] = 0`; estados inicialmente impossíveis recebem `INF`.

| `x` | Melhor escolha | `dp[x]` |
|---:|---|---:|
| 0 | nenhuma | 0 |
| 1 | `1` | 1 |
| 2 | `1 + 1` | 2 |
| 3 | `3` | 1 |
| 4 | `4` | 1 |
| 5 | `4 + 1` | 2 |
| 6 | `3 + 3` | 2 |

```cpp
int minimum_coins(const vector<int>& coins, int target) {
    const int INF = 1e9;
    vector<int> dp(target + 1, INF);
    dp[0] = 0;

    for (int value = 1; value <= target; value++) {
        for (int coin : coins) {
            if (coin <= value && dp[value - coin] != INF) {
                dp[value] = min(dp[value], dp[value - coin] + 1);
            }
        }
    }
    return dp[target] == INF ? -1 : dp[target];
}
```

O laço externo cresce até `target`, então cada transição lê somente estados já calculados. A complexidade é $O(target \cdot |coins|)$.

<!-- AUXÍLIO VISUAL 2 — PRIORITÁRIO

Criar uma sequência de quadros para a DP de moedas `[1, 3, 4]` até a soma `6`.

- Destacar `dp[x]` enquanto é calculado.
- Mostrar setas de `dp[x-1]`, `dp[x-3]` e `dp[x-4]` quando existirem.
- Exibir a escolha vencedora e o valor final de cada célula.

Arquivo sugerido:
../../assets/images/paradigmas/programacao-dinamica/moedas-passo-a-passo.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Preenchimento da DP para mínimo de moedas](../../assets/images/paradigmas/programacao-dinamica/moedas-passo-a-passo.svg)
-->

## 5. A ordem de iteração muda a resposta

Na mochila 0/1, cada item pode ser escolhido no máximo uma vez. Ao processar um item de custo `cost`, atualize o orçamento **de trás para frente**:

```cpp
for (int b = budget; b >= cost; b--) {
    dp[b] = max(dp[b], dp[b - cost] + value);
}
```

Se o laço fosse crescente, `dp[b-cost]` poderia já conter o item atual, permitindo reutilizá-lo por engano. Para mochila ilimitada, em que repetição é permitida, a ordem crescente é a correta.

| Problema | Ordem típica | Motivo |
|---|---|---|
| Mochila 0/1 | orçamento decrescente | Não reutilizar o item atual. |
| Mochila ilimitada | orçamento crescente | Permitir reutilização. |
| DP de intervalos | tamanho crescente | Intervalos menores vêm antes. |
| DP em DAG | ordem topológica | Predecessores vêm antes. |

!!! warning "A recorrência não basta"
    Duas implementações podem ter a mesma fórmula e resultados diferentes se a ordem de preenchimento violar dependências ou reutilizar uma escolha indevidamente.

## 6. Padrões de estado frequentes

| Padrão | Estado típico | Exemplo |
|---|---|---|
| Prefixo | `dp[i]` | melhor resposta nos primeiros `i` elementos |
| Grid | `dp[i][j]` | caminhos até a célula `(i, j)` |
| Mochila | `dp[i][b]` ou `dp[b]` | itens considerados e orçamento |
| Intervalo | `dp[l][r]` | resposta para o subarray `[l, r]` |
| Subconjunto | `dp[mask]` | elementos já escolhidos |
| Árvore | `dp[v][state]` | resposta na subárvore de `v` |
| DAG | `dp[v]` | melhor resposta ao chegar em `v` |

### Exemplo curto: caminhos em um grid

```cpp
dp[0][0] = 1;
for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        if (blocked[i][j]) {
            continue;
        }
        if (i > 0) dp[i][j] += dp[i - 1][j];
        if (j > 0) dp[i][j] += dp[i][j - 1];
    }
}
```

O estado `dp[i][j]` guarda apenas a quantidade de rotas até a célula; não importa qual rota específica foi usada.

## 7. Reconstrução e memória

Quando o valor ótimo não basta, guarde a escolha que melhorou cada estado.

```cpp
vector<int> parent(target + 1, -1);

if (dp[value - coin] + 1 < dp[value]) {
    dp[value] = dp[value - coin] + 1;
    parent[value] = coin;
}
```

No exemplo de moedas, parta de `target` e repita `value -= parent[value]` até chegar a zero.

Uma tabela `dp[i][j]` pode ser comprimida para uma ou duas linhas somente depois que a versão completa estiver correta. Explique quais estados antigos continuam necessários e escolha a ordem de laço compatível.

<!-- AUXÍLIO VISUAL 3

Criar uma comparação entre uma tabela de mochila 0/1 completa e um vetor unidimensional.

- À esquerda, linhas por item e colunas por orçamento.
- À direita, um vetor atualizado da direita para a esquerda.
- Usar setas para mostrar que a ordem decrescente impede reutilizar o item atual.

Arquivo sugerido:
../../assets/images/paradigmas/programacao-dinamica/mochila-ordem.svg

Substituir este comentário pelo Markdown abaixo quando a imagem estiver disponível:

![Ordem de atualização na mochila 0/1](../../assets/images/paradigmas/programacao-dinamica/mochila-ordem.svg)
-->

## 8. Erros comuns

1. **Estado insuficiente:** duas situações com futuros diferentes não podem compartilhar estado.
2. **Caso base incorreto:** a solução vazia pode valer `0`, `1`, `-INF` ou `INF`, conforme o problema.
3. **Zero para impossível:** em minimização, use `INF` e só faça transições de estados alcançáveis.
4. **Ordem errada:** verifique que toda leitura vem de uma versão válida do estado.
5. **Estados demais:** se existem $N \cdot M$ estados e cada um faz $K$ transições, a complexidade é $O(NMK)$.

## 9. Checklist antes de submeter

1. Consigo definir `dp[...]` em uma frase?
2. Cada transição usa estados já calculados?
3. Casos base e impossíveis foram inicializados?
4. A ordem dos laços respeita as dependências?
5. A resposta está no estado certo ou exige máximo/mínimo final?
6. O tipo numérico suporta os valores da DP?

## Problemas

{{ exercise_list(exercises) }}

## Recursos

- [AtCoder Educational DP Contest](https://atcoder.jp/contests/dp)
- [Dynamic Programming - USACO Guide](https://usaco.guide/gold/intro-dp)
- [Dynamic Programming - cp-algorithms](https://cp-algorithms.com/dynamic_programming/intro-to-dp.html)
