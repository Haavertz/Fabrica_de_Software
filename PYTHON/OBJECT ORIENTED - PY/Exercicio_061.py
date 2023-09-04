
#BOAS PRATICAS

class Retangulo:
    def __init__(self, largura: float, altura: float) -> None:
        self.__largura = largura
        self.__altura = altura
        
    def area(self):
        return self.__largura * self.__altura
    
angulo = Retangulo(5, 10)
print(angulo.area)
print(angulo.area())# AQUI PRECISO DE PARENTESES


class Retangulo:
    def __init__(self, largura: float, altura: float) -> None:
        self.__largura = largura
        self.__altura = altura
    @property #SE EU FIZER ISSO NÃO PRECISO DE PARENTESES     
    def area(self):
        return self.__largura * self.__altura
    
angulo = Retangulo(5, 10)
print(angulo.area)