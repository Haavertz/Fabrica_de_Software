import os

class Organizar_Tabuleiro:
    def __init__(self):
        self.Initial()

    def Initial(self, line="|_|"):
        for i in range(0, 9):
            for j in range(0, 9):
                print(line, end=" ")
                if j == 8:
                    print(i, end="")
                    print(end="\n")
                if i == 8 and j == 8:
                    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h"]
                    for describe in alfabeto:
                        print(describe, end="    ")
                    print("\n")

def Organizar_Movimento(movimento_coluna, movimento_linha):
    tabuleiro = Organizar_Tabuleiro()
    print(tabuleiro)

class Organizar_Tabuleiro_Pecas(Organizar_Tabuleiro):
    def __init__(self):
        super().__init__()

    # def Initial(self):
    #     line="♗"
    #     super().Initial(line)

Organizar_Tabuleiro_Pecas()
