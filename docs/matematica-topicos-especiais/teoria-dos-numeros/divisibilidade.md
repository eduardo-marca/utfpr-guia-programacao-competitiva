{% set exercises %}
  recommended:
    - name: Divisibility by Eight
      url: https://codeforces.com/problemset/problem/550/C
      platform: Codeforces
      difficulty: medium
      topics: [divisibilidade, strings, subsequência]
      objective: Use uma propriedade decimal para testar apenas subsequências curtas.
  additional:
    - name: Polycarp and Div 3
      url: https://codeforces.com/problemset/problem/1005/D
      platform: Codeforces
      difficulty: medium
      topics: [divisibilidade por 3, strings, guloso]
      objective: Explore a soma dos dígitos em uma sequência longa.
{% endset %}

# Critérios de divisibilidade

Critérios de divisibilidade vêm da escrita decimal $N=10q+d$. Como `10` tem restos simples em certos módulos, poucos dígitos podem bastar para decidir a divisibilidade.

## 1. Regras decimais úteis

| Divisor | Critério |
|---|---|
| 2 | último dígito par |
| 3 | soma dos dígitos múltipla de 3 |
| 4 | últimos dois dígitos formam múltiplo de 4 |
| 5 | último dígito é 0 ou 5 |
| 6 | divisível por 2 e por 3 |
| 8 | últimos três dígitos formam múltiplo de 8 |
| 9 | soma dos dígitos múltipla de 9 |
| 10 | último dígito é 0 |
| 11 | soma alternada dos dígitos é múltipla de 11 |

As regras de 3 e 9 existem porque $10\equiv1$ nesses módulos. As de 4 e 8 existem porque $100$ e $1000$ já são múltiplos deles. Para 7, uma regra prática é remover o último dígito `d`, subtrair `2d` do restante e repetir; a equivalência vem de $10\equiv3\pmod7$.

## 2. Inteiros grandes em strings

Quando o número não cabe em `long long`, processe seus dígitos e mantenha apenas o resto atual:

$$
r_{novo}=(10r_{atual}+d)\bmod m
$$

```cpp
int remainder_of_decimal_string(const string& s, int mod) {
    int remainder = 0;
    for (char c : s) {
        remainder = (10LL * remainder + (c - '0')) % mod;
    }
    return remainder;
}
```

Essa mesma ideia testa uma string binária, trocando `10` por `2`, ou uma representação em base `B`, trocando `10` por `B`.

## 3. Um exemplo menos óbvio

Para decidir se alguma subsequência de uma string decimal é divisível por 8, basta procurar uma subsequência de até 3 dígitos: a divisibilidade por 8 depende apenas dos três últimos dígitos. Em contraste, para um módulo arbitrário não há garantia semelhante; usar o restante como estado pode exigir programação dinâmica ou automato.

!!! tip "Critério versus algoritmo"
    Um critério é uma simplificação especial de aritmética modular. Quando ele não existir, o algoritmo geral de acumular restos em uma string continua funcionando.

<!-- AUXÍLIO VISUAL 1

Mostrar 5.247 sendo separado em 5 milhares, 2 centenas, 4 dezenas e 7 unidades, com cada parcela reduzida módulo 9 e módulo 8 para explicar por que as regras usam dígitos diferentes.

Arquivo sugerido: images/criterios-divisibilidade.svg
-->

## Problemas

{{ exercise_list(exercises) }}
