from database import db


class Pessoa(db.Model):
    id_pessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column()
