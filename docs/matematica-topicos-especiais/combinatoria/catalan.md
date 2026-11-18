{% set exercises %}
  recommended:
    - name: Bracket Sequences I
      url: https://cses.fi/problemset/task/2064
      platform: CSES
      difficulty: medium
      topics: [Catalan, parênteses balanceados, binomial]
      objective: Conte sequências válidas de parênteses a partir de um binomial central.
    - name: Counting Tilings
      url: https://cses.fi/problemset/task/2181
      platform: CSES
      difficulty: hard
      topics: [Catalan, perfis, programação dinâmica]
      objective: Relacione contagens estruturais com uma DP de estados por perfil.
  additional:
    - name: Bracket Sequences II
      url: https://cses.fi/problemset/task/2187
      platform: CSES
      difficulty: hard
      topics: [Catalan, prefixos, combinação]
      objective: Complete um prefixo de parênteses sem violar a condição de balanço.
{% endset %}

# Números de Catalan

Os números de Catalan contam estruturas aparentemente diferentes que obedecem à mesma regra de equilíbrio. Os primeiros valores são:

```text
C(0)=1, C(1)=1, C(2)=2, C(3)=5, C(4)=14, C(5)=42
```

## 1. Fórmulas

$$
C_n = \frac{1}{n+1}\binom{2n}{n}
$$

e a recorrência é:

$$
C_0=1,\qquad C_n=\sum_{i=0}^{n-1}C_iC_{n-1-i}
$$

A recorrência escolhe a divisão causada pelo primeiro componente: à esquerda ficam `i` pares e à direita ficam os demais.

Para gerar os valores exatos em sequência, outra forma útil é:

$$
C_{n+1}=C_n\frac{2(2n+1)}{n+2}
$$

Ela é ótima para aritmética inteira quando os valores cabem no tipo; sob módulo primo, use inversos modulares ou a fórmula binomial.

## 2. Parênteses balanceados

`C_n` conta sequências válidas com `n` aberturas e `n` fechamentos. Para `n=3`, existem 5:

```text
((()))  (()())  (())()  ()(())  ()()()
```

Há $\binom{2n}{n}$ sequências com `n` de cada símbolo, mas algumas fecham antes de abrir. O argumento de reflexão mostra que a quantidade inválida é $\binom{2n}{n+1}$, então:

$$
C_n=\binom{2n}{n}-\binom{2n}{n+1}
$$

Essa forma é especialmente prática sob módulo, pois usa apenas combinações.

## 3. Outras interpretações úteis

`C_n` também conta:

- árvores binárias enraizadas com `n` nós internos;
- formas de triangular um polígono com `n+2` lados;
- caminhos de `(0,0)` a `(n,n)` que nunca passam acima da diagonal;
- maneiras de empilhar corretamente operações de push e pop.

Reconhecer uma dessas estruturas pode transformar um problema de DP em uma fórmula binomial, ou o contrário.

## 4. Implementação modular

Com a classe de [Coeficientes Binomiais Modulares](binomial-modular.md):

```cpp
long long catalan(int n, const Binomial& binomial) {
    return binomial.choose(2 * n, n) * mod_pow(n + 1, MOD - 2) % MOD;
}
```

Verifique que o pré-cálculo alcança `2*n` e que `MOD` é primo. Para um `n` pequeno sem módulo, a recorrência é uma ótima forma de entender a decomposição estrutural.

<!-- AUXÍLIO VISUAL 1

Criar uma visualização que conecte os cinco objetos contados por C(3): sequências de parênteses, caminhos sob a diagonal e árvores binárias. Destacar a bijeção conceitual entre eles.

Arquivo sugerido: images/catalan-conexoes.svg
-->

## Problemas

{{ exercise_list(exercises) }}
