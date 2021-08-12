from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import Boolean, Float
from app.configs.database import db


class PlanoModel(db.Model):

    __tablename__ = "plano"

    id = Column(Integer, primary_key=True)

    valor = Column(Float, nullable=False)
    velocidade = Column(Float, default=False)

    def serializer(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "velocidade": self.velocidade
        }