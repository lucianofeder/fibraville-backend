from sqlalchemy import Column, Integer, Boolean
from app.services.helper import BaseModel
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class UsuarioPermissaoModel(db.Model, BaseModel):
    id: int
    e_cliente: bool
    e_representante: bool
    e_funcionario: bool
    e_super_usuario: bool


    __tablename__ = "usuario_permissao"

    id = Column(Integer, primary_key=True)

    e_cliente = Column(Boolean, default=True)
    e_representante = Column(Boolean, default=False)
    e_funcionario = Column(Boolean, default=False)
    e_super_usuario = Column(Boolean, default=False)

    def serializer(self):
        return {
            "e_cliente": self.e_cliente,
            "e_representante": self.e_representante,
            "e_funcionario": self.e_funcionario
        }