from app.extensions import db
from enum import Enum

class TipoUsuario(Enum):
    CLIENTE = "cliente"
    ORGANIZACAO = "organizacao"

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    tipo_usuario = db.Column(db.Enum(TipoUsuario), nullable=False)


class UsuarioCliente(db.Model):
    __tablename__ = "usuarios_clientes"

    id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), primary_key=True)
    telefone = db.Column(db.String(20))
    acesso_ethereum = db.Column(db.String(255))