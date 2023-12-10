from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo
from Projeto.ControleControle.Controle.ControleModelo import ControleModelo
from Projeto.ControleControle.Controle.Factory.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.DataInput import DataInput
from Projeto.ControleControle.Controle.Factory.Os import Os


class ExtracaoDeTexto(Processo):
    def executar(self, object_list):
        self.execucao(Arquivo=object_list[0], DataInput=object_list[1], Os=object_list[2],ControleModelo=object_list[3])

    def execucao(self, Arquivo:Arquivo, DataInput:DataInput, Os:Os, ControleModelo:ControleModelo):
        lista = list()
        Os.set_ponteiro(DataInput.get_caminhos_de_relacao()['projeto_pedagogico'])
        for item_dir_name in  Os.get_dir_pointer_name_items():
            total_text = ''
            suport = 0
            pos_dois = 0
            pos_one = 0
            pdf = Os.extract_content_pointer_path(tipo='pdf',Arquivo=Arquivo(nome=item_dir_name,caminho=DataInput.get_caminhos_de_relacao()['projeto_pedagogico'],link=''))
            while len(pdf) != suport :
                dt = pdf[suport].extract_text()
                if dt == '' or dt == ' ':
                    suport += 1
                else:
                    dt = dt.replace('-\n', '')
                    #dt = dt.replace('  ', ' ')
                    total_text += dt
                    suport += 1
            for index, linha in enumerate(total_text.split('\n')):
                if item_dir_name == 'Bacharelado em Agronomia.pdf':
                    if 'ANEXO II' in linha and not '..' in linha:
                        lista.append(index)
                        break
                    elif 'ANEXO I' in linha and not '..' in linha:
                        lista.append(index)

                elif item_dir_name == 'Bacharelado em Ciência da Computação.pdf':
                    if 'ANEXO II – EMENTÁRIO DAS DISCIPLINAS OPTATIVAS' in linha and not '..' in linha:
                        lista.append(index)
                        break
                    elif 'ANEXO I' in linha and not '..' in linha:
                        lista.append(index)

            while len(lista):
                pos_one = lista.pop()
                pos_dois = lista.pop()
                for posicao in range(pos_dois,pos_one):
                    for index,elemento in enumerate(total_text.split('\n')[posicao]):
                        pass
                        #print(elemento)
                        #print(index)
                        #input('index')


                    #for linha_na_pos in total_text.split('\n')[posicao]:
            #       pass
            #input('calaasdpcnsdojcnsa')
            #ControleModelo.add_list_save(Arquivo=Arquivo(nome=item_dir_name, caminho=DataInput.get_caminhos_de_relacao()['projeto_pedagogico'],link=''))
        #ControleModelo.save_list_save(Os=Os)
