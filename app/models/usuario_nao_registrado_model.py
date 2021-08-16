from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import String
from app.configs.database import db


class UsuarioNaoRegistradoModel(db.Model):

    __tablename__ = "usuario_nao_registrado"

    id = Column(Integer, primary_key=True)

    nome = Column(String(150), nullable=False)
    telefone = Column(String(50), unique=True, nullable=False)
    e_comercial = Column(Boolean, default=False)
    cep = Column(String(8))
    rua = Column(String(150))
    numero = Column(Integer)
    complemento = Column(String(255))
    bairro = Column(String(150))
    cidade = Column(String(150))
    estado = Column(String(150))


    def serializer(self):
        return {
            "nome": self.nome,
            "telefone": self.telefone,
            "e_comercial": self.e_comercial,
            "cep": self.cep,
            "rua": self.rua,
            "numero": self.numero,
            "complemento": self.complemento,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado
        }