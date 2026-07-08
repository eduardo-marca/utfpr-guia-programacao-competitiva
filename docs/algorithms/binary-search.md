# Busca Binária

Busca binária é um dos algoritmo mais comums e utilizados em programação competitiva, sendo muito mais eficiente que uma busca padrão.

Ele é um algoritmo de busca que opera em um espaço de busca ordenado (por exemplo um vetor odenado). Ele funciona dividindo o espaço na metade repetidas vezes até achar o valor alvo. Ele se aproveita do fato de saber em que metade o valor alvo pode estar, apenas o olhando o valor centrar, já que o espaço é ordenado.

!!! note
    Reforçando, esse algoritmo só funciona se o espaço de busca for ordenado (ou monótono), muitas vezes sendo possível utilizar o algoritmo de dois ponteiros também.

??? example
    Por exemplo, em um vetor ordenado `{1, 3, 4, 6, 7, 8, 11}` buscando-se o valor 7, primeiro verifica-se o valor central do vetor: 6. Se esse fosse o valor alvo poderiamos para aqui, mas podemos perceber que o valor alvo é maior do que esse valor central, portando ele deve estar a direita dele, então reduzimos a nossa busca ao vetor `{7, 8, 9}` (na prática não é necessário realmente contruir um novo vetor, apenas limitar o espaço de busca). Depois verificamos o valor central desse novo vetor: 8. Como o valor alvo 7 é menor do que 8 olhamos para a esquerda dele, chegando no vetor `{7}`. Por fim, o valor central (e único valor) desse vetor é o nosso valor alvo, portando achamos o valor procurado. Se o nosso espaço de busca se tornar vazio em algum momento, então nosso valor alvo não está no espaço de busca.

!!! tip
    Nem sempre é possível reduzir o espaço de busca exatamente na metade, mas só precisamos estar o mais próximo possível disso para o funcionamento do algoritmo.

Isso é muito melhor que uma busca comum pois não precisamos verificar todas as posições do vetor. Como reduzimos o tamanho do espaço de busca pela metada em cada iteração o algoritmo é logaritmico.

## Complexidade

- Tempo: $O(\log N)$
- Memória $O(1)$

## Implementação

Existem diversas implementações para isso, as mais comumns são a iterativa e recursiva, incluindo variações.

### Implementação Iterativa

```cpp
int binarySearch(vector<int> &arr, int x) {
    int low = 0;
    int high = arr.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;

        // Verifica se x está presente no meio
        if (arr[mid] == x)
            return mid;

        // Se x é maior, ignora a metade esquerda
        if (arr[mid] < x)
            low = mid + 1;

        // Se x é menor, ignora a metade direita
        else
            high = mid - 1;
    }

    // Se chegarmos aqui, então o valor não está presente
    return -1;
}
```

### Implementação Recursiva

```cpp
int binarySearch(vector<int> &arr, int low, int high, int x) {
    if (high >= low) {
        int mid = low + (high - low) / 2;

        // Verifica se x está presente no meio
        if (arr[mid] == x)
            return mid;

        // Se x é menor, ignora a metade direita
        if (arr[mid] > x)
            return binarySearch(arr, low, mid - 1, x);

        // Se x é maior, ignora a metade esquerda
        return binarySearch(arr, mid + 1, high, x);
    }

    // Se chegarmos aqui, então o valor não está presente
    return -1;
}
```

!!! tip
    Nessas implementações retornamos a posição do valor procurado (ou -1 se não estiver presente), mas poderiamos retornar apenas um valor booleano, indicado se o valor está presente ou não.

## Problemas

### Recomendados
1. [Binary Search](https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/A)
2. [Closest to the Left](https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/B)
3. [Closest to the Right](https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/C)
4. [Fast search](https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/D)
5. [Factory Machines](https://cses.fi/problemset/task/1620)
6. [Multiplication Table](https://cses.fi/problemset/task/2422)

### Adicionais
1. [K-th Zero](https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/E)

## Recursos
- [Binary Search - GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)
- [Curso de Binary Search - Codeforces](https://codeforces.com/edu/course/2/lesson/6)
