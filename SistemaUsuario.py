from enum import Enum

class Usuario:

    def __init__(self, nome, senha):
        self.__senha_emergencia = 000000
        self._nome = nome
        self.__senha = senha

    def __del__(self):
        print("excluído com sucesso!")
    @property
    def nome(self):
        print("Acessando nome")
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        print("Alterando o nome...")
        self._nome = novo_nome


    def senha_emergencia(Enum):
        senha = 00000

user1 = Usuario('vinicius_custodio', 123456)
user2 = Usuario ('leonardo_jotta', 130505)


print(user1.nome)
user1.nome = "GB"
print(user1.nome)