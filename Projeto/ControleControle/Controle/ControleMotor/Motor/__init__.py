class Motor:
    def __init__(self):
        self.process_table = list()

    def executar_processos(self,object_list:list):
        print(object_list)
        while len(self.process_table):
            dt = self.process_table.pop()
            dt.executar(object_list)

    def adicionar_processo(self, Processos:list):
        self.process_table.append(Processos)
        print(Processos)
