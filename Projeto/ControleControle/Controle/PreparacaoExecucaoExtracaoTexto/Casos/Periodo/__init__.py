from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.Requisitos import Requisitos
from Projeto.ControleControle.Controle.Factory.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.DataInput import DataInput
from Projeto.ControleControle.Controle.Factory.Os import Os
from typing import Type, List, Dict, Union, Any
from sys import argv

class Periodo(Requisitos):
    def requisito_extracao_periodo(self, dado: list, dado_tratado: str = "", save_dict: Dict[str, Union[str, List[str]]] = None) -> list[str | list | Any]:
        if save_dict is None:
            save_dict = {'periodo': ''}
        if dado:
            save_dict['periodo']=dado.pop()
        return list((save_dict['periodo'],dado))

