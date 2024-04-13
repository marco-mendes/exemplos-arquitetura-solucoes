# Calculadora de Quatro Operações

Este é um projeto Node.js com TypeScript que implementa uma calculadora de quatro operações básicas: adição, subtração, multiplicação e divisão.

## Estrutura do Projeto

```
meu-projeto-calculadora
├── .github
|   └── workflows
|       └── principal.yml
├── src
|   ├── calculadora.ts
|   ├── operacoes
|       ├── adicao.ts
|       ├── subtracao.ts
|       ├── multiplicacao.ts
|       └── divisao.ts
|   └── index.ts
├── testes
|   └── calculadora.teste.ts
├── package.json
├── tsconfig.json
└── README.md
```

## Arquivos

- `src/calculadora.ts`: Este arquivo contém a implementação da classe `Calculadora`, que possui métodos para realizar as quatro operações matemáticas básicas.

- `src/operacoes/adicao.ts`: Este arquivo contém a implementação da função `adicionar`, que realiza a operação de adição.

- `src/operacoes/subtracao.ts`: Este arquivo contém a implementação da função `subtrair`, que realiza a operação de subtração.

- `src/operacoes/multiplicacao.ts`: Este arquivo contém a implementação da função `multiplicar`, que realiza a operação de multiplicação.

- `src/operacoes/divisao.ts`: Este arquivo contém a implementação da função `dividir`, que realiza a operação de divisão.

- `src/index.ts`: Este arquivo é o ponto de entrada da aplicação. Ele cria uma instância da classe `Calculadora` e realiza algumas operações de exemplo.

- `testes/calculadora.teste.ts`: Este arquivo contém os testes unitários para a classe `Calculadora` e as funções de operações.

- `.github/workflows/principal.yml`: Este arquivo contém o fluxo de trabalho do GitHub Actions para executar os testes automatizados sempre que houver um push ou pull request no repositório.

- `package.json`: Este arquivo é o arquivo de configuração do npm. Ele lista as dependências e scripts do projeto.

- `tsconfig.json`: Este arquivo é o arquivo de configuração do TypeScript. Ele especifica as opções do compilador e os arquivos a serem incluídos na compilação.

## Executando o Projeto

1. Certifique-se de ter o Node.js instalado em sua máquina.

2. Clone este repositório.

3. Navegue até o diretório raiz do projeto.

4. Execute o comando `npm install` para instalar as dependências.

5. Execute o comando `npm start` para iniciar a aplicação.

## Executando os Testes

1. Certifique-se de ter o Node.js instalado em sua máquina.

2. Clone este repositório.

3. Navegue até o diretório raiz do projeto.

4. Execute o comando `npm install` para instalar as dependências.

5. Execute o comando `npm test` para executar os testes.

## Contribuindo

Se você quiser contribuir para este projeto, fique à vontade para abrir uma issue ou enviar um pull request. Será um prazer receber sua colaboração!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).