from Projeto.ControleControle.Controle.Factory.Os import Os
from Projeto.ControleControle.Controle.Factory.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.DataInput import DataInput
from Projeto.ControleControle.Controle.PreparacaoExecucaoExtracaoTexto.Casos.Requisitos import Requisitos
from sys import argv


class Ementa(Requisitos):
    def requisito_extracaoPrimariaEmEmenta(self, Os: Os, DataInput: DataInput, total_text: str, item_dir_name: str, content=str(), csv_data_lista=list(), save_dict=dict(diciplina=str(),ementa=str())):
        cond = bool()
        total_text = total_text.replace('HORÁ-\n', 'HORÁ')
        for index, linha in enumerate(total_text.split('\n')):
            if 'ANEXO IV' in linha and not '..' in linha:
                argv.append(str(index))
                break
            elif 'ANEXO  III' in linha and not '..' in linha:
                argv.append(str(index))
        pos_one = argv.pop()
        pos_dois = argv.pop()
        texto = ''

        for posicao in range(int(pos_dois), int(pos_one)):
            dt = total_text.split('\n')
            onde_ta = dt[posicao]
            if 'HORÁRIA' in dt[posicao]:
                dn = total_text.split('\n')[posicao + 1].split()
                content = ''
                while dn.__len__():
                    if dn[-1].isalpha():
                        texto += dn.pop(0)
                    else:
                        dn.pop()
                save_dict['diciplina'] = texto
                texto = ''


            elif 'EMENTA  ' in dt[posicao] and not 'III' in dt[posicao]:
                ss = posicao+1
                while True:
                    texto += dt[ss]
                    ss += 1
                    if 'BIBLIOGRAFIA BÁ SICA' in dt[ss] or 'BIBLIOGRAFIA BÁSICA  ' in dt[ss]:
                        break
                save_dict['ementa'] = texto
                texto=''
                sss = ss+1
                if 'BIBLIOGRAFIA BÁ SICA' in dt[ss] or 'BIBLIOGRAFIA BÁSICA  ' in dt[ss]:
                    cond = True
                else:cond = False
            elif save_dict['ementa'] != '' and save_dict['diciplina'] != '' and cond == True:
                print(save_dict)
        #Os.save(type_save='txt', arquivo=Arquivo(nome=item_dir_name, caminho=DataInput.get_caminhos_de_relacao()['ementa'], conteudo=str(save_dict)))
