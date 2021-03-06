from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date, DateTime, String
from app.services.helper import BaseModel
from app.configs.database import db
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from datetime import datetime
from dataclasses import dataclass
from app.models.usuario_permissao_model import UsuarioPermissaoModel
# from app.models.usuario_endereco_model import UsuarioEnderecoModel
# from app.models.contas_a_receber_model import ContasAReceberModel
# from app.models.ordem_servico_model import OrdemServicoModel
# from app.models.atendimento_model import AtendimentoModel
# from app.models.contrato_model import ContratoModel


@dataclass
class UsuarioModel(db.Model, BaseModel):
    id: int
    nome: str
    sobrenome: str
    email: str
    data_nascimento: datetime
    data_regristro: datetime
    e_pessoa_fisica: bool
    cpf: str
    cnpj: str
    pai_nome: str
    observacao: str
    bloqueado: bool
    ultimo_login: datetime
    usuario_permissao: UsuarioPermissaoModel
    usuario_endereco_list: list #list[UsuarioEnderecoModel]
    contas_list: list #list[ContasAReceberModel]
    # ordens_servicos_list: list #list[OrdemServicoModel]
    atendimentos_recebidos_list: list #list[AtendimentoModel]
    # atendimentos_realizados_list: list #list[AtendimentoModel]


    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)

    nome = Column(String(150), nullable=False)
    sobrenome = Column(String(150), nullable=False)
    password_hash = Column(String(511), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    data_nascimento = Column(Date)
    data_regristro = Column(DateTime(), default=datetime.utcnow())
    e_pessoa_fisica = Column(Boolean, default=True)
    cpf = Column(String(11), unique=True)
    cnpj = Column(String(14), unique=True)
    mae_nome = Column(String(150))
    pai_nome = Column(String(150))
    observacao = Column(String(511))
    bloqueado = Column(Boolean, default=False)
    ultimo_login = Column(String(50))
    salt = Column(String(16), nullable=False)

    usuario_permissao = relationship("UsuarioPermissaoModel", backref=backref("usuario", uselist=False))
    usuario_permissao_id = Column(Integer, ForeignKey("usuario_permissao.id"), nullable=False)

    usuario_endereco_list = relationship("UsuarioEnderecoModel", backref="usuario")
    contas_list = relationship("ContasAReceberModel", backref="usuario")
    ordens_servicos_list = relationship("OrdemServicoModel", backref="usuario")
    atendimentos_recebidos_list = relationship("AtendimentoModel", backref="usuario")
    # atendimentos_realizados_list = relationship("atendimento.atendente_id", backref="atendente")

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!!")


    @password.setter
    def password(self, password_to_hash) -> None:
        self.salt = secrets.token_hex(8)
        password_to_hash = password_to_hash + self.salt 
        self.password_hash = generate_password_hash(password_to_hash)


    def check_password(self, password_to_compare) -> bool:
        return check_password_hash(self.password_hash, password_to_compare + self.salt)


    def serializer(self):
        data = {
            "id": self.id,
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "email": self.email,
            "bloqueado": self.bloqueado,
            "e_pessoa_fisica": self.e_pessoa_fisica,
            "cpf": self.cpf,
            "cnpj": self.cnpj,
            "ultimo_login": self.ultimo_login,
            "usuario_permissao": self.usuario_permissao,
        }

        if len(self.cpf) > 0:
            data.pop('cnpj')
        else:
            data.pop('cpf')
        
        return data
