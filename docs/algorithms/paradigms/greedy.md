# Algoritmos Gulosos (Greedy Algorithms)

Algoritmos Gulosos são uma classe de algoritmos que seguem a abordagem de fazer a escolha localmente ótima em cada etapa, com a esperança de que essas escolhas levem a uma solução globalmente ótima.

A solução é construída passo a passo, escolhendo a melhor opção disponível em cada etapa, sem reconsiderar as escolhas feitas anteriormente, ou seja, uma escolha nunca é desfeita. Isso costuma tornar esses algoritmos mais simples e rápidos do que outras abordagens.

Eles são frequentemente usados para resolver problemas de otimização e são conhecidos por sua simplicidade e eficiência, mas costumam ser limitados a problemas específicos e geralmente mais simples, já que nem sempre uma estratégia gulosa leva a uma solução ótima.

Este tipo de problema também costuma envolver algum valor para se maximixar ou minimizar, e costuma envolver um sort no meio do caminho.

## Características dos Algoritmos Gulosos

- **Escolha Localmente Ótima**: Em cada etapa, o algoritmo faz a escolha que parece ser a melhor no momento.

- **Sem Reconsideração**: Uma vez que uma escolha é feita, ela não é desfeita. O algoritmo não revisita decisões anteriores.

- **Eficiência**: Algoritmos gulosos geralmente têm complexidade de tempo menor do que outras abordagens, como programação dinâmica ou backtracking.

## Exemplos

### Problema da Moeda

Considere que você possua moedas de diferentes valores e deseja fazer um determinado valor com o menor número de moedas possível. Você pode utilizar qualquer quantidade de qualquer moeda.

Por exemplo, suponha que você tenha o seguinte conjunto de moedas:

$$ M = {50, 20, 10, 5, 1} $$

E você deseja formar o valor $N = 67$.

Um algoritmo guloso escolheria sempre a moeda de maior valor que não exceda o valor restante a ser formado. Portando, uma solução possível seria:

$$ 50 + 10 + 5 + 1 + 1 $$

### Aprendendo Algoritmos

Steph tem $X$ minutos de férias para aprender algoritmos. São $N$ algoritmos, e cada um leva um certo tempo para aprender. Quantos algoritmos ela consegue aprender no, no máximo, dentro do tempo disponível?

$$ X = 15 $$

$$ tempos = {4, 3, 8, 4, 7, 3} $$

Você poderia tentar algumas estratégias para escolher os algoritmos a aprender:

- Na ordem que vieram: $4 + 3 + 8 = 15$ (3 algoritmos)
- Os mais demorados primeiro: $8 + 7 = 15$ (2 algoritmos)
- Os mais rápidos primeiro: $3 + 3 + 4 + 4 = 14$ (4 algoritmos)

A estratégia gulosa de escolher os algoritmos mais rápidos primeiro permite que Steph aprenda o maior número possível de algoritmos dentro do tempo disponível. Isso acontece porque cada algoritmo tem o mesmo "peso", ou seja, cada um conta como uma unidade de aprendizado, e escolher os mais rápidos primeiro maximiza o número total de algoritmos aprendidos.

```cpp
vll a(n);                           // tempo de cada algoritmo   
sort(a.begin(), a.end());           // a chave da ordenação
int usado = 0, cnt = 0;
for (int i = 0; i < n; i++) {
    if (usado + a[i] > X) break;    // não cabe: para
    usado += a[i];
    cnt++;
}
cout << cnt << endl;
```

### Problema do Agendamento

Vão ocorrer $N$ eventos, cada um com início e fim. Você só assiste um evento por vez - e se for assitir, assiste **inteiro**. Trocar de sala é instantâneo. Qual o máximo de eventos que dá para assistir?

![](images/exemplo3_1.drawio.svg#center)

Algumas estratégias possíveis são:

- Escolher o evento que começa antes primeiro

![](images/exemplo3_2.drawio.svg#center)

Resulta em *WA*.

- Escolher o evento mais curto primeiro

![](images/exemplo3_3.drawio.svg#center)

Resulta em *WA* e é mais difícil de implementar.

- Escolher o evento que termina antes primeiro

![](images/exemplo3_4.drawio.svg#center)

Resulta em *AC* e é a estratégia correta. A prova de que essa estratégia funciona é um pouco mais complexa, mas a ideia é que, ao escolher o evento que termina mais cedo, você deixa mais espaço para os próximos eventos, aumentando a chance de assistir a mais eventos no total.

```cpp
int n;                            // número de eventos
cin >> n;
vector<pair<int,int>> ev(n);      // {fim, inicio}
sort(ev.begin(), ev.end());       // o sort ordena pelo fim  
int fimAtual = -1, ans = 0;

for (int i = 0; i < n; i++) {
    int fim = ev[i].first, ini = ev[i].second;
    if (ini >= fimAtual) { fimAtual = fim; ans++; }  // cabe? pega
}
cout << ans << endl;;
```

## Exemplos que não funcionam com Algoritmos Gulosos

### Problema da Moeda

A estratégia que vimos para o problema da Moeda funciona para alguns conjuntos de moedas, mas não para todos. Por exemplo, se você tivesse moedas de valores $M = {4, 3, 1}$ e quisesse formar o valor $N = 6$, a estratégia gulosa levaria a uma solução subótima.

A solução ótima seria:

$$ 3 + 3 $$

Mas a estratégia guloso escolheria:

$$ 4 + 1 + 1 $$

No caso mais geral desse problema, uma técnica de [Programação Dinâmica](dynamic-programming.md) é necessária para encontrar a solução ótima.

### Problema da Mochila (Knapsack Problem)

Você tem uma mochila com capacidade $W$ e tem $N$ itens. Cada item tem um peso $w_i$ e um valor $v_i$. O objetivo é maximizar o valor total dos itens na mochila sem exceder a capacidade.

Por exemplo, $W = 4$, $N = 4$, e os itens são:

- Item 1: peso = 3, valor = 14
- Item 2: peso = 2, valor = 10
- Item 3: peso = 2, valor = 10
- Item 4: peso = 1, valor = 4

Algumas estratégias gulosas podem ser tentadas, como escolher os itens com maior valor primeiro ou os itens com menor peso primeiro. No entanto, essas estratégias não garantem uma solução ótima para o problema da mochila.

Novamente, uma abordagem de [Programação Dinâmica](dynamic-programming.md) é necessária para resolver o problema da mochila de forma ótima.

## Prova por AC

Muitas vezes, é extremamente difícil provar que uma estratégia gulosa leva a uma solução ótima. No entanto, se você conseguir implementar a estratégia e ela passar em todos os casos de teste, e possívelmente em outros casos de teste, você pode ter confiança de que a estratégia é correta.

Isso é conhecido como "prova por AC" (Accepted), onde a aceitação do código em todos os casos de teste serve como uma forma de validação da estratégia gulosa.

!!! warning "Aviso"
    Um WA pode custar caro na hora da prova, e como a prova por AC não é uma prova formal, é sempre bom tentar entender o porquê de uma estratégia gulosa funcionar ou não para um determinado problema.

## Problemas

### Recomendados

1. [1D Eraser](https://codeforces.com/contest/1873/problem/D)
2. [Two Arrays And Swaps](https://codeforces.com/contest/1353/problem/B)
3. [Dragons](https://codeforces.com/contest/230/problem/A)
4. [Kanade's Perfect Multiples](https://codeforces.com/problemset/problem/2173/C)
5. [Game on Array](https://codeforces.com/problemset/problem/2147/D)

### Adicionais

1. [Ticket Hoarding](https://codeforces.com/contest/1951/problem/C)
2. [XOR-factorization](https://codeforces.com/problemset/problem/2180/C)
3. [Path and Subsequence](https://atcoder.jp/contests/arc150/tasks/arc150_c)
4. [Stay or Mirror](https://codeforces.com/contest/2129/problem/B)

### Resolvidos

- [Fractional Knapsack](https://www.geeksforgeeks.org/dsa/fractional-knapsack-problem/)
- [Overlapping Intervals](https://www.geeksforgeeks.org/dsa/merging-intervals/)

## Outros Recursos

- [GeeksforGeeks](https://www.geeksforgeeks.org/dsa/greedy-algorithms/)
- [W3Schools](https://www.w3schools.com/dsa/dsa_ref_greedy.php)
- [USACO Guide](https://usaco.guide/bronze/intro-greedy?lang=cpp)
- [Codeforces](https://codeforces.com/blog/entry/150612)
