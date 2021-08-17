from sqlalchemy import Column, Integer
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, String
from app.services.helper import BaseServices
from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, order=True)
class AtendimentoModel(db.Model, BaseServices):
    id: int
    data: datetime
    descricao: str
    setor: str
    usuario_cpf: str
    usuario_telefone: str
    atendente_id: int
    usuario_id: int
    ordem_servico_id: int

    __tablename__ = "atendimento"

    id = Column(Integer, primary_key=True)

    data = Column(DateTime, nullable=False)
    descricao = Column(String(511))
    setor = Column(String(50))
    usuario_cpf = Column(String(11))
    usuario_telefone = Column(String(50))

    atendente_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))

    ordem_servico = relationship("OrdemServicoModel", backref=backref('atendimento', uselist=False))
    ordem_servico_id = Column(Integer, ForeignKey("ordem_servico.id"))

    # def serializer(self):
    #     return {
    #         "id": self.id,
    #         "data": self.data,
    #         "descricao": self.descricao,
    #         "setor": self.setor,
    #         "usuario_cpf": self.usuario_cpf,
    #         "usuario_telefone": self.usuario_telefone,
    #         "atendente_id": self.atendente_id,
    #         "usuario_id": self.usuario_id
    #     }