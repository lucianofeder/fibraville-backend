from sqlalchemy import Column, Integer
from sqlalchemy.sql.elements import collate
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float, String
from app.configs.database import db


class FornecedorModel(db.Model):

    __tablename__ = "fornecedor"

    id = Column(Integer, primary_key=True)

    razao_social = Column(String(150), nullable=False)
    nome_fantasia = Column(String(150), nullable=False)
    cnpj = Column(String(16), nullable=False)
    inscricao_estadual = Column(String(9))
    contato = Column(String(150))



    def serializer(self):
        return {
            "id": self.id,
            "razao_social": self.razao_social,
            "nome_fantasia": self.nome_fantasia,
            "cnpj": self.cnpj,
            "inscricao_estadual": self.inscricao_estadual,
            "contato": self.contato
        }