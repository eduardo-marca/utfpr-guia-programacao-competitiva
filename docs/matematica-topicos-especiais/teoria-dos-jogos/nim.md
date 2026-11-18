{% set exercises %}
  recommended:
    - name: Nim Game I
      url: https://cses.fi/problemset/task/1730
      platform: CSES
      difficulty: easy
      topics: [Nim, XOR, nim-sum]
      objective: Decida o vencedor de Nim normal pela soma XOR das pilhas.
    - name: Nim Game II
      url: https://cses.fi/problemset/task/1098
      platform: CSES
      difficulty: medium
      topics: [jogo de retirada, Grundy, XOR]
      objective: Troque cada pilha por seu Grundy number antes de aplicar XOR.
  additional:
    - name: Strange Nim
      url: https://atcoder.jp/contests/arc091/tasks/arc091_d
      platform: AtCoder
      difficulty: hard
      topics: [Nim, estratégia, teoria dos jogos]
      objective: Reduza uma variação de pilhas a valores equivalentes de Nim.
{% endset %}

# Jogo de Nim

Em Nim normal há várias pilhas; em cada turno, escolhe-se uma única pilha não vazia e remove-se qualquer quantidade positiva de elementos dela. Quem remove o último elemento vence.

O espaço de estados parece enorme, mas toda posição é decidida por um único valor: o **nim-sum**, ou XOR dos tamanhos das pilhas.

$$
X=x_1\oplus x_2\oplus\cdots\oplus x_n
$$

Uma posição é `P` se e somente se `X=0`; caso contrário, é `N`.

## 1. Estratégia construtiva

Se `X=0`, não há movimento vencedor. Se `X≠0`, encontre uma pilha `x_i` para a qual:

$$
y=x_i\oplus X<x_i
$$

e reduza essa pilha de `x_i` para `y`. O novo nim-sum será 0.

Exemplo: em `[3,4,5]`, temos $3\oplus4\oplus5=2$. A primeira pilha pode virar $3\oplus2=1$, produzindo `[1,4,5]`, cujo XOR é 0.

```cpp
struct NimMove {
    int heap;
    long long remaining;
};

optional<NimMove> winning_nim_move(const vector<long long>& heaps) {
    long long nim_sum = 0;
    for (long long heap : heaps) nim_sum ^= heap;
    if (nim_sum == 0) return nullopt;

    for (int i = 0; i < static_cast<int>(heaps.size()); i++) {
        long long target = heaps[i] ^ nim_sum;
        if (target < heaps[i]) return NimMove{i, target};
    }
    return nullopt; // Não ocorre quando nim_sum != 0.
}
```

## 2. Por que XOR igual a zero perde

Há duas partes na demonstração.

**De `X=0`, todo movimento sai de zero.** Uma jogada altera somente uma pilha, de `a` para `b`, com `a≠b`. O novo XOR é $0\oplus a\oplus b=a\oplus b$, que não pode ser zero porque `a` e `b` são diferentes.

**De `X≠0`, existe uma jogada para zero.** Considere o bit 1 mais significativo de `X`. Como esse bit é 1 no XOR de todas as pilhas, uma quantidade ímpar de pilhas o possui; escolha uma delas, `x_i`. Ao calcular `x_i xor X`, esse bit passa de 1 para 0 e nenhum bit mais significativo muda. Portanto, o valor diminui: $x_i\oplus X<x_i$.

Substituir `x_i` por $x_i\oplus X$ torna o novo XOR:

$$
X\oplus x_i\oplus(x_i\oplus X)=0
$$

Assim, posições com XOR zero só levam a posições não nulas, e posições não nulas possuem uma volta a zero. Isso coincide exatamente com a definição de `P/N`.

## 3. Variações de pilha

O XOR dos tamanhos funciona apenas quando cada jogador pode retirar qualquer quantidade de uma única pilha. Se cada pilha permite retirar apenas `1..k` pedras, a pilha de tamanho `s` tem valor equivalente a:

$$
s\bmod(k+1)
$$

pois esses são os Grundy numbers do jogo de retirada. Para combinar pilhas, faça XOR desses valores, não necessariamente dos tamanhos originais. Essa é a ideia por trás de *Nim Game II* e será generalizada em [Números de Grundy](grundy-numbers.md).

!!! warning "Uma única pilha por vez"
    A prova de Nim depende de cada jogada modificar apenas uma componente. Se uma jogada pode retirar pedras de duas pilhas simultaneamente, o nim-sum simples pode falhar; modele o jogo novamente ou calcule Grundy do estado conjunto.

<!-- AUXÍLIO VISUAL 1

Criar três pilhas 3, 4 e 5 com a escrita binária de cada tamanho e o XOR 010. Mostrar a redução 3→1 e o XOR final 000.

Arquivo sugerido: images/estrategia-nim.svg
-->

## Problemas

{{ exercise_list(exercises) }}
