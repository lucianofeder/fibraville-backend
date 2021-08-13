from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import Date
from app.configs.database import db


class ContratoUsuarioModel(db.Model):

    __tablename__ = "contrato_usuario"

    id = Column(Integer, primary_key=True)

    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, default=False)

    def serializer(self):
        return {
            "id": self.id,
            "data_inicio": self.data_inicio,
            "data_fim": self.data_fim
        }