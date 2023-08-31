

class  Carro():
    def __init__(self, marca, modelo):
  
        self.modelo = modelo
        self.marca = marca

    def acelerar(self):
        print(f"O Carro da marca {self.modelo} esta acelerando")
    def freiar(self):
        print ("carro esta freinando")
    def passar_macha(self, marcha):
        self.marcha = int(marcha)
        print(f"carro da {self.modelo} passou marcha para {self.marcha}")
        
print ("=-"*30)
        
carro_new = Carro("M4", "BMW")

carro_new.acelerar()
carro_new.freiar()
carro_new.passar_macha(3)
print(carro_new.marca)

print ("=-"*30)

carro_new2 = Carro("Fusca", "Volkswagen Type 1")
carro_new2.acelerar()
carro_new2.freiar()
carro_new2.passar_macha(3)
print(carro_new2.marca)
print(carro_new2.modelo)

print ("=-"*30)