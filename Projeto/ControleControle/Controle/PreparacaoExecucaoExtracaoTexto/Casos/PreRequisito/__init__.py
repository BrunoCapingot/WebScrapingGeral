from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.Requisitos import Requisitos
from Projeto.ControleControle.Controle.Factory.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.DataInput import DataInput
from Projeto.ControleControle.Controle.Factory.Os import Os
from typing import Type, List, Dict, Union, Any
from sys import argv

class PreRequisito(Requisitos):
    def requisito_extracao_pre_requisito(self, dado: list, dado_tratado: str = "", save_dict: Dict[str, Union[str, List[str]]] = None) -> list[str | list | Any]:
        if save_dict is None:
            save_dict = {'pre_requisito': ''}
        if dado.__len__() > 0 and (dado[-1].__len__() == 1 or dado[-1].__len__() == 7):
            save_dict['pre_requisito']=dado.pop()
            if dado.__len__() > 0 and (dado[-1] == '-'):
                save_dict['pre_requisito'] += dado.pop()
                save_dict['pre_requisito'] += dado.pop()
                if dado.__len__() > 0 and (dado[-1] == '-'):
                    save_dict['pre_requisito'] += dado.pop()
                    save_dict['pre_requisito'] += dado.pop()
        return list((save_dict['pre_requisito'],dado))

