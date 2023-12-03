import requests


class Modelo:
    def __init__(self, Os):
        self.os = Os

    def download(self, nome, caminho, link):
        response = requests.get(url=link)
        if response.status_code == 200:
            caminho_completo = self.os.path.join(caminho, nome)
            with open(caminho_completo, 'wb') as arquivo:
                arquivo.write(response.content)
            print(f"Arquivo '{nome}' baixado com sucesso em '{caminho_completo}'.")
        else:
            print(f"Erro ao baixar o arquivo '{nome}' do link '{link}'. Código de status: {response.status_code}")

    def save(self, Arquivo):
        print(Arquivo.get_link())
        print(Arquivo.get_name())
        print(Arquivo.get_caminho())
