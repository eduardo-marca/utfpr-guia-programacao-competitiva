# KMP

O algoritmo KMP (Knuth-Morris-Pratt) é um algoritmo eficiente para encontrar ocorrências de um padrão em uma string. Ele utiliza a informação do próprio padrão para evitar comparações desnecessárias, resultando em uma complexidade de tempo linear $O(n + m)$, onde $n$ é o tamanho da string e $m$ é o tamanho do padrão.

O algoritmo KMP é baseado na construção de uma tabela de prefixos (também conhecida como tabela de falhas) que indica, para cada posição do padrão, o comprimento do maior prefixo que é também um sufixo. Essa tabela permite que o algoritmo "pule" partes da string quando uma correspondência falha, evitando comparações redundantes.

## Implementação

A implementação do algoritmo KMP envolve duas etapas principais: a construção da tabela de prefixos e a busca do padrão na string. A seguir, apresentamos uma implementação básica em C++:

```cpp
// Função para construir a tabela de prefixos (tabela de falhas)
void buildTable(const char* pattern, int m, vector<int>& table) {
    int len = 0; // comprimento do maior prefixo que é também um sufixo
    table[0] = 0; // o primeiro valor da tabela é sempre 0

    int i = 1;
    while (i < m) {
        if (pattern[i] == pattern[len]) {
            len++;
            table[i] = len;
            i++;
        } else {
            if (len != 0) {
                len = table[len - 1];
            } else {
                table[i] = 0;
                i++;
            }
        }
    }
}
// Função para realizar a busca do padrão na string
int search(const char* text, const char* pattern) {
    const int n = strlen(text);
    const int m = strlen(pattern);
    vector<int> table(m);
    buildTable(pattern, m, table);
    int i = 0; // índice para text
    int j = 0; // índice para pattern
    while (i < n) {
        if (pattern[j] == text[i]) {
            i++;
            j++;
        }
        if (j == m) {
            cout << "Padrão encontrado na posição: " << i - j << endl;
            j = table[j - 1];
        } else if (i < n && pattern[j] != text[i]) {
            if (j != 0) {
                j = table[j - 1];
            } else {
                i++;
            }
        }
    }
}
```

## Complexidade

- **Tempo:** $O(n + m)$, onde $n$ é o tamanho da string e $m$ é o tamanho do padrão.
- **Espaço:** $O(m)$ para armazenar a tabela de prefixos.
