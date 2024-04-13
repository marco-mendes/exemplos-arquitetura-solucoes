from flask import Blueprint

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/endpoint', methods=['GET'])
def endpoint():
    return 'Hello, World!'

@api_bp.route('/api/another_endpoint', methods=['POST'])
def another_endpoint():
    return 'This is another endpoint'

# Adicione mais rotas da API aqui