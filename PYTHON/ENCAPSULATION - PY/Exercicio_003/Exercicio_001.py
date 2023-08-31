

class Calculadora():
    def calcular(self, opcao):
        if opcao == "Somar":
            return self.__adicionar()
        if opcao == "Subtrair":
            return self.__subtrair()
        
    def __adicionar(self):
        valor = int(input("Digite o valor 1: "))
        valor2 = int(input("Digite o valor 2:"))
        soma = valor + valor2
        return soma
        
    def __subtrair (self):
        valor = int(input("Digite o valor 1: "))
        valor2 = int(input("Digite o valor 2:"))
        soma = valor - valor2
        return soma
        
        
        
calculer = Calculadora()
a = input("Digite o quê você quer (Subtrair/Somar):")
print(calculer.calcular(a))
