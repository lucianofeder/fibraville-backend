from sqlalchemy import Column, Integer, Date, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from app.configs.database import db
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class ContratoUsuarioModel(db.Model):

    __tablename__ = "contrato_usuario"

    id = Column(Integer, primary_key=True)

    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, default=False)
    valor_contrato = Column(Float, nullable=False)

    contrato_id = Column(Integer, ForeignKey("contrato.id"))
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    usuario_endereco_id = Column(Integer, ForeignKey("usuario_endereco.id"), nullable=False)
    
    usuario_endereco = relationship("UsuarioEnderecoModel", backref=backref("contrato_usuario", uselist=False))

    def serializer(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "contrato_id": self.contrato_id,
            "endereco_id": self.endereco_id,
            "data_inicio": self.data_inicio,
            "data_fim": self.data_fim
        }