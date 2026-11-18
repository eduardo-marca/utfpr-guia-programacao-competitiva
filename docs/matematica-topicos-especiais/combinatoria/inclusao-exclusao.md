{% set exercises %}
  recommended:
    - name: Prime Multiples
      url: https://cses.fi/problemset/task/2185
      platform: CSES
      difficulty: medium
      topics: [inclusão-exclusão, máscaras de bits, múltiplos]
      objective: Conte números divisíveis por ao menos um primo dado.
    - name: Counting Derangements
      url: https://cses.fi/problemset/task/1717
      platform: CSES
      difficulty: medium
      topics: [inclusão-exclusão, permutação]
      objective: Conte permutações sem elementos em sua posição original.
  additional:
    - name: Count the Arrays
      url: https://codeforces.com/problemset/problem/1513/E
      platform: Codeforces
      difficulty: hard
      topics: [combinatória, inclusão-exclusão, módulo]
      objective: Combine contagem de permutações e restrições sobre valores mínimos.
{% endset %}

# Inclusão-Exclusão

Inclusão-exclusão conta a união de conjuntos que se sobrepõem. A ideia é somar cada conjunto, subtrair as interseções de pares, somar as de triplas e assim por diante.

## 1. Dois conjuntos

Para conjuntos `A` e `B`:

$$
|A \cup B| = |A| + |B| - |A \cap B|
$$

Ao somar `|A|` e `|B|`, os elementos comuns aparecem duas vezes; subtrair a interseção corrige isso.

Exemplo: de 1 a 100, há 50 múltiplos de 2 e 33 múltiplos de 3. Os 16 múltiplos de 6 foram contados duas vezes:

$$
50 + 33 - 16 = 67
$$

## 2. Vários conjuntos

Para `m` conjuntos, a fórmula alterna sinais:

$$
\left|\bigcup A_i\right| =
\sum |A_i| - \sum |A_i \cap A_j| + \sum |A_i \cap A_j \cap A_k| - \cdots
$$

Em problemas com poucos conjuntos, iteramos todos os subconjuntos não vazios. Para contar números até `n` divisíveis por ao menos um primo, a interseção de um subconjunto é o conjunto de múltiplos do MMC dos seus primos.

```cpp
long long count_multiples(long long n, const vector<long long>& primes) {
    long long answer = 0;
    int m = static_cast<int>(primes.size());

    for (int mask = 1; mask < (1 << m); mask++) {
        long long lcm = 1;
        bool overflow = false;
        for (int i = 0; i < m; i++) {
            if (mask & (1 << i)) {
                if (lcm > n / primes[i]) {
                    overflow = true;
                    break;
                }
                lcm *= primes[i];
            }
        }
        if (overflow) continue;

        long long count = n / lcm;
        if (__builtin_popcount(mask) % 2) answer += count;
        else answer -= count;
    }
    return answer;
}
```

O sinal depende da paridade do subconjunto: tamanho ímpar soma, tamanho par subtrai.

## 3. Como reconhecer a técnica

Use inclusão-exclusão quando o enunciado pede elementos que satisfazem **pelo menos uma** propriedade e você consegue contar interseções de propriedades.

!!! warning "Limite de conjuntos"
    A enumeração de subconjuntos custa $O(2^m)$. Ela é adequada para `m` pequeno; a dificuldade real costuma estar em calcular cada interseção e evitar overflow no MMC.

## 4. Derangements: uma aplicação clássica

Considere todas as `n!` permutações e, para cada posição `i`, defina `A_i` como o conjunto de permutações que deixam `i` fixa. Queremos evitar todos os conjuntos `A_i`.

Ao fixar quaisquer `j` posições, restam `(n-j)!` maneiras de permutar as demais. Há $\binom{n}{j}$ escolhas dessas posições; logo, pela inclusão-exclusão:

$$
D(n)=n!-\binom{n}{1}(n-1)!+\binom{n}{2}(n-2)!-\cdots
=n!\sum_{j=0}^{n}\frac{(-1)^j}{j!}
$$

Essa derivação explica a fórmula das [Permutações Caóticas](permutacoes-combinacoes.md). Em código, a recorrência daquela página costuma ser mais simples e evita frações.

<!-- AUXÍLIO VISUAL 1

Criar um diagrama de Venn para múltiplos de 2 e de 3 até 100, destacando a interseção dos múltiplos de 6 e a correção da contagem dupla.

Arquivo sugerido: images/inclusao-exclusao.svg
-->

## Problemas

{{ exercise_list(exercises) }}
