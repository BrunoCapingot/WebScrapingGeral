from Projeto.ControleControle.Controle.Factory.Arquivo import Arquivo
import os
import csv
import requests
from PyPDF2 import PdfReader


class Os:
    def __init__(self):
        self._atribute_dict = {'ponteiro': str(), 'arquivo': object(), 'caminho': str(),
                               'caminho_arquivo_completo': str()}
    def read(self, type_read, arquivo, dado = str()):
        if type_read == 'txt':
            diretorio = arquivo.get_caminho() +'\\'+ arquivo.get_name().replace('.pdf','.txt')
            with open(diretorio, 'r', encoding='utf-8') as txt_file:
                dado+=txt_file.read()
            return dado
        elif type_read == 'csv':
            diretorio = arquivo.get_caminho() +'\\'+ arquivo.get_name().replace('.pdf','.csv')
            with open(diretorio, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    dado += '||||'.join(row)
                    dado += '\n'
            return dado


    def save(self, type_save, arquivo):
        if type_save == 'txt':
            diretorio = arquivo.get_caminho() +'\\'+ arquivo.get_name().replace('.pdf','.txt')
            with open(diretorio, 'w', encoding='utf-8') as txt_file:
                txt_file.write(arquivo.get_conteudo())

    def download_arquivo(self, link, caminho_save):
        response = requests.get(link)
        print(caminho_save)
        if response.status_code == 200:
            with open(r'{}'.format(caminho_save), 'wb') as file:
                file.write(response.content)
            print(f"O arquivo foi baixado e salvo em {caminho_save}")
        else:
            print("Não foi possível baixar o arquivo PDF.")

    def get_diretorio_pointer_name_items(self):
        return os.listdiretorio(self._atribute_dict['ponteiro'])

    def set_ponteiro(self, caminho_facrionado):
        self._atribute_dict['ponteiro'] = caminho_facrionado

    def home_ponteiro(self):
        desktop_path = os.path.expanduser("~/Desktop")
        self._atribute_dict['ponteiro'] = desktop_path
        return desktop_path

    def extract_content_pointer_path(self,tipo,Arquivo:Arquivo):
        if 'pdf' == tipo:
            reader = PdfReader(stream=r''+Arquivo.get_caminho()+'\\'+Arquivo.get_name())
            return reader.pages
