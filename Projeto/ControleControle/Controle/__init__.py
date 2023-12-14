from Projeto.ControleControle.Controle.Factory import Factory
from Projeto.ControleControle.Controle.ControleProcessos import ControleProcessos
from Projeto.ControleControle.Controle.ControleMotor import ControleMotor
from Projeto.ControleControle.Controle.Factory.VarreduraWeb import VarreduraWeb
from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto import PreparacaoExecucaoExtracaoTexto
from Projeto.ControleControle.Controle.Factory.PreparacaoCalculoSimilaridade import PreparacaCalculoSimilaridade
from Projeto.ControleModelo import ControleModelo
from Projeto.ControleControle.Controle.EstruturaX import EstruturaX


class Controle:
    def __init__(self):
        self.estrutura_x = EstruturaX()
        self.estrutura_x.addInTable(pos=0, object=ControleProcessos())
        self.estrutura_x.addInTable(pos=0, object=ControleMotor())
        self.estrutura_x.addInTable(pos=0, object=Factory())
        self.estrutura_x.addInTable(pos=0, object=ControleModelo())


    def preparacoes_execucao_varredura_web(self):
        self.inserir_processo(processo=VarreduraWeb(nome=type, prioridade=10))
        lista = self.carregar(pos=0,object_name='ControleProcessos').get_lista_processo()
        self.carregar(pos=0,object_name='ControleMotor').adicionar_processos(process_list=lista)
        self.carregar(pos=0, object_name='ControleMotor').iniciar_execucao(
            object_list=[
                self.carregar(pos=0,object_name='Factory').get_factory(type_factory='Web'),
                self.carregar(pos=0, object_name='Factory').get_factory(type_factory='DataInput'),
                self.carregar(pos=0, object_name='Factory').get_factory(type_factory='Arquivo'),
                self.carregar(pos=0,object_name='ControleModelo')
            ])
    def preparacao_extrair_texto(self):
        self.inserir_processo(processo=PreparacaoExecucaoExtracaoTexto.get_preparacao())
        self.carregar(pos=0, object_name='ControleMotor').adicionar_processos(process_list=self.carregar(pos=0, object_name='ControleProcessos').get_lista_processo())
        self.carregar(pos=0, object_name='ControleMotor').iniciar_execucao(object_list=[
            self.carregar(pos=0, object_name='Factory').get_factory(type_factory='Arquivo'),
            self.carregar(pos=0, object_name='Factory').get_factory(type_factory='DataInput'),
            self.carregar(pos=0, object_name='Factory').get_factory(type_factory='Os'),
            self.carregar(pos=0, object_name='ControleModelo')
        ])

    def preparacao_extrair_similaridade(self):
        self.inserir_processo(processo=PreparacaCalculoSimilaridade.get_preparacao())
        self.carregar(pos=0, object_name='ControleMotor').adicionar_processos(process_list=self.carregar(pos=0, object_name='ControleProcessos').get_lista_processo())
        self.carregar(pos=0, object_name='ControleMotor').iniciar_execucao(object_list=[
            self.carregar(pos=0, object_name='Factory').get_factory(type_factory='Arquivo'),
            self.carregar(pos=0, object_name='Factory').get_factory(type_factory='DataInput'),
            self.carregar(pos=0, object_name='Factory').get_factory(type_factory='Os'),
            self.carregar(pos=0, object_name='ControleModelo')
        ])













    def carregar(self,pos,object_name)->object:
        return self.estrutura_x.getInTable(type_return=object,pos=pos,object_name=object_name)

    def carregar_motor(self,process_list):
        self.carregar(pos=0, object_name='ControleMotor').adicionar_processos(process_list=process_list)

    def inserir_processo(self,processo)->None:
        if type(processo) != list:
            self.estrutura_x.getInTable(type_return=object,pos=0,object_name='ControleProcessos').adicionar_processo(processo=processo)
        elif type(processo) == list:
            self.estrutura_x.getInTable(type_return=object, pos=0, object_name='ControleProcessos').add_process_list(process_list=processo)