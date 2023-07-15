class Bola():
    def __init__(self,cor,circuferencia,material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material
        
    def troca_Cor(self,trocar_corr):
        self.cor = trocar_corr
        print (f"Cor Trocada para {trocar_corr}.")

    def mostrar_cor(self):
        print (f"A cor é {self.cor}") 


    
