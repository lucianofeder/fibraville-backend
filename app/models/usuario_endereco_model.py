from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, String
from app.services.helper import BaseServices
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class UsuarioEnderecoModel(BaseServices):
    id: int
    e_comercial: bool
    cep: str
    rua: str
    numero: str
    complemento: str
    bairro: str
    cidade: str
    estado: str
    referencia: str
    contato: str
    wireless_login: str
    wireless_senha: str
    onu_login: str
    onu_senha: str
    usuario_id: int
    contrato_usuario_id: int

    __tablename__ = "usuario_endereco"

    id = Column(Integer, primary_key=True)

    e_comercial = Column(Boolean, default=False)
    cep = Column(String(8), nullable=False)
    rua = Column(String(150))
    numero = Column(Integer)
    complemento = Column(String(255))
    bairro = Column(String(150))
    cidade = Column(String(150))
    estado = Column(String(150))
    referencia = Column(String(150))
    contato = Column(String(150))
    wireless_login = Column(String(150))
    wireless_senha = Column(String(150))
    onu_login = Column(String(150))
    onu_senha = Column(String(150))

    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    contrato_usuario_id = Column(Integer, ForeignKey("contrato_usuario.id"))

    # def serializer(self):
    #     return {
    #         "e_comercial": self.e_comercial,
    #         "cep": self.cep,
    #         "rua": self.rua,
    #         "numero": self.numero,
    #         "complemento": self.complemento,
    #         "bairro": self.bairro,
    #         "cidade": self.cidade,
    #         "estado": self.estado,
    #         "referencia": self.referencia,
    #         "contato": self.contato,
    #         "wireless_login": self.wireless_login,
    #         "wireless_senha": self.wireless_senha,
    #         "onu_login": self.onu_login,
    #         "onu_senha": self.onu_senha
    #     }