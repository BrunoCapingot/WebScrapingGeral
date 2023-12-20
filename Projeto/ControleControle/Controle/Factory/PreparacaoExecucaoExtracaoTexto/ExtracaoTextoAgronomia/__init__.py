from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.Casos.AulasSemanais import AulasSemanais
from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.Casos.AulasPraticas import AulasPraticas
from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.Casos.AulasTeoricas import AulasTeoricas
from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.Casos.CargaHoraria import CargaHoraria
from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.Casos.CodigoDaDiciplina import CodigoDaDiciplina
from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.Casos.Diciplina import Diciplina
from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.Casos.Ementa import Ementa
from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.Casos.PreRequisito import PreRequisito
from Projeto.ControleControle.Controle.Factory.PreparacaoExecucaoExtracaoTexto.Casos.Periodo import Periodo
from sys import argv
from typing import Type
from Projeto.ControleModelo.Modelo.Os import Os
from Projeto.ControleModelo.Arquivo import Arquivo
from Projeto.ControleModelo.DataInput import DataInput
from Projeto.ControleModelo import ControleModelo
from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo

class ExtracaoDadosAgronomia(Processo, PreRequisito, AulasSemanais, CargaHoraria, AulasPraticas, AulasTeoricas, Diciplina, CodigoDaDiciplina, Periodo, Ementa):
    def executar(self, ControleModelo:ControleModelo,suport=0, txt_fracionado=str(),save_dict=dict(),csv_dict=dict()) -> None:
        ControleModelo.set_model_data(type_model='caminhos_de_relacao',key_dict='txt')
        #Os.set_ponteiro(caminho_facrionado=DataInput.get_caminhos_de_relacao()['txt'])
        for dado in Os.read(type_read='txt',arquivo=Arquivo(nome=item_dir_name.replace('pdf','txt'),caminho=DataInput.get_caminhos_de_relacao()['txt'],conteudo='')).split('\n'):
            if dado.__len__() != 0 and dado != '':
                dado = dado.split()
                if dado != ' ' and (not 'Total' in dado and not 'AGRONOMIA ' in dado and dado.__len__() > 5 and not 'ATC-202' in dado):
                    save_dict['pre_requisito'], dado = self.requisito_extracao_pre_requisito(dado=dado)
                    save_dict['aulas_semanais'], dado = self.requisito_extracao_aulas_semanais(dado=dado)
                    save_dict['c_h_total'], dado = self.requisito_extracao_carga_horaria_total(dado=dado)
                    save_dict['aulas_praticas'], dado = self.requisito_extracao_aulas_praticas(dado=dado)
                    save_dict['aulas_teoricas'], dado = self.requisito_extracao_aulas_teoricas(dado=dado)
                    save_dict['diciplina'], dado = self.requisito_extracao_nome_diciplina(dado=dado)
                    save_dict['codigo_da_diciplina'], dado = self.requisito_extracao_codigo_da_diciplina(dado=dado)
                    save_dict['periodo'], dado = self.requisito_extracao_periodo(dado=dado)
                    csv_dict = save_dict
                elif 'ATC-202' in dado:
                    pass
                
                    with open('dados.csv', mode='a', newline='') as file:
                        fieldnames = ['pre_requisito', 'aulas_semanais', 'c_h_total', 'aulas_praticas','aulas_teoricas', 'diciplina', 'codigo_da_diciplina', 'periodo']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow(csv_dict)
                        save_dict = dict()












