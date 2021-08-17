from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship
from app.services.helper import BaseServices
from dataclasses import dataclass
# from app.models.fornecedor_model import FornecedorModel
# from app.models.plano_model import PlanoModel


@dataclass(frozen=True, order=True)
class ProdutoModel(BaseServices):
    id: int
    modelo: str
    marca: str
    valor: float
    numero_serie: str
    estoque: float
    velocidade: float
    planos_list: list #list[PlanoModel]
    fornecedores_list: list #list[FornecedorModel]

    __tablename__ = "produto"

    id = Column(Integer, primary_key=True)

    modelo = Column(String(150), nullable=False)
    marca = Column(String(150), nullable=False)
    valor = Column(Float, nullable=False)
    numero_serie = Column(String(150), nullable=False)
    estoque = Column(Float, default=0)
    velocidade = Column(Float, default=False)

    planos_list = relationship("PlanoModel", secondary="plano_produto", backref="produtos_list")
    fornecedores_list = relationship("FornecedorModel", secondary="produto_fornecedor", backref="produtos_list")

    # def serializer(self):
    #     return {
    #         "id": self.id,
    #         "modelo": self.modelo,
    #         "marca": self.marca,
    #         "valor": self.valor,
    #         "numero_serie": self.numero_serie,
    #         "estoque": self.estoque,
    #         "velocidade": self.velocidade,
    #         "fornecedores_list": self.fornecedores_list,
    #         "planos_list": self.planos_list
    #     }