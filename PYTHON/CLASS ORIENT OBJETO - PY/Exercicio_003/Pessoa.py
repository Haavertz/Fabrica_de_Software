class Pessoa():
    def __init__(self, nome,idade, andar = False,falar = False, comendo = False):
        self.nome = nome
        self.andar = andar
        self.idade = idade
        self.falar = falar
        self.comendo = comendo
        pass
    def comer(self,alimento):
        self.alimento = alimento
        if self.comendo:
            print (f"{self.nome} já esta comendo {alimento}")
            print (f"{self.nome} irá parar de comer agora!")
            self.comendo = False
            return
        else:
            self.comendo = True
            print (f"{self.nome} esta comendo {alimento}")
    def falando(self):
        if self.comendo:
            print (f"{self.nome} está comendo {self.alimento} e n pode falar no momento...")
        else:
            print (f"{self.nome} esta conversando...")
