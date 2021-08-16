from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime, Float, String
from app.configs.database import db
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class AtendimentoModel(db.Model):

    __tablename__ = "atendimento"

    id = Column(Integer, primary_key=True)

    data = Column(DateTime, nullable=False)
    descricao = Column(String(511))
    setor = Column(String(50))
    usuario_cpf = Column(String(11))
    usuario_telefone = Column(String(50))

    atendente_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))

    def serializer(self):
        return {
            "id": self.id,
            "data": self.data,
            "descricao": self.descricao,
            "setor": self.setor,
            "usuario_cpf": self.usuario_cpf,
            "usuario_telefone": self.usuario_telefone,
            "atendente_id": self.atendente_id,
            "usuario_id": self.usuario_id
        }