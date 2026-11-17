{% set exercises %}
  recommended:
    - name: Binary Search
      url: https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/A
      platform: Codeforces EDU
      difficulty: easy
      topics: [busca binária]
    - name: Closest to the Left
      url: https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/B
      platform: Codeforces EDU
      difficulty: easy
      topics: [busca binária, lower bound]
    - name: Closest to the Right
      url: https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/C
      platform: Codeforces EDU
      difficulty: easy
      topics: [busca binária, upper bound]
    - name: Fast search
      url: https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/D
      platform: Codeforces EDU
      difficulty: easy
      topics: [busca binária, prefix sum]
  additional:
    - name: K-th Zero
      url: https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/E
      platform: Codeforces EDU
      difficulty: medium
      topics: [busca binária, segment tree]
{% endset %}

# Busca Binária

Busca binária é uma técnica para encontrar um valor em um espaço **ordenado** sem precisar examinar todos os seus elementos.

Em um vetor ordenado, depois de observar o elemento central, sabemos em qual metade o valor procurado ainda pode estar. Repetir essa decisão elimina aproximadamente metade dos candidatos por iteração.

Por exemplo, para procurar `7` em:

```text
Índice:  0  1  2  3  4  5   6
Vetor:  [1, 3, 4, 6, 7, 8, 11]
```

começamos pelo índice central `3`, cujo valor é `6`. Como `7 > 6`, nenhum valor à esquerda ou no próprio índice `3` pode ser a resposta. A busca continua apenas na metade direita.

## 1. Quando a busca binária é aplicável?

Na forma mais comum, precisamos de um vetor em ordem crescente ou decrescente. A ordenação garante que, ao comparar o alvo com o meio, uma das metades não pode conter a resposta.

Ela também pode ser aplicada a qualquer domínio com uma propriedade monotônica, como uma sequência de valores `false` seguida por valores `true`. Esse uso é detalhado em [Busca Binária na Resposta](binary-search-on-answer.md).

!!! important "Condição essencial"
    Não basta o vetor conter números: ele precisa estar ordenado segundo o mesmo critério usado nas comparações.

    Aplicar busca binária em dados desordenados pode descartar justamente a metade que contém a resposta.

## 2. Ideia central e intervalo de busca

Vamos usar o intervalo fechado `[low, high]`: os dois índices ainda são candidatos à resposta. Inicialmente, ele cobre todo o vetor:

```cpp
int low = 0;
int high = static_cast<int>(values.size()) - 1;
```

Enquanto o intervalo não estiver vazio, calculamos o meio:

```cpp
int mid = low + (high - low) / 2;
```

Usar essa fórmula em vez de `(low + high) / 2` evita overflow quando os índices podem ser grandes.

Há três situações:

| Comparação | Conclusão | Próximo intervalo |
|---|---|---|
| `values[mid] == target` | Encontramos o alvo. | Encerrar a busca. |
| `values[mid] < target` | O alvo, se existir, está à direita. | `[mid + 1, high]` |
| `values[mid] > target` | O alvo, se existir, está à esquerda. | `[low, mid - 1]` |

Os `+ 1` e `- 1` são importantes: `mid` já foi testado e não é a resposta. Além de remover esse índice, eles garantem que o intervalo diminua a cada iteração.

## 3. Exemplo passo a passo: valor presente

Vamos procurar `7` no vetor abaixo.

```text
Índice:  0  1  2  3  4  5   6
Vetor:  [1, 3, 4, 6, 7, 8, 11]
```

| Iteração | low | high | mid | values[mid] | Decisão | Próximo intervalo |
|---:|---:|---:|---:|---:|---|---|
| 1 | 0 | 6 | 3 | 6 | `7 > 6`, descartar a esquerda e o meio. | `[4, 6]` |
| 2 | 4 | 6 | 5 | 8 | `7 < 8`, descartar a direita e o meio. | `[4, 4]` |
| 3 | 4 | 4 | 4 | 7 | Encontramos o alvo. | — |

Em apenas três comparações encontramos a posição `4`. Uma busca linear poderia precisar percorrer os sete elementos.

### Visualizando as escolhas

```text
[1, 3, 4, 6, 7, 8, 11]   mid = 6  → procurar à direita
             ^

[7, 8, 11]               mid = 8  → procurar à esquerda
    ^

[7]                      mid = 7  → encontrado
 ^
```

Na implementação, não criamos novos vetores. Apenas atualizamos `low` e `high`.

## 4. Exemplo passo a passo: valor ausente

Também é importante entender como a busca termina quando o valor não aparece. Vamos procurar `5` no mesmo vetor.

| Iteração | low | high | mid | values[mid] | Decisão | Próximo intervalo |
|---:|---:|---:|---:|---:|---|---|
| 1 | 0 | 6 | 3 | 6 | `5 < 6`, procurar à esquerda. | `[0, 2]` |
| 2 | 0 | 2 | 1 | 3 | `5 > 3`, procurar à direita. | `[2, 2]` |
| 3 | 2 | 2 | 2 | 4 | `5 > 4`, procurar à direita. | `[3, 2]` |

Ao final, `low > high`. Não há mais índices candidatos, portanto `5` não está no vetor.

!!! tip "O que a busca retorna?"
    A versão mais simples retorna qualquer índice que contenha o alvo, ou `-1` se ele não existir. Para vetores com valores repetidos, talvez seja necessário procurar especificamente a primeira ou a última ocorrência; veremos essas variações adiante.

## 5. Implementação iterativa

Este é o template mais comum para procurar um valor em um vetor ordenado em ordem crescente.

```cpp
int index_of(const vector<int>& values, int target) {
    int low = 0;
    int high = static_cast<int>(values.size()) - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (values[mid] == target) {
            return mid;
        }

        if (values[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return -1;
}
```

O laço usa `low <= high` porque, enquanto `low == high`, ainda existe um único candidato que precisa ser testado.

### Exemplo de uso

```cpp
vector<int> values = {1, 3, 4, 6, 7, 8, 11};

cout << index_of(values, 7) << '\n';  // 4
cout << index_of(values, 5) << '\n';  // -1
```

## 6. Implementação recursiva

A mesma ideia pode ser escrita de forma recursiva. A versão iterativa costuma ser preferida em competições porque é mais curta e não consome pilha de chamadas, mas a recursiva evidencia bem os subintervalos.

```cpp
int index_of_recursive(const vector<int>& values, int target, int low, int high) {
    if (low > high) {
        return -1;
    }

    int mid = low + (high - low) / 2;

    if (values[mid] == target) {
        return mid;
    }

    if (values[mid] < target) {
        return index_of_recursive(values, target, mid + 1, high);
    }

    return index_of_recursive(values, target, low, mid - 1);
}
```

A chamada inicial é:

```cpp
int answer = index_of_recursive(values, target, 0, static_cast<int>(values.size()) - 1);
```

## 7. Valores repetidos: lower bound e upper bound

Quando o vetor possui elementos repetidos, encontrar uma ocorrência qualquer pode não ser suficiente.

Considere:

```text
Índice:  0  1  2  3  4  5
Vetor:  [1, 2, 2, 2, 5, 8]
```

Para o valor `2`:

- `lower bound` é o primeiro índice cujo valor é **maior ou igual** a `2`: índice `1`.
- `upper bound` é o primeiro índice cujo valor é **maior** que `2`: índice `4`.

Portanto, todas as ocorrências de `2` ocupam o intervalo `[lower_bound, upper_bound)`; neste caso, `[1, 4)`.

### Primeiro índice com valor maior ou igual ao alvo

O objetivo agora não é parar quando encontramos o alvo. Guardamos uma possível resposta e continuamos procurando à esquerda.

```cpp
int lower_bound_index(const vector<int>& values, int target) {
    int low = 0;
    int high = static_cast<int>(values.size());

    while (low < high) {
        int mid = low + (high - low) / 2;

        if (values[mid] >= target) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }

    return low;
}
```

Aqui usamos o intervalo semiaberto `[low, high)`. O retorno pode ser igual a `values.size()`: isso significa que todos os valores são menores que `target`.

### Primeiro índice com valor estritamente maior que o alvo

Basta trocar a comparação:

```cpp
int upper_bound_index(const vector<int>& values, int target) {
    int low = 0;
    int high = static_cast<int>(values.size());

    while (low < high) {
        int mid = low + (high - low) / 2;

        if (values[mid] > target) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }

    return low;
}
```

Com essas funções, podemos testar se o valor existe, contar ocorrências ou obter a primeira e a última posição:

```cpp
int first = lower_bound_index(values, target);
int after_last = upper_bound_index(values, target);

bool exists = first < static_cast<int>(values.size()) && values[first] == target;
int count = after_last - first;
int last = exists ? after_last - 1 : -1;
```

## 8. Funções da biblioteca padrão

Em C++, normalmente devemos preferir as funções prontas de `<algorithm>` quando elas atendem ao problema.

```cpp
vector<int> values = {1, 2, 2, 2, 5, 8};

auto first = lower_bound(values.begin(), values.end(), 2);
auto after_last = upper_bound(values.begin(), values.end(), 2);

bool exists = binary_search(values.begin(), values.end(), 2);
int count = static_cast<int>(after_last - first);  // 3
int first_index = static_cast<int>(first - values.begin());  // 1
```

| Função | Resultado |
|---|---|
| `binary_search(begin, end, x)` | Informa se `x` existe. |
| `lower_bound(begin, end, x)` | Iterador para o primeiro valor `>= x`. |
| `upper_bound(begin, end, x)` | Iterador para o primeiro valor `> x`. |
| `equal_range(begin, end, x)` | Par com os mesmos iteradores de `lower_bound` e `upper_bound`. |

!!! warning "Pré-condição da STL"
    Essas funções também exigem que o intervalo esteja ordenado. Se o vetor foi modificado depois da ordenação, ordene-o novamente antes de fazer a consulta.

## 9. Por que o algoritmo está correto?

Vamos considerar a versão iterativa que procura uma ocorrência do alvo.

### Invariante

No início de cada iteração, se `target` estiver no vetor, então algum índice que o contém pertence ao intervalo `[low, high]`.

Inicialmente, isso é verdade porque o intervalo cobre todo o vetor.

Se `values[mid] < target`, todos os índices até `mid` contêm valores menores que o alvo, pois o vetor está ordenado. Logo, removê-los ao fazer `low = mid + 1` não remove uma resposta possível.

De forma análoga, se `values[mid] > target`, todos os índices a partir de `mid` contêm valores maiores que o alvo. Portanto, `high = mid - 1` também preserva o invariante.

Se `values[mid] == target`, retornar `mid` está correto.

### Término

Em cada iteração que não encontra o alvo, o tamanho do intervalo diminui. Como ele é finito, eventualmente encontramos o alvo ou chegamos a `low > high`.

No segundo caso, o invariante mostra que não existe índice possível para `target`; então retornar `-1` está correto.

## 10. Complexidade

Se o vetor possui `N` elementos, cada iteração elimina aproximadamente metade do intervalo restante. Assim, o número de iterações é $O(\log N)$.

- Tempo: $O(\log N)$
- Memória: $O(1)$ para a versão iterativa.
- Memória: $O(\log N)$ para a versão recursiva, devido à pilha de chamadas.

## 11. Erros comuns

### 1. Usar um vetor desordenado

A busca binária não ordena o vetor por conta própria. Se a ordem não estiver garantida, ordene os dados ou escolha outra técnica.

### 2. Misturar convenções de intervalo

O template com `[low, high]` usa `low <= high`, enquanto o template com `[low, high)` usa `low < high`. Misturar atualizações e condições de parada de convenções diferentes costuma causar respostas incorretas ou laços infinitos.

### 3. Não remover o meio testado

Depois de concluir que `values[mid] < target`, atualizar `low = mid` mantém o mesmo meio quando restam dois elementos. A atualização correta é `low = mid + 1`.

### 4. Ignorar valores repetidos

Se o enunciado pede a primeira ocorrência, retornar ao encontrar qualquer ocorrência não basta. Use `lower_bound`; para a última, use `upper_bound - 1`.

### 5. Calcular o meio com risco de overflow

Prefira `low + (high - low) / 2`. Em problemas com intervalos numéricos grandes, `low + high` pode ultrapassar o limite de um inteiro.

## Problemas

{{ exercise_list(exercises) }}

## Recursos

- [Binary Search - C++ reference](https://en.cppreference.com/w/cpp/algorithm/binary_search)
- [lower_bound - C++ reference](https://en.cppreference.com/w/cpp/algorithm/lower_bound)
- [Curso de Binary Search - Codeforces](https://codeforces.com/edu/course/2/lesson/6)
