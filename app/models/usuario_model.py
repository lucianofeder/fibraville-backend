from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date, DateTime, String
from app.configs.database import db
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from datetime import datetime


class UsuarioModel(db.Model):

    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)

    nome = Column(String(150), nullable=False)
    sobrenome = Column(String(150), nullable=False)
    password_hash = Column(String(511), nullable=False)
    email = Column(String(150), nullable=False)
    data_nascimento = Column(Date)
    data_regristro = Column(DateTime, default=datetime.now())
    e_pessoa_fisica = Column(Boolean, default=True)
    cpf = Column(String(11))
    cnpj = Column(String(14))
    mae_nome = Column(String(150))
    pai_nome = Column(String(150))
    observacao = Column(String(511))
    bloqueado = Column(Boolean, default=False)
    ultimo_login = Column(DateTime)
    salt = Column(String(16), nullable=False)

    ordens_servicos_list = relationship("OrdemServicoModel", backref="usuario")

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!!")


    @password.setter
    def password(self, password_to_hash) -> None:
        self.salt = secrets.token_hex(8)
        password_to_hash = password_to_hash + self.salt 
        self.password_hash = generate_password_hash(password_to_hash)


    def check_password(self, password_to_compare) -> bool:
        return check_password_hash(self.password_hash + self.salt, password_to_compare)


    def serialize(self):
        data = {
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "email": self.email,
            "data_nascimento": self.data_nascimento,
            "data_registro": self.data_regristro,
            "bloqueado": self.bloqueado,
            "e_pessoa_fisica": self.e_pessoa_fisica,
            "cpf": self.cpf,
            "cnpj": self.cnpj,
            "ultimo_login": self.ultimo_login,
            "mae_nome": self.mae_nome,
            "pai_nome": self.pai_nome,
            "ordens_servico_list": self.ordens_servicos_list
        }

        if len(self.cpf) > 0:
            data.pop('cnpj')
        else:
            data.pop('cpf')
        
        return data
