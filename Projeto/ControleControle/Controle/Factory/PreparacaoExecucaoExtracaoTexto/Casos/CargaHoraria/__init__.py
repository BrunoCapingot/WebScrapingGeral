from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.Casos.Requisitos import Requisitos


class CargaHoraria(Requisitos):
    def requisito_extracao_carga_horaria_total(self, dado: list, dado_tratado: str = "", save_dict=dict(c_h_total=str())):
        if save_dict is None:
            save_dict = {'c_h_total': ''}
        save_dict['c_h_total'] = dado.pop()
        return save_dict['c_h_total'],dado

