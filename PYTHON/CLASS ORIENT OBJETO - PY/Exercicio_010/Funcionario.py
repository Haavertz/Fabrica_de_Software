import os 
class Pessoa():
    def __init__(self, nome, cpf, fone):
        self.nome = nome
        self.__cpf = cpf
        self.__fone = fone
    
class Aluno():
    def __init__(self, nome):
        self.nome = nome
        listaluno = []
        self.listaluno = listaluno 
        print(f"Olá {self.nome} você esta estudando... ")
        self.__listaluno = self.nome
    #Parte do Coodenador
    def Advertencia():
        aluno = input("Digite o aluno: ")
        aluno[""] = (aluno.append())

class Professor(Pessoa):
    def __init__(self, nome, cpf, fone, salario):
        super().__init__(nome, cpf, fone)
        self.__salario = salario
    
    def Contratar(self):
        disprofessor = {}
        nome = input("DIgite o nome do professor: ")
        materia = input("DIgite a materia do professor: ")
        number = input("Numero do professor: ")
        disprofessor[number] = {nome:materia}
        for i in disprofessor:
            print (i)
            print(disprofessor[number])

    def Nota(self):
        disaluno = {}
        aluno = input("Digite o nome do aluno: ")
        nota = int(input("Digite o valor da nota: "))
        disaluno["Nota:"] = {aluno:nota}
        print(disaluno["Nota:"]) 

    def MostraSalario(self):
        print(f"{self.nome} o seu salario é: {self.__salario}")      

    def Advertencia(self, nome):
        print(f"{nome} foi advertido.")


class Coodenador(Professor):
    def __init__(self, nome, cpf, fone, salario):
        super().__init__(nome,cpf,fone, salario)
        self.__salario = salario
        print(f"{self.nome} o quê você gostaria de fazer? ")
        print("( 1 ) - Contratar professor")
        print("( 2 ) - Dar advertência")
        print("( 3 ) - Mostrar salario")

        try:
            escolha1 = int(input("Escolha: "))
        except:
            print("Valor invalido")
            return Coodenador(nome, cpf, fone, salario)
        if escolha1 == 1:
            super().Contratar()
        elif escolha1 == 2:
            nome = input("Como é o nome do aluno: ")
            super().Advertencia(nome)
        elif escolha1 == 3:
            print(f"Seu salario é de: {self.__salario} ")
        else:
            print("Valor invalido!")
            os.system("pause")
            os.system("cls")
            return Coodenador(nome, cpf, fone, salario)

class Limpeza():
    def __init__(self, nome, cpf, fone, salario):
        self.nome = nome
        self.__cpf = cpf
        self.__fone = fone
        self.__salario = salario
        self.__valor = False
    def limparVassoura(self):
        if self.__valor == False:
            print(f"{self.nome} Comecou a varrer com a Vassoura.")
            self.__valor = True
    
    def PararDeVarrer(self):
        if self.__valor:        
            print("Parou de varrer!")
            self.__valor = False
            
    def Salario(self):
        print(f"Seu salario é de: {self.__salario}")

c1 = Limpeza("Gleison", 123, 321, 1200)
c1.limparVassoura()
c1.PararDeVarrer()
c1.limparVassoura()
c1.limparVassoura()
c1.Salario()
# c1.MostraSalario()
# p1 = Aluno("GLeison")

