from flask import Blueprint

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/endpoint', methods=['GET'])
def api_endpoint():
    return 'Hello, World! This is an API endpoint.'

@api_bp.route('/api/another-endpoint', methods=['POST'])
def api_another_endpoint():
    return 'This is another API endpoint.'

# Adicione outras rotas da API aqui