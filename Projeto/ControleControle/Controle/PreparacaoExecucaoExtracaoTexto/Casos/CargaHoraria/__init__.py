from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.Requisitos import Requisitos
from Projeto.ControleControle.Controle.Factory.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.DataInput import DataInput
from Projeto.ControleControle.Controle.Factory.Os import Os
from typing import Type, List, Dict, Union, Any
from sys import argv

class CargaHoraria(Requisitos):
    def requisito_extracao_carga_horaria_total(self, dado: list, dado_tratado: str = "", save_dict=dict(c_h_total=str())):
        if save_dict is None:
            save_dict = {'c_h_total': ''}
        save_dict['c_h_total'] = dado.pop()
        return save_dict['c_h_total'],dado

