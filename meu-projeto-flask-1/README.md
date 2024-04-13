# Meu Projeto Flask

Este é um projeto Flask com uma API REST e integração com o Istio para demonstrar funcionalidades de service proxy.

## Estrutura do Projeto

```
meu-projeto-flask
├── app
|   ├── __init__.py
|   ├── main.py
|   ├── api
|       ├── __init__.py
|       ├── routes.py
|       └── views.py
|   └── models
|       ├── __init__.py
|       └── entities.py
├── tests
|   └── test_app.py
├── istio
|   ├── service.yaml
|   ├── virtual-service.yaml
|   └── destination-rule.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Descrição do Projeto

Este projeto Flask é uma API REST que permite interagir com entidades do modelo de dados. Ele possui a seguinte estrutura:

- O diretório `app` contém o código principal da aplicação Flask.
- O diretório `app/api` contém as definições das rotas da API e as implementações das funções de visualização.
- O diretório `app/models` contém as definições das entidades do modelo de dados.
- O diretório `tests` contém os testes unitários para a aplicação Flask.
- O diretório `istio` contém os arquivos de configuração do Istio para demonstrar funcionalidades de service proxy.
- O arquivo `Dockerfile` é usado para criar uma imagem Docker da aplicação Flask.
- O arquivo `requirements.txt` contém as dependências do Python necessárias para executar a aplicação.
- O arquivo `README.md` contém a documentação do projeto.

## Configuração e Execução

Para configurar e executar o projeto, siga as etapas abaixo:

1. Certifique-se de ter o Python instalado em sua máquina.
2. Crie um ambiente virtual para isolar as dependências do projeto.
3. Instale as dependências do projeto executando o comando `pip install -r requirements.txt`.
4. Execute o arquivo `app/main.py` para iniciar o servidor Flask.
5. Acesse a API através das rotas definidas em `app/api/routes.py`.
6. Para demonstrar as funcionalidades de service proxy do Istio, aplique os arquivos de configuração presentes no diretório `istio` em um cluster Istio configurado.

## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Basta abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).