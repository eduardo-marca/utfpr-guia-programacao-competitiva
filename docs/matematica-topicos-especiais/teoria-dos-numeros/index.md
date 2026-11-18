# Teoria dos números

Teoria dos números fornece as ferramentas para trabalhar com divisibilidade, fatores, restos e equações inteiras. Em programação competitiva, uma boa solução costuma surgir ao transformar um valor grande em sua fatoração, em um MDC ou em uma congruência menor.

## Roteiro de estudo

1. [Fundamentos e identidades aritméticas](number-theory-basics.md): somas, progressões e o agrupamento por quocientes.
2. [Números primos e crivo](primos-e-crivo.md): primalidade, fator primo mínimo e pré-processamento.
3. [Fatoração e divisores](fatoracao-e-divisores.md): número, soma e produto dos divisores.
4. [MDC e MMC](mdc-mmc.md): algoritmo de Euclides e propriedades de divisibilidade.
5. [Euclides estendido](euclides-estendido.md): identidade de Bézout e coeficientes do MDC.
6. [Totiente de Euler](totiente-euler.md): números coprimos e redução de expoentes.
7. [Equações inteiras e congruências lineares](equacoes-diofantinas.md): quando soluções existem e como descrevê-las.
8. [Critérios de divisibilidade](divisibilidade.md): atalhos e processamento de inteiros muito longos em strings.
9. [Fibonacci e resultados clássicos](fibonacci-e-resultados-classicos.md): identidades, decomposições e triplas pitagóricas.
10. [Aritmética modular](modular-arithmetic.md): operações, exponenciação e teoremas de Fermat e Euler.
11. [Inverso modular](inverso-modular.md): divisão em módulo e pré-cálculos.
12. [Sistemas de congruências e CRT](sistemas-de-congruencias.md): combinação de condições modulares.

!!! tip "Qual ferramenta procurar?"
    Fatorize quando a propriedade depende de divisores; use MDC quando aparecem combinações lineares ou frações reduzidas; use módulo quando só o resto importa. Se houver várias condições sobre restos, a próxima pergunta é se os módulos são compatíveis para aplicar CRT.

## Mapa rápido

| Sinal no enunciado | Ferramenta inicial |
|---|---|
| Divisores, primalidade ou potências de primos | Fatoração prima e crivo |
| Maior tamanho que divide duas quantidades | MDC / Euclides |
| Menor período comum | MMC |
| Equação `ax + by = c` | Euclides estendido |
| Contar números coprimos | Totiente de Euler |
| Resultado pedido módulo `m` | Aritmética modular |
| Diversos restos simultâneos | Sistemas de congruências / CRT |
