from Projeto.ControleModelo.Modelo import Modelo

class ControleModelo:
    def __init__(self):
        self.table = [list(), list()]

    def add_list_save(self, Arquivo)->None:
        self.table[0].append(Arquivo)

    def add_download_list(self, Arquivo)->None:
        self.table[1].append(Arquivo)

    """def download_list_dowload(self)->None:
        modelo = Modelo(Os=Os)
        while len(self.table[1]):
            arquivo = self.table[1].pop()
            input('calma')
            modelo.download(arquivo.get_name(),arquivo.get_cminho())
            del arquivo
    """

    """def save_list_save(self,Os:Os)->None:
        modelo = Modelo(Os=Os)
        while len(self.table[0]):
            modelo.save(Arquivo=self.table[0].pop())
    """
