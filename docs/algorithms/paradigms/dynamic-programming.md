{% set exercises %}
  recommended:
    - name: New Year and the Permutation Concatenation
      url: https://codeforces.com/problemset/problem/1091/D
      platform: Codeforces
      difficulty: hard
      topics: [combinatória, programação dinâmica]
    - name: Multiplicity
      url: https://codeforces.com/problemset/problem/1061/C
      platform: Codeforces
      difficulty: hard
      topics: [programação dinâmica, divisores]
  additional:
    - name: Appleman and Tree
      url: https://codeforces.com/contest/461/problem/B
      platform: Codeforces
      difficulty: hard
      topics: [DP em árvores]
    - name: Complete Mirror
      url: https://codeforces.com/problemset/problem/1182/D
      platform: Codeforces
      difficulty: hard
      topics: [DP em árvores, hashes]
{% endset %}

# Programação Dinâmica

A programação dinâmica (também chamada de PD, dynamic programming ou DP) é um paradigma de programação que consiste em resolver o problema reutilizando a solução dos subproblemas (versões mais simples ou menores do problema original).

## O Paradigma

Por se tratar de um paradigma, não existe um algoritmo específico para resolver o problema. A programação dinâmica é uma técnica que pode ser aplicada a qualquer problema, mas ela requer algumas considerações importantes:

- Os subproblemas devem ser independentes e não inter-relacionados.
- O resultado de cada subproblema deve ser armazenado em memória para ser usado posteriormente.
- A solução do problema original pode ser obtida a partir da solução dos subproblemas.

As formas mais comuns de implementação da programação dinâmica são:

- Recursão: Uma função recursiva que resolve o problema dividindo-o em subproblemas menores e reutilizando os resultados das chamadas recursivas. A técnica de memoização é uma forma popular de implementar a recursão.
- Iteração: Um loop for ou while que itera sobre todos os elementos do problema, calculando cada elemento da solução do problema em função dos subproblemas já resolvidos.

??? example "Exemplo 1"
    Considere o problema de se calcular os números de Fibonacci. Uma forma de resolver esse problema é usando a programação dinâmica. A ideia básica é que cada número na sequência de Fibonacci pode ser calculado a partir da soma dos dois números anteriores. Ou seja
    $$
    fib(n) = fib(n-1) + fib(n-2)
    $$
    $$
    fib(0) = fib(1) = 1
    $$
    Assim podemos calcular $fib(n)$ usando programação dinâmica.
    
    Solução com iteração:
    ```cpp
    fib[0] = 0;
    fib[1] = 1;
    for(int i = 2; i <= n; i++) {
        fib[i] = fib[i-1] + fib[i-2];
    }
    return fib[n];
    ```

    Solução com recursão:
    ```cpp
    int fib[N+1];
    vector<bool> calculated(N+1, false);

    int fib(int n) {
        if(n < 2) return 1;
        if(calculated[n]) return fib[n];
        calculated[n] = true;
        return fib(n-1) + fib(n-2);
    }
    ```

## Problemas

{{ exercise_list(exercises) }}

## Recursos
- [Geeks for Geeks](https://www.geeksforgeeks.org/dsa/dynamic-programming/)
- [Atcoder Educational DP Contest](https://atcoder.jp/contests/dp)
- [Atcoder Next DP Contest](https://atcoder.jp/contests/ndpc)
