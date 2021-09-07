from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date, DateTime, Float
from app.services.helper import BaseModel
from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class ContasAReceberModel(db.Model, BaseModel):
    id: int
    valor: float
    data_a_pagar: date
    data_pago: datetime
    usuario_id: int

    __tablename__ = "contas_a_receber"

    id = Column(Integer, primary_key=True)

    valor = Column(Float, nullable=False)
    data_a_pagar = Column(Date, nullable=False)
    data_pago = Column(DateTime, default=None)

    usuario_id = Column(Integer, ForeignKey("usuario.id"))

    def serializer(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "data_a_pagar": self.data_a_pagar,
            "data_pago": self.data_pago,
            "usuario_id": self.usuario_id
        }