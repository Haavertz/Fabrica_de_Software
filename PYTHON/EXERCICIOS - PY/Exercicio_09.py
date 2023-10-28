class Organizar_Tabuleiro:
    list_pecas = ["♖","♘"]
    def __init__(self):
        self.Initial()


    def Initial(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if i == 0 and j == 0:
                    print(" +", "-" * 25, "+")
                    # for row in self.list_pecas:
                    #     for col in row:    
                    #         print("",col)
                if j == 8:
                    print("", i, end="")
                    print(end="\n")

                if i == 8 and j == 8:
                    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
                    for describe in alfabeto:
                        print("", describe, end=" ")

                    print("\n", "+", "-" * 25, "+", end="")
                    print("\n")
                    self.process_cell()

    def process_cell(self, row="♖", col="♖"):
        if row == "♖" and col == "♖":
            print("♖")
            



class MovimentoTabuleiro(Organizar_Tabuleiro):
    def __init__(self):
        super().__init__()
        self.Movimento_Percorrer()
      
    def Movimento_Percorrer(self):
        for i in range(0, 9):
            for j in range(0, 9):
                pass

MovimentoTabuleiro()
