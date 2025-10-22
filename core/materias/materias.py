class Materias:
    def __init__ (self, id=0, nome="", sigla="", descricao=""):
        self.__id = id
        self.__nome = nome
        self.__sigla = sigla
        self.__descricao = descricao

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
        def sigla(self):
            return self.__sigla
        @sigla.setter
        def sigla(self, novo_sigla):
            self.__sigla = novo_sigla

        @property
        def descricao(self):
            return self.__descricao
        @descricao.setter
        def descricao(self, novo_descricao):
            self.__descricao = novo_descricao