from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.Requisitos import Requisitos
from Projeto.ControleControle.Controle.Factory.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.DataInput import DataInput
from Projeto.ControleControle.Controle.Factory.Os import Os
from typing import Type, List, Dict, Union, Any
from sys import argv

class AulasPraticas(Requisitos):

    def requisito_extracao_aulas_praticas(self, dado: list, dado_tratado: str = "", save_dict=dict(c_h_total=str())):
        if save_dict is None:
            save_dict = {'aulas_praticas': ''}
        save_dict['aulas_praticas']=dado.pop()
        return save_dict['aulas_praticas'],dado

