from Projeto.ControleControle.Controle import Controle




class ControleControle(Controle):
    def __init__(self):
        super().__init__()

    def execControl(self):
        #self.preparacoes_execucao_varredura_web()
        self.preparacao_extrair_texto()
        #self.preparacao_extrair_similaridade()
