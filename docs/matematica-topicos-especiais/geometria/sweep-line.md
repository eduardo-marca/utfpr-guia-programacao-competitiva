{% set exercises %}
  recommended:
    - name: Minimum Euclidean Distance
      url: https://cses.fi/problemset/task/2194
      platform: CSES
      difficulty: hard
      topics: [sweep line, par mais próximo, ordenação]
      objective: Mantenha apenas candidatos geometricamente próximos durante uma varredura.
  additional:
    - name: Line Segment Intersection
      url: https://cses.fi/problemset/task/2190
      platform: CSES
      difficulty: medium
      topics: [segmentos, eventos, orientação]
      objective: Use predicados robustos antes de aplicar técnicas de varredura.
{% endset %}

# Sweep line e pares próximos

Sweep line transforma um problema 2D em uma sequência ordenada de eventos. Uma linha imaginária percorre o plano; a estrutura ativa guarda apenas objetos que ainda podem interagir com eventos futuros.

## 1. Receita da varredura

1. escolha uma direção de varredura, normalmente `x` crescente;
2. crie eventos de entrada, saída e consulta;
3. ordene eventos por coordenada e defina desempates;
4. mantenha uma estrutura ativa ordenada na outra coordenada;
5. prove quais objetos podem ser removidos sem afetar respostas futuras.

O último item é a parte essencial. A estrutura de dados só é correta se a prova mostrar que objetos removidos nunca mais podem ser relevantes.

## 2. Par euclidiano mais próximo

Ordene pontos por `x` e mantenha a melhor distância quadrada `d²`. Ao processar um novo ponto, remova do conjunto ativo pontos com diferença em `x` maior que `d`. Entre os ativos, consulte apenas pontos cujo `y` está em uma faixa de largura `2d`.

Um argumento de empacotamento mostra que há apenas quantidade constante de candidatos relevantes nessa faixa; o algoritmo custa $O(n\log n)$. Na prática, use um `set` ordenado por `(y,x)` e evite calcular raiz: compare sempre distâncias ao quadrado.

O mesmo resultado pode ser obtido por divide and conquer: resolva metade esquerda e direita, depois examine a faixa central ordenada por `y`.

## 3. Interseção de segmentos

Para segmentos gerais, a varredura de Bentley–Ottmann mantém segmentos ordenados pela altura no `x` atual. Eventos de extremidade e cruzamento atualizam a ordem; só vizinhos no conjunto ativo precisam ser testados. Isso encontra `k` interseções em $O((n+k)\log n)$.

É um algoritmo delicado por causa de segmentos verticais, eventos com mesma coordenada, sobreposições colineares e comparadores que dependem do `x` atual. Em problemas que pedem apenas algumas interseções ou possuem limites pequenos, os testes de orientação de [Retas e Interseções](orientacao-e-intersecao.md) costumam ser mais seguros.

## 4. Outros usos

- união de retângulos: eventos de início/fim em `x` e segment tree de cobertura em `y`;
- contar cruzamentos entre segmentos horizontais e verticais: eventos em `x` e Fenwick tree sobre `y` comprimido;
- intervalos temporais: a mesma ideia sem geometria, com entradas, saídas e consultas;
- linha de visada e sobreposições: mantenha a ordem dos objetos ativos.

!!! warning "Comparador mutável em std::set"
    Em C++, não altere a coordenada global usada pelo comparador de um `std::set` enquanto elementos já estiverem no conjunto: isso viola a ordenação interna. Implemente eventos cuidadosamente ou use uma formulação que mantenha uma ordem fixa.

<!-- AUXÍLIO VISUAL 1

Mostrar uma linha vertical varrendo pontos ordenados por x, a faixa ativa do par mais próximo e um conjunto de segmentos cujo par de vizinhos pode cruzar.

Arquivo sugerido: images/sweep-line.svg
-->

## Problemas

{{ exercise_list(exercises) }}
