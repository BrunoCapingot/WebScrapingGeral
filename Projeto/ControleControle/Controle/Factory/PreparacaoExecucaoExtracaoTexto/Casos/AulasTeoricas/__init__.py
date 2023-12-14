from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.Casos.Requisitos import Requisitos


class AulasTeoricas(Requisitos):
    def requisito_extracao_aulas_teoricas(self, dado: list, dado_tratado: str = "", save_dict=dict(aulas_teoricas=str())):
        if save_dict is None:
            save_dict = {'aulas_teoricas': ''}
        save_dict['aulas_teoricas'] = dado.pop()
        return save_dict['aulas_teoricas'],dado

