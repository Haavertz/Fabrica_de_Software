
class Pessoa():
    ano_atual = 2023
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento2(self):
        return self.ano_atual - self.idade
        
    @classmethod
    def por_ano_nascimento(cls, nome, anoDeNascimento):
        idade = cls.ano_atual - anoDeNascimento
        return cls(nome,idade)
        
