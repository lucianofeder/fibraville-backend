from sqlalchemy import Column, Integer
from sqlalchemy.sql.expression import nullslast
from sqlalchemy.sql.sqltypes import Boolean, Float, String
from app.configs.database import db


class ProdutoModel(db.Model):

    __tablename__ = "produto"

    id = Column(Integer, primary_key=True)

    modelo = Column(String(150), nullable=False)
    marca = Column(String(150), nullable=False)
    valor = Column(Float, nullable=False)
    numero_serie = Column(String(150), nullable=False)
    estoque = Column(Float, default=0)
    velocidade = Column(Float, default=False)

    def serializer(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "velocidade": self.velocidade
        }