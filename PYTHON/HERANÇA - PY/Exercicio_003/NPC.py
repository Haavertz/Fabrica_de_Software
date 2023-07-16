class NPC():
    def __init__(self,nome, time):
        self.nome = nome
        self.time = time
        self.vivo = "Sim"
        self.energia = 100
        
    def info(self):
        print(f"Nome: {self.nome}")
        print(f"Time: {self.time}")
        print(f"Forca: {self.forca}")
        print(f"Municão: {self.municao}")
        print(f"Vivo: {self.vivo}")
        print(f"Energia: {self.energia}")
        print(f"Habilidade: {self.habilidade}")
        print("-="*20)

class Soldado(NPC):
    def __init__(self, nome, time):
        super().__init__(nome, time)
        self.nome = self.nome+" 1"
        self.forca = 200
        self.municao = 200
        self.habilidade = "Passos Silenciosos"
        
class Guarda(NPC):
    def __init__(self, nome, time):
        super().__init__(nome, time)
        self.nome = self.nome+" 2"
        self.forca = 100
        self.municao = 20
        self.habilidade = "Tomar Menos Dano"
    
class Elite(NPC):
    def __init__(self, nome, time):
        super().__init__(nome, time)
        self.nome = self.nome+" 3"
        self.forca = 400
        self.municao = 500
        self.habilidade = "Bala na Agulha"
    


