from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from app.services.helper import BaseModel
from app.configs.database import db
from dataclasses import dataclass
# from app.models.fornecedor_endereco_model import FornecedorEnderecoModel
# from app.models.contas_a_pagar_model import ContasAPagarModel


@dataclass
class FornecedorModel(db.Model, BaseModel):
    id: int
    razao_social: str
    nome_fantasia: str
    cnpj: str
    inscricao_estadual: str
    contato: str
    endereco_fornecedor_id: int
    # endereco_fornecedor: FornecedorEnderecoModel
    contas_a_pagar_list: list #list[ContasAPagarModel]

    __tablename__ = "fornecedor"

    id = Column(Integer, primary_key=True)

    razao_social = Column(String(150), nullable=False)
    nome_fantasia = Column(String(150))
    cnpj = Column(String(16), nullable=False, unique=True)
    inscricao_estadual = Column(String(9))
    contato = Column(String(150))

    endereco_fornecedor_id = Column(Integer, ForeignKey("fornecedor_endereco.id"))
    endereco_fornecedor = relationship("FornecedorEnderecoModel", backref=backref("fornecedor", uselist=False))
    
    contas_a_pagar_list = relationship("ContasAPagarModel", backref="fornecedor")

    def serializer(self):
        return {
            "id": self.id,
            "razao_social": self.razao_social,
            "nome_fantasia": self.nome_fantasia,
            "cnpj": self.cnpj,
            "endereco_fornecedor_id": self.endereco_fornecedor_id,
        }