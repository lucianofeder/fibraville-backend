from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class FornecedorModel(db.Model):

    __tablename__ = "fornecedor"

    id = Column(Integer, primary_key=True)

    razao_social = Column(String(150), nullable=False)
    nome_fantasia = Column(String(150), nullable=False)
    cnpj = Column(String(16), nullable=False)
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
            "inscricao_estadual": self.inscricao_estadual,
            "contato": self.contato,
            "endereco_fornecedor": self.endereco_fornecedor,
            "endereco_fornecedor_id": self.endereco_fornecedor_id,
            "contas_a_pagar_list": self.contas_a_pagar_list
        }