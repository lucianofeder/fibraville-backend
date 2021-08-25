from flask import Flask
from flask_restful import Api


def init_app(app: Flask) -> None:
    api = Api(app)

    from app.models.usuario_model import UsuarioModel
    from app.models.visita_tecnica_model import VisitaTecnicaModel
    from app.models.plano_produto_model import PlanoProdutoModel
    from app.models.contrato_usuario_model import ContratoUsuarioModel
    from app.models.produto_fornecedor_model import ProdutoFornecedorModel
    from app.models.visita_tecnica_produto_model import VisitaTecnicaProtudoModel
    from app.models.visita_tecnica_tecnico_model import VisitaTecnicaTecnicoModel
    from app.models.fornecedor_endereco_model import FornecedorEnderecoModel


    from app.views.usuario_nao_registrado_view import UsuarioNaoRegistradoResource
    api.add_resource(UsuarioNaoRegistradoResource, "/api/v1/usuario_nao_registrado/", endpoint="USUARIOS_NAOREGISTRADO")


    from app.views.plano_view import PlanoResource, PlanoRetrieveResource
    api.add_resource(PlanoResource, "/api/v1/plano/", endpoint="PLANOS")
    api.add_resource(PlanoRetrieveResource, "/api/v1/plano/<int:plano_id>/", endpoint="PLANO_ID")


    from app.views.usuario_permissao_view import UsuarioPermissaoResource, UsuarioPermissaoRetrieveResource
    api.add_resource(UsuarioPermissaoResource, "/api/v1/usuario_permissao/", endpoint="USUARIOS_PERMISSAO")
    api.add_resource(UsuarioPermissaoRetrieveResource, "/api/v1/usuario/<int:usuario_id>/usuario_permissao/", endpoint="USUARIO_PERMISSAO_ID")


    from app.views.usuario_endereco_view import UsuarioEnderecoResource, UsuarioEnderecoRetrieveResource, UsuarioEnderecoByUserResource
    api.add_resource(UsuarioEnderecoResource, "/api/v1/usuario_endereco/", endpoint="USUARIOS_ENDERECOS")
    api.add_resource(UsuarioEnderecoRetrieveResource, "/api/v1/usuario_endereco/<int:endereco_id>/", endpoint="USUARIOENDERECO_ID")
    api.add_resource(UsuarioEnderecoByUserResource, "/api/v1/usuario/<int:usuario_id>/usuario_endereco/", endpoint="USUARIO_ID_USUARIOENDERECO")


    from app.views.contas_a_pagar_view import ContasAPagarResource, ContasAPagarRetrieveResource, ContasAPagarPayBillResource,ContasAPagarByFornecedorResource
    api.add_resource(ContasAPagarResource, "/api/v1/contas_a_pagar/", endpoint="CONTAS_A_PAGAR")
    api.add_resource(ContasAPagarPayBillResource, "/api/v1/contas_a_pagar/<int:conta_id>/pay_bill/", endpoint="CONTASAPAGAR_PAYBILL")
    api.add_resource(ContasAPagarRetrieveResource, "/api/v1/contas_a_pagar/<int:conta_id>/", endpoint="CONTASAPAGAR_ID")
    api.add_resource(ContasAPagarByFornecedorResource, "/api/v1/fornecedor/<int:fornecedor_id>/contas_a_pagar/", endpoint="FORNECEDOR_ID_CONTASAPAGAR")


    from app.views.contas_a_receber_view import ContasAReceberResource, ContasAReceberRetrieveResource, ContasAReceberPayBillResource, ContasAReceberByUsuarioResource
    api.add_resource(ContasAReceberResource, "/api/v1/contas_a_receber/", endpoint="CONTAS_A_RECEBER")
    api.add_resource(ContasAReceberPayBillResource, "/api/v1/contas_a_receber/<int:conta_id>/pay_bill/", endpoint="CONTASARECEBER_PAYBILL")
    api.add_resource(ContasAReceberRetrieveResource, "/api/v1/contas_a_receber/<int:conta_id>/", endpoint="CONTASARECEBER_ID")
    api.add_resource(ContasAReceberByUsuarioResource, "/api/v1/usuario/<int:usuario_id>/contas_a_receber/", endpoint="USUARIO_ID_CONTASARECEBER")


    from app.views.contrato_view import ContratoResource, ContratoRetrieveResource
    api.add_resource(ContratoResource, "/api/v1/contrato/", endpoint="CONTRATOS")
    api.add_resource(ContratoRetrieveResource, "/api/v1/contrato/<int:contrato_id>/", endpoint="CONTRATO_ID")


    from app.views.atendimento_view import AtendimentoResource, AtendimentoRetrieveResource, AtendimentoByUsuarioResource
    api.add_resource(AtendimentoResource, "/api/v1/atendimento/", endpoint="ATENDIMENTOS")
    api.add_resource(AtendimentoRetrieveResource, "/api/v1/atendimento/<int:atendimento_id>/", endpoint="ATENDIMENTO_ID")
    api.add_resource(AtendimentoByUsuarioResource, "/api/v1/usuario/<int:usuario_id>/atendimento/", endpoint="USUARIO_ID_ATENDIMENTO")


    from app.views.ordem_servico_view import OrdemServicoResource, OrdemServicoRetrieveResource, OrdemServicoByUsuarioResource
    api.add_resource(OrdemServicoResource, "/api/v1/ordem_servico/", endpoint="ORDENS_SERVICO")
    api.add_resource(OrdemServicoRetrieveResource, "/api/v1/ordem_servico/<int:os_id>/", endpoint="OS_ID")
    api.add_resource(OrdemServicoByUsuarioResource, "/api/v1/usuario/<int:usuario_id>/ordem_servico/", endpoint="USUARIO_ID_OS")


    from app.views.fornecedor_view import FornecedorResource, FornecedorRetrieveResource
    api.add_resource(FornecedorResource, "/api/v1/fornecedor/", endpoint="FORNECEDORES")
    api.add_resource(FornecedorRetrieveResource, "/api/v1/fornecedor/<int:fornecedor_id>/", endpoint="FORNECEDOR_ID")

    
    from app.views.fornecedor_endereco_view import FornecedorEnderecoResource, FornecedorEnderecoRetrieveResource, FornecedorEnderecoByFornecedorResource
    api.add_resource(FornecedorEnderecoResource, "/api/v1/fornecedor/endereco/", endpoint="FORNECEDORES_ENDERECO")
    api.add_resource(FornecedorEnderecoRetrieveResource, "/api/v1/fornecedor/endereco/<int:endereco_id>/", endpoint="FORNECEDOR_ENDERECO_ID")
    api.add_resource(FornecedorEnderecoByFornecedorResource, "/api/v1/fornecedor/<int:fornecedor_id>/endereco/", endpoint="FORNECEDORENDERECO_BY_FORNECEDOR")


    from app.views.produto_view import ProdutoResource, ProdutoRetrieveResource, ProdutoByFornecedorResource
    api.add_resource(ProdutoResource, "/api/v1/produto/", endpoint="PRODUTOS")
    api.add_resource(ProdutoRetrieveResource, "/api/v1/produto/<int:produto_id>/", endpoint="PRODUTO_ID")
    api.add_resource(ProdutoByFornecedorResource, "/api/v1/fornecedor/<int:fornecedor_id>/produto/")