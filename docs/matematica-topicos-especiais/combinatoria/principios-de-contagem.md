{% set exercises %}
  recommended:
    - name: Creating Strings
      url: https://cses.fi/problemset/task/1622
      platform: CSES
      difficulty: easy
      topics: [permutação, contagem]
      objective: Distinga permutações quando há caracteres repetidos.
    - name: Tower of Hanoi
      url: https://cses.fi/problemset/task/2165
      platform: CSES
      difficulty: easy
      topics: [recorrência, potência de dois]
      objective: Reconheça a contagem de escolhas binárias em uma recorrência clássica.
  additional:
    - name: Two Knights
      url: https://cses.fi/problemset/task/1072
      platform: CSES
      difficulty: medium
      topics: [contagem, complemento]
      objective: Conte pares de posições e remova os pares que atacam entre si.
{% endset %}

# Princípios de Contagem

Os princípios de contagem são a base da combinatória: dividir uma escolha em casos ou etapas permite contar sem gerar cada possibilidade.

## 1. Regra do produto

Se uma construção tem `a` possibilidades na primeira etapa e, para cada uma delas, `b` possibilidades na segunda, há `a × b` resultados.

Exemplo: uma senha com duas letras maiúsculas e três dígitos possui:

$$
26 \cdot 26 \cdot 10 \cdot 10 \cdot 10 = 676000
$$

O produto vale quando cada escolha de uma etapa pode ser combinada com todas as escolhas da etapa seguinte.

## 2. Regra da soma

Se os casos são mutuamente exclusivos, somamos suas quantidades.

Exemplo: escolher uma vogal (`5` opções) **ou** um algarismo (`10` opções) produz `5 + 10 = 15` escolhas. Uma escolha não pode ser simultaneamente vogal e algarismo, então não há sobreposição.

!!! warning "Soma exige casos disjuntos"
    Se os casos podem se sobrepor, somá-los conta elementos repetidos. Esse é o motivo para estudar [Inclusão-Exclusão](inclusao-exclusao.md).

## 3. Complemento

Muitas vezes é mais fácil contar tudo e subtrair os casos proibidos:

$$
\text{casos desejados} = \text{total} - \text{casos indesejados}
$$

Para colocar duas torres em casas distintas de um tabuleiro `n × n`, conte todos os pares de casas e retire os pares que se atacam. Essa ideia evita separar manualmente cada posição válida.

## 4. Escolhas ordenadas e não ordenadas

Antes de aplicar uma fórmula, teste se trocar os elementos cria uma resposta diferente.

| Escolha | A ordem importa? | Exemplo |
|---|---|---|
| Pódio de 3 pessoas | Sim | `(Ana, Bia, Caio)` ≠ `(Bia, Ana, Caio)` |
| Comissão de 3 pessoas | Não | Os mesmos nomes formam a mesma comissão |

Essa distinção leva às fórmulas de [Permutações e Combinações](permutacoes-combinacoes.md).

<!-- AUXÍLIO VISUAL 1

Criar um diagrama com três painéis: regra do produto como árvore de escolhas, regra da soma como ramos disjuntos e complemento como conjunto total menos região proibida.

Arquivo sugerido: images/principios-de-contagem.svg
-->

## Problemas

{{ exercise_list(exercises) }}
