from sqlalchemy import Column, Integer, DateTime, String
from app.configs.database import db


class VisitaTecnicaModel(db.Model):

    __tablename__ = "visita_tecnica"

    id = Column(Integer, primary_key=True)

    data_agendamento = Column(DateTime, nullable=False)
    duracao_estimada = Column(Integer, nullable=False)
    observacao = Column(String)

    def serializer(self):
        return {
            "id": self.id,
            "data_agendamento": self.data_agendamento,
            "duracao_estimada": self.duracao_estimada,
            "observacao": self.observacao
        }
