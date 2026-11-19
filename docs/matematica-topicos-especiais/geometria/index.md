# Geometria computacional

Geometria em programação competitiva é menos sobre decorar figuras e mais sobre escolher uma representação que transforma relações geométricas em operações robustas. Produtos escalares e vetoriais, orientação, ordenação e precisão numérica resolvem grande parte dos problemas.

## Roteiro de estudo

1. [Fundamentos e precisão](geometry-basics.md): coordenadas, tipos numéricos, EPS e um template reutilizável.
2. [Pontos e vetores](pontos-vetores.md): operações, transformações, rotação e ordenação angular.
3. [Produtos escalar e vetorial](produto-escalar-vetorial.md): ângulos, projeções, orientação e volume.
4. [Distâncias e projeções](distancias.md): ponto-reta, ponto-segmento e métricas alternativas.
5. [Retas, orientação e interseções](orientacao-e-intersecao.md): testes robustos para linhas e segmentos.
6. [Polígonos, áreas e pontos de grade](poligonos-e-areas.md): shoelace, Pick, perímetro e centroide.
7. [Localização de pontos](point-in-polygon.md): ponto em segmento, polígono geral ou convexo.
8. [Convex hull e aplicações](convex-hull.md): monotonic chain, calipers e suporte convexo.
9. [Círculos](geometria-circulos.md): relações, interseções e fórmulas de triângulos.
10. [Sweep line e pares próximos](sweep-line.md): eventos, conjunto ativo e algoritmos $O(n\log n)$.
11. [Geometria espacial](geometria-espacial.md): planos, produto vetorial 3D e volumes.

## Escolhendo a ferramenta

| O enunciado menciona | Ferramenta inicial |
|---|---|
| Lados, esquerda/direita, colinearidade | Produto vetorial e orientação |
| Menor distância ou ponto mais próximo | Distância ao segmento, sweep line ou divide and conquer |
| Área, fronteira ou pontos inteiros | Shoelace, `gcd` e teorema de Pick |
| Região convexa ou extremos | Convex hull e busca em polígono convexo |
| Círculos, raios e tangências | Distâncias entre centros e projeções |
| Coordenada `z`, planos ou volume | Produto vetorial 3D e produto misto |

!!! tip "Use coordenadas inteiras quando puder"
    Se a entrada é inteira e a resposta depende apenas de sinais, como orientação ou interseção, prefira aritmética inteira exata. Use ponto flutuante apenas quando medidas não inteiras forem inevitáveis.
