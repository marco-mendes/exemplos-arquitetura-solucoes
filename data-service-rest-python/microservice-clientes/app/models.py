class Cliente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }