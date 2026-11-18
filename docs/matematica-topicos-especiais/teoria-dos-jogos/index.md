# Teoria dos jogos

Em programação competitiva, problemas de jogos normalmente descrevem dois jogadores perfeitos, alternando turnos e tentando maximizar resultados opostos. A primeira tarefa é identificar o tipo de jogo: isso decide se uma simples DP de vitória, Nim, Sprague–Grundy ou minimax é a ferramenta certa.

## Roteiro de estudo

1. [Fundamentos e análise de estados](game-theory-basics.md): posições vencedoras e perdedoras, grafos de estados e jogos de retirada.
2. [Jogo de Nim](nim.md): nim-sum, XOR e a estratégia construtiva para vencer.
3. [Números de Grundy](grundy-numbers.md): `mex`, equivalência com Nim e DP em jogos imparciais.
4. [Teorema de Sprague–Grundy](sprague-grundy-theorem.md): como combinar componentes independentes por XOR.
5. [Jogos misère](misere-games.md): o que muda quando fazer a última jogada perde.
6. [Jogos clássicos](other-games.md): Kayles, Chomp, Wythoff e Green Hackenbush.
7. [Jogos de pontuação e minimax](jogos-de-pontuacao.md): quando o objetivo não é apenas fazer a última jogada.

## Antes de aplicar uma técnica

| Pergunta | Consequência |
|---|---|
| Há aleatoriedade ou informação escondida? | A teoria desta seção pode não se aplicar diretamente. |
| Ambos têm exatamente os mesmos movimentos em cada posição? | O jogo é imparcial; Grundy pode ser aplicável. |
| A última jogada vence? | É jogo normal; caso contrário, verifique misère. |
| O estado é a soma de componentes independentes? | Combine Grundy numbers por XOR. |
| O vencedor depende de pontos acumulados? | Modele a diferença de pontuação com minimax/DP. |

!!! tip "Pense no estado, não na história"
    Uma posição deve guardar apenas o que influencia movimentos futuros. Em uma pilha, é a quantidade de pedras; em um jogo de intervalos, são os extremos restantes; em um jogo de componentes, é a coleção de subposições ainda independentes.
