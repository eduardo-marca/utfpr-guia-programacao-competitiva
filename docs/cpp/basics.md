# Básico de C++

C++ é a linguagem de programação mais utilizada em programação competitiva atualmente, seguida de linguagens como Python, Java, o próprio C, entre outras.

Ela tem muitas semelhanças com a linguagem C, mas possui muitos recursos extras.

O objetivo dessa sessão é mostrar como criar um programa básico em C++ e como compilá-lo. Outras páginas mostrarão como usar diversos recursos do C++.

!!! warning
    Esse guia tem como foco mostrar C++ pelo lado de programação competitiva, e não em mostrar os fundamentos de C++, como variáveis, funções e estruturas de controle. Portanto recomenda-se um conhecimento básico de C++ e programão em geral.

Caso queira aprender C++ do zero, recomenda-mos os seguintes recursos:

- [W3Schools](https://www.w3schools.com/cpp/)
- [Geeks For Geeks](https://www.geeksforgeeks.org/cpp/c-plus-plus/)
- [Documentação Oficial](https://cppreference.com/)
- [Outra Documentação Útil](https://cplusplus.com/doc/tutorial/)

## Estrutura Básica de Um Programa
Um programa em de C++ típico para programação competitiva se parece assim
```cpp
#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    return 0;
}
```

Esse programa não realiza nenhuma ação de fato, mas é um molde comum para programas.

A primeira linha `#include <bits/stdc++.h>` insere **todas** as bibliotecas padrões do C++.
!!! note
    Em um projeto real, não seria recomendado o uso de `#include <bits/stdc++.h>`, mas para programação competitiva isso é extremamente útil, pois não exige a inclusão manual de cada biblioteca utilizada.

A segunda linha `#define ll long long` define uma *macro* que permite digitar apenas `ll` em vez de `long long` (a versão com mais capacidade de `int`) de forma mais rápida. É comum se utilizar diversas macros desse tipo em programação competitiva.

A linha `using namespace std;` indica que usaremos o namespace padrão do C++, assim podemos digitar apenas `cin` em vez de `std::cin`, por exemplo. Isso se aplica a todos os recursos da biblioteca padrão *std* do C++.

A função `main` é a função que é chamada quando o programa é executado. Muitos contests exigem que o seu programa retorne o valor 0 quando o programa é finalizado, isso é feito com a instrução `return 0;`.

Por último, a linha `ios::sync_with_stdio(false); cin.tie(nullptr);` permite que leituras e escritas no terminal sejam feitas de forma muito mais rápida. Não é obrigatória, mas útil em problemas com muitas leituras/escritas.

O seu código normalmente vai entre as linhas `ios::sync_with_stdio(false); cin.tie(nullptr);` e `return 0;`, mas pode passar por outras funções e pode inclusive ser finalizado fora da `main` com a instrução `exit(0);`.

## Compilando e Executando um Código em C++
Suponha que você tem um arquivo em C++ `main.cpp`. Para compila-lo basta utilizar o comando `g++ main.cpp -o main`. Isso irá gerar um arquivo executável (no Windows .exe, no Linux aparece sem extensão) com o nome especificado após `-o`.

!!! Tip
    Para compilar um arquivo C++ você deve ter o compilador **g++** instalado. Além disso, algums compiladores não vêm com a biblioteca `bits/stdc++.h` por padrão.

    Para mais informações veja o guia de instalação do g++.

Para executar o programa bastar utilizar o comando `./main` ou `./main.exe` no terminal, utilizando o nome do executável.

## Lendo e Escrevendo no Terminal
Para ler e escrever algum valor no terminal (a forma padrão em problemas de programação competitiva) são utilizados principalmente as instruções do C++ `cin` para leitura e `cout` para escrita. Além disso é comum usar `endl` para imprimir uma quebra de linha, além do caractere `'\n'`.

As variáveis lidas com `cin` devem estar separadas por ">>".

Os valores escritos com `cout` devem estar separados por "<<".

!!! tip
    Também podem ser utilizadas as funções de C `scanf()` para leitura e `printf()` para escrita.

Por exemplo:
```
int A, B;
cin >> A >> B;
cout << "Soma: " << A+B << endl;
```

!!! note
    Perceba que `cin` e `cout` automaticamente reconhecem os tipos utilizados, não sendo necessário especificá-los na hora da leitura/escrita. Além disso ele permite misturar diferentes tipos na mesma linha, usar operadores e até chamadas de funções.
