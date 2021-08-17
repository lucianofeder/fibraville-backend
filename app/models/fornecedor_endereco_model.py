from sqlalchemy import Column, Integer, String
from app.services.helper import BaseServices
from app.configs.database import db
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class FornecedorEnderecoModel(db.Model, BaseServices):
    id: int
    cep: str
    rua: str
    numero: str
    bairro: str
    cidade: str
    estado: str
    complemento: str
    referencia: str

    __tablename__ = "fornecedor_endereco"

    id = Column(Integer, primary_key=True)

    cep = Column(String(8), nullable=False)
    rua = Column(String(150), nullable=False)
    numero = Column(String(20))
    bairro = Column(String(150), nullable=False)
    cidade = Column(String(150), nullable=False)
    estado = Column(String(150), nullable=False)
    complemento = Column(String(150))
    referencia = Column(String(150))

    # def serializer(self):
    #     return {
    #         "id": self.id,
    #         "cep": self.cep,
    #         "rua": self.rua,
    #         "numero": self.numero,
    #         "bairro": self.bairro,
    #         "cidade": self.cidade,
    #         "estado": self.estado,
    #         "complemento": self.complemento,
    #         "referencia": self.referencia
    #     }