from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from app.services.helper import BaseModel
from app.configs.database import db
from dataclasses import dataclass
# from app.models.plano_model import PlanoModel


@dataclass
class ContratoModel(db.Model, BaseModel):
    id: int
    valor: float
    duracao_meses: int
    plano_id: int
    # plano: PlanoModel

    __tablename__ = "contrato"

    id = Column(Integer, primary_key=True)

    valor = Column(Float, nullable=False)
    duracao_meses = Column(Integer, nullable=False)

    plano = relationship("PlanoModel", backref=backref("contrato", uselist=False))
    plano_id = Column(Integer, ForeignKey("plano.id"))

    def serializer(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "duracao_meses": self.duracao_meses,
            "plano_id": self.plano_id
        }