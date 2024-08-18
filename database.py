from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import Engine 
from sqlalchemy import event

db = SQLAlchemy()


# Suporte a chave estrangeira no SQLite
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


#  Object-Relational Mapping
class Setores(db.Model):
    __tablename__ = 'setores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)

class Ativos(db.Model):
    __tablename__ = 'ativos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    sigla = db.Column(db.String(10), nullable=False)
    setor_id = db.Column(db.Integer, db.ForeignKey('setores.id'), nullable=False)

    # Relacionamento com a tabela Setores
    setor = db.relationship('Setores', backref=db.backref('ativos', lazy=True))

class usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)

class Precos(db.Model):
    __tablename__ = 'precos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ativo_id = db.Column(db.Integer, db.ForeignKey('ativos.id'), nullable=False)
    data = db.Column(db.Date, nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)

    # Relacionamento com a tabela Ativos
    ativo = db.relationship('Ativos', backref=db.backref('precos', lazy=True))

class Movimentacoes(db.Model):
    __tablename__ = 'movimentacoes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer,  db.ForeignKey('usuarios.id'), nullable=False)
    ativo_id = db.Column(db.Integer,  db.ForeignKey('ativos.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_id = db.Column(db.Integer,  db.ForeignKey('precos.id'), nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)  # unitario
    data = db.Column(db.Date, nullable=False)
    tipo = db.Column(db.String(1), nullable=False)  # C = Compra, V = Venda

    # Relacionamentos
usuario = db.relationship('Usuarios', backref=db.backref('movimentacoes', lazy=True))
ativo = db.relationship('Ativos', backref=db.backref('movimentacoes', lazy=True))
preco = db.relationship('Precos', backref=db.backref('movimentacoes', lazy=True))
