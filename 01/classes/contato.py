class Contato:

    def __init__(self):
        self.__nome = ''
        self.telefone = ''
        self.email = ''

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome

    def get_telefone(self):
        return self.__telefone
    def set_telefone(self, telefone):
        self.__telefone = telefone
