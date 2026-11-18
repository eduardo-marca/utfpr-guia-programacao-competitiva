{% set exercises %}
  recommended:
    - name: Distinct Numbers
      url: https://cses.fi/problemset/task/1621
      platform: CSES
      difficulty: easy
      topics: [casa dos pombos, valores distintos]
      objective: Relacione a quantidade de valores distintos à existência de repetições.
  additional:
    - name: Subarray Divisibility
      url: https://cses.fi/problemset/task/1662
      platform: CSES
      difficulty: medium
      topics: [casa dos pombos, prefix sum, restos]
      objective: Use restos de prefixos iguais para garantir um subarray divisível.
{% endset %}

# Princípio da Casa dos Pombos

Se colocamos mais de `n` objetos em apenas `n` categorias, ao menos uma categoria recebe dois ou mais objetos. Essa observação simples produz provas curtas para existência de repetições, pares e colisões.

## 1. Forma geral

Ao distribuir `N` objetos em `K` caixas, alguma caixa recebe pelo menos:

$$
\left\lceil \frac{N}{K} \right\rceil
$$

objetos.

Exemplo: entre 13 pessoas, ao menos duas fazem aniversário no mesmo mês, pois existem apenas 12 meses.

## 2. Escolha as caixas corretamente

A parte difícil é definir o que são “pombos” e “casas”.

| Objetos | Caixas | Conclusão |
|---|---|---|
| 13 pessoas | meses de aniversário | duas compartilham um mês |
| 11 inteiros | restos módulo 10 | dois têm o mesmo resto |
| `n + 1` números em `[1, 2n]` | pares `{1,2}`, `{3,4}`, ... | dois números diferem no máximo 1 |

No último exemplo, os pares consecutivos são as caixas. Não basta dizer que os números estão no intervalo: a escolha das categorias deve produzir exatamente a propriedade desejada.

## 3. Aplicação modular

Entre `K + 1` prefix sums, sempre existem dois com o mesmo resto módulo `K`. A diferença entre eles é divisível por `K`, logo o subarray correspondente possui soma múltipla de `K`.

Essa prova explica a solução de problemas que usam [prefix sums](../../tecnicas-estruturas/tecnicas/prefix-sum.md) e frequências de restos.

!!! tip "Para provar existência"
    O princípio normalmente mostra que um objeto existe, mas não o encontra. Em algoritmos, guarde a primeira ocorrência de cada caixa para localizar o par ou subarray quando a colisão aparecer.

## Problemas

{{ exercise_list(exercises) }}
