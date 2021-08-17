from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import Float
from sqlalchemy.orm import relationship
from app.services.helper import BaseServices
from app.configs.database import db
from dataclasses import dataclass
# from app.models.produto_model import ProdutoModel


@dataclass(frozen=True, order=True)
class PlanoModel(db.Model, BaseServices):
    id: int
    valor: float
    velocidade: float
    produtos_list: list #list[ProdutoModel]

    __tablename__ = "plano"

    id = Column(Integer, primary_key=True)

    valor = Column(Float, nullable=False)
    velocidade = Column(Float, default=False)

    produtos_list = relationship("ProdutoModel", secondary="plano_produto", backref="planos_list")

    # def serializer(self):
    #     return {
    #         "id": self.id,
    #         "valor": self.valor,
    #         "velocidade": self.velocidade,
    #         "produtos_list": self.produtos_list
    #     }
