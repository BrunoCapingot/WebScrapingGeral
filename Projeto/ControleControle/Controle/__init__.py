from Projeto.ControleControle.Controle.Factory import Factory
from Projeto.ControleControle.Controle.ControleProcessos import ControleProcessos
from Projeto.ControleControle.Controle.ControleMotor import ControleMotor
from Projeto.ControleModelo import ControleModelo


class Controle(Factory):
    def __init__(self):
        self.estrutura_x = self.get_extrutura_x()
        self.estrutura_x.addInTable(pos=0, object=ControleProcessos())
        self.estrutura_x.addInTable(pos=0, object=ControleMotor())


    def preparacoes_execucao_varredura_web(self)->None:
        self.inserir_processo(processo=self.get_varredura_web())
        lista = self.carregar(pos=0,object_name='ControleProcessos').get_lista_processo()
        self.carregar(pos=0,object_name='ControleMotor').adicionar_processos(process_list=lista)
        self.carregar(pos=0, object_name='ControleMotor').iniciar_execucao(object_list=[self.get_web(),ControleModelo()])

    def preparacao_extrair_texto(self)->None:
        self.inserir_processo(processo=self.get_preparacao_execucao_extracao_texto().get_preparacao())
        self.carregar(pos=0, object_name='ControleMotor').adicionar_processos(process_list=self.carregar(pos=0, object_name='ControleProcessos').get_lista_processo())
        self.carregar(pos=0, object_name='ControleMotor').iniciar_execucao(object_list=ControleModelo())

    def preparacao_extrair_similaridade(self)->None:
        self.inserir_processo(processo=self.get_preparacao_calculo_similaridade().get_preparacao())
        self.carregar(pos=0, object_name='ControleMotor').adicionar_processos(process_list=self.carregar(pos=0, object_name='ControleProcessos').get_lista_processo())
        self.carregar(pos=0, object_name='ControleMotor').iniciar_execucao(object_list=ControleModelo())

    def carregar(self,pos,object_name)->object:
        return self.estrutura_x.getInTable(type_return=object,pos=pos,object_name=object_name)

    def carregar_motor(self,process_list)->None:
        self.carregar(pos=0, object_name='ControleMotor').adicionar_processos(process_list=process_list)

    def inserir_processo(self,processo)->None:
        if type(processo) != list:
            self.estrutura_x.getInTable(type_return=object,pos=0,object_name='ControleProcessos').adicionar_processo(processo=processo)
        elif type(processo) == list:
            self.estrutura_x.getInTable(type_return=object, pos=0, object_name='ControleProcessos').add_process_list(process_list=processo)

