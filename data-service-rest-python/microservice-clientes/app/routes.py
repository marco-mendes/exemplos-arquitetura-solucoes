from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120))
    telefone = db.Column(db.String(20))
    

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email, "telefone": self.telefone}

with app.app_context():
    db.create_all()

@app.route("/clients", methods=["GET"])
def get_clients():
    clients = Client.query.all()
    return jsonify([client.to_dict() for client in clients])

@app.route("/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
    client = Client.query.get(client_id)
    if client:
        return jsonify(client.to_dict())
    else:
        return jsonify({"error": "Client not found"}), 404

@app.route("/clients", methods=["POST"])
def create_client():
    new_client = Client(name=request.json["name"], email=request.json["email"])
    db.session.add(new_client)
    db.session.commit()
    return jsonify(new_client.to_dict()), 201

@app.route("/clients/<int:client_id>", methods=["PUT"])
def update_client(client_id):
    client = Client.query.get(client_id)
    if client:
        client.name = request.json.get("name", client.name)
        client.email = request.json.get("email", client.email)
        db.session.commit()
        return jsonify(client.to_dict())
    else:
        return jsonify({"error": "Client not found"}), 404

@app.route("/clients/<int:client_id>", methods=["DELETE"])
def delete_client(client_id):
    client = Client.query.get(client_id)
    if client:
        db.session.delete(client)
        db.session.commit()
        return jsonify({"message": "Client deleted"})
    else:
        return jsonify({"error": "Client not found"}), 404
    
if __name__ == "__main__":
    app.run(debug=True)   
    
