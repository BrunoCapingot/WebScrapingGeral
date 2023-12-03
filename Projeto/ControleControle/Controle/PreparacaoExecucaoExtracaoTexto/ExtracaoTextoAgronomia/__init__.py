from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.AulasSemanais import AulasSemanais
from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.AulasPraticas import AulasPraticas
from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.AulasTeoricas import AulasTeoricas
from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.CargaHoraria import CargaHoraria
from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.CodigoDaDiciplina import CodigoDaDiciplina
from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.Diciplina import Diciplina
from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.PreRequisito import PreRequisito
from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.Periodo import Periodo

from Projeto.ControleControle.Controle.ControleModelo import ControleModelo
from Projeto.ControleControle.Controle.Factory.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.DataInput import DataInput
from Projeto.ControleControle.Controle.Factory.Os import Os
from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo
from typing import Type
from sys import argv
import csv


class ExtracaoTextoAgronomia(Processo,PreRequisito,AulasSemanais,CargaHoraria,AulasPraticas,AulasTeoricas,Diciplina,CodigoDaDiciplina,Periodo):
    def executar(self, object_list):
        self.execucao(Arquivo=object_list[0], DataInput=object_list[1], Os=object_list[2],ControleModelo=object_list[3])

    def execucao(self, Arquivo: Arquivo, DataInput: DataInput, Os: Os, ControleModelo: ControleModelo, suport=0, txt_fracionado=str(),save_dict=dict(),csv_dict=dict()) -> None:
        Os.set_ponteiro(DataInput.get_caminhos_de_relacao()['projeto_pedagogico'])
        for item_dir_name in Os.get_dir_pointer_name_items():
            if item_dir_name == 'Bacharelado em Agronomia.pdf':
                total_text = self.extracaoPrimaria(item_dir_name=item_dir_name, Os=Os, DataInput=DataInput,suport=suport)
                self.extracaoPrimariaEmPosicao(Os=Os,DataInput=DataInput,item_dir_name=item_dir_name,total_text=total_text)
                Os.set_ponteiro(caminho_facrionado=DataInput.get_caminhos_de_relacao()['txt'])
                for dado in Os.read(type_read='txt',arquivo=Arquivo(nome=item_dir_name.replace('pdf','txt'),caminho=DataInput.get_caminhos_de_relacao()['txt'],conteudo='')).split('\n'):
                    if dado.__len__() != 0 and dado != '':
                        dado = dado.split()
                        if dado != ' ' and (not 'Total' in dado and not 'AGRONOMIA ' in dado and dado.__len__() > 5 and not 'ATC-202' in dado):
                            p
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


















    def extracaoPrimaria(self, item_dir_name: str, suport: int, Os: Os, DataInput: DataInput,total_text = str()) -> Type[str]:
        pdf = Os.extract_content_pointer_path(tipo='pdf', Arquivo=Arquivo(nome=item_dir_name,caminho=DataInput.get_caminhos_de_relacao()['projeto_pedagogico'], conteudo=str()))
        while len(pdf) != suport:
            dt = pdf[suport].extract_text()
            dt = dt.replace('-\n', '')
            dt = dt.rstrip()
            total_text += pdf[suport].extract_text()
            suport += 1

        return total_text

    def extracaoPrimariaEmPosicao(self,total_text:str,Os:Os,DataInput,item_dir_name,content = str())->Type[None]:
        for index, linha in enumerate(total_text.split('\n')):
            if 'ANEXO II' in linha and not '..' in linha:
                argv.append(str(index))
                break
            elif 'ANEXO I' in linha and not '..' in linha:
                argv.append(str(index))
        pos_one = argv.pop()
        pos_dois = argv.pop()
        cond = False
        for posicao in range(int(pos_dois),int(pos_one)):
            #print(total_text.split('\n')[posicao])
            #Os.save(type_save='txt',arquivo=Arquivo(nome=total_text.split('\n')))
            if 'requisitos' in total_text.split('\n')[posicao]:cond = True
            elif 'Semestre' in total_text.split('\n')[posicao]:cond = False
            elif cond:content += '\n'+str(total_text.split('\n')[posicao])
        #content=content.replace(' - \n',' - ')
        content=content.replace('OPT -','OPT-')
        content=content.replace('ATC ','ATC')
        content=content.replace('GAM -','GAM-')
        content=content.replace('EAL -','EAL-')
        content=content.replace('ZOO -','ZOO-')
        content=content.replace('ENG -','ENG-')
        content=content.replace('EXA -','EXA-')
        content=content.replace('AGR -','AGR-')
        content=content.replace('AGR-218-','AGR-218 -')
        content=content.replace('AGR-226 - \n', 'AGR-226 - ')
        content=content.replace('AGR- ','AGR-')
        content=content.replace('HUM -','HUM-')
        content=content.replace('Manejo e Conservação do Solo e da \n','Manejo e Conservação do Solo e da ')
        content=content.replace('Plantas e Receituário \n','Plantas e Receituário ')
        content=content.replace('AGR-222 Avaliação e Perícia Rural','9º AGR-222 Avaliação e Perícia Rural')
        content=content.replace('Café e \n','Café e ')
        content=content.replace('Al-\n','Al')
        content=content.replace('Bacharelado  \n','')
        content=content.replace('AGRONOMIA  \n','')
        content=content.replace('das unidades \ncurriculares','das unidades curriculares')
        content=content.replace('estágio curri-\n','estágio curri')
        content=content.replace('(Milho, Arroz, Trigo e \n','(Milho, Arroz, Trigo e ')

        Os.save(type_save='txt',arquivo=Arquivo(nome=item_dir_name.replace('.pdf','.txt'),caminho=DataInput.get_caminhos_de_relacao()['txt'],conteudo=content))