from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import nullslast
from sqlalchemy.sql.sqltypes import Boolean, Float, String
from app.configs.database import db


class ProdutoModel(db.Model):

    __tablename__ = "produto"

    id = Column(Integer, primary_key=True)

    modelo = Column(String(150), nullable=False)
    marca = Column(String(150), nullable=False)
    valor = Column(Float, nullable=False)
    numero_serie = Column(String(150), nullable=False)
    estoque = Column(Float, default=0)
    velocidade = Column(Float, default=False)

    planos_list = relationship("FornecedorModel", secondary="plano_produto", backref="produtos_list")
    fornecedores_list = relationship("FornecedorModel", secondary="produto_fornecedor", backref="produtos_list")

    def serializer(self):
        return {
            "id": self.id,
            "modelo": self.modelo,
            "marca": self.marca,
            "valor": self.valor,
            "numero_serie": self.numero_serie,
            "estoque": self.estoque,
            "velocidade": self.velocidade,
            "fornecedores_list": self.fornecedores_list,
            "planos_list": self.planos_list
        }