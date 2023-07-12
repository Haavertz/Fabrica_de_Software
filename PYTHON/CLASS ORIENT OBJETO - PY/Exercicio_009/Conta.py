class Conta:
    def __init__(self, nome, cpf, saldo, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        self.__senha = senha
        pass
    pass
    def depositar(self, newvalor):
        self.__newvalor = newvalor
        self.__saldo = self.__saldo + self.__newvalor
        return self.__saldo

    def extrato(self, senha):
        if senha == self.__senha:
            print(f"O seu saldo é {self.saldo}")
            return
        else:
            print("Senha Invalido!")

    def sacar(self, senha):
        if senha == self.__senha:
            print(f"O seu saldo é: {self.__saldo}")
            return
        else:
            print("Senha Invalida")