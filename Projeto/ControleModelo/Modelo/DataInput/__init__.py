from typing import Dict, List


class DataInput:
    def __init__(self)->None:
        self.dicionarioPrincipal = dict(
            caminhos_de_relacao = dict(
                projeto_pedagogico= r'C:\Users\CPGT\Desktop\WebScrapingGeral\Projeto\Download\projetoPedagogicoCurso',
                ementa= r'C:\Users\CPGT\Desktop\WebScrapingGeral\Projeto\Download\Csv',
                txt= r'C:\Users\CPGT\Desktop\WebScrapingGeral\Projeto\Download\Textos',
                csv= r'C:\Users\CPGT\Desktop\WebScrapingGeral\Projeto\Download\Csv',
        ),
            localização_nome_link_comando = {
                'Bacharelado em Agronomia': {
                    'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                        '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[1]/div[1]/h2/a',
                        '//*[@id="content-section"]/div/div[1]/ul[2]/li[8]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    )),
                },
                'Bacharelado em Ciência da Computação': {
                    'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                        '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[2]/div[1]/h2/a',
                        '//*[@id="content-section"]/div/div[1]/ul[2]/li[4]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    )),
                },
                'Bacharelado em Química Industrial': {
                    'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                        '//*[@id="adminForm"]/div[2]/div[4]/div[1]/h2/a',
                        '//*[@id="content-section"]/div/div[1]/ul[2]/li[3]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    )),
                },
                'Bacharelado em Zootecnia': {
                    'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                        '//*[@id="adminForm"]/div[2]/div[4]/div[1]/h2/a',
                        '//*[@id="content-section"]/div/div[1]/ul[2]/li[2]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    )),
                },
                'Licenciatura em Pedagogia': {
                    'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                        '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[5]/div[1]/h2/a',
                        '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div[1]/p[12]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    )),
                },
                'Licenciatura em Química': {
                    'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                        '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[6]/div[1]/h2/a',
                        '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div[1]/ul[2]/li[2]/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    )),
                },
                'Tecnologia em Alimentos': {
                    'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                        '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[7]/div[1]/h2/a',
                        '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div[1]/ul[2]/li[6]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb'
                    )),
                },
                'Tecnologia em Sistemas para Internet': {
                    'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                        '//*[@id="adminForm"]/div[2]/div[8]/div[1]/h2/a',
                        '//*[@id="content-section"]/div/div[1]/ul[2]/li[6]/strong/a',
                        'pdfDownloadLinkUrl',
                        'finishWeb',
                    ))
                },
            },
        )

    def get_data(self)-> dict[str, dict[str, str] | dict[str, dict[str, list[str]] | dict[str, list[str]] | dict[str, list[str]] | dict[str, list[str]] | dict[str, list[str]] | dict[str, list[str]] | dict[str, list[str]] | dict[str, list[str]]]]:
        return self.dicionarioPrincipal

    def get_caminhos_de_relacao(self)-> dict[str, str]:
        return self.dicionarioPrincipal['caminhos_de_relacao']

    def get_localizacao_link_comando(self)-> dict[str, dict[str, list[str]] | dict[str, list[str]] | dict[str, list[str]] | dict[str, list[str]] | dict[str, list[str]] | dict[str, list[str]] | dict[str, list[str]] | dict[str, list[str]]]:
        return self.dicionarioPrincipal['localização_nome_link_comando']