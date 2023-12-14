from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.Casos.Requisitos import Requisitos


class AulasPraticas(Requisitos):

    def requisito_extracao_aulas_praticas(self, dado: list, dado_tratado: str = "", save_dict=dict(c_h_total=str())):
        if save_dict is None:
            save_dict = {'aulas_praticas': ''}
        save_dict['aulas_praticas']=dado.pop()
        return save_dict['aulas_praticas'],dado

