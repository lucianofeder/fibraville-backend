from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class PlanoProdutoModel(db.Model):

    __tablename__ = "plano_produto"

    id = Column(Integer, primary_key=True)

    plano_id = Column(Integer, ForeignKey("plano.id"))
    produto_id = Column(Integer, ForeignKey("produto.id"))

    def serializer(self):
        return {
            "id": self.id,
            "plano_id": self.plano_id,
            "produto_id": self.produto_id
        }   