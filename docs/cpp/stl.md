# STL

A biblioteca padrão do C++ (STL) oferece uma série de estruturas de dados e funções úteis para facilitar a implementação de algoritmos em programação competitiva. A seguir, apresentamos algumas das mais comuns e suas principais características.

## Array
São espaços na memória para armazenar um número fixo de valores do mesmo tipo. O acesso a um elemento é feito através de um índice, que começa em 0. Seu tamanho deve ser definido no momento da declaração e não pode ser alterado posteriormente.

- `int arr[n]` - declara um array de $n$ inteiros. Complexidade: $O(1)$ para dados primitivos.
- `arr[i]` - acessa o elemento na posição $i$. Complexidade: $O(1)$.

!!! note
    O C++ também oferece a classe `std::array` da biblioteca padrão, mas não costuma ser utilizada em programação competitiva, pois é mais verbosa e não oferece vantagens significativas em relação a um array comum.

## Vector
É uma estrutura de dados dinâmica que pode crescer ou diminuir de tamanho conforme necessário. Ele é implementado como um array dinâmico, o que significa que ele aloca mais memória do que o necessário para armazenar os elementos atuais, permitindo que novos elementos sejam adicionados sem a necessidade de realocar toda a estrutura.

Ele oferece uma série de métodos para manipulação dos elementos, como `push_back` para adicionar um elemento no final, `pop_back` para remover o último elemento, `size` para obter o número de elementos, entre outros.

Pode ser usado como array normal, apesar de ser mais verboso. É uma das estruturas de dados mais utilizadas em programação competitiva, devido a sua flexibilidade e facilidade de uso.

- `vector<int> v(n, x)` — cria um vetor com n elementos inicializados com x. Complexidade: $O(n)$.
- `v.push_back(x)` — adiciona x ao final do vetor. Complexidade: $O(1)$.
- `v.pop_back()` — remove o último elemento do vetor. Complexidade: $O(1)$.
- `v.size()` — retorna o tamanho do vetor. Complexidade: $O(1)$.
- `v.empty()` — retorna true se o vetor estiver vazio. Complexidade: $O(1)$.
- `v.clear()` — remove todos os elementos do vetor. Complexidade: $O(n)$.
- `v.front()` — retorna o primeiro elemento. Complexidade: $O(1)$.
- `v.back()` — retorna o último elemento. Complexidade: $O(1)$.
- `v.begin()` — retorna iterador para o primeiro elemento. Complexidade: $O(1)$.
- `v.end()` — retorna iterador para a posição após o último elemento. Complexidade: $O(1)$.
- `v.insert(it, x)` — insere x na posição do iterador it. Complexidade: $O(n)$.
- `v.erase(it)` — remove o elemento apontado por it. Complexidade: $O(n)$.
- `v.erase(it1, it2)` — remove os elementos no intervalo [it1, it2). Complexidade: $O(n)$.
- `v.resize(n)` — redimensiona o vetor para n elementos. Complexidade: $O(n)$.
- `v.resize(n, x)` — redimensiona o vetor para n elementos inicializados com x. Complexidade: $O(n)$.
- `fill(v.begin(), v.end(), x)` — preenche o vetor v com o valor x. Complexidade: $O(n)$.
- `sort(v.begin(), v.end())` — ordena o vetor v. Complexidade: $O(n \log n)$.
- `reverse(v.begin(), v.end())` — inverte o vetor v. Complexidade: $O(n)$.
- `accumulate(v.begin(), v.end(), 0)` — soma todos os elementos do vetor v. Complexidade: $O(n)$.
- `max_element(v.begin(), v.end())` — retorna iterador para o maior elemento. Complexidade: $O(n)$.
- `min_element(v.begin(), v.end())` — retorna iterador para o menor elemento. Complexidade: $O(n)$.
- `count(v.begin(), v.end(), x)` — retorna o número de ocorrências de x. Complexidade: $O(n)$.
- `find(v.begin(), v.end(), x)` — retorna iterador para a primeira ocorrência de x ou v.end(). Complexidade: $O(n)$.
- `lower_bound(v.begin(), v.end(), x)` — primeiro elemento ≥ x (vetor ordenado). Complexidade: $O(\log n)$.
- `upper_bound(v.begin(), v.end(), x)` — primeiro elemento > x (vetor ordenado). Complexidade: $O(\log n)$.
- `next_permutation(a.begin(), a.end())` — gera a próxima permutação lexicográfica. Complexidade: $O(n)$.

## Pair

O `pair` é uma estrutura de dados que armazena dois valores de tipos possivelmente diferentes. Ele é útil para armazenar pares de dados relacionados, como coordenadas, chaves e valores, entre outros.

- `pair<int, int> p` — cria um par de inteiros. Complexidade: $O(1)$.
- `p.first` — retorna o primeiro elemento do par. Complexidade: $O(1)$.
- `p.second` — retorna o segundo elemento do par. Complexidade: $O(1)$.

!!! tip
    `auto [x, y] = p` — desempacota os elementos do par em variáveis x e y. Complexidade: $O(1)$.

Quando comparamos dois pares, eles são comparados primeiro pelo `first` e, em caso de empate, pelo `second`. Isso é útil para ordenar pares em estruturas como `set` ou `map`.

## Tuple

A `tuple` é uma estrutura de dados que armazena um número fixo de valores de tipos possivelmente diferentes. Ela é útil para armazenar grupos de dados relacionados, como coordenadas em 3D, informações de um aluno (nome, idade, nota), entre outros.

- `tuple<int, string, double> t` — cria uma tupla com um inteiro, uma string e um double. Complexidade: $O(1)$.
- `get<i>(t)` — retorna o elemento na posição i da tupla. Complexidade: $O(1)$.

!!! danger
    Não é possível acessar os elementos da tupla usando `t.first`, como em um par. É necessário usar a função `get` para acessar os elementos ou desempacotá-los diretamente.

!!! tip
    `auto [x, y, z] = t` — desempacota os elementos da tupla em variáveis x, y e z. Complexidade: $O(1)$.

## Sets
### Set
Estrutura que permite armazenar elementos únicos em uma coleção ordenada. Ele é implementado como uma árvore binária balanceada, o que significa que as operações de inserção, remoção e busca são realizadas em tempo logarítmico. Ele é útil para armazenar elementos sem duplicatas e para realizar operações de conjunto, como união, interseção e diferença.

### Unordered Set
Estrutura que permite armazenar elementos únicos em uma coleção não ordenada. Ele é implementado como uma tabela hash, o que significa que as operações de inserção, remoção e busca são realizadas em tempo constante em média.

Ele funciona de forma similar ao `set`, com praticamente as mesmas operações, mas não mantém os elementos em ordem, o que pode ser útil em algumas situações onde a ordem dos elementos não é importante.

Porém ele pode ser mais lento que o `set` em alguns casos, especialmente quando há muitas colisões na tabela hash, o que pode levar a um tempo de execução pior do que o esperado. Por isso, é importante avaliar qual estrutura é mais adequada para cada situação específica.

### Multiset
Estrutura que permite armazenar elementos repetidos em uma coleção ordenada. Ele é implementado como uma árvore binária balanceada, o que significa que as operações de inserção, remoção e busca são realizadas em tempo logarítmico. Ele é útil para 1
armazenar elementos com repetição e para realizar operações de conjunto, como união, interseção e diferença.

### Operações
- `set<int> s` — cria um conjunto de inteiros. Complexidade: $O(1)$.
- `s.insert(x)` — insere o elemento x no conjunto. Complexidade: $O(\log n)$.
- `s.erase(x)` — remove o elemento x do conjunto. Complexidade: $O(\log n)$.
- `s.find(x)` — retorna iterador para x ou `s.end()` se não existir. Complexidade: $O(\log n)$.
- `s.size()` — retorna o tamanho do conjunto. Complexidade: $O(1)$.
- `s.empty()` — retorna true se o conjunto estiver vazio. Complexidade: $O(1)$.
- `s.clear()` — remove todos os elementos do conjunto. Complexidade: $O(n)$.
- `s.begin()` — retorna iterador para o primeiro elemento. Complexidade: $O(1)$.
- `s.end()` — retorna iterador para a posição após o último elemento. Complexidade: $O(1)$.
- `unordered_set<int> us` — conjunto não ordenado de inteiros. Complexidade: $O(1)$ para inserção, remoção e busca em média.
- `multiset<int> ms` — conjunto de inteiros que permite elementos repetidos.
- `ms.erase(ms.find(x))` — remove apenas uma ocorrência de x do multiset. Complexidade: $O(\log n)$.

## Maps

### Map
Estrutura que armazena pares de chave-valor, onde cada chave é única. Ele é implementado como uma árvore binária balanceada, o que significa que as operações de inserção, remoção e busca são realizadas em tempo logarítmico. Ele é útil para armazenar dados associados a chaves únicas e para realizar operações de mapeamento, como busca por chave, inserção de pares chave-valor e remoção de pares chave-valor.


### Unordered Map
Estrutura que armazena pares de chave-valor, onde cada chave é única. Ele é implementado como uma tabela hash, o que significa que as operações de inserção, remoção e busca são realizadas em tempo constante em média. Ele é útil para armazenar dados associados a chaves únicas e para realizar operações de mapeamento, como busca por chave, inserção de pares chave-valor e remoção de pares chave-valor.

Ele funciona de forma similar ao `map`, com praticamente as mesmas operações, mas não mantém os pares chave-valor em ordem, o que pode ser útil em algumas situações onde a ordem dos elementos não é importante.

Porém ele pode ser mais lento que o `map` em alguns casos, especialmente quando há muitas colisões na tabela hash, o que pode levar a um tempo de execução pior do que o esperado. Por isso, é importante avaliar qual estrutura é mais adequada para cada situação específica.

### Multimap
Estrutura que armazena pares de chave-valor, onde as chaves podem ser repetidas. Ele é implementado como uma árvore binária balanceada, o que significa que as operações de inserção, remoção e busca são realizadas em tempo logarítmico. Ele é útil para armazenar dados associados a chaves com repetição e para realizar operações de mapeamento, como busca por chave, inserção de pares chave-valor e remoção de pares chave-valor.


### Operações

- `map<int,int> m` — cria um mapa de inteiros para inteiros. Complexidade: $O(1)$.
- `m[key]` — retorna o valor associado à chave key. Complexidade: $O(\log n)$.
- `m[key] = value` — associa value à chave key. Complexidade: $O(\log n)$.
- `m.erase(key)` — remove a chave key do mapa. Complexidade: $O(\log n)$.
- `m.find(key)` — retorna iterador para a chave key ou m.end() se não existir. Complexidade: $O(\log n)$.
- `m.size()` — retorna o tamanho do mapa. Complexidade: $O(1)$.
- `m.empty()` — retorna true se o mapa estiver vazio. Complexidade: $O(1)$.
- `m.clear()` — remove todos os pares chave–valor do mapa. Complexidade: $O(n)$.
- `m.begin()` — retorna iterador para o primeiro par chave–valor. Complexidade: $O(1)$.
- `m.end()` — retorna iterador para a posição após o último elemento. Complexidade: $O(1)$.

## Iterators

Os iteradores são objetos que permitem percorrer os elementos de uma estrutura de dados, como um vetor, um conjunto ou um mapa. Eles são usados para acessar e manipular os elementos de forma eficiente, sem a necessidade de conhecer a implementação interna da estrutura.

Podem ser usados para percorrer os elementos de uma estrutura de dados usando um loop, como um `for` ou um `while`, ou para realizar operações específicas, como ordenação, busca ou contagem.

Funcionam com quase todas as estruturas de dados da STL, como `vector`, `set`, `map`, entre outras, e são uma parte fundamental da programação em C++.

- `o.begin()` — retorna um iterador para o primeiro elemento do objeto **o**. Complexidade: $O(1)$.
- `o.end()` — retorna um iterador para a posição após o último elemento do objeto **o**. Complexidade: $O(1)$.
- `*it` — acessa o elemento apontado pelo iterador it. Complexidade: $O(1)$.
- `for (auto it = o.begin(); it != o.end(); ++it)` — percorre os elementos do objeto **o** usando um iterador. Complexidade: $O(n)$.
- `for (auto& x : o)` — percorre os elementos do objeto **o** usando um loop for-each. Complexidade: $O(n)$.

### Exemplos
- `for (auto it = v.begin(); it != v.end(); ++it) { cout << *it << endl; }` — imprime os elementos do vetor **v** usando um iterador.
- `for (auto& x : v) { cout << x << endl; }` — imprime os elementos do vetor **v** usando um loop for-each.
- `sort(v.begin(), v.end())` — ordena os elementos do vetor **v** usando iteradores. Complexidade: $O(n \log n)$.
- `count(v.begin(), v.end(), x)` — conta o número de ocorrências de x no vetor **v** usando iteradores. Complexidade: $O(n)$.
- `find(v.begin(), v.end(), x)` — encontra a primeira ocorrência de x no vetor **v** usando iteradores. Complexidade: $O(n)$.
- `for (auto [key, value] : m) { cout << key << ": " << value << endl; }` — percorre os pares chave-valor do mapa **m** usando um loop for-each com desempacotamento de tupla.

## Stack
A pilha é uma estrutura de dados que segue o princípio LIFO (Last In, First Out), ou seja, o último elemento inserido é o primeiro a ser removido. Ela é útil para armazenar dados temporários e para realizar operações de backtracking, como em algoritmos de busca em profundidade.

- `stack<int> s` — cria uma pilha de inteiros. Complexidade: $O(1)$.
- `s.push(x)` — adiciona x ao topo da pilha. Complexidade: $O(1)$.
- `s.pop()` — remove o elemento do topo da pilha. Complexidade: $O(1)$.
- `s.top()` — retorna o elemento do topo da pilha. Complexidade: $O(1)$.
- `s.size()` — retorna o tamanho da pilha. Complexidade: $O(1)$.
- `s.empty()` — retorna true se a pilha estiver vazia. Complexidade: $O(1)$.

!!! tip
    `while (!s.empty()) { cout << s.top() << endl; s.pop(); }` — imprime os elementos da pilha **s** do topo para a base.

## Queue

A fila é uma estrutura de dados que segue o princípio FIFO (First In, First Out), ou seja, o primeiro elemento inserido é o primeiro a ser removido. Ela é útil para armazenar dados temporários e para realizar operações de breadth-first search (BFS) em grafos.

- `queue<int> q` — cria uma fila de inteiros. Complexidade: $O(1)$.
- `q.push(x)` — adiciona x ao final da fila. Complexidade: $O(1)$.
- `q.pop()` — remove o primeiro elemento da fila. Complexidade: $O(1)$.
- `q.front()` — retorna o primeiro elemento da fila. Complexidade: $O(1)$.
- `q.size()` — retorna o tamanho da fila. Complexidade: $O(1)$.
- `q.empty()` — retorna true se a fila estiver vazia. Complexidade: $O(1)$.

!!! tip
    `while (!q.empty()) { cout << q.front() << endl; q.pop(); }` — imprime os elementos da fila **q** do início para o final.

## Deque

A deque (double-ended queue) é uma estrutura de dados que permite inserção e remoção de elementos em ambas as extremidades. É útil para armazenar dados temporários e para realizar operações de forma eficiente em ambas as extremidades.

- `deque<int> d` — cria um deque de inteiros. Complexidade: $O(1)$.
- `d.push_back(x)` — adiciona x ao final do deque. Complexidade: $O(1)$.
- `d.push_front(x)` — adiciona x ao início do deque. Complexidade: $O(1)$.
- `d.pop_back()` — remove o elemento do final do deque. Complexidade: $O(1)$.
- `d.pop_front()` — remove o elemento do início do deque. Complexidade: $O(1)$.
- `d.front()` — retorna o primeiro elemento do deque. Complexidade: $O(1)$.
- `d.back()` — retorna o último elemento do deque. Complexidade: $O(1)$.
- `d.size()` — retorna o tamanho do deque. Complexidade: $O(1)$.
- `d.empty()` — retorna true se o deque estiver vazio. Complexidade: $O(1)$.

!!! tip
    `while (!d.empty()) { cout << d.front() << endl; d.pop_front(); }` — imprime os elementos do deque **d** do início para o final.

## Priority Queue

- `priority_queue<int> pq` — cria uma fila de prioridade de inteiros (máx-heap). Complexidade: $O(1)$.
- `pq.push(x)` — adiciona o elemento x na fila de prioridade. Complexidade: $O(\log n)$.
- `pq.pop()` — remove o maior elemento da fila de prioridade. Complexidade: $O(\log n)$.
- `pq.top()` — retorna o maior elemento da fila de prioridade. Complexidade: $O(1)$.
- `pq.size()` — retorna o tamanho da fila de prioridade. Complexidade: $O(1)$.
- `pq.empty()` — retorna true se a fila de prioridade estiver vazia. Complexidade: $O(1)$.

!!! tip
    `while (!pq.empty()) { cout << pq.top() << endl; pq.pop(); }` — imprime os elementos da fila de prioridade **pq** do maior para o menor.

    `priority_queue<int, vector<int>, greater<int>> pq` — cria uma fila de prioridade de inteiros (mín-heap). Complexidade: $O(1)$.

## Funções Úteis

O C++ oferece uma série de funções úteis para realizar operações comuns em programação competitiva. Algumas das mais utilizadas são:

- `min(a, b)` — retorna o menor entre $a$ e $b$. Complexidade: $O(1)$.
- `max(a, b)` — retorna o maior entre $a$ e $b$. Complexidade: $O(1)$.
- `abs(a)` — retorna o valor absoluto de $a$. Complexidade: $O(1)$.
- `swap(a, b)` — troca os valores de $a$ e $b$. Complexidade: $O(1)$.
- `sqrt(a)` — retorna a raiz quadrada de $a$. Complexidade: $O(\log a)$.
- `ceil(a)` — retorna o menor inteiro $\geq a$. Complexidade: $O(1)$.
- `floor(a)` — retorna o maior inteiro $\leq a$. Complexidade: $O(1)$.
- `round(a)` — retorna o inteiro mais próximo de $a$. Complexidade: $O(1)$.
