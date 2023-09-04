

class Cadastro():
    def __init__(self, nome, idade) -> None:
        self.__Checking(nome, idade)
    
    def cadastrar(self, nome: str, idade: int) -> None:
        print("Banco de Dados")
        print(f"Usuario {nome}, com idade {idade} cadastrado.")
        
    def __Checking(self, nome: str, idade: int):
        if type(nome) == str and type(idade) == int:
            self.cadastrar(nome, idade)
        else:
            print("NO")
    
bah = Cadastro("name", 10)