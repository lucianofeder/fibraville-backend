from sqlalchemy import Column, Integer, Float
from sqlalchemy.sql.schema import ForeignKey
from app.services.helper import BaseServices
from app.configs.database import db
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class VisitaTecnicaProtudoModel(db.Model):
    id: int
    produto_id: int
    visita_tecnica_id: int
    quantidade: float

    __tablename__ = "visita_tecnica_produto"

    id = Column(Integer, primary_key=True)

    produto_id = Column(Integer, ForeignKey("produto.id"))
    visita_tecnica_id = Column(Integer, ForeignKey("visita_tecnica.id"))
    quantidade = Column(Float, nullable=False)

    # def serializer(self):
    #     return {
    #         "id": self.id,
    #         "produto_id": self.produto_id,
    #         "visita_tecnica_id": self.visita_tecnica_id,
    #         "quantidade": self.quantidade
    #     }   