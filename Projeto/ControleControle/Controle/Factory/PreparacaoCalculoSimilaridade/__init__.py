from Projeto.ControleControle.Controle.Factory.PreparacaoCalculoSimilaridade.Similaridade import Similaridade

class PreparacaCalculoSimilaridade:
    @staticmethod
    def get_preparacao() -> list:
        return [Similaridade(nome='calculo_similaridade', prioridade=8)]