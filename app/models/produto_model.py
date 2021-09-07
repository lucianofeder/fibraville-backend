from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship
from app.services.helper import BaseModel
from app.configs.database import db
from dataclasses import dataclass
# from app.models.fornecedor_model import FornecedorModel
# from app.models.plano_model import PlanoModel


@dataclass
class ProdutoModel(db.Model, BaseModel):
    id: int
    modelo: str
    marca: str
    valor: float
    numero_serie: str
    estoque: float
    velocidade: float
    # planos_list: list #list[PlanoModel]
    fornecedores_list: list #list[FornecedorModel]

    __tablename__ = "produto"

    id = Column(Integer, primary_key=True)

    modelo = Column(String(150), nullable=False)
    marca = Column(String(150), nullable=False)
    valor = Column(Float, nullable=False)
    numero_serie = Column(String(150))
    estoque = Column(Float, default=0)
    velocidade = Column(Float, default=None)

    # planos_list = relationship("PlanoModel", secondary="plano_produto", backref="produtos_list")
    fornecedores_list = relationship("FornecedorModel", secondary="produto_fornecedor", backref="produtos_list")

    def serializer(self):
        return {
            "id": self.id,
            "modelo": self.modelo,
            "valor": self.valor,
            "estoque": self.estoque,
            "velocidade": self.velocidade,
        }