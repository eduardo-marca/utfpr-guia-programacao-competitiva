# Combinatória

Combinatória estuda como contar objetos sem enumerá-los. Em programação competitiva, ela aparece em contagem de configurações, probabilidades, programação dinâmica, strings, grafos e aritmética modular.

## Roteiro de estudo

Siga esta ordem para construir os fundamentos e depois aplicá-los a problemas mais difíceis:

1. [Princípios de Contagem](principios-de-contagem.md): regra da soma e do produto, a linguagem para decompor escolhas.
2. [Permutações e Combinações](permutacoes-combinacoes.md): arranjos, repetições, círculos, distribuições e derangements.
3. [Coeficientes Binomiais](coeficientes-binomial.md): propriedades, triângulo de Pascal, teorema binomial e multinomiais.
4. [Coeficientes Binomiais Modulares](binomial-modular.md): pré-cálculo de fatoriais e inversos para responder combinações grandes.
5. [Números de Catalan](catalan.md): parênteses, caminhos, árvores e outras estruturas equilibradas.
6. [Inclusão-Exclusão](inclusao-exclusao.md): como corrigir contagens que se sobrepõem.
7. [Princípio da Casa dos Pombos](pigeonhole.md): como provar que uma colisão ou repetição é inevitável.

!!! tip "Antes de escolher uma fórmula"
    Defina o que constitui uma escolha diferente, identifique se a ordem importa e verifique se há restrições que geram sobreposição. A maior parte dos erros de combinatória acontece antes do cálculo.

## Mapa de decisões

| Situação | Ferramenta inicial |
|---|---|
| Etapas independentes de escolha | Princípio multiplicativo |
| Casos mutuamente exclusivos | Princípio aditivo |
| Escolher ou ordenar elementos distintos | Permutação, arranjo ou combinação |
| Estruturas balanceadas e decomponíveis | Números de Catalan |
| Contagem com módulo primo | Fatoriais e inversos modulares |
| União de propriedades que se sobrepõem | Inclusão-exclusão |
| Provar que dois objetos compartilham uma categoria | Casa dos pombos |

Quando a escolha depende de decisões anteriores, talvez o problema seja de [programação dinâmica](../../algoritmos/programacao-dinamica/dynamic-programming.md), e não de uma fórmula fechada.
