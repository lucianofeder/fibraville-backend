from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime, Float, String
from app.configs.database import db
from datetime import datetime



class ContasAPagarModel(db.Model):

    __tablename__ = "contas_a_pagar"

    id = Column(Integer, primary_key=True)

    valor = Column(Float, nullable=False)
    data_digitado = Column(DateTime, default=datetime.now())
    data_emissao = Column(Date, nullable=False)
    data_a_pagar = Column(Date, nullable=False)
    nfe = Column(String(150))
    n_documento = Column(String(150))
    pago = Column(Boolean, default=False)

    fornecedor_id = Column(Integer, ForeignKey("fornecedor.id"), nullable=False)

    def serializer(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "data_digitado": self.data_digitado,
            "data_emissao": self.data_emissao,
            "data_a_pagar": self.data_a_pagar,
            "nfe": self.nfe,
            "n_documento": self.n_documento,
            "pago": self.pago,
            "fornecedor_id": self.fornecedor_id
        }