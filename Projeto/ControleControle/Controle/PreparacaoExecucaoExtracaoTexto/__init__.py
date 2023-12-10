from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.ExtracaoTextoAgronomia import ExtracaoTextoAgronomia
from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.ExtracaoTextoAlimentos import ExtracaoTextoAlimentos


class PreparacaoExecucaoExtracaoTexto:
    @staticmethod
    def get_preparacao() -> list:
        return [ExtracaoTextoAgronomia(nome='ext_agronomia', prioridade=9)]
