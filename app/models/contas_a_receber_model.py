from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime, Float, String
from app.configs.database import db
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class ContasAReceberModel(db.Model):

    __tablename__ = "contas_a_receber"

    id = Column(Integer, primary_key=True)

    valor = Column(Float, nullable=False)
    data_a_pagar = Column(Date, nullable=False)
    data_pago = Column(DateTime)
    pago = Column(Boolean, default=False)

    usuario_id = Column(Integer, ForeignKey("usuario.id"))

    def serializer(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "data_a_pagar": self.data_a_pagar,
            "data_pago": self.data_pago,
            "pago": self.pago,
            "usuario_id": self.usuario_id
        }