from sqlalchemy import Column, Integer
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float, String
from app.services.helper import BaseModel
from app.configs.database import db
from datetime import datetime
from dataclasses import dataclass
# from app.models.visita_tecnica_model import VisitaTecnicaModel


@dataclass
class OrdemServicoModel(db.Model, BaseModel):
    id: int
    data_abertura: datetime
    data_fechamento: datetime
    valor: float
    proposito: str
    descricao: str
    usuario_id: int
    visitas_tecnicas_list: list #list[VisitaTecnicaModel]
    finalizado: bool

    __tablename__ = "ordem_servico"

    id = Column(Integer, primary_key=True)

    data_abertura = Column(DateTime, default=datetime.utcnow())
    data_fechamento = Column(DateTime)
    valor = Column(Float, default=0)
    proposito = Column(String(511))
    descricao = Column(String(511))
    finalizado = Column(Boolean, default=False)

    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)

    visitas_tecnicas_list = relationship("VisitaTecnicaModel", backref=backref("ordem_servico"))

    def serializer(self):
        return {
            "id": self.id,
            "data_abertura": self.data_abertura,
            "data_fechamento": self.data_fechamento,
            "valor": self.valor,
            "visitas_tecnicas_list": self.visitas_tecnicas_list
        }