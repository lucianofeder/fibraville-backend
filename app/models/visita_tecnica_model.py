from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db


class VisitaTecnicaModel(db.Model):

    __tablename__ = "visita_tecnica"

    id = Column(Integer, primary_key=True)

    data_agendamento = Column(DateTime, nullable=False)
    duracao_estimada = Column(Integer, nullable=False)
    observacao = Column(String)

    ordem_servico_id = Column(Integer, ForeignKey("ordem_servico.id"))

    produtos_list = relationship("ProdutoModel", secondary="visita_tecnica_produto", backref="visitas_tecnicas_list")
    tecnicos_list = relationship("UsuarioModel", secondary="visita_tecnica_tecnico", backref="visitas_tecnicas_list")

    def serializer(self):
        return {
            "id": self.id,
            "data_agendamento": self.data_agendamento,
            "duracao_estimada": self.duracao_estimada,
            "observacao": self.observacao,
            "produtos_list": self.produtos_list,
            "tecnicos_list": self.tecnicos_list,
            "ordem_servico_id": self.ordem_servico_id
        }
