from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo
from Projeto.ControleModelo import ControleModelo
from Projeto.ControleModelo.Arquivo import Arquivo


def extracaoPrimaria(pdf, suport: int,argv_list=list()) -> str:
    while len(pdf) != suport:
        argv_list.append(pdf[suport].extract_text())
        suport += 1
    return ''.join(argv_list)


def extracaoPrimariaEmPosicao(total_text: str, item_dir_name, ControleModelo:ControleModelo, content=str()) -> None:
    for index, linha in enumerate(total_text.split('\n')):
        if 'ANEXO II' in linha and not '..' in linha:
            argv.append(str(index))
            break
        elif 'ANEXO I' in linha and not '..' in linha:
            argv.append(str(index))
    pos_one = argv.pop()
    pos_dois = argv.pop()
    cond = False
    for posicao in range(int(pos_dois), int(pos_one)):
        if 'requisitos' in total_text.split('\n')[posicao]:
            cond = True
        elif 'Semestre' in total_text.split('\n')[posicao]:
            cond = False
        elif cond:
            content += '\n' + str(total_text.split('\n')[posicao])
    # '-\n': '',
    ControleModelo.set_model_data(type_model='caminhos_de_relacao', key_dict='substitutions')
    for key, value in ControleModelo.get_caminho_relacoes()['substitutions'].items(): content = content.replace(key, value)
    ControleModelo.set_model_data(type_model='caminhos_de_relacao', key_dict='txt_fracionado')
    ControleModelo.save(type_save='txt', arquivo=Arquivo(nome=item_dir_name.replace('.pdf', '.txt'),caminho=ControleModelo.get_model_data(), conteudo=content))



class ExtracaoDeTexto(Processo):
    def executar(self, ControleModelo: ControleModelo,suport = 0) -> None:
        ControleModelo.set_model_data(type_model='caminhos_de_relacao', key_dict='projeto_pedagogico')
        for item_dir_name in ControleModelo.get_diretorio_pointer_name_items():
            # Os.set_ponteiro(DataInput.get_caminhos_de_relacao()['projeto_pedagogico'])
            ControleModelo.set_model_data(type_model='caminhos_de_relacao', key_dict='projeto_pedagogico')
            tt = extracaoPrimaria(pdf=ControleModelo.get_conteudo_do_arquivo(type_arq='pdf',Arquivo=Arquivo(nome=item_dir_name,caminho=ControleModelo.get_model_data())),suport=suport)
            ControleModelo.set_model_data(type_model='caminhos_de_relacao', key_dict='texto_bruto')
            ControleModelo.add_list_save(Arquivo=Arquivo(nome=item_dir_name,caminho=ControleModelo.get_model_data(),conteudo=tt))
            #extracaoPrimariaEmPosicao(item_dir_name=item_dir_name,ControleModelo=ControleModelo,total_text=)
        ControleModelo.save_list(type_save='txt')
"""content = content.replace('OPT -', 'OPT-')
    content = content.replace('-\n', '')
    content = content.replace('ATC ', 'ATC')
    content = content.replace('GAM -', 'GAM-')
    content = content.replace('EAL -', 'EAL-')
    content = content.replace('ZOO -', 'ZOO-')
    content = content.replace('ENG -', 'ENG-')
    content = content.replace('EXA -', 'EXA-')
    content = content.replace('AGR -', 'AGR-')
    content = content.replace('AGR-218-', 'AGR-218 -')
    content = content.replace('AGR-226 - \n', 'AGR-226 - ')
    content = content.replace('AGR- ', 'AGR-')
    content = content.replace('HUM -', 'HUM-')
    content = content.replace('Manejo e Conservação do Solo e da \n', 'Manejo e Conservação do Solo e da ')
    content = content.replace('Plantas e Receituário \n', 'Plantas e Receituário ')
    content = content.replace('AGR-222 Avaliação e Perícia Rural', '9º AGR-222 Avaliação e Perícia Rural')
    content = content.replace('Café e \n', 'Café e ')
    content = content.replace('Al-\n', 'Al')
    content = content.replace('Bacharelado  \n', '')
    content = content.replace('AGRONOMIA  \n', '')
    content = content.replace('das unidades \ncurriculares', 'das unidades curriculares')
    content = content.replace('estágio curri-\n', 'estágio curri')
    content = content.replace('(Milho, Arroz, Trigo e \n', '(Milho, Arroz, Trigo e ')
    content = content.replace('BIBLIOGRA FIA BÁSICA', 'BIBLIOGRAFIA BÁSICA')
    content = content.replace('BIBLIOGRAF IA \n', 'BIBLIOGRAFIA')"""