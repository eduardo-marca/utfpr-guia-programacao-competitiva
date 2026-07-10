# Busca Completa
A Busca Completa (ou Complete Search) é um método geral que pode ser usado para resolver praticamente qualquer problema algoritmo (mesmo que nem sempre de forma eficiênte). Ele consiste em gerar todas as possíveis soluções para o problema através da força bruta, e testar cada uma delas até achar a solução correta.

## Quando Usar?
Esse método é útil se existe tempo ou recursos suficientes para gerar e testar todas as possibilidades de um problema. Ele geralmente só pode ser usado em problemas que não são tão complexos, já que gera uma quantidade enorme de possibilidades pois não usa nenhuma estratégia de busca.

## Gerando Subconjuntos
Muitos problemas de Busca Completa envolvem gerar todos os subconjuntos de um conjunto de $n$ elementos. Por exemplo, os subconjuntos de ${0, 1, 2}$ são $\varnothing$, $\{0\}$, $\{1\}$, $\{2\}$, $\{0, 1\}$, $\{0, 2\}$, $\{1, 2\}$ e $\{0, 1, 2\}$.

Existem dois métodos comums de se fazer isso: com uma busca recursiva ou com bitmask.

### Recursão
A busca recursiva é uma das formas mais simples de se fazer isso. O seguinte exemplo permite criar todos os subconjuntos de $\{0, 1, 2, \dots, n-1\}$. Essa função precisa de um $vector$ para guardar o subconjunto atual. A busca começa com a chamada $search(0)$.
```cpp
int n; // tamnho do conjunto
vector<int> subset; // subconjunto atual
void search(int k) {
    if(k == n) {
        // processa o subconjunto
    } else {
        search(k+1);
        subset.push_back(k);
        search(k+1);
        subset.pop_back();
    }
}
```
Quando essa função é chamada com parâmtro $k$, ela criar duas novas chamadas: uma incluindo o elemento $k$ e outra não. Assim, cada uma dessas novas chamadas vai incluir ou não $k+1$, e assim por diante, até chegar em $k=n$.

Esse algoritmo tem complexidade $O(2^n)$ e complexidade de espaço $O(n)$.

!!! tip "Implementação Alternativa"
    Também é possível implementar o algoritmo usando outras estruturas para matner o subconjunto, como um $set$, por exemplo.
    
    Além disso, é possível começar a chamada em $1$ para gerar os subconjuntos sem o $0$.
    Também é possível gerar os subconjuntos indo até $n$ se colocarmos `if(k > n)` na função.

### Bitmask
Também é possível utilizar a representação binário de números inteiros para gerar subconjuntos. Se você considerar os números de $0$ até $7$, por exemplo, temos as seguintes representações em binário: 000, 001, 010, 011, 100, 101, 110, 111. Se considerarmos que cada bit representa um elemento do conjunto, onde $0$ representa a ausência do elemento e $1$ a presença do mesmo, podemos gerar os subconjuntos de forma mais eficiente. Para isso, basta percorrer todos os bits de um número inteiro para obter os subconjuntos. Para isso começamos no número $0$ (conjunto vazio) até o número $2^n-1$.

```c++
for(int b = 0; b < (1<<n); b++) {
    vector<int> subset;
    for(int i = 0; i < n; i++) {
        if(b & (1<<i)) subset.push_back(i);
    }
    // processa o subconjunto
}
```
Esse algoritmo tem complexidade $O(2^n)$ e complexidade de espaço $O(n)$.

A técnica de bitmask pode ser usada em muitas outras situações, sendo muito popular em programação competitiva.

## Gerando Permutações
Muitos problemas exigem achar uma permutação de um conjunto de elementos de tamanho $n$. Uma permutação é uma sequência de elementos em que a ordem dos elementos importa. Por exemplo, se temos um conjunto $\{0, 1, 2\}$, as permutações são: $\{0, 1, 2\}$, $\{0, 2, 1\}$, $\{1, 0, 2\}$, $\{1, 2, 0\}$, $\{2, 0, 1\}$ e $\{2, 1, 0\}$.

Novamente temos duas formas comums de se fazer isso: com recursão e usando a função `next_permutation` da STL do C++.

### Recursão
De forma parecida com os subconjuntos, podemos gerar permutações utilizando recursão. A seguinte função cria todas as permutações de $\{0, 1, 2, \dots, n-1\}$. A função constroi um vetor `permutation` que contém a permutação.
```cpp
vector<int> permutation;
bool chosen[n];
void search() {
    if(permutation.size() == n) {
        // processa a permutação
    } else {
        for(int i = 0; i < n; i++) {
            if(chosen[i]) continue;
            chosen[i] = true;
            permutation.push_back(i);
            search();
            chosen[i] = false;
            permutation.pop_back();
        }
    }
}
```
Esse algoritmo tem complexidade $O(n!)$ e complexidade de espaço $O(n)$.

Cada chamada dessa função adiciona um novo elemento que ainda não foi escolhido à permutação, e para cada escolha criar uma nova chamada recursiva. Quando o tamanho da permutação chegar a $n$, então uma permutação foi gerada.

### STL
A biblioteca padrão do C++ possui a função `next_permutation`, que permite criar a próxima permutação em ordem crescente, então começando com o vetor $[0, 1, ..., n - 1]$ podemos gerar todas as permutações.
```cpp
vector<int> permutation;
for(int i = 0; i < n; i++) {
    permutation.push_back(i);
}
do {
    // processa a permutação
} while(next_permutation(permutation.begin(), permutation.end()));
```
Esse algoritmo tem complexidade $O(n!)$ e complexidade de espaço $O(n)$.

## Backtracking
Um algoritmo de *backtracking* começa com uma solução vazia e extende a solução passo a passo. A busca acontece de forma recursiva passando por todas as diferentes formas de se construir uma solução. Na prática funciona de forma parecida com os dois algoritmos recursivos que vimos a cima, mas podemos extender essa idea para muitos outros problemas.

### O problema das $n$ rainhas
Este é um problema muito famoso que pode ser resolvido por *backtracking* e pode ajudar a tenter essa técnica.

Imagine que você tem $n$ rainhas e precisa colocá-las em um tabuleiro de $n \times n$ de forma que nenhuma rainha ataca outra. Como fazer isso? Uma solução possível seria testar todas as formas de se colocar as $n$ rainhas no tabuleiro e testar se algum par de rainhas se atacam, e contar todas as soluções que funciona, mas isso teria uma complexidade de $O(n^2!)$. Existe uma solução muito mais simples usando *backtracking*.

Primeiro, perceba que só podemos colocar uma rainha por linha, uma por coluna, uma por diagonal principal, e uma por diagonal secundária. Então só precisamos testar soluções que sigam essas regras, mas a questão é como gerar essas soluções.

Podemos colocar uma rainha por linha, e manter as colunas e diagonais que já foram ocupadas, e então testar se a rainha pode ser colocada na linha seguinte. Então continuamos o processo somente das posições que estão atualmente válidas.

```cpp
void search(int y) {
    if(y == n) {
        count++;
        return;
    }
    for(int x = 0; x < n; x++) {
        if(column[x] || diag1[x+y] || diag2[x-y+n-1]) continue;
        column[x] = diag1[x+y] = diag2[x-y+n-1] = true;
        search(y+1);
        column[x] = diag1[x+y] = diag2[x-y+n-1] = false;
    }
}
```

## Alternativas
Existem outras técnicas que usam estratégias de busca mais eficientes para resolver um problema. Elas geralmente são mais rápidas e podem ser aplicadas em problemas maiores. São úteis caso a Busca Completa não seja aplicável. Alguams dessas técnicas são:

- [Busca Binária](../basic-algorithms/binary-search.md)
- [Algoritmos Gulosos](greedy.md)
- [Programação Dinâmica](dynamic-programming.md)

## Problemas

### Recomendados
[Product of Closures](https://codeforces.com/problemset/problem/2242/E)
[Unstable Elements](https://codeforces.com/problemset/problem/2242/C)
[Annoying the Ghost](https://codeforces.com/problemset/problem/2237/B)
[Friendly Gifts](https://codeforces.com/problemset/problem/2236/E)

### Adicionais
[Omsk Programmers](https://codeforces.com/problemset/problem/2236/C)
[Quadratic Jumps](https://codeforces.com/problemset/problem/2231/F)
