from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import Float
from sqlalchemy.orm import relationship
from app.services.helper import BaseModel
from app.configs.database import db
from dataclasses import dataclass
# from app.models.produto_model import ProdutoModel


@dataclass
class PlanoModel(db.Model, BaseModel):
    id: int
    valor: float
    velocidade: int
    produtos_list: list #list[ProdutoModel]

    __tablename__ = "plano"

    id = Column(Integer, primary_key=True)

    valor = Column(Float, nullable=False)
    velocidade = Column(Integer)

    produtos_list = relationship("ProdutoModel", secondary="plano_produto", backref="planos_list")

    # def serializer(self):
    #     return {
    #         "id": self.id,
    #         "valor": self.valor,
    #         "velocidade": self.velocidade,
    #         "produtos_list": self.produtos_list
    #     }
