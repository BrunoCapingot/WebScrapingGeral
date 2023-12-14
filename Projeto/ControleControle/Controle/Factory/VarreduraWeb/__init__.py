from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo
from Projeto.ControleModelo import ControleModelo
from Projeto.ControleControle.Controle.Factory.Web import Web


class VarreduraWeb(Processo):
    def executar(self, object_list: list) -> None:
        self.execucao(
            Web=object_list[0], DataInput_comandos=object_list[1].get_localizacao_link_comando(),
            DataInput_caminhos=object_list[1].get_caminhos_de_relacao(),
            Arquivo=object_list[2],
            ControleModelo=object_list[3]
        )

    def execucao(self, Web:Web, DataInput_comandos: dict, DataInput_caminhos: dict, Arquivo: classmethod, ControleModelo: ControleModelo) -> None:
        for nome in DataInput_comandos:
            for link in DataInput_comandos[nome]:
                Web.open_link(link=link)
                for comando in DataInput_comandos[nome][link]:
                    [ControleModelo.add_download_list(
                        Arquivo=Arquivo(
                            nome=nome, caminho=DataInput_caminhos['projeto_pedagogico'],link=link)
                    )
                        for links in Web.clickElementoPorComando(comand=comando) if '.pdf' in links]
        ControleModelo.download_list_dowload()