from sqlalchemy import Column, Integer
from sqlalchemy.sql.elements import collate
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float, String
from app.configs.database import db


class FornecedorEnderecoModel(db.Model):

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

    def serializer(self):
        return {
            "id": self.id,
            "cep": self.cep,
            "rua": self.rua,
            "numero": self.numero,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado,
            "complemento": self.complemento,
            "referencia": self.referencia
        }