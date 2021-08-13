from sqlalchemy import Column, Integer
from sqlalchemy.sql.elements import collate
from sqlalchemy.sql.expression import nullslast
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float, String
from app.configs.database import db
from datetime import datetime



class OrdemServicoModel(db.Model):

    __tablename__ = "ordem_servico"

    id = Column(Integer, primary_key=True)

    data_abertura = Column(DateTime, default=datetime.now())
    data_fechamento = Column(DateTime)
    valor = Column(Float, nullable=False)
    proposito = Column(String)
    descricao = Column(String)

    def serializer(self):
        return {
            "id": self.id,
            "data_abertura": self.data_abertura,
            "data_fechamento": self.data_fechamento,
            "valor": self.valor,
            "proposito": self.proposito,
            "descricao": self.descricao
        }