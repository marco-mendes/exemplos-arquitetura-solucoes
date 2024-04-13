from flask import Blueprint, jsonify

# Cria um blueprint para as views da API
api_blueprint = Blueprint('api', __name__)

# Rota de exemplo
@api_blueprint.route('/api/exemplo', methods=['GET'])
def exemplo():
    return jsonify({'mensagem': 'Exemplo de rota da API'})

# Outra rota de exemplo
@api_blueprint.route('/api/outro-exemplo', methods=['GET'])
def outro_exemplo():
    return jsonify({'mensagem': 'Outro exemplo de rota da API'})