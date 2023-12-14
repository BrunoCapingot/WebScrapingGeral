from abc import ABC, abstractmethod
from Projeto.ControleControle.Controle.Factory.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.DataInput import DataInput
from Projeto.ControleControle.Controle.Factory.Driver import Driver
from Projeto.ControleControle.Controle.Factory.Os import Os
from Projeto.ControleControle.Controle.Factory.Web import Web
from Projeto.ControleControle.Controle.Factory.VarreduraWeb import VarreduraWeb


class FacFactory(ABC):
    @abstractmethod
    def get_factory(self, type_factory: str):
        pass


class Factory(FacFactory):
    def get_factory(self, type_factory: str) -> object:
        if type_factory == 'DataInput':
            return DataInput()
        elif type_factory =='Arquivo':
            return Arquivo
        elif type_factory == 'Os':
            return Os()
        elif type_factory == 'Web':
            return Web(driver=Driver())
        elif type_factory == 'varredura_web':
            return VarreduraWeb(nome=type_factory, prioridade=9)
