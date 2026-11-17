
{% set exercises %}
  recommended:
    - name: Factory Machines
      url: https://cses.fi/problemset/task/1620
      platform: CSES
      difficulty: medium
      topics: [busca binária na resposta, monotonicidade]
      objective: Encontre o menor tempo necessário para produzir uma quantidade desejada de produtos.
    - name: Array Division
      url: https://cses.fi/problemset/task/1085
      platform: CSES
      difficulty: medium
      topics: [busca binária na resposta, guloso]
      objective: Divida um vetor em até K subarrays minimizando a maior soma entre eles.
  additional:
    - name: Maximum Median
      url: https://codeforces.com/problemset/problem/1201/C
      platform: Codeforces
      difficulty: medium
      topics: [busca binária na resposta, mediana]
      objective: Maximize a mediana de um vetor com um orçamento limitado de incrementos.
    - name: Aggressive Cows
      url: https://www.spoj.com/problems/AGGRCOW/
      platform: SPOJ
      difficulty: medium
      topics: [busca binária na resposta, maior valor viável]
      objective: Maximize a menor distância entre vacas posicionadas em estábulos.
{% endset %}

# Busca Binária na Resposta

## 1. Introdução

A busca binária é conhecida por encontrar elementos em vetores ordenados em tempo $O(\log N)$.

Entretanto, ela possui uma aplicação muito mais geral: encontrar o menor ou maior valor que satisfaz determinada condição.

Essa técnica é conhecida como **Busca Binária na Resposta** (*Binary Search on Answer*).

Considere um problema de otimização:

> Qual é o menor tempo necessário para produzir uma determinada quantidade de produtos?

Uma abordagem seria calcular diretamente esse tempo. Porém, em muitos problemas, isso é difícil.

Em contrapartida, pode ser muito mais simples responder:

> É possível produzir a quantidade desejada em até `X` unidades de tempo?

Se conseguimos responder essa pergunta eficientemente, podemos utilizar busca binária para encontrar o menor valor possível de `X`.

A ideia central é transformar um **problema de otimização** em um **problema de decisão**.

## 2. A propriedade fundamental: monotonicidade

A busca binária funciona quando existe uma propriedade monotônica.

Por exemplo, imagine uma função booleana `possible(x)` que indica se conseguimos realizar uma tarefa dentro de um limite de tempo `x`.

Se a tarefa pode ser realizada em `10` minutos, também pode ser realizada em `11`, `12`, `13` minutos e assim por diante.

Portanto, os resultados possíveis seguem o padrão:

```text
Tempo:      0  1  2  3  4  5  6  7  8  9 10 11 12 13
possible:   F  F  F  F  F  F  F  F  F  V  V  V  V  V
                                      ^
                                Primeira resposta válida
```

Queremos encontrar a primeira posição em que `possible(x)` retorna verdadeiro.

Matematicamente, procuramos:

$$
\min\{x \mid possible(x)=\text{true}\}
$$

!!! important "Condição necessária"
    Para procurar o menor valor válido, precisamos garantir que, se `possible(x)` é verdadeiro, então `possible(y)` também será verdadeiro para todo `y > x` dentro do domínio.

    Sem essa propriedade, a busca binária pode descartar regiões que contêm a resposta correta.

<!-- AUXÍLIO VISUAL 1

Criar uma imagem SVG com uma reta numérica horizontal.

- Região falsa à esquerda, em vermelho.
- Região verdadeira à direita, em verde.
- Uma seta indicando a primeira posição verdadeira.
- Destacar que a busca binária procura a fronteira.

Arquivo:
../../assets/images/tecnicas/busca-binaria-na-resposta/fronteira.svg

![Fronteira entre valores inviáveis e viáveis](../../assets/images/tecnicas/busca-binaria-na-resposta/fronteira.svg)
-->

## 3. Problema exemplo: Factory Machines

Vamos utilizar como exemplo o problema
[Factory Machines — CSES](https://cses.fi/problemset/task/1620/).

Temos `N` máquinas, e a máquina `i` precisa de `t[i]` unidades de tempo para produzir um produto.

Todas as máquinas trabalham simultaneamente e podem produzir quantos produtos forem necessários, um de cada vez.

Nosso objetivo é produzir pelo menos `T` produtos no menor tempo possível.

### Exemplo

Considere três máquinas:

| Máquina | Tempo por produto |
|---|---:|
| A | 2 |
| B | 3 |
| C | 7 |

Queremos produzir pelo menos `8` produtos.

Quanto tempo precisamos esperar?

### 3.1. Transformando em um problema de decisão

Em vez de calcular diretamente o menor tempo, vamos verificar se determinado tempo `X` é suficiente.

Uma máquina que produz um produto a cada `t[i]` unidades de tempo consegue produzir:

$$
\left\lfloor \frac{X}{t[i]} \right\rfloor
$$

produtos em `X` unidades de tempo.

Como todas trabalham simultaneamente, a produção total é:

$$
P(X)=\sum_{i=1}^{N}
\left\lfloor \frac{X}{t[i]} \right\rfloor
$$

Portanto:

$$
possible(X) =
\begin{cases}
\text{true}, & P(X)\ge T\\
\text{false}, & P(X)<T
\end{cases}
$$

### 3.2. Verificando X = 8

Em oito unidades de tempo:

| Máquina | Produtos |
|---|---:|
| A | $\lfloor 8/2 \rfloor=4$ |
| B | $\lfloor 8/3 \rfloor=2$ |
| C | $\lfloor 8/7 \rfloor=1$ |
| **Total** | **7** |

Como precisamos de oito produtos, esse tempo não é suficiente.

Logo:

```text
possible(8) = false
```

### 3.3. Verificando X = 9

Em nove unidades de tempo:

| Máquina | Produtos |
|---|---:|
| A | $\lfloor 9/2 \rfloor=4$ |
| B | $\lfloor 9/3 \rfloor=3$ |
| C | $\lfloor 9/7 \rfloor=1$ |
| **Total** | **8** |

Portanto:

```text
possible(9) = true
```

Como a produção não diminui quando aumentamos o tempo, a função `possible(X)` é monotônica.

Assim, podemos utilizar busca binária.

<!-- AUXÍLIO VISUAL 2 — PRIORITÁRIO

Criar uma linha do tempo de 0 até 9.

Mostrar três linhas, uma para cada máquina:

A: produz nos instantes 2, 4, 6, 8
B: produz nos instantes 3, 6, 9
C: produz no instante 7

Destacar os sete produtos concluídos até t=8
e o oitavo produto concluído em t=9.

Arquivo:
../../assets/images/tecnicas/busca-binaria-na-resposta/maquinas-linha-tempo.svg

![Produção simultânea das máquinas](../../assets/images/tecnicas/busca-binaria-na-resposta/maquinas-linha-tempo.svg)
-->

## 4. Aplicando a busca binária

Precisamos definir um intervalo inicial que contenha a resposta.

### 4.1. Limite inferior

O menor tempo possível é zero:

```cpp
long long low = 0;
```

Para `T >= 1`, sabemos que esse tempo é insuficiente, mas podemos utilizá-lo como limite inferior da busca.

### 4.2. Limite superior

Mesmo que todas as outras máquinas fiquem paradas, a máquina mais rápida consegue produzir os `T` produtos sozinha.

Se `minTime` é o menor tempo de produção entre as máquinas, então:

$$
high = minTime \cdot T
$$

Esse valor é um limite superior válido, embora nem sempre seja a resposta ótima.

Para nosso exemplo:

$$
high=2\cdot8=16
$$

Portanto, começamos procurando no intervalo:

$$
[0,16]
$$

### 4.3. Simulação passo a passo

Em cada iteração, calculamos:

$$
mid=low+\left\lfloor\frac{high-low}{2}\right\rfloor
$$

Se `possible(mid)` for verdadeiro, sabemos que a resposta é menor ou igual a `mid`.

Caso contrário, a resposta deve ser maior que `mid`.

| Iteração | low | high | mid | P(mid) | Possível? | Novo intervalo |
|---|---:|---:|---:|---:|---|---|
| 1 | 0 | 16 | 8 | 7 | Não | [9, 16] |
| 2 | 9 | 16 | 12 | 11 | Sim | [9, 12] |
| 3 | 9 | 12 | 10 | 9 | Sim | [9, 10] |
| 4 | 9 | 10 | 9 | 8 | Sim | [9, 9] |

Quando `low == high`, encontramos a resposta.

Resultado:

```text
9
```

Observe que não precisamos testar todos os valores de tempo.

A cada iteração, eliminamos aproximadamente metade dos candidatos.

<!-- AUXÍLIO VISUAL 3 — PRIORITÁRIO

Criar um diagrama com quatro retas numéricas,
uma para cada iteração.

Representar:
[0,16] -> [9,16] -> [9,12] -> [9,10] -> [9,9]

Destacar:
- O ponto médio testado.
- O resultado da função possible.
- A região descartada.
- A região restante.

Arquivo:
../../assets/images/tecnicas/busca-binaria-na-resposta/iteracoes.svg

![Iterações da busca binária na resposta](../../assets/images/tecnicas/busca-binaria-na-resposta/iteracoes.svg)
-->

## 5. Implementação completa em C++17

A solução utiliza `long long`, pois os tempos podem ser grandes.

```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    ll target;
    cin >> n >> target;

    vector<ll> t(n);

    for (int i = 0; i < n; i++) {
        cin >> t[i];
    }

    auto possible = [&](ll time) -> bool {
        ll produced = 0;

        for (ll x : t) {
            ll count = time / x;

            // Evita overflow na soma.
            if (count >= target - produced) {
                return true;
            }

            produced += count;
        }

        return false;
    };

    ll fastest = *min_element(t.begin(), t.end());

    ll low = 0;
    ll high = fastest * target;

    while (low < high) {
        ll mid = low + (high - low) / 2;

        if (possible(mid)) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }

    cout << low << '\n';

    return 0;
}
```

### Entrada de exemplo

```text
3 8
2 3 7
```

### Saída

```text
9
```

!!! warning "Overflow"
    É importante evitar somar a produção de todas as máquinas sem verificar se o resultado ultrapassará o limite do tipo inteiro.

    Como só precisamos saber se a produção atingiu `target`, podemos interromper a verificação assim que isso acontecer.

    O limite superior `fastest * target` também precisa caber em `long long`. Isso é garantido pelas restrições do problema Factory Machines, mas deve ser verificado ao adaptar a solução para outros problemas.

## 6. Por que a solução está correta?

Podemos demonstrar a correção utilizando a monotonicidade da função `possible`.

### Lema 1: a função possible é monotônica

Para qualquer máquina `i`, a quantidade produzida até o tempo `X` é:

$$
\left\lfloor\frac{X}{t[i]}\right\rfloor
$$

Essa quantidade nunca diminui quando aumentamos `X`.

Consequentemente, a soma das produções também nunca diminui.

Portanto, se `possible(X)` é verdadeiro, então `possible(Y)` também é verdadeiro para qualquer `Y >= X`.

### Lema 2: a resposta ótima permanece no intervalo de busca

Seja `OPT` o menor tempo suficiente.

Inicialmente:

$$
0\le OPT\le high
$$

Em cada iteração:

- Se `possible(mid)` é verdadeiro, então `OPT <= mid`. Podemos atualizar `high = mid`.
- Se `possible(mid)` é falso, então `OPT > mid`. Podemos atualizar `low = mid + 1`.

Assim, a resposta ótima nunca é descartada.

### Teorema: o algoritmo retorna o menor tempo suficiente

O intervalo diminui a cada iteração e sempre contém `OPT`.

Como trabalhamos com um intervalo finito de inteiros, eventualmente teremos:

$$
low=high
$$

Nesse momento, o intervalo contém apenas um candidato.

Como `OPT` permanece dentro dele, necessariamente:

$$
low=high=OPT
$$

Portanto, o algoritmo retorna a resposta ótima.

## 7. Análise de complexidade

Sejam:

- `N`: número de máquinas.
- `U`: limite superior inicial da resposta.

### Complexidade da verificação

A função `possible(X)` percorre no máximo as `N` máquinas.

Portanto:

$$
O(N)
$$

### Complexidade da busca binária

A busca binária reduz aproximadamente pela metade o intervalo de candidatos em cada iteração.

O número de iterações é:

$$
O(\log(U+1))
$$

Como realizamos uma verificação a cada iteração, a complexidade total é:

$$
\boxed{O(N\log(U+1))}
$$

### Complexidade espacial

O vetor de tempos utiliza:

$$
O(N)
$$

As demais variáveis ocupam espaço constante.

Logo, a complexidade espacial total é:

$$
\boxed{O(N)}
$$

O espaço auxiliar, desconsiderando o vetor de entrada, é $O(1)$.

## 8. Dois padrões importantes

Existem duas formas particularmente comuns de busca binária na resposta.

### 8.1. Encontrar o menor valor viável

Nesse padrão, a função possui a forma:

```text
F F F F F V V V V V
          ^
        Resposta
```

O objetivo é encontrar o primeiro `true`.

Template:

```cpp
while (low < high) {
    long long mid = low + (high - low) / 2;

    if (possible(mid)) {
        high = mid;
    } else {
        low = mid + 1;
    }
}
```

Esse padrão aparece em problemas como:

- Menor tempo necessário.
- Menor capacidade suficiente.
- Menor custo que atende a uma condição.

### 8.2. Encontrar o maior valor viável

Nesse caso, a função possui a forma:

```text
V V V V V F F F F F
        ^
      Resposta
```

O objetivo é encontrar o último `true`.

Template para uma busca com pelo menos um candidato viável:

```cpp
while (low < high) {
    long long mid = low + (high - low + 1) / 2;

    if (possible(mid)) {
        low = mid;
    } else {
        high = mid - 1;
    }
}
```

Note o arredondamento para cima no cálculo de `mid`.

Isso evita que a busca fique presa quando restarem apenas dois candidatos.

Esse padrão aparece em problemas como:

- Maior distância mínima entre objetos.
- Maior tamanho possível de segmentos.
- Maior valor que respeita um limite de recursos.

!!! tip "Escolhendo o template"
    Antes de implementar, determine se a condição é do tipo `false → true` ou `true → false`.

    Também verifique se existe pelo menos um candidato válido no intervalo inicial.

    Esses detalhes ajudam a evitar erros de limites e laços infinitos.

## 9. Como reconhecer problemas de busca binária na resposta?

Uma boa estratégia é fazer três perguntas.

### 1. O problema pede um valor mínimo ou máximo?

Expressões como "menor tempo", "maior distância" ou "capacidade mínima" são pistas importantes.

Porém, não garantem que a técnica seja aplicável.

### 2. É mais fácil verificar uma resposta do que calculá-la diretamente?

Em Factory Machines, calcular diretamente o tempo mínimo é difícil.

Mas verificar se determinado tempo é suficiente exige apenas uma soma.

### 3. A condição de viabilidade é monotônica?

Essa é a pergunta mais importante.

Se um tempo é suficiente, qualquer tempo maior também será.

Portanto, podemos procurar a fronteira entre valores inviáveis e viáveis.

Se a condição não for monotônica, a busca binária convencional não será adequada.

## 10. Erros comuns

### 1. Não demonstrar a monotonicidade

Não basta criar uma função `possible`.

É necessário justificar por que sua resposta segue um dos padrões monotônicos.

### 2. Escolher limites incorretos

O intervalo inicial deve conter a resposta ótima.

Um limite superior muito pequeno pode excluir a solução correta.

### 3. Utilizar o template errado

A busca pelo primeiro `true` não utiliza exatamente as mesmas atualizações da busca pelo último `true`.

### 4. Não considerar overflow

Problemas de otimização frequentemente envolvem valores grandes.

Utilize `long long` quando necessário e evite somas ou multiplicações que possam ultrapassar seus limites.

### 5. Confundir complexidade em N com complexidade no valor da resposta

Em Factory Machines, a busca binária não é realizada sobre os índices das máquinas.

Ela é realizada sobre os possíveis tempos.

Portanto, a complexidade depende de $\log U$, e não necessariamente de $\log N$.

## Problemas

{{ exercise_list(exercises) }}

## 11. Desafio adicional

Considere o problema Array Division.

Dado um vetor de inteiros positivos, queremos dividi-lo em exatamente `K` subarrays não vazios, minimizando a maior soma.

Tente responder:

1. Qual é o menor valor possível para a maior soma?
2. Qual é um limite superior válido?
3. Como verificar, em $O(N)$, se uma maior soma `X` é suficiente?
4. Por que a verificação é monotônica?

**Dica:** para um limite `X`, percorra o vetor formando segmentos e inicie um novo segmento sempre que adicionar o próximo elemento ultrapassaria `X`.

Se todos os elementos forem positivos e `K <= N`, conseguir uma divisão com no máximo `K` segmentos é suficiente: podemos subdividir segmentos até obter exatamente `K`, sem aumentar suas somas.

## 12. Resumo

A busca binária na resposta é uma técnica para resolver problemas de otimização por meio de verificações de viabilidade.

Seu funcionamento depende de três elementos fundamentais:

- Um espaço ordenado de respostas candidatas.
- Uma função de decisão eficiente.
- Uma propriedade monotônica que permita descartar metade dos candidatos.

Quando essas condições são satisfeitas, podemos transformar problemas que parecem difíceis em soluções eficientes, frequentemente com complexidade $O(N\log U)$.

A principal habilidade não é memorizar o código da busca binária, mas aprender a formular corretamente a função de viabilidade.
