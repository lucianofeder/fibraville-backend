from app.models.visita_tecnica_model import VisitaTecnicaModel
from app.models.produto_model import ProdutoModel
from app.models.visita_tecnica_produto_model import VisitaTecnicaProdutoModel
from app.exc import DataNotFound

import ipdb

class VisitaTecnicaProdutoService:

    @staticmethod
    def relate_visita_produtos_list(visita_id, produtos_dict_list):
        visita = VisitaTecnicaModel.query.get(visita_id)
        if not visita:
            raise DataNotFound('Visita')
        
        for produto_dict in produtos_dict_list:
            produto = ProdutoModel.query.get(produto_dict['id'])
            if not produto:
                raise DataNotFound('Produto')
            
        for produto_dict in produtos_dict_list:
            visita_produto = VisitaTecnicaProdutoModel(produto_id=produto_dict['id'], visita_tecnica_id=visita_id, quantidade=produto_dict['quantidade'])
            visita_produto.save()
        
        visita.save()
        return visita

    
    @staticmethod
    def update_visita_produtos_list(visita_id, produtos_dict_list):
        visita = VisitaTecnicaModel.query.get(visita_id)
        if not visita:
            raise DataNotFound('Visita')
        
        for produto_dict in produtos_dict_list:
            produto = ProdutoModel.query.get(produto_dict['id'])
            if not produto:
                raise DataNotFound('Produto')
            
        old_visitas = VisitaTecnicaProdutoModel.query.filter_by(visita_tecnica_id=visita_id).all()
        if old_visitas:
            for ov in old_visitas:
                ov.delete()

        visita = VisitaTecnicaProdutoService.relate_visita_produtos_list(visita_id, produtos_dict_list)
        return visita
    
