
# Dois Ponteiros e Janela Deslizante

**Dificuldade:** Iniciante / Intermediário  
**Pré-requisitos:** Vetores, laços e estruturas associativas  
**Categoria:** Técnicas de algoritmos

## 1. Introdução

Em programação competitiva, muitos problemas envolvem encontrar ou contar segmentos contínuos de um vetor ou de uma string.

Esses segmentos são chamados de **subarrays** (em vetores) ou **substrings** (em strings).

Por exemplo, considere o vetor:

```text
A = [1, 2, 3, 4, 5]
```

Alguns subarrays possíveis são:

```text
[1, 2]
[2, 3, 4]
[3]
[1, 2, 3, 4, 5]
```

Já `[1, 3, 5]` não é um subarray, porque seus elementos não são consecutivos no vetor original.

Um vetor de tamanho `N` possui:

\[
\frac{N(N+1)}{2}
\]

subarrays não vazios.

Portanto, enumerar todos eles exige pelo menos \(O(N^2)\) operações.

Para valores grandes de `N`, essa abordagem pode ser inviável.

A técnica de **janela deslizante (sliding window)** permite resolver certos problemas de intervalos contínuos em tempo linear, mantendo apenas as informações necessárias sobre um intervalo atual.

## 2. A ideia dos dois ponteiros

A técnica de dois ponteiros consiste em utilizar dois índices para percorrer uma sequência.

Dependendo do problema, eles podem:

- Começar nas extremidades opostas de um vetor.
- Avançar na mesma direção.
- Representar os limites de um intervalo contínuo.

Neste capítulo, estudaremos principalmente a terceira situação.

Representaremos a janela atual por:

\[
[L,R]
\]

onde `L` e `R` são os índices inicial e final do intervalo, ambos inclusivos.

```text
Índice:  0   1   2   3   4   5   6
Vetor:  [4,  2,  7,  1,  3,  5,  2]
                 L           R

Janela: [7, 1, 3, 5]
```

O objetivo é movimentar os ponteiros de maneira controlada, aproveitando as informações calculadas para a janela anterior.

<!-- AUXÍLIO VISUAL 1
Tipo: Diagrama SVG de um vetor.

Mostrar os índices, os valores e dois ponteiros L e R.
Destacar os elementos dentro da janela.

Arquivo sugerido:
../../assets/images/tecnicas/janela-deslizante/estrutura-janela.svg

Substituir este comentário pelo Markdown abaixo quando
a imagem estiver disponível:

![Representação de uma janela deslizante](../../assets/images/tecnicas/janela-deslizante/estrutura-janela.svg)
-->

## 3. Quando podemos utilizar uma janela deslizante?

A ideia central é manter uma **janela válida**, ou seja, um intervalo que satisfaz alguma condição do problema.

Em muitos problemas de maximização, podemos:

1. Expandir a janela movendo `R`.
2. Verificar se a condição continua satisfeita.
3. Caso contrário, mover `L` até recuperar a validade.
4. Atualizar a melhor resposta encontrada.

Um aspecto importante é que **os dois ponteiros nunca precisam retroceder**.

Entretanto, isso não funciona para qualquer propriedade.

Para utilizar essa estratégia, precisamos que o comportamento da condição permita descartar definitivamente posições à esquerda.

Por exemplo:

- Para encontrar o maior intervalo sem elementos repetidos, remover elementos da esquerda não cria novas repetições.
- Para limitar a soma de um intervalo de números não negativos, remover elementos da esquerda não aumenta a soma.
- Para encontrar uma soma específica em um vetor que contém números negativos, a mesma estratégia pode falhar, pois aumentar ou diminuir o intervalo não provoca necessariamente uma mudança previsível na soma.

!!! warning "Atenção"
    Não basta que um problema envolva subarrays para que a janela deslizante funcione.

    Antes de utilizar a técnica, devemos justificar por que os ponteiros podem avançar sem perder uma resposta ótima.

## 4. Problema exemplo: maior subarray sem repetições

Considere o seguinte problema:

> Dado um vetor de `N` inteiros, encontre o comprimento do maior subarray no qual todos os elementos são distintos.

Por exemplo:

```text
N = 8

A = [1, 2, 1, 3, 2, 7, 4, 2]
```

O maior subarray sem elementos repetidos é:

```text
[1, 3, 2, 7, 4]
```

Portanto, a resposta é:

```text
5
```

### 4.1. Solução ingênua

Uma abordagem seria considerar todos os índices iniciais `L` e expandir `R` enquanto não encontramos elementos repetidos.

Podemos usar um `set` para identificar duplicatas.

Para cada início `L`, criamos um novo conjunto e tentamos adicionar sucessivamente os valores `A[R]`.

Como podemos percorrer até `N` elementos para cada início, a abordagem tem complexidade \(O(N^2 \log N)\) usando `set`.

O problema é que descartamos todo o trabalho anterior ao mudar o início do intervalo.

Por exemplo, se já sabemos que `[1, 3, 2, 7]` não possui repetições, não precisamos verificar novamente todo esse intervalo ao tentar acrescentar o próximo elemento.

É exatamente essa informação que a janela deslizante aproveita.

### 4.2. Solução utilizando janela deslizante

Vamos manter uma janela `[L, R]` que nunca possui elementos repetidos.

Também guardaremos a última posição em que cada valor apareceu.

Quando adicionamos `A[R]`, podem ocorrer duas situações:

**Caso 1: o elemento não aparece na janela atual.**

A janela continua válida e podemos atualizar a resposta.

**Caso 2: o elemento já aparece na janela atual.**

Suponha que sua ocorrência anterior esteja no índice `p`.

Precisamos mover o início da janela até `p + 1`, eliminando a ocorrência anterior.

Assim:

\[
L = \max(L,p+1)
\]

O máximo é necessário porque a última ocorrência global de um elemento pode estar fora da janela atual.

Depois de ajustar `L`, atualizamos a última ocorrência de `A[R]` para `R`.

O comprimento da janela é:

\[
R-L+1
\]

## 5. Exemplo passo a passo

Vamos executar o algoritmo no vetor:

```text
A = [1, 2, 1, 3, 2, 7, 4, 2]
```

Inicialmente:

```text
L = 0
Resposta = 0
```

O ponteiro `R` percorre o vetor da esquerda para a direita.

| R | A[R] | Novo L | Janela válida | Maior comprimento |
|---:|---:|---:|---|---:|
| 0 | 1 | 0 | [1] | 1 |
| 1 | 2 | 0 | [1, 2] | 2 |
| 2 | 1 | 1 | [2, 1] | 2 |
| 3 | 3 | 1 | [2, 1, 3] | 3 |
| 4 | 2 | 2 | [1, 3, 2] | 3 |
| 5 | 7 | 2 | [1, 3, 2, 7] | 4 |
| 6 | 4 | 2 | [1, 3, 2, 7, 4] | 5 |
| 7 | 2 | 5 | [7, 4, 2] | 5 |

Observe o que acontece nas posições `R = 2`, `R = 4` e `R = 7`.

Essas são as situações em que encontramos elementos repetidos e precisamos mover o ponteiro `L`.

### Exemplo: processando R = 4

Antes de processar o elemento, temos:

```text
Índice:   0   1   2   3   4   5   6   7
Vetor:   [1,  2,  1,  3,  2,  7,  4,  2]
              L           R

Janela anterior: [2, 1, 3]
```

O elemento `2` já aparece na posição `1`.

Como queremos manter apenas elementos distintos, devemos mover `L` para `2`.

A nova janela será:

```text
Índice:   0   1   2   3   4   5   6   7
Vetor:   [1,  2,  1,  3,  2,  7,  4,  2]
                  L       R

Nova janela: [1, 3, 2]
```

Agora todos os elementos são distintos novamente.

### Exemplo: processando R = 7

Antes de processar o último elemento:

```text
Índice:   0   1   2   3   4   5   6   7
Vetor:   [1,  2,  1,  3,  2,  7,  4,  2]
                  L                   R
```

A ocorrência anterior do valor `2` está no índice `4`.

Logo:

\[
L = \max(2,4+1)=5
\]

A janela torna-se:

```text
[7, 4, 2]
```

Embora a janela tenha diminuído, não precisamos voltar a examinar os elementos anteriores.

A maior resposta encontrada continua sendo `5`.

<!-- AUXÍLIO VISUAL 2 — PRIORITÁRIO
Tipo: GIF animado ou sequência de 8 diagramas.

Utilizar exatamente o vetor:
[1, 2, 1, 3, 2, 7, 4, 2]

Cada quadro deve mostrar:
- A posição dos ponteiros L e R.
- O intervalo válido destacado.
- A última ocorrência do valor atual.
- O maior comprimento encontrado.
- Uma indicação visual quando L avança.

Sugestão de cores:
Azul: janela válida.
Laranja: elemento sendo processado.
Vermelho: ocorrência anterior de um elemento repetido.

Arquivo sugerido:
../../assets/images/tecnicas/janela-deslizante/execucao.gif

![Execução da janela deslizante](../../assets/images/tecnicas/janela-deslizante/execucao.gif)
-->

## 6. Implementação em C++17

A implementação utiliza um `unordered_map` para armazenar a última posição de cada elemento.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    unordered_map<int, int> last;

    int l = 0;
    int answer = 0;

    for (int r = 0; r < n; r++) {
        int x = a[r];

        // Se x já apareceu, podemos precisar
        // mover o início da janela.
        if (last.count(x)) {
            l = max(l, last[x] + 1);
        }

        // Atualiza a última ocorrência.
        last[x] = r;

        // A janela [l, r] não possui repetições.
        answer = max(answer, r - l + 1);
    }

    cout << answer << '\n';

    return 0;
}
```

### Entrada

```text
8
1 2 1 3 2 7 4 2
```

### Saída

```text
5
```

### Por que utilizar max ao atualizar L?

Considere o vetor:

```text
[2, 1, 1, 2]
```

Quando processamos o último elemento, a janela válida já começa na posição `2`.

A ocorrência anterior do valor `2` está na posição `0`.

Sem utilizar `max`, poderíamos atualizar:

```cpp
l = last[x] + 1;
```

Isso faria `L` voltar para `1`.

Considere também o vetor:

```text
[1, 2, 3, 1, 2, 4, 1]
```

Quando chegamos ao último `1`, precisamos garantir que `L` nunca retroceda, mesmo que a última ocorrência armazenada de algum valor esteja fora da janela atual.

A regra geral é:

```cpp
l = max(l, last[x] + 1);
```

Ela preserva a propriedade fundamental de que o ponteiro esquerdo nunca se move para trás.

## 7. Por que o algoritmo funciona?

A correção depende de dois invariantes.

### Invariante 1: a janela atual não possui elementos repetidos

Antes de adicionar `A[R]`, a janela anterior é válida.

Se `A[R]` não aparece nessa janela, podemos adicioná-lo diretamente.

Caso contrário, basta mover `L` para uma posição imediatamente após a ocorrência anterior.

Nenhum outro elemento se torna repetido ao remover elementos da esquerda.

Portanto, após cada iteração, `[L, R]` permanece válido.

### Invariante 2: L é o menor índice inicial válido para o R atual

Se a ocorrência anterior de `A[R]` está dentro da janela, qualquer início anterior ou igual àquela ocorrência produziria uma repetição.

Por isso, precisamos avançar `L`.

Se não existe repetição dentro da janela, não precisamos movê-lo.

Consequentemente, para cada posição `R`, encontramos o maior subarray válido que termina exatamente em `R`.

Como todas as posições finais são consideradas, o maior comprimento encontrado é a resposta ótima global.

## 8. Análise de complexidade

### Complexidade temporal

O ponteiro `R` percorre as `N` posições do vetor exatamente uma vez.

Já o ponteiro `L` apenas avança e nunca retrocede.

Na implementação com `unordered_map`, cada consulta ou atualização possui custo esperado amortizado \(O(1)\).

Logo, a complexidade temporal esperada é:

\[
\boxed{O(N)}
\]

!!! note "Complexidade do unordered_map"
    Embora o custo esperado das operações seja constante, um `unordered_map` pode apresentar desempenho ruim em situações patológicas com muitas colisões.

    Para obter uma garantia determinística, podemos substituir `unordered_map` por `map`, resultando em \(O(N\log N)\).

### Complexidade espacial

O vetor de entrada ocupa \(O(N)\).

O mapa pode armazenar até `N` valores distintos, consumindo \(O(N)\) memória adicional.

Portanto:

\[
\boxed{O(N)}
\]

O número de variáveis auxiliares, excluindo vetor e mapa, é constante.

## 9. Outro padrão: janela com soma limitada

Nem todos os problemas de janela deslizante envolvem elementos repetidos.

Considere agora:

> Dado um vetor de inteiros positivos e um limite `K`, encontre o comprimento do maior subarray cuja soma seja menor ou igual a `K`.

Por exemplo:

```text
A = [2, 1, 3, 2, 4]
K = 6
```

Uma resposta ótima é:

```text
[2, 1, 3]
```

com comprimento `3` e soma `6`.

Podemos manter a soma da janela atual.

A cada novo elemento:

1. Adicionamos `A[R]` à soma.
2. Enquanto a soma for maior que `K`, removemos `A[L]` e avançamos `L`.
3. Atualizamos a resposta.

### Implementação

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;

    cin >> n >> k;

    vector<long long> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int l = 0;
    int answer = 0;
    long long sum = 0;

    for (int r = 0; r < n; r++) {
        sum += a[r];

        while (sum > k) {
            sum -= a[l];
            l++;
        }

        answer = max(answer, r - l + 1);
    }

    cout << answer << '\n';

    return 0;
}
```

Essa solução também utiliza \(O(N)\) tempo e \(O(N)\) espaço total, sendo \(O(1)\) de espaço auxiliar além do vetor.

### Por que funciona?

Como todos os elementos são positivos, remover elementos da esquerda sempre reduz a soma.

Além disso, acrescentar elementos à direita nunca diminui a soma.

Portanto, se uma janela ultrapassa `K`, mover o ponteiro esquerdo é uma maneira segura de recuperar uma janela válida.

!!! warning "E se existirem números negativos?"
    Com números negativos, remover o primeiro elemento pode aumentar a soma.

    Por exemplo, considere o vetor `[-5, 10, 1]` com `K = 6`.

    A janela completa possui soma `6` e comprimento `3`.

    Entretanto, uma implementação que remove elementos imediatamente ao ultrapassar o limite depois de processar `[-5, 10]` perderia essa solução.

    Assim, o algoritmo apresentado não funciona diretamente para vetores com números negativos.

<!-- AUXÍLIO VISUAL 3
Tipo: Diagrama de evolução da soma.

Representar o vetor:
[2, 1, 3, 2, 4]

Mostrar como a soma varia com o movimento
dos ponteiros e quando ultrapassa K = 6.

Sugestão: uma linha do tempo com os valores
de L, R e sum após cada ajuste.

Arquivo:
../../assets/images/tecnicas/janela-deslizante/soma-limitada.svg

![Evolução da soma na janela](../../assets/images/tecnicas/janela-deslizante/soma-limitada.svg)
-->

## 10. Janela fixa e janela variável

Existem duas versões comuns da técnica.

### Janela de tamanho fixo

Utilizada quando todos os intervalos considerados possuem exatamente `K` elementos.

Um exemplo é encontrar a maior soma entre todos os subarrays de tamanho `K`.

Podemos calcular a primeira soma e, para cada deslocamento, remover o elemento que saiu e adicionar o novo elemento.

```cpp
long long sum = 0;

for (int i = 0; i < k; i++) {
    sum += a[i];
}

long long answer = sum;

for (int r = k; r < n; r++) {
    sum += a[r];
    sum -= a[r - k];

    answer = max(answer, sum);
}
```

Considere \(1 \leq K \leq N\).

A complexidade é \(O(N)\).

### Janela de tamanho variável

Utilizada quando precisamos encontrar intervalos que satisfazem alguma propriedade, mas não sabemos seus tamanhos antecipadamente.

O formato mais comum é:

```cpp
int l = 0;

for (int r = 0; r < n; r++) {
    // Adicionar a[r] à janela

    while (/* janela inválida */) {
        // Remover a[l] da janela
        l++;
    }

    // Atualizar a resposta
}
```

O aspecto mais importante é definir corretamente:

- O que torna uma janela válida.
- Como adicionar um elemento.
- Como remover um elemento.
- Em qual momento atualizar a resposta.

<!-- AUXÍLIO VISUAL 4
Tipo: Comparação lado a lado.

Painel esquerdo:
Janela de tamanho fixo deslocando-se pelo vetor.

Painel direito:
Janela de tamanho variável expandindo e contraindo.

Arquivo:
../../assets/images/tecnicas/janela-deslizante/fixa-vs-variavel.svg

![Janela fixa versus variável](../../assets/images/tecnicas/janela-deslizante/fixa-vs-variavel.svg)
-->

## 11. Exercícios sugeridos

### 1. [Playlist — CSES](https://cses.fi/problemset/task/1141/)

**Dificuldade sugerida:** Fácil / Intermediário

Encontre a maior sequência contínua de músicas sem repetições.

**Objetivo:** aplicar diretamente a técnica de última ocorrência apresentada no capítulo.

### 2. [Books — Codeforces 279B](https://codeforces.com/problemset/problem/279/B)

**Dificuldade sugerida:** Intermediário

Dado o tempo necessário para ler cada livro, encontre o maior número de livros consecutivos que podem ser lidos dentro de um limite de tempo.

**Objetivo:** praticar a janela de soma limitada.

### 3. [Subarray Sums I — CSES](https://cses.fi/problemset/task/1660/)

**Dificuldade sugerida:** Intermediário

Dado um vetor de inteiros positivos, conte quantos subarrays possuem soma exatamente igual a `X`.

**Objetivo:** adaptar a janela deslizante para contagem.

!!! tip "Dica para Subarray Sums I"
    A restrição de que todos os elementos são positivos é importante.

    Ela permite ajustar os limites da janela com base na comparação entre a soma atual e o valor desejado.

    Cuidado para não confundir esse problema com versões que permitem valores negativos.

## 12. Erros comuns

### 1. Esquecer que o intervalo deve ser contínuo

Uma janela representa um subarray ou substring, não uma subsequência arbitrária.

### 2. Mover L para trás

Em muitos problemas de dois ponteiros, a eficiência depende de os ponteiros avançarem monotonamente.

Mover `L` para trás pode tanto invalidar a lógica quanto destruir a complexidade linear.

### 3. Atualizar a resposta antes de corrigir a janela

Quando buscamos o maior intervalo válido, devemos atualizar a resposta somente depois de garantir que a janela atual satisfaz a condição.

### 4. Utilizar int para somas grandes

Mesmo que os elementos individuais caibam em um `int`, sua soma pode ultrapassar esse limite.

Prefira `long long` quando necessário.

### 5. Aplicar a técnica sem verificar as propriedades do problema

A janela deslizante não é uma solução universal para problemas de subarrays.

É necessário justificar por que podemos avançar os ponteiros sem perder soluções importantes.

## 13. Resumo

A técnica de dois ponteiros permite explorar propriedades de uma sequência utilizando índices que avançam de maneira controlada.

A janela deslizante é uma aplicação importante dessa ideia.

Seus principais conceitos são:

- Representar um intervalo contínuo por dois ponteiros.
- Manter informações incrementais sobre a janela.
- Expandir e, quando necessário, contrair o intervalo.
- Explorar propriedades que permitem evitar revisitar estados.
- Reduzir problemas que seriam quadráticos para soluções lineares, quando as condições permitirem.

Dominar essa técnica é fundamental para resolver problemas envolvendo subarrays, substrings, somas, restrições e otimizações em sequências.
