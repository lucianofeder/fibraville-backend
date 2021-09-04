from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float
from app.services.helper import BaseModel
from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime
# from app.models.usuario_endereco_model import UsuarioEnderecoModel


@dataclass
class ContratoUsuarioModel(db.Model, BaseModel):
    id: int
    data_inicio: datetime
    data_fim: datetime
    valor_contrato: float
    contrato_id: int
    # usuario_id: int
    # usuario_endereco_id: int
    # usuario_endereco: UsuarioEnderecoModel

    __tablename__ = "contrato_usuario"

    id = Column(Integer, primary_key=True)

    data_inicio = Column(DateTime, nullable=False)
    data_fim = Column(DateTime, default=False)
    valor_contrato = Column(Float, nullable=False)

    contrato_id = Column(Integer, ForeignKey("contrato.id"))
   
    # def serializer(self):
    #     return {
    #         "id": self.id,
    #         "usuario_id": self.usuario_id,
    #         "contrato_id": self.contrato_id,
    #         "endereco_id": self.endereco_id,
    #         "data_inicio": self.data_inicio,
    #         "data_fim": self.data_fim
    #     }