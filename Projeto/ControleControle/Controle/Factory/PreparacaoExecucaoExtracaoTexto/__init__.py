from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.ExtracaoTextoAgronomia import ExtracaoTextoAgronomia


class PreparacaoExecucaoExtracaoTexto:
    @staticmethod
    def get_preparacao() -> list:
        return [ExtracaoTextoAgronomia(nome='ext_agronomia', prioridade=9)]
