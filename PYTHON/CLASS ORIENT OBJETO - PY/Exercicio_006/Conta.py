class Conta:
    def __init__(self,nome,conta,fone,saldo,cpf,agencia):
        self.nome = nome
        self.conta = conta
        self.fone = fone
        self.saldo = saldo
        self.cpf = cpf
        self.agencia = agencia

    def saque(self, saqueretirar):
        self.saqueretirar = saqueretirar
        if self.saqueretirar > 0 and self.saqueretirar < self.saldo:
            self.saqueretirar -= self.saldo 
            self.saqueretirar = self.saqueretirar * (-1)
            print (f"{self.nome} o saque que você tinha de {self.saldo}, sobrou: {self.saqueretirar}, retirando: {saqueretirar}")
            return
        if self.saqueretirar < 0 or saqueretirar > self.saldo:
            print (f"{self.nome} não tem dinheiro suficiente para retirar! ")
            return
        
    def deposito(self, depositar):
        self.depositar = depositar
        if self.depositar <= 0:
            print ("Valor incomun, favor digitar novamente!") 
        else:
            self.saqueretirar += depositar
            print (f"{self.nome} depositou: {depositar} na conta totalizando {self.saqueretirar}")

    def extrato(self):
        print (self.saqueretirar)