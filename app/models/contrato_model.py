from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import Boolean, Float
from app.configs.database import db


class ContratoModel(db.Model):

    __tablename__ = "contrato"

    id = Column(Integer, primary_key=True)

    valor = Column(Float, nullable=False)
    duracao_meses = Column(Integer, nullable=False)

    def serializer(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "duracao_meses": self.duracao_meses
        }