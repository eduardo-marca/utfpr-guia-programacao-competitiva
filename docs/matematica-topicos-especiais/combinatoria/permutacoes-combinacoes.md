{% set exercises %}
  recommended:
    - name: Creating Strings II
      url: https://cses.fi/problemset/task/1715
      platform: CSES
      difficulty: medium
      topics: [permutação com repetição, multinomial, módulo]
      objective: Conte anagramas distintos de uma string com letras repetidas.
    - name: Distributing Apples
      url: https://cses.fi/problemset/task/1716
      platform: CSES
      difficulty: medium
      topics: [combinação com repetição, stars and bars]
      objective: Transforme uma distribuição de objetos em uma escolha de separadores.
  additional:
    - name: Counting Derangements
      url: https://cses.fi/problemset/task/1717
      platform: CSES
      difficulty: medium
      topics: [permutação caótica, inclusão-exclusão]
      objective: Conte permutações em que nenhum elemento permanece na posição original.
{% endset %}

# Permutações e combinações

Permutações e combinações contam maneiras de escolher elementos. A pergunta decisiva é sempre: **trocar a ordem cria um resultado diferente?**

## 1. Fatorial e arranjos

O fatorial conta todas as ordens de `n` elementos distintos:

$$
n! = n(n-1)(n-2)\cdots 1
$$

Se escolhemos e ordenamos apenas `k` entre `n` elementos, usamos o **arranjo**:

$$
A(n,k) = P(n,k) = \frac{n!}{(n-k)!}
$$

Para um pódio com ouro, prata e bronze entre 10 atletas, temos `A(10,3) = 10 × 9 × 8`. A ordem importa porque trocar ouro e prata muda o resultado.

## 2. Combinações

Ao escolher um grupo sem ordem, cada conjunto de `k` elementos foi contado `k!` vezes pelo arranjo. Assim:

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

Uma comissão de 3 entre 10 pessoas tem $\binom{10}{3}$ escolhas. As mesmas três pessoas continuam sendo a mesma comissão em qualquer ordem.

| Situação | Ordem importa? | Contagem |
|---|---|---|
| Senha com `k` símbolos distintos | Sim | $A(n,k)$ |
| Grupo de `k` pessoas | Não | $\binom{n}{k}$ |
| Ordenar todos os `n` elementos | Sim | $n!$ |

## 3. Permutações com repetição: exemplos de strings

Se alguns objetos são indistinguíveis, dividir por suas permutações internas remove as cópias repetidas:

$$
\frac{n!}{c_1!c_2!\cdots c_m!}
$$

Aqui, $c_i$ é a quantidade de ocorrências de cada tipo e $\sum c_i=n$.

Exemplo: quantos anagramas distintos possui `MISSISSIPPI`? São 11 letras, com 4 `I`, 4 `S`, 2 `P` e 1 `M`:

$$
\frac{11!}{4!4!2!} = 34650
$$

Esse é um exemplo importante porque traduz uma string em uma contagem de objetos indistinguíveis.

## 4. Permutação circular

Em uma mesa redonda, rotações representam o mesmo arranjo. Podemos fixar uma pessoa e ordenar as demais:

$$
(n-1)!
$$

Se reflexões também são consideradas iguais — por exemplo, colares que podem ser virados — normalmente dividimos por 2, obtendo $(n-1)!/2$ para `n > 2`. Não faça essa divisão em uma mesa comum: sentar à esquerda ou à direita de alguém produz disposições diferentes.

## 5. Combinação com repetição: stars and bars

Para distribuir `k` objetos idênticos em `n` caixas, permitindo caixas vazias, use:

$$
\binom{n+k-1}{k}
$$

Exemplo: distribuir 7 balas idênticas entre 3 crianças corresponde a sequências com 7 estrelas e 2 barras:

```text
***|**|**  →  3, 2, 2
```

Há $\binom{9}{2}=36$ maneiras de escolher as posições das duas barras.

Para exigir pelo menos um objeto em cada caixa, entregue primeiro uma unidade a cada caixa. A contagem passa a ser:

$$
\binom{k-1}{n-1}
$$

## 6. Permutação caótica (derangement)

Uma **permutação caótica** (ou *derangement*) é uma permutação em que nenhum elemento fica na posição original. Em um amigo secreto, ela garante que ninguém tire a si mesmo.

O número de derangements de `n` elementos é denotado por `D(n)` e obedece:

$$
D(0)=1,\quad D(1)=0,\quad D(n)=(n-1)(D(n-1)+D(n-2))
$$

Para quatro pessoas, `D(4)=9`. A recorrência vem de escolher para onde o primeiro elemento vai e separar os casos em que ocorre ou não uma troca com essa posição. A fórmula por [Inclusão-Exclusão](inclusao-exclusao.md) explica a mesma contagem por outro ponto de vista.

Também vale a fórmula fechada:

$$
D(n)=n!\sum_{i=0}^{n}\frac{(-1)^i}{i!}
$$

Ela é exata quando calculada como soma racional; a aproximação $D(n)\approx n!/e$ só serve como intuição. Para calcular muitos valores inteiros, prefira a recorrência:

```cpp
vector<long long> derangement(n + 1);
derangement[0] = 1;
if (n >= 1) derangement[1] = 0;
for (int i = 2; i <= n; i++) {
    derangement[i] = (i - 1) * (derangement[i - 1] + derangement[i - 2]);
}
```

## 7. Um padrão menos óbvio: uns sem adjacência

Quantas strings binárias de tamanho `n` têm exatamente `k` uns, sem dois uns consecutivos?

Coloque primeiro os `k` uns, que criam `k-1` separações obrigatórias. Depois escolha as posições adicionais entre os espaços disponíveis. O resultado é:

$$
\binom{n-k+1}{k}
$$

Por exemplo, para `n=5` e `k=2`, a resposta é $\binom{4}{2}=6$. Esse método de “reservar espaços” é útil em strings, posições em uma reta e seleções com distância mínima.

Outra forma de pensar para chegar na fórmula, é primeiro colocar os `n-k` zeros da string, e adicionar os `k` uns nos `n-k+1` espaços formados antes, entre, e depois dos zeros. Cada espaço só pode ser ocupado um único `1` porque dois uns não podem ser adjacentes.

<!-- AUXÍLIO VISUAL 1 — PRIORITÁRIO

Criar três painéis: pódio versus comissão, anagramas de uma string com letras repetidas e stars and bars para distribuir objetos idênticos. Incluir um pequeno exemplo visual de uns sem adjacência.

Arquivo sugerido: images/permutacoes-combinacoes.svg
-->

Para identidades e cálculo eficiente de $\binom{n}{k}$, siga para [Coeficientes Binomiais](coeficientes-binomial.md).

## Problemas

{{ exercise_list(exercises) }}
