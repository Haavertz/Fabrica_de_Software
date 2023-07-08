class PessoaAula():
    def __init__(self, nome,idade,falando = False, comendo = False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

    def falar(self, assunto):
        self.assunto = assunto
        if self.comendo:
            print (f"{self.nome} não pode falar comendo.")
            return
        if self.falando:
            print (f"{self.nome} já esta falando sobre {assunto}... ")
            return
        print (f"{self.nome} está falando sobre {assunto}...")
        self.falando = True

    def parar_falar(self):
        if self.falando:
            print (f"{self.nome} parou de falar.")
            self.falando = False
            return
        if self.comendo:
            print (f"{self.nome} esta comendo {self.alimento} por isso n pode falar")
            return
        print (f"{self.nome} não esta falando!")

    def comer(self,alimento):
        self.alimento = alimento
        if self.comendo:
            print (f"{self.nome} já esta comendo {alimento}")
            return
        if self.falando:
            print (F"{self.nome} não pode comer enquanto fala.")
            return
        self.comendo = True
        print (f"{self.nome} esta comendo {alimento}")

    def parar_comer(self):
        if not self.comendo:
            print (f"{self.nome} não esta comendo")
            return
        print (f"{self.nome} parou de comer. ")
        self.comendo = False

