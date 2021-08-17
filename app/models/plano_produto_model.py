from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from app.services.helper import BaseServices
from app.configs.database import db
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class PlanoProdutoModel(db.Model, BaseServices):
    id: int
    plano_id: int
    produto_id: int

    __tablename__ = "plano_produto"

    id = Column(Integer, primary_key=True)

    plano_id = Column(Integer, ForeignKey("plano.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produto.id"), nullable=False)

    # def serializer(self):
    #     return {
    #         "id": self.id,
    #         "plano_id": self.plano_id,
    #         "produto_id": self.produto_id
    #     }   