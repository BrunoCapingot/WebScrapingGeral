from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.Requisitos import Requisitos
from Projeto.ControleControle.Controle.Factory.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.DataInput import DataInput
from Projeto.ControleControle.Controle.Factory.Os import Os
from typing import Type, List, Dict, Union, Any, Tuple
from sys import argv

class AulasTeoricas(Requisitos):
    def requisito_extracao_aulas_teoricas(self, dado: list, dado_tratado: str = "", save_dict=dict(aulas_teoricas=str())):
        if save_dict is None:
            save_dict = {'aulas_teoricas': ''}
        save_dict['aulas_teoricas'] = dado.pop()
        return save_dict['aulas_teoricas'],dado

