from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo
from Projeto.ControleControle.Controle.Factory.Os import Os
from Projeto.ControleControle.Controle.Factory.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.DataInput import DataInput
from Projeto.ControleModelo import ControleModelo
from Projeto.ControleControle.Controle.Factory.PreparacaoCalculoSimilaridade.Jaccard import Jaccard
from sys import argv

class Similaridade(Processo,Jaccard):

    def executar(self, object_list):
        self.execucao(Arquivo=object_list[0], DataInput=object_list[1], Os=object_list[2],ControleModelo=object_list[3])

    def execucao(self, Arquivo: Arquivo, DataInput: DataInput, Os: Os, ControleModelo: ControleModelo, suport=0,txt_fracionado=str(), csv_list=list(),item_name_dir=str('Bacharelado em Agronomia.csv'),suport_dict = dict(diciplina=str(),ementa=str())) -> None:
        csv_item = Os.read(type_read='csv',arquivo=Arquivo(nome=item_name_dir, caminho=DataInput.get_caminhos_de_relacao()['csv'],conteudo='')).split('\n')
        for elemento in csv_item:
            if elemento != '':
                dt = elemento.split('||||')
                suport_dict['diciplina'] = dt[0]
                suport_dict['ementa'] = dt[1]
                csv_list.append(suport_dict.copy())
        for dicionario in csv_list:
            if not 'ementa' in dicionario['ementa'] and argv.__len__() < 3:
                argv.append(dicionario)
            elif argv.__len__() == 3:
                print('Similaridade: {}'.format(self.calcular_similaridade(set_one=argv.pop(),set_two=argv.pop())))

