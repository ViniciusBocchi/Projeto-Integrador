# Projeto-Integrador

# Aqui importamos bibliotecas de terceiros, essa biblioteca serve para controlarmos o computador pelo codigo
git init
git add main.py
git commit -m 
git tag -a v1.0 -m "Versão 1.0"

from enum import Enum

class Usuario:

    def __init__(self, nome, senha):
        self.__senha_emergencia = 000000
        self._nome = nome
        self.__senha = senha
# Codificando Metodos Destrutores para deletarmos o codigo desejado
    def __del__(self):
        print("excluído com sucesso!")
# Codificando propriedades, utilizamos para acessarmos e alterarmos os nomes
    @property
    def nome(self):
        print("Acessando nome")
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        print("Alterando o nome...")
        self._nome = novo_nome

# Codificando Enum, pois a senha de emergencia nao pode ser acessada
    def senha_emergencia(Enum):
        senha = 00000

user1 = Usuario('vinicius_custodio', 123456)
user2 = Usuario ('leonardo_jotta', 130505)

# Codificando testes unitarios, para testar o funcionamento passo a passo do codigo
print(user1.nome)
user1.nome = "GB"
print(user1.nome)
