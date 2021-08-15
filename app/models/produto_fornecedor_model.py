from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db


class ProdutoFornecedorModel(db.Model):

    __tablename__ = "produto_fornecedor"

    id = Column(Integer, primary_key=True)

    produto_id = Column(Integer, ForeignKey("produto.id"))
    fornecedor_id = Column(Integer, ForeignKey("fornecedor.id"))

    def serializer(self):
        return {
            "id": self.id,
            "produto_id": self.produto_id,
            "fornecedor_id": self.fornecedor_id
        }