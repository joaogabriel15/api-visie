from api_visie.database import db


class Pessoa(db.Model):
    id_pessoa = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(80), nullable=False)
    rg = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date(), nullable=False)
    data_admissao = db.Column(db.Date(), nullable=False)
    funcao = db.Column(db.String(100), nullable=True)
