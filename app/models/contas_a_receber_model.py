from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime, Float, String
from app.configs.database import db
from datetime import datetime



class ContasAReceberModel(db.Model):

    __tablename__ = "contas_a_receber"

    id = Column(Integer, primary_key=True)

    valor = Column(Float, nullable=False)
    data_a_pagar = Column(Date, nullable=False)
    data_pago = Column(DateTime)
    pago = Column(Boolean, default=False)

    def serializer(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "data_a_pagar": self.data_a_pagar,
            "data_pago": self.data_pago,
            "pago": self.pago
        }