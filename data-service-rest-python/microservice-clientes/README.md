# Microservice Clientes

Este é um projeto de microsserviço de dados com uma API REST para gerenciar uma tabela de clientes. O microsserviço é desenvolvido em Python e utiliza um banco de dados em memória.

# Arquitetura do Projeto

Cliente HTTP <---> Serviço REST (Microsserviço) <---> Banco de Dados

## Estrutura do Projeto

```
microservice-clientes
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── routes.py
├── tests
│   ├── __init__.py
│   └── test_app.py
├── .env
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

## Arquivos do Projeto

- `app/__init__.py`: Este arquivo é um arquivo vazio que marca o diretório `app` como um pacote Python.

- `app/main.py`: Este arquivo é o ponto de entrada do microsserviço. Ele cria uma instância do aplicativo Flask, configura as rotas e inicia o servidor.

- `app/models.py`: Este arquivo define o modelo de dados para os clientes. Ele pode incluir classes ou estruturas de dados para representar os dados do cliente.

- `app/routes.py`: Este arquivo define as rotas para a API. Ele pode incluir funções ou classes que lidam com as requisições e respostas HTTP para os dados do cliente.

- `tests/__init__.py`: Este arquivo é um arquivo vazio que marca o diretório `tests` como um pacote Python.

- `tests/test_app.py`: Este arquivo contém casos de teste para o microsserviço. Ele pode incluir funções ou classes que testam a funcionalidade das rotas ou modelos.

- `.env`: Este arquivo é usado para armazenar variáveis de ambiente para o microsserviço. Ele pode incluir variáveis como detalhes de conexão com o banco de dados ou chaves de API.

- `.gitignore`: Este arquivo especifica os arquivos e diretórios que devem ser ignorados pelo controle de versão do Git.

- `Dockerfile`: Este arquivo é usado para construir uma imagem Docker para o microsserviço. Ele especifica a imagem base, as dependências e os comandos para executar o microsserviço.

- `requirements.txt`: Este arquivo lista as dependências Python necessárias para o microsserviço. Ele pode incluir bibliotecas como Flask ou SQLAlchemy.

- `README.md`: Este arquivo contém a documentação para o microsserviço. Ele pode incluir instruções sobre como configurar e executar o microsserviço, bem como qualquer informação adicional ou exemplos de uso.

## Executando o Microsserviço

Para executar o microsserviço, siga as etapas abaixo:

1. Certifique-se de ter o Python instalado em sua máquina.

2. Clone este repositório para o seu ambiente local.

3. Navegue até o diretório do projeto:

   ```
   cd microservice-clientes
   ```

4. Crie um ambiente virtual:

   ```
   python -m venv venv
   ```

5. Ative o ambiente virtual:

   - No Windows:

     ```
     venv\Scripts\activate
     ```

   - No macOS e Linux:

     ```
     source venv/bin/activate
     ```

6. Instale as dependências do projeto:

   ```
   pip install -r requirements.txt
   ```

7. Execute o microsserviço:

   ```
   python app/main.py
   ```

8. O microsserviço estará em execução em `http://localhost:5000`. Você pode enviar requisições HTTP para as rotas definidas no arquivo `app/routes.py` para gerenciar os dados dos clientes.

## Testando o Microsserviço

Para executar os testes do microsserviço, siga as etapas abaixo:

1. Certifique-se de ter seguido as etapas de instalação e configuração do ambiente virtual descritas acima.

2. Navegue até o diretório do projeto:

   ```
   cd microservice-clientes
   ```

3. Execute os testes:

   ```
   python -m unittest discover tests
   ```

   Isso executará todos os casos de teste definidos no arquivo `tests/test_app.py` e exibirá os resultados no console.

## Contribuindo

Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request. Será um prazer receber sua contribuição!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).