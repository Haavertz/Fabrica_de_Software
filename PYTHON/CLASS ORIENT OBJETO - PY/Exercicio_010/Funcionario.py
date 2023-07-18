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
    def Advertencia():
        aluno = input("Digite o aluno: ")
        aluno[""] = (aluno.append())
        # if aluno in aluno:
            
        #     pass

        # pass

class Professor(Pessoa):
    def __init__(self, nome, cpf, fone, salario):
        super().__init__(nome, cpf, fone)
        self.__salario = salario
    
    def Contratar(self):
        disprofessor = {}
        nome = input("DIgite o nome do professor: ")
        materia = input("DIgite a materia do professor: ")
        disprofessor["ListaProfessor"] = {nome:materia}
        print(disprofessor["ListaProfessor"])
        

    def Nota(self):
        disaluno = {}
        aluno = input("Digite o nome do aluno: ")
        nota = int(input("Digite o valor da nota: "))
        disaluno["Nota:"] = {aluno:nota}
        print(disaluno["Nota:"]) 

    def MostraSalario(self):
        print(f"{self.nome} o seu salario é: {self.__salario}")       


class Coodenador(Professor):
    def __init__(self, nome, cpf, fone, salario):
        super().__init__(nome,cpf,fone, salario)
        print(f"{self.nome} o quê você gostaria de fazer? ")
        print("( 1 ) - Contratar professor")
        print("( 2 ) - Dar advertência")
        escolha1 = int(input("Escolha: "))
        if escolha1 == 1:
            super().Contratar()
        elif escolha1 == 2:
            pass
        else:
            print("Valor invalido!")
            # os.system("cls")
            # os.system("pause")
            # return

class Limpeza(Coodenador):
    def __init__(self, nome, cpf, fone, salario):
        super().__init__(nome, cpf, fone, salario)
        

c1 = Coodenador("Gleison", 123, 321, 12000)
c1.Contratar()
# c1.MostraSalario()
# p1 = Aluno("GLeison")

