from flask import Flask
from flask_restful import Api


def init_app(app: Flask) -> None:
    api = Api(app)

    from app.models.usuario_model import UsuarioModel
    from app.models.produto_model import ProdutoModel
    from app.models.contrato_model import ContratoModel
    from app.models.atendimento_model import AtendimentoModel
    from app.models.ordem_servico_model import OrdemServicoModel
    from app.models.visita_tecnica_model import VisitaTecnicaModel
    from app.models.fornecedor_model import FornecedorModel
    from app.models.contas_a_pagar_model import ContasAPagarModel
    from app.models.contas_a_receber_model import ContasAReceberModel
    from app.models.usuario_endereco_model import UsuarioEnderecoModel
    from app.models.usuario_permissao_model import UsuarioPermissaoModel
    from app.models.plano_produto_model import PlanoProdutoModel
    from app.models.contrato_usuario_model import ContratoUsuarioModel
    from app.models.produto_fornecedor_model import ProdutoFornecedorModel
    from app.models.visita_tecnica_produto_model import VisitaTecnicaProtudoModel
    from app.models.visita_tecnica_tecnico_model import VisitaTecnicaTecnicoModel
    from app.models.fornecedor_endereco_model import FornecedorEnderecoModel

    from app.views.usuario_nao_registrado_view import UsuarioNaoRegistradoResource
    api.add_resource(UsuarioNaoRegistradoResource, "/api/usuario_nao_registrado/", endpoint="USUARIOS_NAOREGISTRADO")

    from app.views.plano_view import PlanoResource, PlanoRetrieveResource
    api.add_resource(PlanoResource, "/api/plano/", endpoint="PLANOS")
    api.add_resource(PlanoRetrieveResource, "/api/plano/<int:plano_id>/", endpoint="PLANO_ID")

    from app.views.usuario_permissao_view import UsuarioPermissaoResource, UsuarioPermissaoRetrieveResource
    api.add_resource(UsuarioPermissaoResource, "/api/usuario_permissa/", endpoint="USUARIOS_PERMISSAO")
    api.add_resource(UsuarioPermissaoRetrieveResource, "/api/usuario_permissao/<int:usuario_id>/", endpoint="USUARIO_PERMISSAO_ID")