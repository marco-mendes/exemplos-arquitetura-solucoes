from flask import Blueprint, jsonify

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, World!')

@api_blueprint.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify(message=f'Hello, {name}!')

@api_blueprint.route('/api/sum/<int:num1>/<int:num2>', methods=['GET'])
def sum_numbers(num1, num2):
    result = num1 + num2
    return jsonify(result=result)