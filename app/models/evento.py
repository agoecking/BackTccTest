from app.extensions import db

class Eventos(db.Model):
    __tablename__ = 'eventos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade_ingresso = db.Column(db.Integer, nullable=False)

    id_organizacao = db.Column(db.Integer, db.ForeignKey('organizacao.id'), nullable=False)