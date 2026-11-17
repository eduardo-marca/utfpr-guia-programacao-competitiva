# Referência em PDF

O PDF oficial é gerado separadamente do site. Ele usa a página única do plugin
`print-site`, o navegador Chrome para a paginação e regras de impressão próprias.
Assim, a versão de competição pode ser compacta sem sacrificar a leitura no site.

## Gerar o arquivo

Após instalar as dependências, execute na raiz do repositório:

```bash
python scripts/build_pdf.py
```

O resultado fica em `output/pdf/guia-programacao-competitiva-utfpr.pdf`. Esse
diretório é ignorado pelo Git para que cada organização publique apenas a revisão
que aprovou. A exportação aceita ajustes sem editar o código:

```bash
# Uma folha horizontal, útil quando há muito código ou tabelas largas.
python scripts/build_pdf.py --orientation landscape

# Gerar uma versão mais simples, sem capa, em outro caminho.
python scripts/build_pdf.py --no-cover --margin-mm 8 --output distribuicao/guia.pdf
```

Use `python scripts/build_pdf.py --help` para todos os parâmetros. O comando
requer Google Chrome ou Chromium instalado no computador.

## Escolher o conteúdo impresso

As diretivas são comentários HTML, então não aparecem como texto no site. Elas
podem envolver parágrafos, listas, avisos, figuras ou blocos de código. Não use
as diretivas dentro de um bloco de código delimitado por crases.

```markdown
<!-- pdf:exclude:start -->
Este roteiro detalhado ajuda no site, mas não ocupa espaço no PDF.
<!-- pdf:exclude:end -->

<!-- pdf:only:start -->
Use esta nota curta apenas para quem imprimir a referência.
<!-- pdf:only:end -->

<!-- pdf:page-break -->
```

- `pdf:exclude` deixa o trecho no site e o remove do PDF.
- `pdf:only` mostra o trecho apenas no PDF; ele fica oculto na tela.
- `pdf:page-break` inicia a próxima parte em uma nova página.
- `<!-- pdf:exclude-page -->`, em qualquer linha fora de bloco de código,
  mantém a página no site e retira a página inteira da referência.

Os pares `start` e `end` devem ser fechados na ordem em que foram abertos. O
build falha com uma mensagem apontando o arquivo se uma diretiva estiver sem par.

## Ajustar o visual

As regras compactas ficam em `docs/stylesheets/pdf.css`: tamanho de texto,
margens de blocos de código, quebras e tratamento de tabelas. O cabeçalho/rodapé,
formato de papel, orientação, margens e capa são definidos pelo comando de
exportação. Essa separação permite experimentar a referência impressa sem mudar
o CSS que os leitores veem no site.
