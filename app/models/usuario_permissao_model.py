from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import Boolean
from app.configs.database import db


class UsuarioPermissaoModel(db.Model):

    __tablename__ = "usuario_permissao"

    id = Column(Integer, primary_key=True)

    e_cliente = Column(Boolean, default=True)
    e_representante = Column(Boolean, default=False)
    e_funcionario = Column(Boolean, default=False)

    def serializer(self):
        return {
            "e_cliente": self.e_cliente,
            "e_representante": self.e_representante,
            "e_funcionario": self.e_funcionario
        }