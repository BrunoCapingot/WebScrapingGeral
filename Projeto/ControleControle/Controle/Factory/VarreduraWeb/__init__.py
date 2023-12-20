from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo
from Projeto.ControleModelo import ControleModelo, Arquivo
from Projeto.ControleModelo.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.Web import Web


class VarreduraWeb(Processo):
    def executar(self, object_list: list) -> None:
        self.execucao(Web=object_list[0],ControleModelo=object_list[1])

    def execucao(self, Web:Web, ControleModelo: ControleModelo) -> None:
        for nome in ControleModelo.get_localizacao_link_comando():
            for link in ControleModelo.get_localizacao_link_comando()[nome]:
                Web.open_link(link=link)
                for comando in ControleModelo.get_localizacao_link_comando()[nome][link]:
                    links = Web.clickElementoPorComando(comand=comando)
                    [ControleModelo.add_list_download(Arquivo=Arquivo(nome=nome, caminho=ControleModelo.get_caminho_relacoes()['projeto_pedagogico'],conteudo=links))for links in Web.clickElementoPorComando(comand=comando) if '.pdf' in links]
            ControleModelo.download_list()