from Projeto.ControleControle.Controle import Controle


class ControleControle:
    def __init__(self):
        self.table_tables = [Controle()]

    def execControl(self):
        kk = self.table_tables.pop()
        #kk.preparacao_extrair_similaridade()
        #kk.preparacao_extrair_texto()
        kk.preparacoes_execucao_varredura_web()
        #self.table_tables.pop().preparacao_execucao_varreduraWeb()
        #self.table_tables.append(Controle())
        #self.table_tables.pop().preparacao_execucao_extrair_texto()