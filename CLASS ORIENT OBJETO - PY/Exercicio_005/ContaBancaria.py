class ContaBancaria():
    def __init__(self, nome, valor_Inicial, real = False):
        self.real = real
        self.nome = nome
        self.valor_Inicial = valor_Inicial
    
    def depositar(self,saldo):
        print (f"Olá {self.nome} o valor incial é {self.valor_Inicial} seu saldo é de {saldo}", end="")
        self.saldo = saldo
        self.valor_Inicial += self.saldo
        self.saldoFinal = self.valor_Inicial
        print (f" Adicionado o valor desejado fica: {self.valor_Inicial}")
    
    def sacar(self, sacado):
        if self.saldoFinal > 0:    
            self.valor_Inicial -= sacado
            self.saldoFinal = self.valor_Inicial
            if self.valor_Inicial <= 0:
                print (f"{self.nome} você não tem {self.valor_Inicial} para retirar da sua conta.")
                return
            self.real = self.valor_Inicial
            print (f"{self.nome} após ter efetuado o saque, {self.nome} tem {self.real} em mãos")

    def valortotal(self):
        print (f"{self.saldoFinal}")
        

