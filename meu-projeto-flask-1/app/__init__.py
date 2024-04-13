# /meu-projeto-flask/app/__init__.py

# Este arquivo é necessário para tornar o diretório `app` um pacote Python.
# Aqui você pode definir as configurações e inicializações necessárias para a sua aplicação Flask.

from flask import Flask

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Importa os módulos de rotas da API
from app.api import routes

# Configurações adicionais do Flask podem ser definidas aqui

# Inicializa a aplicação Flask
if __name__ == '__main__':
    app.run()