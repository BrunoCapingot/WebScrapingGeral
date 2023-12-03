from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.Requisitos import Requisitos
from Projeto.ControleControle.Controle.Factory.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.DataInput import DataInput
from Projeto.ControleControle.Controle.Factory.Os import Os
from typing import Type, List, Dict, Union, Any
from sys import argv

class AulasSemanais(Requisitos):
    def requisito_extracao_aulas_semanais(self, dado: list, dado_tratado: str = "", save_dict: Dict[str, Union[str, List[str]]] = None) -> list[str | list | Any]:
        if save_dict is None:
            save_dict = {'aulas_semanais': ''}
        if dado and dado.__len__()!=1:
            if dado[-1].__len__() == 1:
                save_dict['aulas_semanais'] = dado.pop()
        return list((save_dict['aulas_semanais'],dado))

