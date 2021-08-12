from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import String
from app.configs.database import db


class UsuarioNaoRegistradoModel(db.Model):

    __tablename__ = "usuario_nao_registrado"

    id = Column(Integer, primary_key=True)

    nome = Column(String(150), nullable=False)
    telefone = Column(String(50), unique=True, nullable=False)

    def serializer(self):
        return {
            "nome": self.nome,
            "telefone": self.telefone
        }