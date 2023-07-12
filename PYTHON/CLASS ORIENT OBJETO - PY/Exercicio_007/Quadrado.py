class Quadrado:
    def __init__(self,tamanhoLado):
        self.tamanhoLado = tamanhoLado

    def mostrarArea(self):
        self.area = self.tamanhoLado**2
        print(f"O valor da areá é: {self.area}")
    
    def mudarValor(self,valor):
        self.tamanhoLado = valor
