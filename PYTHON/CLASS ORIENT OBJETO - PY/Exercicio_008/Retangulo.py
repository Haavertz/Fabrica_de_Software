class Retangulo:
    
    def __init__(self,ladoA,ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def mudarValor(self,valorAnew,valorBnew):
        self.ladoA = valorAnew
        self.ladoB = valorBnew

    def returne(self):
        self.area = self.ladoA*self.ladoB
        self.perimetro = self.ladoA*2+self.ladoB*2
        print (f"Á area é de: {self.area}")
        print (f"O perimetro é de: {self.perimetro}")

    def rodape(self):
        self.valorodape =(self.area*0.15)
        print (f"O valor dos 15% são {self.valorodape}.")