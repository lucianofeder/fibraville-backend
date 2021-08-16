from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class ContratoModel(db.Model):

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