{% set exercises %}
  recommended:
    - name: Misère Nim
      url: https://www.hackerrank.com/challenges/misere-nim-1/problem
      platform: HackerRank
      difficulty: easy
      topics: [misère, Nim, XOR]
      objective: Trate corretamente o caso especial em que todas as pilhas têm tamanho 1.
  additional:
    - name: Nim Game II
      url: https://cses.fi/problemset/task/1098
      platform: CSES
      difficulty: medium
      topics: [jogo de retirada, estratégia]
      objective: Compare uma variação normal de retirada com a inversão de condição em misère.
{% endset %}

# Jogos misère

Em um jogo **misère**, quem realiza a última jogada perde. A alteração troca o significado da posição terminal: se não há movimentos, o jogador da vez já venceu, pois o adversário acabou de fazer a última jogada e perdeu.

## 1. Análise de estados em misère

As regras recursivas `P/N` continuam iguais, mas a base muda:

- no jogo normal, a posição terminal é `P`;
- no jogo misère, a posição terminal é `N`.

Por exemplo, em uma pilha em que se pode retirar `1..k`, as posições perdedoras misère são aquelas com:

$$
n\equiv1\pmod{k+1}
$$

**Demonstração.** A pilha vazia é `N`. Com uma pedra, toda jogada vai para a posição vazia e perde por ser a última, então 1 é `P`. De uma posição com resto 1, qualquer retirada chega a um resto diferente; de qualquer outro resto, é possível retirar a quantidade necessária para deixar resto 1. O padrão se repete em blocos de `k+1`.

Para regras de retirada arbitrárias, refaça a DP com `win[0]=true`; não reaproveite cegamente a tabela normal.

## 2. Misère Nim

Em misère Nim, as jogadas são as mesmas de Nim, mas remover a última pedra perde. A classificação é quase a do Nim normal:

1. se todas as pilhas têm tamanho 1, a posição é `P` quando o número de pilhas é ímpar;
2. caso exista alguma pilha maior que 1, a posição é `P` se e somente se o XOR de todas as pilhas é zero.

```cpp
bool misere_nim_first_wins(const vector<long long>& heaps) {
    long long nim_sum = 0;
    int ones = 0, large = 0;
    for (long long heap : heaps) {
        nim_sum ^= heap;
        if (heap == 1) ones++;
        if (heap > 1) large++;
    }
    if (large == 0) return ones % 2 == 0;
    return nim_sum != 0;
}
```

### Estratégia vencedora

Se todas as pilhas são 1, retire uma pilha somente quando a quantidade for par, deixando uma quantidade ímpar ao adversário.

Se há duas ou mais pilhas grandes, aplique a jogada normal de Nim que zera o XOR. Se há exatamente uma pilha grande, reduza-a para 1 quando o número atual de pilhas unitárias é par; reduza-a para 0 quando esse número é ímpar. Em ambos os casos, você deixa uma quantidade ímpar de pilhas unitárias.

Exemplo: `[1,1,2]` tem XOR 2. A jogada normal que zera o XOR levaria a `[1,1]`, mas isso é vencedor para o próximo jogador em misère. A jogada correta é `2→1`, deixando três pilhas unitárias: uma posição perdedora.

## 3. Por que Sprague–Grundy não basta

O teorema de Sprague–Grundy classifica jogos sob condição normal. Em misère, trocar a base terminal muda a equivalência entre uma posição e uma pilha de Nim, principalmente perto do fim do jogo.

Para uma única componente pequena, uma DP `P/N` misère costuma bastar. Para uma soma de subgames misère gerais, não existe uma regra universal tão simples quanto o XOR de Grundy numbers; analise a estrutura específica ou procure um resultado conhecido da variante.

!!! warning "Não inverta simplesmente a resposta"
    Um jogo misère não é obtido trocando `N` por `P` em toda tabela normal. Apenas a condição terminal é invertida; as transições propagam essa mudança de forma não trivial.

<!-- AUXÍLIO VISUAL 1

Comparar a sequência normal e misère para retirada de 1 a 3 pedras: destacar posições P em múltiplos de 4 no normal e em valores 1 mod 4 no misère. Incluir o caso [1,1,2] de misère Nim.

Arquivo sugerido: images/misere-nim.svg
-->

## Problemas

{{ exercise_list(exercises) }}
