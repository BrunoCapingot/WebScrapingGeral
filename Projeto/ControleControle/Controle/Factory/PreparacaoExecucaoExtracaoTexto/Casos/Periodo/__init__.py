from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.Casos.Requisitos import Requisitos
from typing import List, Dict, Union, Any


class Periodo(Requisitos):
    def requisito_extracao_periodo(self, dado: list, dado_tratado: str = "", save_dict: Dict[str, Union[str, List[str]]] = None) -> list[str | list | Any]:
        if save_dict is None:
            save_dict = {'periodo': ''}
        if dado:
            save_dict['periodo']=dado.pop()
        return list((save_dict['periodo'],dado))

