from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db


class VisitaTecnicaTecnicoModel(db.Model):

    __tablename__ = "visita_tecnica_tecnico"

    id = Column(Integer, primary_key=True)

    tecnico_id = Column(Integer, ForeignKey("usuario.id"))
    visita_tecnica_id = Column(Integer, ForeignKey("visita_tecnica.id"))

    def serializer(self):
        return {
            "id": self.id,
            "tecnico_id": self.usuario_id,
            "visita_tecnica_id": self.visita_tecnica_id,
        }   