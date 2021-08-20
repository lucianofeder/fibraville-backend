from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from app.services.helper import BaseServices
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class ProdutoFornecedorModel(db.Model, BaseServices):
    id: int
    produto_id: int
    fornecedor_id: int

    __tablename__ = "produto_fornecedor"

    id = Column(Integer, primary_key=True)

    produto_id = Column(Integer, ForeignKey("produto.id"), nullable=False)
    fornecedor_id = Column(Integer, ForeignKey("fornecedor.id"), nullable=False)

    # def serializer(self):
    #     return {
    #         "id": self.id,
    #         "produto_id": self.produto_id,
    #         "fornecedor_id": self.fornecedor_id
    #     }   