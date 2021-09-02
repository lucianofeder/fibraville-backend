from app.models.visita_tecnica_model import VisitaTecnicaModel
from app.models.usuario_model import UsuarioModel
from app.models.visita_tecnica_tecnico_model import VisitaTecnicaTecnicoModel
from app.exc import DataNotFound


class VisitaTecnicaTecnicoService:

    @staticmethod
    def relate_visita_tecnico_list(visita_id, tecnicos_id_list):
        visita = VisitaTecnicaModel.query.get(visita_id)
        if not visita:
            raise DataNotFound('Visita')
        
        for tecnico_id in tecnicos_id_list:
            tecnico = UsuarioModel.query.get(tecnico_id)
            if not tecnico:
                raise DataNotFound('Tecnico')
            
        for tecnico_id in tecnicos_id_list:
            visita_tecnico = VisitaTecnicaTecnicoModel(tecnico_id=tecnico_id, visita_tecnica_id=visita_id)
            visita_tecnico.save()          
        
        visita.save()
        return visita

    @staticmethod
    def update_visita_tecnico_list(visita_id, tecnicos_id_list):
        visita = VisitaTecnicaModel.query.get(visita_id)
        if not visita:
            raise DataNotFound('Visita')
        
        old_visitas = VisitaTecnicaTecnicoModel.query.filter_by(visita_tecnica_id=visita_id).all()
        if old_visitas:
            for ov in old_visitas:
                ov.delete()
    
        visita = VisitaTecnicaTecnicoService.relate_visita_tecnico_list(visita_id, tecnicos_id_list)
        return visita