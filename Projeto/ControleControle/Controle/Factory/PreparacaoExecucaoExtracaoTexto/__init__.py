from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.ExtracaoTexto import ExtracaoDeTexto
from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.ExtracaoTextoAgronomia import ExtracaoDadosAgronomia


class PreparacaoExecucaoExtracaoTexto:
    @staticmethod
    def get_preparacao() -> list:
        return [ExtracaoDeTexto(nome='ext_texto_geral', prioridade=9)]
