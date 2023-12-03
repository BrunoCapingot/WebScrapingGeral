import sys


class EstadoRequisito:
    def simples(self):
        pass
    def facil(self):
        pass
    def medio(self):
        pass
    def dicil(self):
        pass
    def divino(self):
        pass

class Simples(EstadoRequisito):
    def simples(self):
        pass
    def facil(self):
        pass
    def medio(self):
        pass
    def dicil(self):
        pass
    def divino(self):
        pass
    def ocupado(self):
        sys.stdout.write('O mercador ja esta ocupado\n')

    def desocupado(self):
        sys.stdout.write('Desocupando Mercador\n')
        return Desocupado()
class Facil(EstadoRequisito):
    def simples(self):
        pass
    def facil(self):
        pass
    def medio(self):
        pass
    def dicil(self):
        pass
    def divino(self):
        pass

