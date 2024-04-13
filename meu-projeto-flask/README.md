# Meu Projeto Flask

Este é um projeto Flask com uma API REST e integração com o serviço do Istio para demonstrar algumas funcionalidades de service proxy.

## Estrutura do Projeto

```
meu-projeto-flask
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── views.py
│   └── models
│       ├── __init__.py
│       └── entities.py
├── tests
│   └── test_app.py
├── istio
│   ├── service.yaml
│   └── virtual-service.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Arquivos do Projeto

- `app/__init__.py`: Este arquivo é necessário para que o diretório `app` seja reconhecido como um pacote Python.

- `app/main.py`: Este arquivo é o ponto de entrada da aplicação Flask. Ele cria uma instância do objeto Flask e configura as rotas e os endpoints da API REST.

- `app/api/__init__.py`: Este arquivo é necessário para que o diretório `api` seja reconhecido como um pacote Python.

- `app/api/routes.py`: Este arquivo define as rotas da API REST. Ele importa as views e associa as funções de view aos endpoints.

- `app/api/views.py`: Este arquivo contém as funções de view da API REST. Cada função de view é responsável por lidar com uma rota específica e retornar a resposta adequada.

- `app/models/__init__.py`: Este arquivo é necessário para que o diretório `models` seja reconhecido como um pacote Python.

- `app/models/entities.py`: Este arquivo contém as definições das entidades do modelo de dados da aplicação.

- `tests/test_app.py`: Este arquivo contém os testes unitários para a aplicação Flask. Ele importa o objeto Flask e testa as rotas e os endpoints da API REST.

- `istio/service.yaml`: Este arquivo é usado para configurar o serviço do Istio. Ele define as configurações de rede, como portas e protocolos.

- `istio/virtual-service.yaml`: Este arquivo é usado para configurar o serviço virtual do Istio. Ele define as regras de roteamento e balanceamento de carga para o serviço.

- `Dockerfile`: Este arquivo é usado para criar uma imagem Docker da aplicação Flask. Ele especifica as dependências, o diretório de trabalho e os comandos para executar a aplicação.

- `requirements.txt`: Este arquivo lista as dependências do projeto. Ele é usado pelo gerenciador de pacotes do Python para instalar as dependências necessárias.

- `README.md`: Este arquivo contém a documentação do projeto. Ele fornece informações sobre como configurar e executar a aplicação Flask, bem como detalhes sobre as funcionalidades do serviço do Istio.