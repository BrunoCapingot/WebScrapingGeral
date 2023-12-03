from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.Requisitos import Requisitos
from Projeto.ControleControle.Controle.Factory.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.DataInput import DataInput
from Projeto.ControleControle.Controle.Factory.Os import Os
from typing import Type, List, Dict, Union, Any
from sys import argv

class CodigoDaDiciplina(Requisitos):
    def requisito_extracao_codigo_da_diciplina(self, dado: list, dado_tratado: str = "", save_dict=dict(codigo_da_diciplina=str())):
        if save_dict is None:
            save_dict = {'codigo_da_diciplina': ''}
        if dado.__len__() != 2: save_dict['codigo_da_diciplina'] = dado.pop()
        else:save_dict['codigo_da_diciplina'] = dado.pop()
        return save_dict['codigo_da_diciplina'],dado