from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from app.services.helper import BaseModel
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class VisitaTecnicaTecnicoModel(db.Model, BaseModel):
    id: int
    tecnico_id: int
    visita_tecnica_id: int

    __tablename__ = "visita_tecnica_tecnico"

    id = Column(Integer, primary_key=True)

    tecnico_id = Column(Integer, ForeignKey("usuario.id"))
    visita_tecnica_id = Column(Integer, ForeignKey("visita_tecnica.id"))

    # def serializer(self):
    #     return {
    #         "id": self.id,
    #         "tecnico_id": self.usuario_id,
    #         "visita_tecnica_id": self.visita_tecnica_id,
    #     }   