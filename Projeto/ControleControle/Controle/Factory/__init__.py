from abc import ABC, abstractmethod
from Projeto.ControleControle.Controle.Factory.Web import Web
from Projeto.ControleControle.Controle.Factory.EstruturaX import EstruturaX
from Projeto.ControleControle.Controle.Factory.PreparacaoCalculoSimilaridade import PreparacaCalculoSimilaridade
from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto import PreparacaoExecucaoExtracaoTexto
from Projeto.ControleControle.Controle.Factory.VarreduraWeb import VarreduraWeb



class FacFactory(ABC):
    @abstractmethod
    def get_extrutura_x(self) -> EstruturaX:
        pass

    def get_web(self) -> Web:
        pass

    def get_preparacao_calculo_similaridade(self) -> PreparacaCalculoSimilaridade:
        pass

    def get_varredura_web(self) -> VarreduraWeb:
        pass



class Factory(FacFactory):
    def get_varredura_web(self) -> VarreduraWeb:
        return VarreduraWeb(nome='varredura_web', prioridade=10)

    def get_extrutura_x(self)->EstruturaX:
        return EstruturaX()

    def get_web(self)->Web:
        return Web()

    def get_preparacao_calculo_similaridade(self)->PreparacaCalculoSimilaridade:
        return PreparacaCalculoSimilaridade()

    def get_preparacao_execucao_extracao_texto(self)->PreparacaoExecucaoExtracaoTexto:
        return PreparacaoExecucaoExtracaoTexto()
