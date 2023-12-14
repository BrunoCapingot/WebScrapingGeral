from Projeto.ControleControle.Controle import Controle
from Projeto.ControleModelo import ControleModelo




class ControleControle(Controle,ControleModelo):
    def __init__(self):
        super().__init__()

    def execControl(self):
        #kk.preparacao_extrair_similaridade()
        #kk.preparacao_extrair_texto()
        self.preparacoes_execucao_varredura_web()
        #self.table_tables.pop().preparacao_execucao_varreduraWeb()
        #self.table_tables.append(Controle())
        #self.table_tables.pop().preparacao_execucao_extrair_texto()