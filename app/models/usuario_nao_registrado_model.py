from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import String
from app.configs.database import db


class UsuarioNaoRegistradoModel(db.Model):

    __tablename__ = "usuario_nao_registrado"

    id = Column(Integer, primary_key=True)

    nome = Column(String(150))
    telefone = Column(String(50), unique=True)

    def serializer(self):
        return {
            "nome": self.nome,
            "telefone": self.telefone
        }