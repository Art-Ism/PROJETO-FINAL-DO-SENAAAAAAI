class Aluno:
    def __init__ (self, id=0, nome="", cpf="", idade=0):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade

        @property
        def id(self):
            return self.__id
        @id.setter
        def id(self, novo_id):
            self.__id = novo_id

        @property
        def nome(self):
            return self.__nome
        @nome.setter
        def nome(self, novo_nome):
            self.__nome = novo_nome

        @property
        def cpf(self):
            return self.__cpf
        @nome.setter
        def cpf(self, novo_cpf):
            self.__cpf = novo_cpf

        @property
        def idade(self):
            return self.__idade
        @nome.setter
        def idade(self, novo_idade):
            self.__idade = novo_idade
