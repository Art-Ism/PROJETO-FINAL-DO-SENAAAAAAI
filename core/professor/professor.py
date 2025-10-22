class Professor:
    def __init__ (self, id=0, nome="", formacao="", idade=0):
        self.__id = id
        self.__nome = nome
        self.__formacao = formacao
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
        def formacao(self):
            return self.__formacao
        @formacao.setter
        def formacao(self, novo_formacao):
            self.__formacao = novo_formacao

        @property
        def idade(self):
            return self.__idade
        @idade.setter
        def idade(self, novo_idade):
            self.__idade = novo_idade
