class Controle():
    def __init__(self, buttons):
        self.buttons = buttons

    def muto(self):
        if self.buttons == 1:
            print ("A TV está mutada.")

    def desligado(self):
        if self.buttons == 2:
            print ("TV esta Desligada.")

    def aumentaVolume(self):
        if self.buttons == 3:
            print ("Aumentando o Volume")
    
    def diminuirVolume(self):
        if self.buttons == 4:
            print ("Dimuindo o Volume")
            