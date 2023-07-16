class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        # print(nome, idade, self.cpf) 

class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, nota):
        super().__init__(nome, idade, cpf)
        self.nota = nota 
        # print(nome, idade, self.nota)
    
    