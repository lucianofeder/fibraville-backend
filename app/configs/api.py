from flask import Flask
from flask_restful import Api


def init_app(app: Flask) -> None:
    api = Api(app)

    from app.models.usuario_model import UsuarioModel
    from app.models.usuario_nao_registrado_model import UsuarioNaoRegistradoModel
    from app.models.usuario_endereco_model import UsuarioEnderecoModel
    from app.models.usuario_permissao_model import UsuarioPermissaoModel
    from app.models.plano_model import PlanoModel
    from app.models.contrato_model import ContratoModel
    from app.models.contrato_usuario_model import ContratoUsuarioModel
    from app.models.produto_model import ProdutoModel
    from app.models.ordem_servico_model import OrdemServicoModel
    from app.models.visita_tecnica_model import VisitaTecnicaModel
    from app.models.fornecedor_model import FornecedorModel
    from app.models.fornecedor_endereco_model import FornecedorEnderecoModel
    from app.models.contas_a_pagar_model import ContasAPagarModel
    
