class Pessoa:


    def __init__(self, nome, idade, endereco, cidade, estado):        
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado

    def relatorio(self):    
        print (f"Nome... {self.nome}")
        print (f"Idade... {self.idade}")
        print (f"Endereço... {self.endereco}")
        print (f"Cidade... {self.cidade}")
        print (f"Estado... {self.estado}")

class Aluno(Pessoa):
    
    def __init__(self, nome, idade, endereco, cidade, estado, saldo):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.saldo = saldo
        print ("-="*20)
        print ("Seja bem-vindo Aluno")
        super().relatorio()
        print ("Analisado: ", self.saldo)
        print ("-="*20)

